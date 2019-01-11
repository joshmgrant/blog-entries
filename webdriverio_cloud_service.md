[Webdriverio](http://webdriver.io/) is a rising star in the UI automation world, riding high on the surge in NodeJS's popularity. It's a good tool, written with test automation issues in mind, such as using cloud services like [Sauce Labs](https://saucelabs.com/).

However, even though the tooling is well thought-out, there still can be some hiccups when moving from a local grid or device setup to a cloud service. I'll go through some common problems that occur and possible ways to solve them. 

For this post, I'll be using tests with WebdriverIO, Mocha and Sauce Labs. I'll also assume some familiarity with NodeJS.

## Issues with Strange Timeouts

_Problem_: One of the most common issues that comes up when running existing tests on Sauce for the first time is tests timing out. This can be somewhat mysterious, since tests that run fine on a local grid may apparently error out. One error that appears frequently is along the lines of

    timeout of 2000ms exceeded. The execution in the test "My Awesome Test" took too long.

This error occurs with Mocha-based tests. It can seem strange because it may not have appeared ever when designing and running tests. 

_Explanation_: Mocha specs have a built-in [feature](https://mochajs.org/#timeouts) where tests will fail if spec execution takes longer than a defined timeout. The defaults can be low (2 seconds) which are appropriate for a unit test but might be dramatically incorrect for a functional or UI-based test. As well, when using a cloud server, Webdriver commands must be sent to the service's cloud over the internet, introducing longer latencies and test runtime. The combination of short Mocha timeouts and latencies based on cloud services can create errors as seen above. 

_Solution_: The most straightforward solution is to either increase or disable Mocha timeouts in your tests. This can be done at the spec (`describe`) level, test level (`it`) or before hook level (`before`). It may be possible to disable or change timeouts globally if you are using the Mocha test runner, but not if you are using the `wdio` runner.

## Issues with Strange Failures and ESOCKETTIMEOUT Errors

_Problem_: Here's one that's bit me a few times, and is particularly relevant to tests with a long startup or connection time, such as connecting to a mobile device, emulator or simulator. Tests are triggered and then there's a delay in them starting. Eventually, on the test runner side, the tests error out with a message like

    Error: ESOCKETTIMEOUT

or

    Error: ETIMEOUT

then the test runner promptly stops. However, on the Sauce side, test sessions are started but then eventually error out with a message like

    Your test errored. Test did not see a new command for 90 seconds. Timing out.

with a only a single POST Webdriver command starting a new browser session. As well, sometimes this causes multiple sessions per test case to start, all of which occur after the tests from the runner have errored out and stopped. All sessions look the same but why there are multiple sessions for each test case is confusing.

This can be cryptic and very frustrating because not only are tests not being executed but they're also not easy to debug. 

_Explanation_: WebdriverIO has logic that automatically tries and retries to connect to a remote session if it doesn't succeed. There are two parameters in the `wdio.conf` file that set this:

- `connectionRetryTimeout` tells WebdriverIO how long it should wait up to until it retries starting a sesssion
- `connectionRetryCount` tells WebdriverIO how many retries it should execute before stopping.

Based on these values, WebdriverIO tries to connect using the following flow:

1. if a device takes longer than the `connectionRetryTimeout`, then the retry logic triggers
3. a new remote driver session connection is attempted
4. Sauce is still up and has received the command
5. Sauce doesn't start a new session within the `connectionRetryTimeout`, so step 1 occurs again
6. the retry logic repeats again up to the `connectionRetryCount`.

On the test framework side, WebdriverIO throws ESOCKETTIMEOUT errors and fails out as expected (since the connection couldn't be established). On the Sauce side, since an initial connection was made to Sauce infrastructure (not necessarily the device or remote server since Sauce is a bit more complex than a remote grid), Sauce receives the initial request, starts a session, but then errors out since no further driver commands are sent. Hence the situation appears as described.

_Solution_: The easiest solution is to increase `connectionRetryTimeout` to as high a value as needed. In some cases this is over 5 or 10 minutes, depending on device startup and/or network latency. Note that `connectionRetryTimeout` tells WebdriverIO to wait _up to_ the timeout value, so there's little harm in having a large value for the timeout. You can also reduce `connectionRetry` to 0 to avoid needless sessions being started.

## WebdriverIO and Sauce Connect

This issue is more oriented to more experienced Sauce users but can still create confusion. 

One thing to note is that WebdriverIO can start standalone dynamic Sauce Connect proxy tunnels on its own. This is good if you are using an internal website with a simple network configuration and using the [Sauce Service](https://github.com/webdriverio-boneyard/wdio-sauce-service) module. This may be problematic if you are using a persistent tunnel already set up for other tests and/or using a tunnel with an additional proxy. 

If you are currently using Sauce Connect as part of your automated test setup, take a look at how you are using Sauce Connect tunnels and how WebdriverIO may interact with these tunnels. Remember to include `sauceConnectOpts` as mentioned in the [WebdriverIO documentation](http://webdriver.io/guide/services/sauce.html#sauceConnectOpts). You can also include additional proxy settings in these options if necessary, such as if Sauce Connect needs to tunnel through an additional proxy in your setup.

Moving to a cloud service like Sauce can be a bit painful at first, but the benefits and flexibility is usually worth it in the long run. Happy testing!


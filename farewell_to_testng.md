When I was working with Selenium for the first time, the tool stack I learned with was Java-based. The test runner that my team used at the time was [TestNG](https://testng.org/), and we made pretty liberal use of its functionalities. I also got to know TestNG pretty well. Although I _liked_ Java, I _loved_ TestNG. It was a powerful test framework that was well-suited to building a Selenium-based test harness. While I've worked with different languages and tool stacks since then, my fondness for TestNG remained. 

Until now. 

During the past few months, I've seen enough issues with Java-based test frameworks to see TestNG (and other libraries) from some different perspectives. And based on these experience, my love for TestNG has faded and I can no longer recommend TestNG as a "default" choice for Java-based test projects. The main reasons come down to characteristics of good test projects and what really matters when writing good test harnesses, Selenium-based or not. 

In my experience, the most critical criteria of successful test automation frameworks are the following:

1. Running _all_ tests in a test harness on a regular basis. This may mean quarantining some tests temporarily and/or deleting tests permanently.
2. Writing independent and stable tests that can be executed at any time during the development cycle.
3. Realizing that long-term project maintenance is far more important than short-term test writing.

TestNG, for all of its merits, eventually fails at supporting these three points. While there may be some helpful features that TestNG provides in the short-run, in the long-run there are simply better choices.

## TestNG: The Good Parts

Before I write about the downsides of TestNG, I feel like I should mention why I was drawn to it in the first place. One thing that I've become acutely aware of in the past years is that user experience in test automation tooling is critical for both tooling adoption and day-to-day work. If a tool is nice to use and solves real problems, not only am *I* more likely to use it but it's more likely *other people* will use it as well. This creates communities and shared knowledge which can move the needle forward in general. Test automation is no exception; being able to write code that can test specific circumstances and solve key problems is important and tooling that help in a neat and tidy way will get some attention.

After working with TestNG for a while, I found it had good developer UX. There were underlying conventions in TestNG that I could get a "feel" for after some experience using it. Although there was a lot of functionality and surprisingly large number of annotations, after a while I could guess what I needed to use and was often correct. If I needed a particular [annotation](https://testng.org/doc/documentation-main.html#annotations), I could often deduce which one I needed based on experience and logical thinking and _voila_, the tests would run as expected. 

As well, TestNG provided some functionality to - for lack of a better term - paper over some shortcomings that Java had for test automation. For example, Java notoriously does not have default/optional method parameter values, so TestNG [implemented this feature](https://stackoverflow.com/a/22304811). This is extremely helpful for Selenium tests where default browser types or configuration values are commonly used. TestNG also allowed for grouping and organizing tests in sophisticated ways and provided [listener functionality](https://testng.org/doc/documentation-main.html#testng-listeners) to perform particular actions not just on test success or failure but other events too. At the time, these features were vital for writing good test harnesses that did more than evaluate class instances as in unit testing.

Based on this, TestNG should be applauded for solving some gnarly issues in designing good test automation. But even these beautiful features have faded from glory as time went on.

## Getting It All Together: Running All Tests Regularly

When I worked with TestNG, one of the draws to using it over JUnit was the ability to organize tests into different groups or suites. On my team we had acceptance test suites for each product, and on the product I worked on this was a subset of all the automated tests that were written. Additionally there were regression suites and some additional suites for more specific functionality for security or specific features. Specifying a new suite was pretty easy since TestNG tests were executed using a specific `testng.xml` file. In such a file we could include or exclude tests by package, class or test method name and even pass in additional parameters needed per suite. Each test suite was executed using an Ant script on our Jenkins instance. It all worked wonderfully. 

Except it didn't. 

I realize now that breaking down these tests into such suites was a slippery slope toward instability and extra work for us. Each new test class needed to be carefully added or removed from existing `testng.xml` files, and the number of Jenkins jobs executing tests became unwieldy. Eventually some suites were run regularly, and others were not run regularly and instead run "on demand" - meaning basically never. This increased complexity in maintaining existing suites and adding new tests to suites. 

Test code is production code, and like production code it experiences its own form of [rot](https://en.wikipedia.org/wiki/Software_rot). In the case of automated tests, the application under test changes and updates, along with the test framework tools and language. In the case of Selenium tests, locators, URLs, application screens, and flows change leading to broken tests. Tests that aren't exercised regularly start to rot, and when they are run it is painful to try to update them to work which in turn lowers and information or value those tests produce for teams. It leads to frustration with the whole test automation enterprise and reduces confidence overall. This is a bad scene. 

The problem with TestNG is that it makes it too easy to divide up tests into such suites in the first place. With some foresight, building test suites that are designed to run _all tests_ regularly pays dividends over time in avoiding rotting test code. Regularly can mean whatever works best in a team's context - nightly, hourly, on every pull request, on every commit, on every merge to mainline, or similar. Even dividing up tests in to two or three groups (smoke/regression or smoke/acceptance/regression, for example) can be done with a bit of planning and low overhead. Maven and JUnit are essentially designed from this perspective; find all test classes in the `src/test` package following a basic naming convention and run them. The TestNG grouping approach leads to suites that are too finely organized, and running tests via `testng.xml` files can facilitate this issue.

## Standing On My Own: Why Writing Independent Tests

Another problem more applicable to web-based browser testing is designing tests that execute well independently of each other. For many teams, this is no small task. Often with enterprise applications there are limitations in creating and using test data and application instances. A team may have to share a server instance with other teams, such as other QA teams or development teams. Also there may be long or complex workflows that need to be tested that cannot be easily executed concurrently or repeated.

Here again TestNG has some easy solutions that turn out to be terrible.

TestNG allows for tests to depend on other tests or set conditions. For example, TestNG has the [`@dependsOnMethod` annotation](https://www.mkyong.com/unittest/testng-tutorial-7-dependency-test/) where you can specify a method that must execute before a given test method can execute. I've used this as `testA` must run and succeed before `testB` can execute. This means I can be assured that any side effects from `testA` are in place that may affect `testB` which was helpful working in environments as mentioned above where there were limited application instances to test again or test data was difficult to create. There's also ways to set a priority of tests in TestNG where tests of priority 1 execute first, then tests of priority 2 execute, and so on until all priorities are executed. 

These capabilities are great workarounds. But to really succeed, tests should be run independently and in any order without such workarounds. This means arranging for stable test environments dedicated to test automation, managing test data as best you can, using hooks to setup test data without relying on a (G)UI layer by injecting data at the database or API level. And certainly tests should be designed to be executed independently from the start. Again TestNG seemingly provides good tools to solve hard problems but ends up making matters more difficult than needed.

## The Little Things: Thinking Long Term

The most important costs for any test automation project are maintenance costs. Writing a test - even a complicated one - often takes much less effort than maintaining that test over time. This is also true of test infrastructure such how a test is run, when a test is run, what happens before and after test runs, and so on. Little things like how a test gets executed can make a big impact.

TestNG typically leans on the `testng.xml` for selecting tests to run. This is fine or even desirable in an development or IDE setting. Running a set of TestNG tests from Eclipse or IntelliJ is pretty straightforward. Running `testng.xml` files on a continuous integration (CI) server is slightly more complicated but can also be accomplished but will also look different from running tests locally. Where running `testng.xml`-based tests are often a right-click-select-Run operation in an IDE, continuous integration services like Jenkins will need something else. This could be an Ant script, using a TestNG-based plugin or some edits to the `pom.xml` for using Maven. This is true even if there's a single `testng.xml` with a single suite. 

In contrast, executing tests directly using Maven is identical even if using TestNG as your sole test framework in code. Adding the Maven Surefire plugin even allows for running [specific tests or subsets of tests](http://maven.apache.org/surefire/maven-surefire-plugin/examples/single-test.html) both from a development environment and CI environment. It also removes the overhead managing an additional XML file. This may seem like a slight improvement, but over time the lower maintenance costs and unified approach to test execution will pay off.

## It's Not You, It's Me

I really don't want to sound like TestNG is terrible (or that Maven is amazing). TestNG is a well-built library and many teams have found success using its functionality. But over time, I find that the downsides outweigh the benefits. 

I'll always remember TestNG as a good first step on my journey, but it is no longer the tool I reach for first in my Java toolbox.
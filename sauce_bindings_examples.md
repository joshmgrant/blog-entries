In my [previous post](https://simplythetest.tumblr.com/post/635881097097592833/whats-new-in-sauce-bindings-v100) I provided an overview of the (Java) [Sauce Bindings](https://github.com/saucelabs/sauce_bindings/blob/master/java/README.md#) project, and its benefits. Theory is great and all, but let's take a look at some code samples. 

## Basic Test Sample

First, adding the Sauce Bindings to your Java project requires these Maven coordinates:

```xml
<!-- https://mvnrepository.com/artifact/com.saucelabs/sauce_bindings -->
<dependency>
    <groupId>com.saucelabs</groupId>
    <artifactId>sauce_bindings</artifactId>
    <version>1.0.1</version>
</dependency>
```

Once that dependency is added, consider this test case, written using JUnit 4:

```java
import com.saucelabs.saucebindings.SauceSession;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class BasicTest {

    private SauceSession sauceSession;

    @Before
    public  void setUp() {
        // default is to create a desktop web session with latest Chrome on Windows 10
        sauceSession = new SauceSession();
        sauceSession.start();
    }

    @After
    public void tearDown() {
        sauceSession.stop("passed");
    }

    @Test
    public void loginTest() {
        // use the Sauce Session instance to initialize a WebDriver instance
        WebDriver driver = sauceSession.getDriver();

        // use the WebDriver instance in your tests/page objects without changes
        driver.get("http://www.saucedemo.com");
        driver.findElement(By.id("user-name")).sendKeys("standard_user");
        driver.findElement(By.id("password")).sendKeys("secret_sauce");
        driver.findElement(By.id("login-button")).click();

        Assert.assertTrue(driver.findElement(By.cssSelector(".shopping_cart_container")).isDisplayed());
    }
}
```

This test can be copied and pasted into an existing Java project, which can then be built and executed. 

If you have [Sauce credentials set as environment variables](https://opensource.saucelabs.com/sauce_bindings/docs/getting-started#universal-prerequisites), once you run this test, you will get output like the following: 

```bash
Dec. 04, 2020 1:45:01 P.M. org.openqa.selenium.remote.ProtocolHandshake createSession
INFO: Detected dialect: W3C
SauceOnDemandSessionID=some-long-hash-like-thing1234 job-name=null
Test Job Link: https://app.saucelabs.com/tests/some-long-hash-like-thing1234

Process finished with exit code 0
```

and this test should appear within your Sauce Labs account. 

What just happened? Let's unpack this. 

## W3C By Default

There's a few notable parts of this code snippet. First, there's this line from the terminal output: 

```bash
INFO: Detected dialect: W3C
```

This means that the protocol used to connect the Selenium client to the Sauce Labs was the (new) W3C protocol. This would appear in the console logs of any Selenium-based test script that is using the [W3C protocol](https://sfconservancy.org/news/2018/may/31/seleniumW3C/) instead of the older JSON web protocol, which would instead have a line like

```bash
INFO: Detected dialect: OSS
```

Any idea how the Sauce Bindings did that? Or how capabilities were set up to make this happen? No? 

Encapsulating this new protocol is one of the features of the Sauce Bindings. These details are now abstracted away from end users, in a [neat and tidy way](http://gph.is/2ns7D3v). Using the Sauce Bindings mean that using the new W3C protocol will _just work_. 

## Start a Sauce Session in a Simple Way

Typically I like to look at the code in `@Test` methods but the only notable thing in the above code is that the test uses a standad WebDriver instance to control the browser. I'm more interested in the `@Before` and `@After` methods in this case. 

Looking at the `@Before` method, we see it's pretty simple: 

```java
 @Before
public  void setUp() {
    // default is to create a desktop web session with latest Chrome on Windows 10
    sauceSession = new SauceSession();
    sauceSession.start();
}
```

a `sauceSession` instance is created using no additional configurations or parameters. This will create a default session instance on Sauce Labs, which in this case contains a `RemoteWebDriver` instance that creates an instance of the latest version of Chrome Sauce supports on a Windows 10 machine. Of course we could shorten this down to a single line of Java code, and start a Sauce Labs session and set the driver using

```java
 @Before
public  void setUp() {
    driver = new SauceSession().start();
}
```

As promised, with Sauce Bindings you can create a Sauce Labs session in _one line of Java_ and without [changing any existing WebDriver code](http://gph.is/2n1pX5s). 

## Using Sauce Features in An Easy Way

Now that we've seen some basic examples, let's see what else we can do. Reworking the `@Before` method to run on a different platform and browser combination can be done by introducing the `SauceOptions` object. Here's how we might rework the test to run on MacOS using Firefox by just changing the `@Before` method logic:

```java
 @Before
public  void setUp() {
    // set your browser/platform combination using a Sauce Options object
    SauceOptions sauceOptions = new SauceOptions();

    sauceOptions.setBrowserName(Browser.FIREFOX);
    sauceOptions.setBrowserVersion("65.0");
    sauceOptions.setPlatformName(SaucePlatform.MAC_MOJAVE);

    sauceSession = new SauceSession(sauceOptions);
    sauceSession.start();
}
```

Again, compare this to using (Desired) Capabilities and options classes. Here there's some utilities such as the `Browser` and `SaucePlatform` enums that allow for selection from a list of known values instead of stringly typing capability values. Also `SauceOptions` instances can be created independently of WebDriver instances or `SauceSession` instances, which is helpful for configuration or setting up multiple platform configurations before actually initializing the WebDriver.

In addition to Selenium-specific capabilities, the Sauce Bindings also handle Sauce-specific capabilities: 

```java
 @Before
public  void setUp() {
    SauceOptions sauceOptions = new SauceOptions();

    // set the test name from the default "untitled" test name
    sauceOptions.setName("My Awesome Test");

    // set a build name - helpful if you're running in Jenkins, CircleCI, etc
    sauceOptions.setBuild("My Awesome Sauce Build");

    // set the Sauce Connect tunnel, if required
    sauceOptions.setTunnelIdentifier("my-pretty-good-tunnel");

    sauceSession = new SauceSession(sauceOptions);
    sauceSession.start();
}
```

or change your Sauce session to use a different Sauce data centre: 

```java
 @Before
public  void setUp() {
    // run a test on the latest chrome on Windows 10 with a name
    SauceOptions sauceOptions = new SauceOptions();
    sauceOptions.setName("Mein großartiger test");

    sauceSession = new SauceSession();
    sauceSession.setDataCenter(DataCenter.EU_CENTRAL);

    sauceSession.start();
}
```

without having to remember or look up remote URL values. Sauce-specific values are handled as much as possible by the bindings directly and not by end users. 

Isn't this so [great](http://gph.is/2lxUsfp)? 

## What's next? 

So far I think this is a good start for the Java Bindings Sauce Bindings. Similar functionality exists in C#, Python and Ruby now as well, and we're looking to add similar functionality for mobile environments and devices. One of the goals of this project is to make connecting to Sauce in automated tests simple and straightforward, and believe me that means including mobile in this. 

Happy Testing!
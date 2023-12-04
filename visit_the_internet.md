# Visit the Internet in Different Languages

Here's a list of ways you can visit [The Internet](https://the-internet.herokuapp.com/), a web app demonstrating web functionality and elements, using a web browser in various (programming) languages.

## HTML

```
<html>
    <a href="https://the-internet.herokuapp.com/>Click Me to Visit the Internet</a>
</html>
```

## Java

Using Java 19 and the Selenium WebDriver, 

```
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class VisitTheInternet {

    public static void main(String[] argv){
        WebDriver browser = new FirefoxDriver();

        browser.get("https://the-internet.herokuapp.com");
    }
}```

## Python

Using Python 3.10 and the Selenium WebDriver,

```
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://the-internet.herokuapp.com")
```

## Ruby

Using Ruby 2.7.1 and Watir, 

```
require 'watir'

browser = Watir::Browser.new

browser.goto 'https://the-internet.herokuapp.com'
```

## C#

Using C# and Selenium WebDriver,

```
using System;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

public static class Visit
{
    public static void Main()
    {
        IWebDriver driver = new ChromeDriver();

        driver.Navigate().GoToUrl("https://the-internet.herokuapp.com");
    }
}
```

## JavaScript

In browser JavaScript, 

```
window.location.href = "https://the-internet.herokuapp.com
```

In NodeJS, using WebDriverIO,

```
import WebDriver from 'webdriver'

const browser = await WebDriver.newSession({
    capabilities: { browserName: 'chrome'}
    }
)

await browser.navigateTo('https://www.google.com/ncr')
```

## Kotlin

```
import org.openqa.selenium.WebDriver
import org.openqa.selenium.chrome.SafariDriver

driver = ChromeDriver()

driver.get("https://the-internet.herokuapp.com")
```

## Perl

```
use Selenium::Remote::Driver;

my $driver = new Selenium::Remote::Driver(browser_name => 'chrome');
$driver->get('https://the-internet.herokuapp.com');
```
## R


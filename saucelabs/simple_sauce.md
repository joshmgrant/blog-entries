# Announcing Simple Sauce

Test automation is highly beneficial in modern software development, but writing good automated tests is hard work. Designing good tests that work well for different teams in different contexts takes dedication. 

Sauce Labs want to help make this as simple as possible, so Sauce Labs' [Solutions Architects](https://saucelabs.com/our-experts) has developed [Simple Sauce](https://www.github.com/saucelabs/simple_sauce). This is a cross-language open source project that contains several wrappers around Selenium functionality to help connect to Sauce Labs. These wrappers are called _bindings_ and are currently available in Java, C#, Python and Ruby this project. 

The Simple Sauce project solves two main problems that many Sauce users have, making connection to Sauce and starting sessions straightforward and helping to expose Sauce features and functionality in a simpler way. Simple Sauce also has a goal of providing an excellent developer user experience.

Connecting and starting sessions on Sauce can be cumbersome for users. For some users starting out, getting started with Sauce and their existing Selenium tests can be daunting if they're not familiar with some of [the features of Selenium](https://ultimateqa.com/selenium-webdriver-latest-version-features/). Simple Sauce aims to make connecting much simpler, using a few as four lines of code. Here's a pseudocode example of creating a browser session on Sauce Labs with Simple Sauce:

```java
sauce = new SauceSession();

sauce.start();

sauce.driver.get("https://www.saucelabs.com")

sauce.stop();
```

This code starts a new session, visits Sauce Lab's website and closes the session. Clean and straightforward. This approach works in all language bindings in Simple Sauce in a similar way. Simple Sauce also provides the flexibility to allow desired capabilities to be passed into a Sauce session for users that need specific platform configurations. 

Simple Sauce also tries to allow users to make use of existing Sauce Labs features in a straightforward way. Having a single library as a point of access for Sauce Labs and its features would help both novice and expert SDETs alike. 

Lastly, as Solution Architects we love test automation and we want users of Sauce Labs to have the best possible experience when working with Sauce. Good user experience means getting tests written quickly and in a more maintainable manner. The Solutions Architects have put our years of experience in designing and maintaining tests into this project, focusing on having a clean, simple design.

Since Sauce Labs is a major supporter of open source software and projects, we have designed this project to be open sourced from the beginning. This means that we encourage participation from our community and also want Simple Sauce to learn more about both Sauce and Selenium. 

This project early on and so is a good time to help out if you are interested. We are releasing Alpha versions soon, which will contain basic features to Sauce Labs users to give us feedback before firming up features in the Beta and getting ready for version 1.0.0 release. There are multiple ways for folks to [contribute](https://github.com/saucelabs/simple_sauce/blob/master/README.md#contributing) in all of the language bindings and those developing examples of using Simple Sauce in their language of choice. And if you need help with making a contribution to Simple Sauce? Ask! Open an issue in the project describing what you'd like to do and what kind of help you need. 
Currently there's a lot going on in the world of software development. There's a lot going generally all over the world at present, but I digress. I do want to take some time to talk about automated tests.

Imagine sitting down and starting to work with a codebase that is brand new to you. You may know the language and frameworks involved, or maybe not. You may have some domain knowledge of the app's main functionality. Or maybe you're pretty new to software development overall. What do you do first?

One thing that is new and trendy is using AI tools to work with existing codebases. You can use such tools to either ask questions about the code, like "How does EventRegistrationController class work?" or "How does data get inserted into the database?", or you can generate working or example code that you can play with. These are pretty good methods for getting up to speed on a codebase, and many development-oriented AI tools (which are really large-learning models or LLMs) are effective when used this way.

You could also sift through the version control history of the codebase, looking for parts of the app that are edited the most often, or the most recently, or are the oldest. This might give you some insight into what parts of codebase change the most, or which ones are "core" to the application.

You could also read developer documentation, which can be surprisingly helpful. It can also be shockingly out-of-date or even non-existent.

Let me share a secret to getting up and running on a codebase quickly: run automated tests.

Why run tests, even running tests as the first thing you should do? Because running tests will provide quite a bit of information with minimal effort. If tests run and all pass, you can take a look at these tests to see what they do and how various parts of the application work. You can even get a good sense of functionality from an end user's perspective in some cases. 

If tests run and some pass and some fail, you know there's some work to do to fixup the tests. You can start fixing tests or at least evaulating the failures to learn about the codebase. Bug fixing is usually a good start to learning a codebase, and failing tests are a good step toward that. 

If tests don't run or crash, this can tell you that the automated tests are neglected. This is a signal that maybe tests aren't run often or at all, which can also be a sign of things to come.

Of course you can analyze test code further, looking at what kinds of tests are automated (browser-based, GUI, unit level, integrated, API, performance, security, and so on) and use design patterns like the test automation pyramid to get an even deeper sense of what's going on. Or you can simply run the tests and see what happens. 

Tests are a feature of a good codebase, and are essential for a professional one.


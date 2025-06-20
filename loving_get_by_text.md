I have a confession: I've been writing browser tests lately, and my preferred approach to locators is becoming get by text or get by label. 

I am aware that some of you might want to throw some full wine bottles at me now. But I stand by it.

Over the course of my career as a test automation specialist, I've worked with a bunch of web applications for which I automated browser tests. One of the most critical aspects of writing browser tests is finding good locators to hook into in order to drive the application. Naturally, since there are plenty of options there are also plenty of opinions on what kind of locator strategies to use. Typically these follow some kind pattern like this;

- Use `id` attributes that are permanent, if you can. If you can't, then
- Use `data-testid` or other custom attributes specifically for automation if you can. If this isn't an option then
- Use class attributes, which tend to be stable. If you can't do this, then
- Use CSS properties to specify elements. And if all the above aren't options, then
- Use text or xpath locators or something and hope for the best.

Generally patterns like this are a good heuristic for identifying locators. However, the nature of front-end web applications has gradually changed over the past decade. Most front-ends are now generated through frameworks and not through hand-written HTML, CSS and JS. A result of such frameworks is that elements aren't always able to be directly manipulated by developers, and you need to rely on the capabilities of the framework. Browsers (and computers more generally) have gotten faster and more efficient. And lastly, tooling has evolved greatly for browser automation. Selenium WebDriver is a web standard now, and there's lots of other tools that can be used.

Based on all this progress, one would imagine that there's been progress on how to choose or use locators well with modern and maybe less-modern web apps and pages. One would be, I think, disappointed to find out there hasn't been much progress here. Finding and maintaining locators is pretty similar to how things looked many years ago. Front-end developers still hesitate to add custom attributes for testing sometimes. Newer web frameworks dynamically create elements, so `id` attributes are either not present or not reliable enough for automation. No one understands CSS, still.

What to do based on this state of affairs? I've been using Playwright lately for browser automation, and Playwright provides a `getByText()` method for finding elements. I started using it out of convenience at first and, well, I'm convinced it's a good approach. Why? Because - frankly - it works well.

The thing about text in web applications, whether that be labels next to inputs or placeholder text, is that it's actually fairly stable. Most buttons with the text `Submit` will continue to have the text `Submit` for a long time. And if the text does change on an element it is straightforward and obvious to update your tests. Plus, text doesn't tend to go away: moving from Angular to React to Vue to Svelte still means your Name field has a label of "Name" that end users will see.

One big objection to using text is localization internationalization, which can be a valid point. However, if your web app has five options for language, does that mean the logic and workflows change as well? They might, but if they don't, you can likely test one language and still feel confident in the test results. If you can't use text-based locators, then you'll have to evalutate your strategy anyway.

I am a big fan of the adage "What's the simplest thing that could possibly work". When it comes to finding elements by text, this advice seems to hold true.

A lot can change in a few years. Just look at the state of affairs in the JavaScript (JS) test automation space. 

In 2015, if you asked me my opinion on JS and browser testing, I would've said "Avoid using JS altogether as much as possible, but if you need to use JS use Protractor."

Now, my position has completely flipped: "[WebdriverIO](https://webdriver.io/) is the best choice overall for browser (and mobile app) UI test automation, and I would definitely encourage JS-based tools over Java-based tools."

(If you're thinking "Where do you think JS tools for test automation be in 2026?" my answer is "No friggin idea".)

I think it might be helpful to think through why this position has flipped, since it might be helpful to understand the current landscape of JS-based testing tools but also for browser test automation tools more generally. Not just that, but JS-based tools are now applicable beyond purely JS projects and organizations, with Playwright going [cross-language](https://playwright.dev/docs/languages) after beginning in JS. Test tools with JS aren't just surviving, but also thriving.

First, back in '15, Angular was _de rigeur_ in the front-end JS framework world. React was only coming out, and tools like VueJS and Svelte were still many years away. Angular had a lot of mindshare and a lot of usage, so naturally a test framework that came along with it would get a lot of attention as well. And the Angular project (correctly) treated browser testing as a first-class citizen in its ecosystem, putting appropriate resources behind getting Protractor right. Protractor itself had at least one full-time developer at Google dedicated to it and a lively GitHub with issues and bugs being opened a closed.

As well, JS was a dramatically different language then. Promises were being incorporated into NodeJS itself, meaning asynchronicity had a better API to work with than function callbacks. ES6 classes were a few years away, and even npm scripts were not widely used in 2015. All of these features of NodeJS (or lack thereof) also helped buoy Protractor's interest from the development and testing communities. Since Protractor used WebdriverJS, the JS language bindings provided by the Selenium project, and WebdriverJS made use of promises, Protractor code was as idiomatic and "standard" as possible for NodeJS around 2015. 

Still, despite all of the above, JS was an asynchronous language. Since virtually all browser-based automated tests were designed to be run synchronously, learning promise syntax and semantics were an extra and nontrivial step in learning to write good Protractor tests. As well, writing page objects was, well, tricky in a language that didn't have the concept of class-based objects. There was a lot of overhead in writing good tests in Protractor compared to Java or Python. Similar projects for writing browser-tests in NodeJS ranged from not quite mature enough (WebdriverIO) to almost unusable (NightwatchJS) mostly because these projects were also relatively young. Add in the fact that Protractor was Angular-specific and Node tooling wasn't as fully developed as compared to Java (remember [Grunt](https://www.npmjs.com/package/grunt-cli) for running things?), choosing Java over Protractor (for example) was a somewhat easy choice.

Let's roll forward to 2021.

The world has changed, and with it so has server-side JS. Now class-based object-oriented programming is possible in JS, and defining and running scripts from a `package.json` is standard fare. Server-side JavaScript, both the language and tooling around it, has matured quite quickly. Now writing scalable codebases of mostly synchronous code (including test projects) that are maintainable is completely possible in NodeJS. Along with this, the maturity of tools such as WebdriverIO and NightwatchJS has grown too. There is even a new category of tools that do no use Selenium in any way (using the client-side JS bindings or the W3C protocol) including Cypress, Playwright and TestCafe. There is a complete buffet of choices for anyone who wants to write browser-based test automation in JS these days. 

And in my opinion, the best of these tools is WebdriverIO. The main reasons for choosing this are

- its has a robust service/plugin ecosystem, which allows teams to pick and choose what functionality they need,
- its active community, where questions can be answers, features discussed and general help with the tool is encouraged, and
- its well-thought-out API and tooling design allows for different tests and structures to reuse the same code.

Overall WebdriverIO isn't just the best tool (in my opinion) in the NodeJS world, it might be the best choice overall for teams starting with browser (or mobile!) test automation. 

Meanwhile, Protractor is [reaching the end of its life](https://github.com/angular/protractor/issues/5502). For some, this comes as no surprise. Protractor bugs and issues keep steadily increasing for a few years, while contributors and dedicated engineers from Google kept decreasing. Using WebdriverJS and not encapsulating asynchronicity from end users turned out to be a mistake, while Angular-specific features eventually were removed or lost value for test developers. Finally, the Angular project announced that Protractor will not be maintained after the release of Angular 15. The go-to JS tool of my halcyon days of test development will be no more. 

I'm reminded of the quote that "The only constant is change". It looks like this definitely applies to the NodeJS test tool landscape.

mnju34t y,. v7 t57b7. 74 v.7vb .7 5 g7z68 6n?  
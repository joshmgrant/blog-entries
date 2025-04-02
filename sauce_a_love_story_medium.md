This time last year, I was a manager of a small but might team of technical folks in a Go-To-Market organization at [Sauce Labs](https://www.saucelabs.com), a Silicon Valley-based startup working in the software technology space. What I would love to write about is how Sauce Labs successfully exited through a high-value acquisition or IPO and I was able to watch and benefit from this as a valued employee.

Reader, this is not that story.

In fact, I was laid off unceremoniously during the first wave of tech layoffs last year (during the week of Burning Man, no less). And as far as I know, Sauce Labs has not seen an impressive exit event as of this writing.

Still, I've had some time to think about things, and I think that Sauce Labs is a story of success. In particular, Sauce Labs is a story of multiple successes. 

## An Open Source Success Story

Sauce Labs was co-founded by one of the creators of [Selenium](https://selenium.dev) which is a large and fairly well-known open source project. Very briefly, Selenium is a tool for automating real browsers, but the project has grown from its humble roots of creating a software tool for driving a browser. Selenium has gone through a few major iterations and now includes clients in several major programming languages, server-side tools for controlling both a single local browser and for scaling up to managing a cluster of browsers on a remote server, and a [W3C specification](https://www.w3.org/TR/webdriver1/) for generically writing browser automation. I would say that Selenium is a bona fide success story about how open source can enable new technologies to change the world.

Based on this fledging technology (circa 2008) Sauce Labs was born in part to create a commercial opportunity based on this free and open source technology. Selenium could automate browsers free of charge, but managing those browsers for use with automation was (and still is, to be quite honest) a viable business opportunity. Sauce Labs was founded the same year as Microsoft Azure and six years before Docker, coming about years before the rise of cloud computing and containerization. The idea of having specialized virtual machines "on demand" on the cloud was still novel at the time, let alone virtual machines that were purposely configured with browsers for testing. Sauce Labs smartly built on top of the remote connection capabilities of the Selenium project and could allow for remote execution at scale for browser automation.

I'll also mention that at one point in history, this offering made Sauce Labs cool in the eyes of SDETs and developers, something I'll return to later on.

Like most Silicon Valley start-ups, the story of Sauce Lab's success is not quite neat and linear. Going from a nerdy idea worked on in San Francisco's Tenderloin district to international presence with hundreds of employees does show there was business potential found in an open source idea. Whatever happens in the future, Sauce Labs can be called a commercial triumph. 

## A Branding Success Story

On top of Sauce Lab's open source and financial success, Sauce Labs also showed the power of good branding and how to make a highly technical product appealing to non-experts and experts alike.

I think there were two steps to how Sauce Labs did this:
- Create an honest-to-goodness product for developers, and later
- Create an approachable brand for a highly specialized product and solution space.

Let's start with the good stuff: creating a product that developers love. This isn't easy, but the early days of Sauce Labs had a product that was appealing to developers and in particular, Selenium users. I think this was because Sauce Labs solved a real problem, managing several browser/operating system combinations for use for testing, and did it in a way that was interesting and clever. Sauce Labs was one of the first "cloud solutions" for a particular problem space and all that was needed to make use of Sauce Labs was a configuration in a developer's code. Connecting to the service and authentication were handled in code. This had the benefits of not requiring any additional infrastructure on the client/end users side and of abstracting away details such as virtual machine management. There was even a proxy offered by Sauce Labs to allow further integration with internal-only testing environments that was considerably more seamless and scalable than using the Selenium capabilities alone. 

As a result, Sauce Labs had a bit of cultural caché among SDETs and other developers, which resulted in [GitHub badges](https://shields.io/) based around browser coverage and Selenium/Sauce Labs usage in general. Seeing these badges on GitHub projects at the time gave the project a bit higher standing in some developer's eyes. Combine this with the positive view Sauce Labs had in the open source world by supporting Selenium as a first-class citizen and Sauce Labs was hip.

As any software professional knows, a decent product and praise from developers isn't always enough to keep a business growing. Sauce Labs had (and I'd argue still has) an additional problem: reaching folks who aren't necessarily Selenium experts and explaining the value of their offering. A developer who manages a Java-based Selenium test framework might understand Sauce Lab's value proposition almost instantly, but her manager may not and the director that department definitely will not.

One elegant way to solve this problem of offering a complex developer tool is create a brand presence that is the opposite of this: fun, approachable and interesting to a wide audience. This is exactly what the marketing department did with Sauce Labs. There was a creation of [Sauce Bot](https://youtu.be/NAK2MBMjqA4) a lovable robot character that captured many aspects of Sauce Labs (automated testing, Selenium, scaling). Sauce Bot and the associated brand messaging was easy to understand and take interest in, even if Sauce Labs core product wasn't. And crucially, this branding resonated with developers already interested in and using Selenium. It was a hit.

Of course, time passed and now Sauce Labs has a new brand identity that's only vaguely like it was before. I'm sure management at Sauce Labs had excellent reasons for this.

Marketing to developers and their managers is not easy, but Sauce Labs found a way to do this with success.

## A Personal Success Story

Up until now I've really only talked about Sauce Labs the company. What I haven't mentioned is that I started out a Sauce Labs fan long before I had the chance to work with Sauce Labs, let alone spend four and half years working there.

Like a lot of other folks in testing, I fell into it accidentally. I don't come from a massively wealthy or tech-focused background. I wrote my first C++ code in my 20s, and eventually took an entry level job writing test automation in a QA department at a software company. I'd only heard of software development up until that time. 

Late in 2011, I downloaded an installed Selenium RC (a client-server version of what would become the Selenium WebDriver) on my work computer. It was a bit clunky, but it worked. I was able to automate browsers like Firefox and Internet Explorer. From that moment on, I knew I was on to something. 

A few months later was the first time I'd heard of Sauce Labs. Someone had mentioned using it since we were then building a test framework with Selenium. I recall seeing the ["mustard and ketchup" logo](https://khyatisehgal.wordpress.com/2019/05/27/cross-browser-testing-via-sauce-labs/) that Sauce currently had, with links to adding various badges to GitHub projects. It was, as the kids say these days, _a vibe_. The idea that I could run my tests in Toronto on all sorts of browsers in California was amazing to me. The Sauce Labs brand stuck with me after that, and I continued to learn Selenium and keep up with the progress of that project. Overtime, I built up a reasonably good career writing test automation, not just for browser testing but also API testing and some unit testing framework work as well.

Then after a fortuitous meeting with [Titus Fortner](https://titusfortner.com), I was hired as Solution Architect on the Go-To-Market team. In this role, I could actually help teams from all over the place improve their testing practices and implement Sauce Labs and related technologies into their Selenium-based frameworks. I honestly thought a job like this was unreal, and I was extremely excited. Not only that, I was able to travel the world and see exotic locations ranging from Monarch Beach, Californa to Minsk, Belarus to Cambridge, Ontario (probably the least interesting Cambridge of the lot but I digress). I learned a lot about the Selenium project, the business of software development and met wonderful people. In some ways, it's a Cinderella story but with more web standards.

Then I was laid off like a whole bunch of other people. I'm sure management at Sauce Labs had excellent reasons for doing so.

In conclusion, Sauce Labs isn't the place it was ten years ago, four years ago or even one year ago, and it won't be the place it is now in a year or so. Regardless, it's a success story in more ways than one.




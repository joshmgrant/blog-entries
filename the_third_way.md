Lately I've been thinking about UI automation approaches. It's been my jam for a while. 

From my experience, there's been two ways to build up automated end-to-end/UI tests: 

- Bottom-Up using the bare Selenium WebDriver or similar tool
- Top-Down using an "off the shelf" test framework

Both of these approaches have their downsides. 

I've done a Bottom Up approach. We took the WebDriver (Java bindings) and built a custom set of tests on top of it. This is main intended use-case for the WebDriver, which was designed to be a low-level API that is fairly general purpose for driving browser operations. In my opinion, the WebDriver achieves this design goal well. Tests and related tooling is built directly by teams based on their tech stack and needs.

The downsides to the Bottom Up approach:

- Lots of upfront work. The WebDriver needs to be carefully wrapped to handle exceptions thrown by its main methods and structures built on top of it to make it effective in a test automation context. This is often before writing a single usable test. 
- Steep learning curve: getting to know how the WebDriver works and what tools to work along with it involves some fairly deep learning about tooling ecosystems. It's also something too large for a single individual to do in spare time as part of a dev or test role.
- Constantly re-inventing the wheel: I found myself solving the same problems over and over again, even with careful insight. 

I've also done a Top Down approach. I've used the [Protractor](http://www.protractortest.org/#/) framework and seen other popular frameworks such as [Capybara](http://teamcapybara.github.io/capybara/). These frameworks provide tooling for writing and running UI tests in an opinionated but smart way. The goals of these frameworks is to make writing tests fast and easy without getting bogged down by the WebDriver details. 

The downsides to the Top Down approach:

- Fighting the framework: in my experience, in any UI test framework my needs eventually conflict with that the framework offers. I need to access some component of it that the framework was designed to prevent access to. Hitting walls like this can be annoying or even show-stoppers for good tests. 
- Dependence on third-parties: Like any other software, test frameworks have dependencies and bugs. If a bug appears in the framework that prevents your testing goals, you have to depend on the framework maintainers to fix it or dive in and fix it yourself (where possible).
- Constantly re-inventing the wheel: I found myself solving the same problems over and over again, even with careful insight. 

Notice the final downsides in both Top Down and Bottom Up are the same. It's 2017 and I'm still getting StaleElementExceptions thrown from time to time, and I still have to slide in sleep statements in places where nothing else really works. Maybe there needs to be some _Third Way_ that addresses this issue of redoing the same work over and over again, of splitting the difference between writing custom code and using off-the-shelf frameworks.

Enter [Watir](http://watir.com/). 

I've recently gotten into trying out Watir. I think it's hitting on something interesting in being a part of the _Third Way_ described above. You can use Watir as part of a framework like [Cucumber](https://cucumber.io/), or directly by itself. It provides built-in waiting and synchronization specifically for test automation contexts. It's not as low-level as the WebDriver but it's not as high-level as a DSL-like test framework. It also has a great community around it _driven by_ test automation specifically. 

I've never been a Ruby dev or part of a Ruby shop which is why I've never really thought much of Watir. But based on discussions I've had with [Titus Fortner](http://titusfortner.com/) and [Chris McMahon](http://chrismcmahonsblog.blogspot.ca/) (both active in the Watir/Ruby community), that's _exactly_ why I _should_ be looking at Watir. It's designed to be a tool that works for writing good UI automated tests with a low bar of entry for new comers but still has the power to scale up when necessary. Writing UI test automation [could be fun again](https://xkcd.com/353/)! It may also be a good pattern to follow for other programming languages/ecosystems to follow. 

These are some rough thoughts but I've been thinking of them lately. 



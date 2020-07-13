Recently, I came across a post written by Tedu [discussing why they don't like writing automated tests](https://flak.tedunangst.com/post/against-testing). It's a good post, even if I disagree with a lot of the particular reasons why Tedu doesn't like writing or maintaining automated tests. Overall I agree with the sentiment, that testing and related code infrastructure can feel cumbersome and slow down development work unnecessarily. 

I started thinking about "bad" automated tests - low value tests that don't provide helpful feedback for developers. These are part of the frustration with test harnesses since they sometimes break and need to be updated but also don't provide much help in return. Why do such tests exist in the first place? 

Sometimes these tests exist to satisfy coverage requirements, such as test coverage or code execution coverage. Other times they exist as part of workflows that require TDD or tests to be written to pass code review. In many cases these tests are grandfathered in from previous work and conform to workflows or requirements that they were not designed for. 

However, the question remains: why write bad tests in the first place? 

Based on my experience, here are a few reasons why good developers (including SDETs) might write bad tests: 

**Novice Developers**: Many different folks said a variation of "if you aren't embarrassed by code you've written in the earlier part of your career, you aren't growing enough as a developer". We all start out a novices. This is true of writing test code in addition other forms of programming. In many organizations, novice developers are tasked with writing test automation (particularly UI automation but this applies generally). This means there's some green approaches to writing code generally, perhaps not with a good eye for maintenance or good coding practices. Along with the grave error of thinking test automation code is "easy" to write, this situation may produce a lot of bad tests.

I'll also note the somewhat shocking point that even well-versed developers in other areas may be novices when it comes to writing and maintaining test automation code.

**Learning Test Code Ergonomics**: If developers are experienced with writing test code, they still might write simplistic tests to get a feel for the test framework or related tools. Like learning a new stack or language, learning how to use test tooling in writing tests is a progression. Sometimes writing simple tests help a developer feel out how to perform testing tasks, such as how before/ after hooks or mocking library may work. Tools may vary from language to language or even project to project, and like other forms of code test code can benefit from introducing the latest and greatest stuff from time to time. The net result of this may be tests that are themselves not too valuable after the fact. Articulating this is tricky, and it can be easy to have such low value tests checked in even after code review.

**The Psychology of Quick Wins**: Related to test code ergonomics, sometimes we all need a quick win. Writing even a single passing test might help motivate a developer to complete a bigger task. This may be true if the test is low value and checking something basic. When it comes to UI tests, which are more complicated and have more moving pieces, the psychological effect might be greater, creating more reason for a developer or team to keep a test that doesn't provide value. Of course, the test may exist long after the feeling of a win passes, much to the chagrin of future team members and test maintenance.

**Outdated Requirements**: Software changes, and ideally that includes the automated tests within a software project. This doesn't always happen for a bunch of reasons. Tests that might've provided value in past versions of a project might not provide value now due to changing requirements or even larger shifts. Tests that contain conditions like `if platform == "Windows 98"` or `if javaVersion < 1.7` might always pass now, but may not be helpful. 

So what can be done when good developers write bad tests? 

In my opinion, low value tests are low hanging tech debt. One of the most straightforward solutions is to delete tests that are of low value and see what the result is. In many cases, there will be no side effects and all is good. If an issue is raised regarding coverage or linting or some other code analysis result, first consider what the issue being raised is and whether it itself has value or not before reworking or re-introducing the low value test.

We're all trying our best during these times, even if we've written some not so great automated tests.

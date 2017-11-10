One idea that's been on the back of my mind for a while now is looking at UI automated test projects in terms of size. How big is your UI test project? Thinking about how big a project is may help guide how to improve it or set the right expectations for making sure the effort succeeds. 

I think that UI automation projects can be safely partitioned into one of these four sizes: 

1. Minimal
1. Small
1. Medium
1. Enterprise

Here's a description of each size project, expectations team members may have with such a project size, and how to succeed with a UI automation project at a given size.

## Minimal

Minimal projects have only the essential requirements to be called a UI automation project. Perhaps there's a single script that does exactly one thing that was written by a single person. This person may not have any previous experience with test automation or UI automation. This project may not make use of a test framework. The project may not make use of any programming language tooling beyond what is needed to write and run the script. It may not even make proper or typical use of a UI automation library or tool. The main characteristic of this project is that it does contain _some_ reference to _some_ tool used for UI automation. At this point, minimal projects look more like an approach for solving for a one-off problem or a proof-of-concept. Most minimal projects try to answer the question "Does UI automation solve my testing problem in my context?".

_Expectations_: In a minimal project expectations are usually of the yes/no variety: Can I solve my problem with these approaches, or not? It may also try to answer the question of "How can I accomplish this task?". Code and artifacts can probably be thrown away regardless of the outcomes, and there is a lot of learning happening at this stage. 

_How to succeed_: Minimal projects can succeed mainly by providing a definitive answer to a specific question, and giving enough information to proceed.

## Small

Small UI automation projects have a handful of tests and often part of a larger software project or approach. They are ongoing efforts but still may be simple enough that a single developer or tester isn't responsible for them full-time. There is often a small number of simple tests that may be run regularly or not. Test frameworks and programming language tooling come into play here but may not be big concern. Small projects may only need to work on a very specific environment such a given team member's machine but not on every team member's machine or test environments but there is some expectation of _working_. There may also not be any expectation of automated or triggered runs of these tests;manual execution of these tests may be acceptable. Initial end-to-end smoke tests or user acceptance tests on larger teams or automation efforts on dedicated test teams often fall into this category. 

_Expectations_: In small projects the expectation is that the UI tests are exercised regularly or at least _could be_ exercised regularly. The main difference between small and minimal is that small projects are ongoing concerns. There may also be some expectation of particular and specific kinds of bugs or problems being caught with such UI tests. 

_How to succeed_: Small projects need some kind concept of regularity. Good small projects succeed by meeting expectations above but also being maintainable enough to grow into larger projects. 

## Medium

Medium projects are often grown-up small projects. Basic UI tests that catch basic happy-path bugs in a fast and effective way are "promoted" into looking for a larger class of issues. Here the number of tests has increased to the point where one or more team members may have to be responsible for these UI tests full-time. Possibly, someone with previous experience in UI automation or similar work may have to be brought in to manage this project. Along with a growing number of tests and testing scope, infrastructural issues begin to appear. Running tests in a particular environment may not sufficient and effort may be required to make sure UI automated tests can be run agnostic to who is working on them. It may make sense to make use of continuous integration tools or other automation in running medium-sized test projects. As well, teams may start to hit the limits of their UI automation tools and custom additions to tools/frameworks/environments may have to be considered. Another issue that starts to appear is test runtime. Medium projects may start to see UI automation that takes long enough to divide tests into short vs long run time (or from a different perspective, smoke vs regression tests). 

_Expectations_: Medium projects are all about maintenance and expectations while providing value. More tests may catch more problems, but it may also incur a larger maintenance cost. Further, this is the point where projects have "too many" tests, which is often a sign of low-value tests or a lack of UI automation optimization. Aligning testing goals with UI automation is often important in these projects.

_How to succeed_: Balancing the trade-off between maintenance and test value is key here. If this trade-off provides a net benefit to a team, then UI automation can be called a success. 

## Enterprise

Like enterprise software project, enterprise sized UI automation projects are big enough that they create special circumstances. Enterprise projects are medium projects at an order of magnitude larger in size and scope. Custom infrastructure is required and process automation is a given. There may be specialists needed to be hired to work on particular issues that only this project may ever have. Whole teams can be dedicated _solely_ to the UI automation. Enterprise projects can have a big influence _on_ UI automation tools directly and not the other way around. These projects are often associated with large, complicated pieces of software that could only benefit from large, complicated testing solutions. 

_Expectations_: Working on an enterprise UI automation project is basically like working on a full-fledged software project, from bottom to top. Skills beyond software testing or test automation may routinely be required.

_How to succeed_: Success here is largely driven by the underlying company's goals and objectives and how well this effort meets those goals and objectives. 

These are some rough thoughts on UI automation projects and these projects can - and do! - live inside other projects and teams (eg a QA department or agile team getting familiar with test automation).
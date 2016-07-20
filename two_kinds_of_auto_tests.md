A lot of people have problems using automated tests as part of a workflow. This could be mean running unit-level tests before/after every developer commit or running end-to-end tests using a tool like Selenium on pull requests. Developers get frustrated with failing tests and blocked processes and give up on automated tests. It leaves a bad taste in developers' mouths about test automation which can lead to bad feelings about automation in general. 

I think the main problem is misplaced expectations about what a developer _gets_ out of automated tests. 

To help set these expectations, here's two ways of thinking of how to use automated tests from a workflow perspective: 

1. Look for Problems
2. Look for Changes

*Look for Problems*
This is the more common approach when using automated tests as part of a workflow. The idea is pretty simple: use failed tests as signifiers of problems. Only when all tests pass are certain actions allowed like a commit to be added to history. Once something is identified as a problem, you can use automation to [stop it](https://www.youtube.com/watch?v=Ow0lr63y4Mw). The goal is to use automated tests to prevent certain problems or classes of bugs from occurring in the first place during development. This approach necessarily blocks activities from happening. This can help assure certain properties of a codebase such not having particular kinds of bugs and business rules certainly being followed. 

One advantage to this approach is that it extends past automated testing and can apply to other aspects of a project such as signing a [CLA](https://en.wikipedia.org/wiki/Contributor_License_Agreement), enforcing code styles or passing through a [linter](http://proselint.com/).

*Look for Changes*
This approach means watching test results over a period of time to track changes. The results of these tests are non-blocking, meaning that actions like a pull request getting merged still occur even if there's failing tests. The idea here is that test results occur alongside changes and can be used to see what changes at specific points of time. In this case, having test results be non-blocking is essential because those results give you some clues to answer the question "What happened here?". 

As an example, imagine you notice that your end-to-end automated test failures increase from 9% overall to 20% overall on a given build. This could be an oracle to inform you of a something like a UI modification or business rule change. You could also look at individual test failures to get an idea of where those changes could be happening. It doesn't necessarily suggest something is _wrong_ but that something is different. Similarly, if test failures decrease from 9% to 4% it may indicate that some bugs may have been fixed. 

These aren't the only two philosophies around how to use automated tests as part of a workflow (feel free to tell me about others!) but they're two helpful ones. They're also not mutually exclusive. Starting with one approach might yield to the other. But they might help set expectations about what automated tests can do.
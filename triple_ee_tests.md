Much ink has been spilled (metaphorically) around the topic of writing good unit tests. One of the best patterns I've seen for thinking about how to write good unit tests is the Arrange-Act-Assert pattern, also known as Triple AAA tests. Here's a selection of articles illustrating this pattern:

- [The Automation Panda's Take on AAA tests](https://automationpanda.com/2020/07/07/arrange-act-assert-a-pattern-for-writing-good-tests/)
- [Jay Cruz and the Three A's of Unit Testing on Dev.to](https://dev.to/coderjay06/the-three-a-s-of-unit-testing-b22)
- [Leaning unit testing from Microsoft](https://learn.microsoft.com/en-us/visualstudio/test/unit-test-basics?view=vs-2022#write-your-tests)

and so on. 

The gist is that every unit test should have three parts: _arrange_ your test with fixtues and elements to test, perform an _act_ on these fixtures that you wish to test, and then _assert_ the actual result of the action is the same as you expect.

This is a great pattern, except for one tiny issue: in some languages, there isn't really an "assert".

Increasingly, instead of the syntax

```
assert expected_condition == actual_condition
```

we see something like

```
expect(expected_condition).toBe(actual_condition)
```

This is true in JavaScript/TypeScript world, as well as in the Ruby world. In JS you have this pattern in libraries like [Jest](https://jestjs.io/docs/expect), while in Ruby the RSpec framework uses [expect](https://www.rubypigeon.com/posts/rspec-expectations-cheat-sheet/) as well. This could lead to developers who never actually use an `assert` keyword in code. This leads the Triple AAA mnemonic to shambles. 

Hence, here is the recipe _Triple EEE_ tests:

- _Enable_ test fixtures as needed
- _Execute_ a step to be tested
- _Expect_ a result and verify this happens.

A nice acronym, exactly expected. 
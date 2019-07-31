In programming and software development tooling, sometimes you get stuck somewhere and find yourself in need an escape door. The escape may be temporary (getting over a small problem in your workflow) or long-term (a gateway to a whole other level of functionality).

Some examples of such cases I've faced are

- when using a git GUI like [Git Extensions](https://git-extensions-documentation.readthedocs.io/en/latest/git_extensions.html) or [SourceTree](https://www.sourcetreeapp.com/), sometimes there's a git action I want to complete that either isn't supported by the GUI or is just a bit too complicated to do via UI, and I need the git CLI to execute a command and
- when writing browser-based tests, I use the Page Object pattern faithfully but find myself in a situation where it is simply easier to invoke functionality through the WebDriver object directly instead of some page object abstraction. 

In the above cases my tooling allows me to solve the majority of my problems through helpful abstractions (a GUI app and design pattern, respectively) but these abstractions fall a bit short in a few cases. Hence, I need some way to _escape_ the abstractions to get to a different layer of abstraction, at least temporarily.

In the git GUI case, both apps provide a "open CLI terminal" option/button where I can type in whatever git commands I need to before returning to the GUI app. In the Page Object case, exposing a `driver` member in my page object classes allows me to make use of the WebDriver directly alongside my neat and tidy methods.

I think this pattern widely applicable beyond software tooling or test automation, but it definitely applies to those contexts. The key in both cases is that the escape door isn't the main approach to solving a problem - better abstractions exist for those. The escape door is available as a _back-up plan_ along with the abstractions. It's there for when you absolutely need it and not as a main interaction. At the same time, the escape is designed with usage in mind and isn't some buggy accident. Intentionally exposing this functionality is important.

Sometimes things go smoothly, and sometimes you need to escape for just a bit. This applies to software development in addition to life.
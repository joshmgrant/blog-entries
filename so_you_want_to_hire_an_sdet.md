As software companies grow so do their engineering teams. A role that comes along with growing teams is the software engineer in test (SEIT), a software developer who primarily works with test automation and related testing infrastructure. SEITs can be extremely valuable to engineering teams as they can enable good automation practices for shipping quality code faster, and they can be a great touchpoint for test engineers and operations engineers to work with development teams. They can also be a bit tricky to hire since SEITs don't have quite the same skills as application developers or test engineers. 

Let's take a look at how your might approach hiring SEITs at different levels.

# Junior/Intern

I've worked with several interns (in Ontario these people are called co-op students) and working with test automation is a great introduction to being a software engineer of any kind. 

## When to hire
Juniors are great on teams with established SEITs and test engineers. In some organizations there are entire teams dedicated to test automation efforts. If you need someone to bang out many test code or take partial ownership of a large test automation project, a junior hire could be a great choice.

Like in other software develoment roles, hiring a junior usually comes with an expectation that the junior candidate will receive some menitorship and early career training and experience.

## What to look for
Candidates for a junior SEIT should show characteristics of a junior test engineer and/or application developer. On the testing side, an ideal candidate should show curiosity about software or systems, the ability to develop at least basic mental models of how a piece of software might work, and good communication skills, written or oral. On the development side, an ideal candidate should show at least a basic aptitude for programming from school or otherwise. They should be able to read, write and understand code in some programming language even a language that your organization doesn't use. Previous experience working in software development is _nice_ but not a requirement. It can be safe to assume that junior candidates have worked with _at most one_ test automation tool and likely none.

## Key questions to ask
- "How would you test a pen?": a classic test engineering question to access a candidate's reasoning skills, communication skills and question asking ability.
- "Write a function to reverse a list in a given language": a basic but straightforward assessment of programming skills. The language can be set by the interviewer or chosen by the candidate.
- "What is something you achieved that you are proud of?": a question to get some insight into the candidate's motivations and interests.

# Intermediate
Teams getting started with test automation or parts of test automation could benefit from hiring experienced SEITs. Experienced SEITs can write test code but also set up needed infrastructure and coordinate with developers, operation engineers, and testers. Intermediate SEITs may also be able to start test automation efforts for new projects as needed.

## When to hire
The main reason to look for an intermediate SEIT is when automation efforts exist but have grown past being managed part time by single individuals. For example, a team may have written some Selenium-based tests to test some scenarios, and at first a small number of tests can be handled by the team or specific members of the team without a test automation speciality. Once the number of tests grow to a certain size and/or complexity, that team may want to have a dedicated person looking after them. This could also be the case with automated performance tests, service-level tests, and so on. Or a team may seek to level up on test automation skills. 

## What to look for
Test automation is a speciality of software development, and as I've said before (if slightly reworded) [SEITs are developers](https://simplythetest.tumblr.com/post/169623787610/test-developers-arent-testers). Evaluating them as you would other intermediate developers isn't unreasonable. Look for one or more roles where they worked as SEITs, DevOps engineers, or other forms of automation. Note however that SEITs may have written many, many lines of code but aren't traditionally skilled in areas of programming. Most SEITs wouldn't be able to code low level algorithms like linked lists or binary trees and may have never really used map/reduce/fold approaches. Intermediate SEITs should be able to discuss tools they've used well, and strong intermediates can identify differences between tools and levels of testing. And they can definitely write tests; any intermediate SEIT should be able to write a few tests for _at least one_ layer of an application, such as unit or component tests, API level tests, and/or end-to-end tests.

## Key questions to ask

- "Write three automated tests in a given language to test this class": This question assess a candidate's knowledge of test development code writng
- "Here is an example login test. How would you improve it?": A possibly fun exercise that helps evaluate a candidate's knowledge and technical communication skills.
- "Suppose a software bug is found using test code that you wrote. What would be your first reaction?": Teams handle bug reporting in various ways with varying levels of success, so this question can shed some light on a candidate's experiences.
- "Describe a time that you and a team mate - could be an app developer, tester or SEIT - disagreed. How did you resolve your differences?": Classic interview question for verifying what a candidate's personality is like.
- "What's your favourite continuous integration tool and why"

# Senior
If you work for a organization that has experienced growth and is now "established" in some sense, you may find some senior SEITs or other roles similar to that. In medium- to large-sized companies - companies a typical person may have heard of - there are often whole testing teams and sometimes engineering teams dedicated strictly to internal infrastructure. If you consider automated tests as infrastructure, this means you'll need dedicated folks to oversee project health. This includes writing and maintaining test code, but also includes managing people and computational resources. Good SEITs know how to put things together from a testing standpoint, and how to organize accordingly.

## When to hire
This is definitely a bit of a "I'll know it when I see it" situation. Teams can often get pretty far with hiring and retaining good intermediate SEITs or a combination of SEITs, testers and DevOps folks. In many larger organizations, test frameworks can grow to require their own dedicated team leads and managers. This is often where senior SEITs come in. Another scenario is where test automation efforts expect to ramp up, and having someone knowledagble in test automation can guide the process.

## What to look for
Senior SEITs have worked with _multiple_ forms of test automation at most or all layers of an application. They will likely be well versed in more than one area of test automation, and have built test frameworks from stratch and worked with existing test frameworks. Depending on the circumstance, they also may have some team lead or engineering management experience, and so may be able to work with more junior members on a team in addition to coding and configuring infrastructure. One of the most valuable aspects that senior SEITs can bring to the table is an informed opinion on test automation topics.   

## Key questions to ask
- "Suppose you were asked to review a test suite of 1000 tests. How would you approach this?": This question gets at how a candidate approaches a relatively complex situation. The idea here is spur discussion more than provide a flat answer. 
- "What's your preferred test framework and why? What's your least preferred?": In light of hiring someone who brings experience and opinions, this question asks for some of those opinions directly. It can also be a good indicator of communication abilities and temperment. 
- "Describe a time that you and a team mate - could be an app developer, tester or SEIT - disagreed. How did you resolve your differences?": Again, a classic interview question that could be critical if the candidate in question has to manage people.
- "Are you willing to mentor junior app developers and SEITs?"
- "Explain the value of end-to-end testing to me if I were the CEO of the company": Test automation can seem like an esoteric speciality to those not in engineering organizations. Senior developers of all kinds (in my opinion) should be able to talk in business terms in addition to technical terms.
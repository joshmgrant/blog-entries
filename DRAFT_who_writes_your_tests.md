Test automation has come a long way in the past decade or so. The [automation test pyramid](http://blog.goneopen.com/2010/08/test-automation-pyramid-review/) has been a good guide for how much and what kinds of tests to automate while test tools, design patterns and communities have grown and matured. 

But many teams still struggle when it comes to ownership of test automation. Who writes the tests? 

At the unit test level, this problem has been largely solved: developers own unit testing and it is considered part of writing application code. Mainstream languages have unit test tools and frameworks and practices like test driven development have become commonplace. Largely and open and shut case. 

What about at the higher layers? 

UI tests have historically been the responsibility of test/QA teams, to varying degrees of success. In some cases this can work out well particularly on teams where there is a lot of inter-team communication between developers, operations and testers. It can also work with highly motivated and technically skilled testers with coding ability. However, UI test efforts can also fail miserably if testers aren't skilled in coding or aren't provided enough support (managerial or infrastructural). In addition, UI tests are often expensive to write and maintain, adding extra complexity to managing UI test efforts. 

The service/API test layer can also be a quagmire. Writing good service layer tests often requires programming competency and a working understanding of the internals of an application. Testers generally - but not always! - do not have these skills. By definition, black box testing means being kept away from the internals being tested, which are the domain of developers. However, knowing how and what to test in service layer automated tests more suited to testers. Often a lack of testability or poor architecture for service layer tests can also be a problem and one that testers need to advocate for. To top it off, service layer testing can also be highly context dependent, unlike unit and UI automation. What works in one contex/application may not carry over well to another. 

Why does it matter who owns these automated tests? Because in many cases, initially _someone_ has to for test automation to succeed. As well, because there's often a split between development and test teams for who should own test automation, 

insurance - deductable maybe $750, 
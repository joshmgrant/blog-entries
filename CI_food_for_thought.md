A short bit of food for thought: 

In the book [Beautiful Testing](https://www.amazon.com/Beautiful-Testing-Professionals-Software-Practice/dp/0596159811), there's a chapter on large-scale test automation written by Alan Page from Microsoft. It discusses writing and running automated tests that check aspects of Microsoft-sized apps (read: large and relatively complex). These tests are written in C++ and require fairly significant dedicated resources to deploy and run. The idea of having such a setup for automated tests was mostly seen as enterprise-level for companies at the size and scope of Microsoft. This book was written in 2010. 

Fast forward to today, six years later. [TravisCI](https://travis-ci.org/) is a cloud-based service that offers free continuous integration services for open source projects (particularly ones found on Github). Basically, the same capabilities that Microsoft had are now available
- in the cloud
- can be managed casually by semi-professional developers
- do not require low-level programming knowledge
- can apply to simple apps
- for free.

Software development changes quickly but tools and approaches may move even quicker.
How would you test a generative AI? 

There's a lot of ink being spilled about generative AI. Whether it's text-based generation like ChatGPT or image-based like DALL-E, a lot of folks are interested in the future of this, whether [good](https://about.sourcegraph.com/blog/cheating-is-all-you-need), [bad](https://www.forbes.com/sites/ariannajohnson/2023/03/30/which-jobs-will-ai-replace-these-4-industries-will-be-heavily-impacted/?sh=57307bf55957), or [ugly](https://www.theverge.com/2023/5/27/23739913/chatgpt-ai-lawsuit-avianca-airlines-chatbot-research).

As a test developer, I'm interested in a simpler question: how can you test a generative AI? 

Lately I've been thinking about "going back to basics" in testing, and testing an AI should be tested in the same way. So I'm going to take some time to test [DALL-E](https://openai.com/product/dall-e-2), a generative AI using these three approaches:

2. Invariant Testing
3. Testing the Documentation
4. Boundary Value Analysis

These are all conventional software testing approaches, and more information can be found online about these topics. I'll try to include a short summary of each testing approach in each post. 

A _critically important note_ on this experiment is that I'll be creating _test cases_, which are slightly different from _user cases_. In a test case, a tester/developer is trying to learn about the underlying software, or validate some kind of assumption. Test cases aren't _necessarily_ the kind of cases that "real" users might undertake, but then again, they might be. The important distinction is that testing a piece of software is different from how an end user may use the system.


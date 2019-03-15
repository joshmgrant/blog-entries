Imagine this: your software team is working on a new release deployment with some major changes. It turns out that the work for this release is completed on a Friday afternoon, and ready to be deployed around 5:30 PM on Friday. Should your team release these changes then, or wait until Monday? 

I really enjoy this question. (Shoutout to [Noah Sussman](https://twitter.com/noahsussman) who provoked some thinking on this question for me a while back.)

It may seem like a silly question. But it can reveal some deeper insights to how teams release, how much autonomy teams have and how folks think about prioritizing work.

For me, the short answer is "yes, if the team's release process is strong enough to support such a release".

In my opinion, whether a team should release late on a Friday afternoon greatly depends on how mature that team is in terms of Continuous Delivery. Of the core ideas of continuous delivery is that a team has a strong pipeline that every release small or large needs to go through successfully or else the release candidate is automatically rejected. If such a pipeline doesn't exist - or a team isn't _sure_ it exists - then I'd say that the team should not deploy late on a Friday afternoon since there's no guarantee that the release won't cause any production or maintenance issues that occur on off-hours. Waiting until staff are readily available during work hours to address unforseen circumstances is better than scrambling to get people looking at those same issues haphazardly. 

On the other hand, if a team does have a strong continuous delivery pipeline in place, one of the benefits is being able to release anytime. This includes off-hours, and I would say yes to the Friday afternoon deployment. Keep in mind that such a pipeline would allow for some automated form of roll-back or roll-forward in case things go sideways. 

The true power of continuous delivery is shown here because teams have a greater level of autonomy over how and when to release new software. Decisions around how and what to features to write become decoupled from when to release these new features. I don' think there's anything wrong with releasing less often without using a continuous delivery approach. The problem arises when teams think they can handle "continuous" delivery when they can't, which sometimes comes back to how teams "own" their release processes. 
In hearthstone there is a card called Mantid Queen. At the start of each combat mantid gets a number of randomized buffs depending on the number of 
distinct unit tribes you control. There are a total of four distinct buffs: additional stats, windfury, divine shield and taunt. The most sought after buff is 
divine shield, without it, Mantid Queen is useless. The question is thus as follows: Given a number of n tribes, what are the odds of getting divine shield?

At first, the question may seem simple. However, there is a caveat that makes it more difficult than an ordinary combinatorial problem. You see, some buffs can only
trigger once while others may trigger infinitely many times. In this case, windfury, divine shield and taunt may only trigger once, whilst additional stats
can be obtained multiple times. Let us call effects that may only trigger once "special effects".

To solve the problem we use a dynamic programming approach. We start by introducing the function M(t,n), the probability that we trigger n special effects
given a total of t buffs. The main idea is that M(t,n) only depends on the state of the previous event. A total of n special effects after t buffs can only be achieved 
if either n-1 or n special effects have been achieved after t-1 buffs. More precisely we have that
* M(t,n) = M(t-1,n) * prob(the t-th buff is stats) + M(t-1,n-1) * prob(the t-th buff is a special effect) for $t \geq 1$.

It is obvious that M(0,n)=100% for all n as we cannot obtain a special effect if no buff is triggered. We now have the initial states, M(0,n), what remains to be able
to calculate M(t,n) is prob(the t-th buff is stats)= $p_{\text{stats}}$(t) and prob(the t-th buff is a special effect)=$p_{\text{special}}$(t)$.

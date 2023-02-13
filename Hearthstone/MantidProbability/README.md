In hearthstone there is a card called Mantid Queen. At the start of each combat mantid gets a number of randomized buffs depending on the number of 
distinct unit tribes you control. There are a total of four distinct buffs: additional stats, windfury, divine shield and taunt. The most sought after buff is 
divine shield, without it, Mantid Queen is useless. The question is thus as follows: Given a number of n tribes, what are the odds of getting divine shield?

At first, the question may seem simple. However, there is a caveat that makes it more difficult than an ordinary combinatorial problem. You see, some buffs can only
trigger once while others may trigger infinitely many times. In this case, windfury, divine shield and taunt may only trigger once, whilst additional stats
can be obtained multiple times. Let us call effects that may only trigger once "special effects".

To solve the problem we use a dynamic programming approach. We start by introducing the function M(t,n), the probability that we trigger n special effects
given a total of t buffs. The main idea is that M(t,n) only depends on the state of the previous event. A total of n special effects after t buffs can only be achieved 
if either n-1 or n special effects have been achieved after t-1 buffs. More precisely we have that
* $M(t,n) = M(t-1,n) \cdot$ prob(the t-th buff is stats given n special effects) + $M(t-1,n-1) \cdot$ prob(the t-th buff is a special effect given n special effects) for $t \geq 1$ and $1 \leq n \leq N$,

where N is the total distinct special effects. It is obvious that $M(0,n)=100$% for all n as we cannot obtain a special effect if no buff is triggered. To continue we have $M(t,0) = \frac{1}{N+1}$.  We now have the initial states, what remains to be able
to calculate $M(t,n)$ is $p_{\text{stats}}$(t,n) = prob(the t-th buff is stats given n special effects) and $p_{\text{special}}$(t,n)=prob(the t-th buff is a special effect given n special effects). These probabilities depend on how many special effects are still obtainable. If there are a total of N distinct special effects and n have been obtained, there are N-n still obtainable special effects. Thus N-n+1 buffs are available as additional stats is also a possible buff. The probability of gaining a special effect is thus given by $p_{\text{special}}(t,n)=\frac{N-n}{N-n+1}$. and the probability of gaining stats is $p_{\text{stats}}(t,n) =\frac{1}{N-n+1}$. We now have
* $M(t,n) = M(t-1,n) \cdot \frac{1}{N-n+1}  + M(t-1,n-1) \cdot \frac{N-n}{N-n+1}$ for $t \geq 1$ and $1 \leq n \leq N$ . 

The odds of gaining a particular special effect (divine shield) after t buffs is obtained by summing the probabilities $M(t,n)$ for $1 \leq n \leq N$ multiplied by $p_{divine}(n)$ = prob(divine shield given n special effects) = $\frac{ {n \choose x} N-1 \choose n-1}{N \choose n}
${N}\choose{k}$

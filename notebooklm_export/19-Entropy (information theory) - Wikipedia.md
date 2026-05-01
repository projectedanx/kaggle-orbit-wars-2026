> Source: https://en.wikipedia.org/wiki/Entropy_(information_theory)

Entropy (information theory) - Wikipedia
Jump to content [-]
Main menu
Main menu
move to sidebar hide
Navigation
Main page
Contents
Current events
Random article
About Wikipedia
Contact us
Contribute
Help
Learn to edit
Community portal
Recent changes
Upload file
Special pages
Search
Search [-]
Appearance
Donate
Create account
Log in [-]
Personal tools
Donate
Create account
Log in
Contents
move to sidebar hide
(Top)
1 Introduction Toggle Introduction subsection
1.1 Example
2 Definition Toggle Definition subsection
2.1 Measure theory
3 Example
4 Characterization Toggle Characterization subsection
4.1 Alternative characterization
4.1.1 Discussion
4.2 Alternative characterization via additivity and subadditivity
4.2.1 Discussion
5 Further properties
6 Aspects Toggle Aspects subsection
6.1 Relationship to thermodynamic entropy
6.2 Data compression
6.3 Entropy as a measure of diversity
6.4 Entropy of a sequence
6.5 Limitations of entropy in cryptography
6.6 Data as a Markov process
7 Efficiency (normalized entropy)
8 Entropy for continuous random variables Toggle Entropy for continuous random variables subsection
8.1 Differential entropy
8.2 Limiting density of discrete points
8.3 Relative entropy
9 Use in number theory
10 Use in combinatorics Toggle Use in combinatorics subsection
10.1 Loomis–Whitney inequality
10.2 Approximation to binomial coefficient
11 Use in machine learning
12 See also
13 Notes
14 References
15 Further reading Toggle Further reading subsection
15.1 Textbooks on information theory
16 External links [-]
Toggle the table of contents
Entropy (information theory)
[-]
46 languages
Afrikaans
العربية
Boarisch
Български
Bosanski
Català
کوردی
Čeština
Cymraeg
Dansk
Deutsch
Ελληνικά
Español
Euskara
فارسی
Suomi
Français
Galego
עברית
Magyar
Bahasa Indonesia
Italiano
日本語
한국어
Lietuvių
Олык марий
Nederlands
ਪੰਜਾਬੀ
Polski
Português
Română
Русский
Simple English
Slovenčina
Slovenščina
Shqip
Српски / srpski
Sunda
Svenska
ไทย
Türkçe
Українська
اردو
Tiếng Việt
粵語
中文
Edit links
Article
Talk [-]
English
Read
Edit
View history [-]
Tools
Tools
move to sidebar hide
Actions
Read
Edit
View history
General
What links here
Related changes
Upload file
Permanent link
Page information
Cite this page
Get shortened URL
Expand all
Edit interlanguage links
Print/export
Download as PDF
Printable version
In other projects
Wikimedia Commons
Wikidata item
Appearance
move to sidebar hide
Text
[-] 0 Small [x] 1 Standard [-] 2 Large
This page always uses small font size
Width
[x] 1 Standard [-] 0 Wide
The content is as wide as possible for your browser window.
Color (beta)
[-] os Automatic [x] day Light [-] night Dark
This page is always in light mode.
From Wikipedia, the free encyclopedia
Average uncertainty in variable's states
For other uses, see Entropy (disambiguation). 
This article may contain original research. Please improve it by verifying the claims made and adding inline citations. Statements consisting only of original research should be removed. ( March 2026) ( Learn how and when to remove this message)
This article needs additional citations for verification. Please help improve this article by adding citations to reliable sources. Unsourced material may be challenged and removed.
Find sources: "Entropy" information theory – news
· newspapers
· books
· scholar
· JSTOR ( February 2019) ( Learn how and when to remove this message)
Information theory 
Entropy
Differential entropy
Conditional entropy
Joint entropy
Mutual information
Directed information
Conditional mutual information
Relative entropy
Entropy rate
Limiting density of discrete points
Asymptotic equipartition property
Rate–distortion theory
Shannon's source coding theorem
Channel capacity
Noisy-channel coding theorem
Shannon–Hartley theorem
v
t
e
In information theory, the entropy of a random variable quantifies the average level of uncertainty or information associated with the variable's potential states or possible outcomes. This measures the expected amount of information needed to describe the state of the variable, considering the distribution of probabilities across all potential states. Given a discrete random variable X {\displaystyle X} 
, which may be any member x {\displaystyle x} 
within the set X {\displaystyle {\mathcal {X}}} 
and is distributed according to p : X → [ 0 , 1 ] {\displaystyle p\colon {\mathcal {X}}\to [0,1]} 
, the entropy is H ( X ) := − ∑ x ∈ X p ( x ) log  p ( x ) , {\displaystyle \mathrm {H} (X):=-\sum _{x\in {\mathcal {X}}}p(x)\log p(x),} 
where Σ {\displaystyle \Sigma } 
denotes the sum over the variable's possible values. [Note1] The choice of base for log {\displaystyle \log } 
, the logarithm, varies for different applications. Base 2 gives the unit of bits (or " shannons"), while base e gives "natural units" nat, and base 10 gives units of "dits", "bans", or " hartleys". An equivalent definition of entropy is the expected value of the self-information of a variable. [1]
The concept of information entropy was introduced by Claude Shannon in his 1948 paper " A Mathematical Theory of Communication", [2] [3] and is also referred to as Shannon entropy. Shannon's theory defines a data communication system composed of three elements: a source of data, a communication channel, and a receiver. The "fundamental problem of communication" – as expressed by Shannon – is for the receiver to be able to identify what data was generated by the source, based on the signal it receives through the channel. [2] [3] Shannon considered various ways to encode, compress, and transmit messages from a data source, and proved in his source coding theorem that the entropy represents an absolute mathematical limit on how well data from the source can be losslessly compressed onto a perfectly noiseless channel. Shannon strengthened this result considerably for noisy channels in his noisy-channel coding theorem.
Entropy in information theory is directly analogous to the entropy in statistical thermodynamics. The analogy results when the values of the random variable designate energies of microstates, so Gibbs's formula for the entropy is formally identical to Shannon's formula. Entropy has relevance to other areas of mathematics such as combinatorics and machine learning. The definition can be derived from a set of axioms establishing that entropy should be a measure of how informative the average outcome of a variable is. For a continuous random variable, differential entropy is analogous to entropy. The definition E [ − log  p ( X ) ] {\displaystyle \mathbb {E} [-\log p(X)]} 
generalizes the above.
Introduction
[ edit]
The core idea of information theory is that the "informational value" of a communicated message depends on the degree to which the content of the message is surprising. If a highly likely event occurs, the message carries very little information. On the other hand, if a highly unlikely event occurs, the message is much more informative. For instance, the knowledge that some particular number will not be the winning number of a lottery provides very little information, because any particular chosen number will almost certainly not win. However, knowledge that a particular number will win a lottery has high informational value because it communicates the occurrence of a very low probability event.
The information content, also called the surprisal or self-information, of an event E {\displaystyle E} 
is a function that increases as the probability p ( E ) {\displaystyle p(E)} 
of an event decreases. When p ( E ) {\displaystyle p(E)} 
is close to 1, the surprisal of the event is low, but if p ( E ) {\displaystyle p(E)} 
is close to 0, the surprisal of the event is high. This relationship is described by the function log  ( 1 p ( E ) ) , {\displaystyle \log \left({\frac {1}{p(E)}}\right),} 
where log {\displaystyle \log } 
is the logarithm, which gives 0 surprise when the probability of the event is 1. [4] In fact, log is the only function that satisfies a specific set of conditions defined in section § Characterization.
Hence, we can define the information, or surprisal, of an event E {\displaystyle E} 
by
I ( E ) = log  ( 1 p ( E ) ) , {\displaystyle I(E)=\log \left({\frac {1}{p(E)}}\right),} 
or equivalently, I ( E ) = − log  ( p ( E ) ) . {\displaystyle I(E)=-\log(p(E)).} 
Entropy measures the expected (i.e., average) amount of information conveyed by identifying the outcome of a random trial. [5] :67 This implies that rolling a die has higher entropy than tossing a coin because each outcome of a single die roll has smaller probability ( p = 1 / 6 {\displaystyle p=1/6} 
) than each outcome of a coin toss ( p = 1 / 2 {\displaystyle p=1/2} 
).
Consider a coin with probability p of landing on heads and probability 1 − p of landing on tails. The maximum surprise is when p = 1/2, for which one outcome is not expected over the other. In this case a coin flip has an entropy of one bit (similarly, one trit with equiprobable values contains log 2  3 {\displaystyle \log _{2}3} 
(about 1.58496) bits of information because it can have one of three values). The minimum surprise is when p = 0 (impossibility) or p = 1 (certainty) and the entropy is zero bits. When the entropy is zero, there is no uncertainty at all – no freedom of choice – no information. [6] Other values of p give entropies between zero and one bits.
Example
[ edit]
Information theory is useful to calculate the smallest amount of information required to convey a message, as in data compression. For example, consider the transmission of sequences comprising the 4 characters 'A', 'B', 'C', and 'D' over a binary channel. If all 4 letters are equally likely (25%), one cannot do better than using two bits to encode each letter. 'A' might code as '00', 'B' as '01', 'C' as '10', and 'D' as '11'. However, if the probabilities of each letter are unequal, say 'A' occurs with 70% probability, 'B' with 26%, and 'C' and 'D' with 2% each, one could assign variable length codes. In this case, 'A' would be coded as '0', 'B' as '10', 'C' as '110', and 'D' as '111'. With this representation, 70% of the time only one bit needs to be sent, 26% of the time two bits, and only 4% of the time 3 bits. On average, fewer than 2 bits are required since the entropy is lower (owing to the high prevalence of 'A' followed by 'B' – together 96% of characters). The calculation of the sum of probability-weighted log probabilities measures and captures this effect.
English text, treated as a string of characters, has fairly low entropy; i.e. it is fairly predictable. We can be fairly certain that, for example, 'e' will be far more common than 'z', that the combination 'qu' will be much more common than any other combination with a 'q' in it, and that the combination 'th' will be more common than 'z', 'q', or 'qu'. After the first few letters one can often guess the rest of the word. English text has between 0.6 and 1.3 bits of entropy per character of the message. [7] :234
Definition
[ edit]
Named after Boltzmann's Η-theorem, Shannon defined the entropy Η (Greek capital letter eta) of a discrete random variable X {\textstyle X} 
, which takes values in the set X {\displaystyle {\mathcal {X}}} 
and is distributed according to p : X → [ 0 , 1 ] {\displaystyle p:{\mathcal {X}}\to [0,1]} 
such that p ( x ) := P [ X = x ] {\displaystyle p(x):=\mathbb {P} [X=x]} 
:
H ( X ) = E [ I  ( X ) ] = E [ − log  p ( X ) ] . {\displaystyle \mathrm {H} (X)=\mathbb {E} [\operatorname {I} (X)]=\mathbb {E} [-\log p(X)].} 
Here E {\displaystyle \mathbb {E} } 
is the expected value operator, and I is the information content of X. [8] :11 [9] :19–20 I  ( X ) {\displaystyle \operatorname {I} (X)} 
is itself a random variable.
The entropy can explicitly be written as: H ( X ) = − ∑ x ∈ X p ( x ) log b  p ( x ) , {\displaystyle \mathrm {H} (X)=-\sum _{x\in {\mathcal {X}}}p(x)\log _{b}p(x),} 
where b is the base of the logarithm used. Common values of b are 2, Euler's number e, and 10, and the corresponding units of entropy are the bits for b = 2, nats for b = e, and bans for b = 10.
In the case of p ( x ) = 0 {\displaystyle p(x)=0} 
for some x ∈ X {\displaystyle x\in {\mathcal {X}}} 
, the value of the corresponding summand 0 log b(0) is taken to be 0, which is consistent with the limit: [10] :13 lim p → 0 + p log  ( p ) = 0. {\displaystyle \lim _{p\to 0^{+}}p\log(p)=0.} 
One may also define the conditional entropy of two variables X {\displaystyle X} 
and Y {\displaystyle Y} 
taking values from sets X {\displaystyle {\mathcal {X}}} 
and Y {\displaystyle {\mathcal {Y}}} 
respectively, as: [10] :16 H ( X | Y ) = − ∑ x , y ∈ X × Y p X , Y ( x , y ) log  p X , Y ( x , y ) p Y ( y ) , {\displaystyle \mathrm {H} (X|Y)=-\sum {x,y\in {\mathcal {X}}\times {\mathcal {Y}}}p{X,Y}(x,y)\log {\frac {p_{X,Y}(x,y)}{p_{Y}(y)}},} 
where p X , Y ( x , y ) := P [ X = x , Y = y ] {\displaystyle p_{X,Y}(x,y):=\mathbb {P} [X=x,Y=y]} 
and p Y ( y ) = P [ Y = y ] {\displaystyle p_{Y}(y)=\mathbb {P} [Y=y]} 
. This quantity should be understood as the remaining randomness in the random variable X {\displaystyle X} 
given the random variable Y {\displaystyle Y} 
.
Measure theory
[ edit]
Entropy can be formally defined in the language of measure theory as follows: [11] Let ( X , Σ , μ ) {\displaystyle (X,\Sigma ,\mu )} 
be a probability space. Let A ∈ Σ {\displaystyle A\in \Sigma } 
be an event. The surprisal of A {\displaystyle A} 
is σ μ ( A ) = − ln  μ ( A ) . {\displaystyle \sigma _{\mu }(A)=-\ln \mu (A).} 
The expected surprisal of A {\displaystyle A} 
is h μ ( A ) = μ ( A ) σ μ ( A ) . {\displaystyle h_{\mu }(A)=\mu (A)\sigma _{\mu }(A).} 
A μ {\displaystyle \mu } 
-almost partition is a set family P ⊆ P ( X ) {\displaystyle P\subseteq {\mathcal {P}}(X)} 
such that μ ( ∪  P ) = 1 {\displaystyle \mu (\mathop {\cup } P)=1} 
and μ ( A ∩ B ) = 0 {\displaystyle \mu (A\cap B)=0} 
for all distinct A , B ∈ P {\displaystyle A,B\in P} 
. (This is a relaxation of the usual conditions for a partition.) The entropy of P {\displaystyle P} 
is H μ ( P ) = ∑ A ∈ P h μ ( A ) . {\displaystyle \mathrm {H} _{\mu }(P)=\sum {A\in P}h{\mu }(A).} 
Let M {\displaystyle M} 
be a sigma-algebra on X {\displaystyle X} 
. The entropy of M {\displaystyle M} 
is H μ ( M ) = sup P ⊆ M H μ ( P ) . {\displaystyle \mathrm {H} _{\mu }(M)=\sup _{P\subseteq M}\mathrm {H} _{\mu }(P).} 
Finally, the entropy of the probability space is H μ ( Σ ) {\displaystyle \mathrm {H} _{\mu }(\Sigma )} 
, that is, the entropy with respect to μ {\displaystyle \mu } 
of the sigma-algebra of all measurable subsets of X {\displaystyle X} 
.
Example
[ edit] 
Entropy Η( X) (i.e. the expected surprisal) of a coin flip, measured in bits, graphed versus the bias of the coin Pr( X = 1), where X = 1 represents a result of heads. [10] :14–15
Here, the entropy is at most 1 bit, and to communicate the outcome of a coin flip (2 possible values) will require an average of at most 1 bit (exactly 1 bit for a fair coin). The result of a fair die (6 possible values) would have entropy log 2 6 bits.
Main articles: Binary entropy function and Bernoulli process
Consider tossing a coin with known, not necessarily fair, probabilities of coming up heads or tails; this can be modeled as a Bernoulli process.
The entropy of the unknown result of the next toss of the coin is maximized if the coin is fair (that is, if heads and tails both have equal probability 1/2). This is the situation of maximum uncertainty as it is most difficult to predict the outcome of the next toss; the result of each toss of the coin delivers one full bit of information. This is because H ( X ) = − ∑ i = 1 n p ( x i ) log b  p ( x i ) = − ∑ i = 1 2 1 2 log 2  1 2 = − ∑ i = 1 2 1 2 ⋅ ( − 1 ) = 1. {\displaystyle {\begin{aligned}\mathrm {H} (X)&=-\sum {i=1}^{n}{p(x{i})\log {b}p(x{i})}\&=-\sum _{i=1}^{2}{{\frac {1}{2}}\log _{2}{\frac {1}{2}}}\&=-\sum _{i=1}^{2}{{\frac {1}{2}}\cdot (-1)}=1.\end{aligned}}} 
However, if we know the coin is not fair, but comes up heads or tails with probabilities p and q, where p ≠ q, then there is less uncertainty. Every time it is tossed, one side is more likely to come up than the other. The reduced uncertainty is quantified in a lower entropy: on average each toss of the coin delivers less than one full bit of information. For example, if p = 0.7, then H ( X ) = − p log 2  p − q log 2  q = − 0.7 log 2  ( 0.7 ) − 0.3 log 2  ( 0.3 ) ≈ − 0.7 ⋅ ( − 0.515 ) − 0.3 ⋅ ( − 1.737 ) = 0.8816 < 1. {\displaystyle {\begin{aligned}\mathrm {H} (X)&=-p\log _{2}p-q\log _{2}q\[1ex]&=-0.7\log _{2}(0.7)-0.3\log _{2}(0.3)\[1ex]&\approx -0.7\cdot (-0.515)-0.3\cdot (-1.737)\[1ex]&=0.8816<1.\end{aligned}}} 
Uniform probability yields maximum uncertainty and therefore maximum entropy. Entropy, then, can only decrease from the value associated with uniform probability. The extreme case is that of a double-headed coin that never comes up tails, or a double-tailed coin that never results in a head. Then there is no uncertainty. The entropy is zero: each toss of the coin delivers no new information as the outcome of each coin toss is always certain. [10] :14–15
Characterization
[ edit]
To understand the meaning of −Σ p i log( p i), first define an information function I in terms of an event i with probability p i. The amount of information acquired due to the observation of event i follows from Shannon's solution of the fundamental properties of information: [12]
I( p) is monotonically decreasing in p: an increase in the probability of an event decreases the information from an observed event, and vice versa.
I(1) = 0: events that always occur do not communicate information.
I( p 1 · p 2) = I( p 1) + I( p 2): the information learned from independent events is the sum of the information learned from each event.
I( p) is a twice continuously differentiable function of p.
Given two independent events, if the first event can yield one of n equiprobable outcomes and another has one of m equiprobable outcomes then there are mn equiprobable outcomes of the joint event. This means that if log 2( n) bits are needed to encode the first value and log 2( m) to encode the second, one needs log 2( mn) = log 2( m) + log 2( n) to encode both.
Shannon discovered that a suitable choice of I {\displaystyle \operatorname {I} } 
is given by: [13] I  ( p ) = log  ( 1 p ) = − log  ( p ) . {\displaystyle \operatorname {I} (p)=\log \left({\tfrac {1}{p}}\right)=-\log(p).} 
In fact, the only possible values of I {\displaystyle \operatorname {I} } 
are I  ( u ) = k log  u {\displaystyle \operatorname {I} (u)=k\log u} 
for k < 0 {\displaystyle k<0} 
. Additionally, choosing a value for k is equivalent to choosing a value x > 1 {\displaystyle x>1} 
for k = − 1 / log  x {\displaystyle k=-1/\log x} 
, so that x corresponds to the base for the logarithm. Thus, entropy is characterized by the above four properties.
show Proof
Let I {\textstyle \operatorname {I} } 
be the information function which one assumes to be twice continuously differentiable, one has:
I  ( p 1 p 2 ) = I  ( p 1 ) + I  ( p 2 ) Starting from property 3 p 2 I ′  ( p 1 p 2 ) = I ′  ( p 1 ) taking the derivative w.r.t p 1 I ′  ( p 1 p 2 ) + p 1 p 2 I ″  ( p 1 p 2 ) = 0 taking the derivative w.r.t p 2 I ′  ( u ) + u I ″  ( u ) = 0 introducing u = p 1 p 2 ( u I ′  ( u ) ) ′ = 0 combining terms into one u I ′  ( u ) − k = 0 integrating w.r.t u , producing constant k {\displaystyle {\begin{aligned}&\operatorname {I} (p_{1}p_{2})&=\ &\operatorname {I} (p_{1})+\operatorname {I} (p_{2})&&\quad {\text{Starting from property 3}}\&p_{2}\operatorname {I} '(p_{1}p_{2})&=\ &\operatorname {I} '(p_{1})&&\quad {\text{taking the derivative w.r.t}}\ p_{1}\&\operatorname {I} '(p_{1}p_{2})+p_{1}p_{2}\operatorname {I} ''(p_{1}p_{2})&=\ &0&&\quad {\text{taking the derivative w.r.t}}\ p_{2}\&\operatorname {I} '(u)+u\operatorname {I} ''(u)&=\ &0&&\quad {\text{introducing}},u=p_{1}p_{2}\&(u\operatorname {I} '(u))'&=\ &0&&\quad {\text{combining terms into one}}\ \&u\operatorname {I} '(u)-k&=\ &0&&\quad {\text{integrating w.r.t}}\ u,{\text{producing constant}},k\\end{aligned}}} 
This differential equation leads to the solution I  ( u ) = k log  u + c {\displaystyle \operatorname {I} (u)=k\log u+c} 
for some k , c ∈ R {\displaystyle k,c\in \mathbb {R} } 
. Property 2 gives c = 0 {\displaystyle c=0} 
. Property 1 and 2 give that I  ( p ) ≥ 0 {\displaystyle \operatorname {I} (p)\geq 0} 
for all p ∈ [ 0 , 1 ] {\displaystyle p\in [0,1]} 
, so that k < 0 {\displaystyle k<0} 
.
The different units of information ( bits for the binary logarithm log 2, nats for the natural logarithm ln, bans for the decimal logarithm log 10 and so on) are constant multiples of each other. For instance, in case of a fair coin toss, heads provides log 2(2) = 1 bit of information, which is approximately 0.693 nats or 0.301 decimal digits. Because of additivity, n tosses provide n bits of information, which is approximately0.693n ** nats or0.301n ** decimal digits.
The meaning of the events observed (the meaning of messages) does not matter in the definition of entropy. Entropy only takes into account the probability of observing a specific event, so the information it encapsulates is information about the underlying probability distribution, not the meaning of the events themselves.
Alternative characterization
[ edit]
Another characterization of entropy uses the following properties. We denote p i = Pr( X = x i) and Η n( p 1, ..., p n) = Η( X).
Continuity: H should be continuous, so that changing the values of the probabilities by a very small amount should only change the entropy by a small amount.
Symmetry: H should be unchanged if the outcomes x i are re-ordered. That is, H n ( p 1 , p 2 , … , p n ) = H n ( p i 1 , p i 2 , … , p i n ) {\displaystyle \mathrm {H} {n}\left(p{1},p_{2},\ldots ,p_{n}\right)=\mathrm {H} {n}\left(p{i_{1}},p_{i_{2}},\ldots ,p_{i_{n}}\right)} for any permutation { i 1 , ... , i n } {\displaystyle {i_{1},...,i_{n}}} of { 1 , ... , n } {\displaystyle {1,...,n}} .
Maximum: H n {\displaystyle \mathrm {H} {n}} should be maximal if all the outcomes are equally likely i.e. H n ( p 1 , … , p n ) ≤ H n ( 1 n , … , 1 n ) {\displaystyle \mathrm {H} {n}(p{1},\ldots ,p{n})\leq \mathrm {H} _{n}\left({\frac {1}{n}},\ldots ,{\frac {1}{n}}\right)} .
Increasing number of outcomes: for equiprobable events, the entropy should increase with the number of outcomes i.e. H n ( 1 n , … , 1 n ⏟ n ) < H n + 1 ( 1 n + 1 , … , 1 n + 1 ⏟ n + 1 ) . {\displaystyle \mathrm {H} _{n}{\bigg (}\underbrace {{\frac {1}{n}},\ldots ,{\frac {1}{n}}} _{n}{\bigg )}<\mathrm {H} _{n+1}{\bigg (}\underbrace {{\frac {1}{n+1}},\ldots ,{\frac {1}{n+1}}} _{n+1}{\bigg )}.}
Additivity: given an ensemble of n uniformly distributed elements that are partitioned into k boxes (sub-systems) with b 1, ..., b k elements each, the entropy of the whole ensemble should be equal to the sum of the entropy of the system of boxes and the individual entropies of the boxes, each weighted with the probability of being in that particular box.
Discussion
[ edit]
The rule of additivity has the following consequences: for positive integers b i where b 1 + ... + b k = n, H n ( 1 n , … , 1 n ) = H k ( b 1 n , … , b k n ) + ∑ i = 1 k b i n H b i ( 1 b i , … , 1 b i ) . {\displaystyle \mathrm {H} {n}\left({\frac {1}{n}},\ldots ,{\frac {1}{n}}\right)=\mathrm {H} {k}\left({\frac {b{1}}{n}},\ldots ,{\frac {b{k}}{n}}\right)+\sum {i=1}^{k}{\frac {b{i}}{n}},\mathrm {H} {b{i}}\left({\frac {1}{b_{i}}},\ldots ,{\frac {1}{b_{i}}}\right).} 
Choosing k = n, b 1 = ... = b n = 1 this implies that the entropy of a certain outcome is zero: Η 1(1) = 0. This implies that the efficiency of a source set with n symbols can be defined simply as being equal to its n-ary entropy. See also Redundancy (information theory).
The characterization here imposes an additive property with respect to a partition of a set. Meanwhile, the conditional probability is defined in terms of a multiplicative property, P ( A ∣ B ) ⋅ P ( B ) = P ( A ∩ B ) {\displaystyle P(A\mid B)\cdot P(B)=P(A\cap B)} 
. Observe that a logarithm mediates between these two operations. The conditional entropy and related quantities inherit simple relation, in turn. The measure theoretic definition in the previous section defined the entropy as a sum over expected surprisals μ ( A ) ⋅ ln  μ ( A ) {\displaystyle \mu (A)\cdot \ln \mu (A)} 
for an extremal partition. Here the logarithm is ad hoc and the entropy is not a measure in itself. At least in the information theory of a binary string, log 2 {\displaystyle \log _{2}} 
lends itself to practical interpretations.
Motivated by such relations, a plethora of related and competing quantities have been defined. For example, David Ellerman's analysis of a "logic of partitions" defines a competing measure in structures dual to that of subsets of a universal set. [14] Information is quantified as "dits" (distinctions), a measure on partitions. "Dits" can be converted into Shannon's bits, to get the formulas for conditional entropy, and so on.
Alternative characterization via additivity and subadditivity
[ edit]
Another succinct axiomatic characterization of Shannon entropy was given by Aczél, Forte and Ng, [15] via the following properties:
Subadditivity: H ( X , Y ) ≤ H ( X ) + H ( Y ) {\displaystyle \mathrm {H} (X,Y)\leq \mathrm {H} (X)+\mathrm {H} (Y)} for jointly distributed random variables X , Y {\displaystyle X,Y} .
Additivity: H ( X , Y ) = H ( X ) + H ( Y ) {\displaystyle \mathrm {H} (X,Y)=\mathrm {H} (X)+\mathrm {H} (Y)} when the random variables X , Y {\displaystyle X,Y} are independent.
Expansibility: H n + 1 ( p 1 , … , p n , 0 ) = H n ( p 1 , … , p n ) {\displaystyle \mathrm {H} {n+1}(p{1},\ldots ,p_{n},0)=\mathrm {H} {n}(p{1},\ldots ,p_{n})} , i.e., adding an outcome with probability zero does not change the entropy.
Symmetry: H n ( p 1 , … , p n ) {\displaystyle \mathrm {H} {n}(p{1},\ldots ,p_{n})} is invariant under permutation of p 1 , … , p n {\displaystyle p_{1},\ldots ,p_{n}} .
Small for small probabilities: lim q → 0 + H 2 ( 1 − q , q ) = 0 {\displaystyle \lim _{q\to 0^{+}}\mathrm {H} _{2}(1-q,q)=0} .
Discussion
[ edit]
It was shown that any function H {\displaystyle \mathrm {H} } 
satisfying the above properties must be a constant multiple of Shannon entropy, with a non-negative constant. [15] Compared to the previously mentioned characterizations of entropy, this characterization focuses on the properties of entropy as a function of random variables (subadditivity and additivity), rather than the properties of entropy as a function of the probability vector p 1 , … , p n {\displaystyle p_{1},\ldots ,p_{n}} 
.
It is worth noting that if we drop the "small for small probabilities" property, then H {\displaystyle \mathrm {H} } 
must be a non-negative linear combination of the Shannon entropy and the Hartley entropy. [15]
Further properties
[ edit]
The Shannon entropy satisfies the following properties, for some of which it is useful to interpret entropy as the expected amount of information learned (or uncertainty eliminated) by revealing the value of a random variable X:
Adding or removing an event with probability zero does not contribute to the entropy: H n + 1 ( p 1 , … , p n , 0 ) = H n ( p 1 , … , p n ) . {\displaystyle \mathrm {H} {n+1}(p{1},\ldots ,p_{n},0)=\mathrm {H} {n}(p{1},\ldots ,p_{n}).}
The maximal entropy of an event with n different outcomes is log b( n): it is attained by the uniform probability distribution. That is, uncertainty is maximal when all possible events are equiprobable: [10] :29 H ( p 1 , … , p n ) ≤ log b  n . {\displaystyle \mathrm {H} (p_{1},\dots ,p_{n})\leq \log _{b}n.}
The entropy or the amount of information revealed by evaluating ( X, Y) (that is, evaluating X and Y simultaneously) is equal to the information revealed by conducting two consecutive experiments: first evaluating the value of Y, then revealing the value of X given that you know the value of Y. This may be written as: [10] :16 H ( X , Y ) = H ( X | Y ) + H ( Y ) = H ( Y | X ) + H ( X ) . {\displaystyle \mathrm {H} (X,Y)=\mathrm {H} (X|Y)+\mathrm {H} (Y)=\mathrm {H} (Y|X)+\mathrm {H} (X).}
If Y = f ( X ) {\displaystyle Y=f(X)} where f {\displaystyle f} is a function, then H ( f ( X ) | X ) = 0 {\displaystyle \mathrm {H} (f(X)|X)=0} . Applying the previous formula to H ( X , f ( X ) ) {\displaystyle \mathrm {H} (X,f(X))} yields H ( X ) + H ( f ( X ) | X ) = H ( f ( X ) ) + H ( X | f ( X ) ) , {\displaystyle \mathrm {H} (X)+\mathrm {H} (f(X)|X)=\mathrm {H} (f(X))+\mathrm {H} (X|f(X)),} so H ( f ( X ) ) ≤ H ( X ) {\displaystyle \mathrm {H} (f(X))\leq \mathrm {H} (X)} , the entropy of a variable can only decrease when the latter is passed through a function.
If X and Y are two independent random variables, then knowing the value of Y doesn't influence our knowledge of the value of X (since the two don't influence each other by independence): H ( X | Y ) = H ( X ) . {\displaystyle \mathrm {H} (X|Y)=\mathrm {H} (X).}
More generally, for any random variables X and Y, we have [10] :29 H ( X | Y ) ≤ H ( X ) . {\displaystyle \mathrm {H} (X|Y)\leq \mathrm {H} (X).}
The entropy of two simultaneous events is no more than the sum of the entropies of each individual event i.e., H ( X , Y ) ≤ H ( X ) + H ( Y ) {\displaystyle \mathrm {H} (X,Y)\leq \mathrm {H} (X)+\mathrm {H} (Y)} , with equality if and only if the two events are independent. [10] :28
The entropy H ( p ) {\displaystyle \mathrm {H} (p)} is concave in the probability mass function p {\displaystyle p} , i.e. [10] :30 H ( λ p 1 + ( 1 − λ ) p 2 ) ≥ λ H ( p 1 ) + ( 1 − λ ) H ( p 2 ) {\displaystyle \mathrm {H} (\lambda p_{1}+(1-\lambda )p_{2})\geq \lambda \mathrm {H} (p_{1})+(1-\lambda )\mathrm {H} (p_{2})} for all probability mass functions p 1 , p 2 {\displaystyle p_{1},p_{2}} and 0 ≤ λ ≤ 1 {\displaystyle 0\leq \lambda \leq 1} . [10] :32
Accordingly, the negative entropy (negentropy) function is convex, and its convex conjugate is LogSumExp.
Aspects
[ edit]
Relationship to thermodynamic entropy
[ edit]
Main article: Entropy in thermodynamics and information theory
The inspiration for adopting the word entropy in information theory came from the close resemblance between Shannon's formula and very similar known formulae from statistical mechanics.
In statistical thermodynamics the most general formula for the thermodynamic entropy S of a thermodynamic system is the Gibbs entropy S = − k B ∑ i p i ln  p i , {\displaystyle S=-k_{\text{B}}\sum {i}p{i}\ln p_{i},,} 
where k B is the Boltzmann constant, and p i is the probability of a microstate. The Gibbs entropy was defined by J. Willard Gibbs in 1878 after earlier work by Ludwig Boltzmann (1872). [16]
The Gibbs entropy translates over almost unchanged into the world of quantum physics to give the von Neumann entropy introduced by John von Neumann in 1927: S = − k B T r ( ρ ln  ρ ) , {\displaystyle S=-k_{\text{B}},{\rm {Tr}}(\rho \ln \rho ),,} 
where ρ is the density matrix of the quantum mechanical system and Tr is the trace. [17]
At an everyday practical level, the links between information entropy and thermodynamic entropy are not evident. Physicists and chemists are apt to be more interested in changes in entropy as a system spontaneously evolves away from its initial conditions, in accordance with the second law of thermodynamics, rather than an unchanging probability distribution. As the minuteness of the Boltzmann constant k B indicates, the changes in S / k B for even tiny amounts of substances in chemical and physical processes represent amounts of entropy that are extremely large compared to anything in data compression or signal processing. In classical thermodynamics, entropy is defined in terms of macroscopic measurements and makes no reference to any probability distribution, which is central to the definition of information entropy.
The connection between thermodynamics and what is now known as information theory was first made by Boltzmann and expressed by his equation:
S = k B ln  W , {\displaystyle S=k_{\text{B}}\ln W,} 
where S {\displaystyle S} 
is the thermodynamic entropy of a particular macrostate (defined by thermodynamic parameters such as temperature, volume, energy, etc.), W is the number of microstates (various combinations of particles in various energy states) that can yield the given macrostate, and k B is the Boltzmann constant. [18] It is assumed that each microstate is equally likely, so that the probability of a given microstate is p i = 1/ W. When these probabilities are substituted into the above expression for the Gibbs entropy (or equivalently k B times the Shannon entropy), Boltzmann's equation results. In information theoretic terms, the information entropy of a system is the amount of "missing" information needed to determine a microstate, given the macrostate.
In the view of Jaynes (1957), [19] thermodynamic entropy, as explained by statistical mechanics, should be seen as an application of Shannon's information theory: the thermodynamic entropy is interpreted as being proportional to the amount of further Shannon information needed to define the detailed microscopic state of the system, that remains uncommunicated by a description solely in terms of the macroscopic variables of classical thermodynamics, with the constant of proportionality being just the Boltzmann constant. Adding heat to a system increases its thermodynamic entropy because it increases the number of possible microscopic states of the system that are consistent with the measurable values of its macroscopic variables, making any complete state description longer. (See article: maximum entropy thermodynamics). Maxwell's demon can (hypothetically) reduce the thermodynamic entropy of a system by using information about the states of individual molecules; but, as Landauer (from 1961) and co-workers [20] have shown, to function the demon himself must increase thermodynamic entropy in the process, by at least the amount of Shannon information he proposes to first acquire and store; and so the total thermodynamic entropy does not decrease (which resolves the paradox). Landauer's principle imposes a lower bound on the amount of heat a computer must generate to process a given amount of information, though modern computers are far less efficient.
Data compression
[ edit]
Main articles: Shannon's source coding theorem and Data compression
Shannon's definition of entropy, when applied to an information source, can determine the minimum channel capacity required to reliably transmit the source as encoded binary digits. Shannon's entropy measures the information contained in a message as opposed to the portion of the message that is determined (or predictable). Examples of the latter include redundancy in language structure or statistical properties relating to the occurrence frequencies of letter or word pairs, triplets etc. The minimum channel capacity can be realized in theory by using the typical set or in practice using Huffman, Lempel–Ziv or arithmetic coding. (See also Kolmogorov complexity.) In practice, compression algorithms deliberately include some judicious redundancy in the form of checksums to protect against errors. The entropy rate of a data source is the average number of bits per symbol needed to encode it. Shannon's experiments with human predictors show an information rate between 0.6 and 1.3 bits per character in English; [21] the PPM compression algorithm can achieve a compression ratio of 1.5 bits per character in English text.
If a compression scheme is lossless – one in which you can always recover the entire original message by decompression – then a compressed message has the same quantity of information as the original but is communicated in fewer characters. It has more information (higher entropy) per character. A compressed message has less redundancy. Shannon's source coding theorem states a lossless compression scheme cannot compress messages, on average, to have more than one bit of information per bit of message, but that any value less than one bit of information per bit of message can be attained by employing a suitable coding scheme. The entropy of a message per bit multiplied by the length of that message is a measure of how much total information the message contains. Shannon's theorem also implies that no lossless compression scheme can shorten all messages. If some messages come out shorter, at least one must come out longer due to the pigeonhole principle. In practical use, this is generally not a problem, because one is usually only interested in compressing certain types of messages, such as a document in English, as opposed to gibberish text, or digital photographs rather than noise, and it is unimportant if a compression algorithm makes some unlikely or uninteresting sequences larger.
A 2011 study in Science estimates the world's technological capacity to store and communicate optimally compressed information normalized on the most effective compression algorithms available in the year 2007, therefore estimating the entropy of the technologically available sources. [22] :60–65
All figures in entropically compressed exabytes
The authors estimate humankind technological capacity to store information (fully entropically compressed) in 1986 and again in 2007. They break the information into three categories—to store information on a medium, to receive information through one-way broadcast networks, or to exchange information through two-way telecommunications networks. [22]
Entropy as a measure of diversity
[ edit]
Main article: Diversity index
Entropy is one of several ways to measure biodiversity and is applied in the form of the Shannon index. [23] A diversity index is a quantitative statistical measure of how many different types exist in a dataset, such as species in a community, accounting for ecological richness, evenness, and dominance. Specifically, Shannon entropy is the logarithm of 1 D, the true diversity index with parameter equal to 1. The Shannon index is related to the proportional abundances of types.
Entropy of a sequence
[ edit]
There are a number of entropy-related concepts that mathematically quantify information content of a sequence or message:
the self-information of an individual message or symbol taken from a given probability distribution (message or sequence seen as an individual event),
the joint entropy of the symbols forming the message or sequence (seen as a set of events),
the entropy rate of a stochastic process (message or sequence is seen as a succession of events).
(The "rate of self-information" can also be defined for a particular sequence of messages or symbols generated by a given stochastic process: this will always be equal to the entropy rate in the case of a stationary process.) Other quantities of information are also used to compare or relate different sources of information.
It is important not to confuse the above concepts. Often it is only clear from context which one is meant. For example, when someone says that the "entropy" of the English language is about 1 bit per character, they are actually modeling the English language as a stochastic process and talking about its entropy rate. Shannon himself used the term in this way.
If very large blocks are used, the estimate of per-character entropy rate may become artificially low because the probability distribution of the sequence is not known exactly; it is only an estimate. If one considers the text of every book ever published as a sequence, with each symbol being the text of a complete book, and if there are N published books, and each book is only published once, the estimate of the probability of each book is 1/ N, and the entropy (in bits) is −log 2(1/ N) = log 2( N). As a practical code, this corresponds to assigning each book a unique identifier and using it in place of the text of the book whenever one wants to refer to the book. This is enormously useful for talking about books, but it is not so useful for characterizing the information content of an individual book, or of language in general: it is not possible to reconstruct the book from its identifier without knowing the probability distribution, that is, the complete text of all the books. The key idea is that the complexity of the probabilistic model must be considered. Kolmogorov complexity is a theoretical generalization of this idea that allows the consideration of the information content of a sequence independent of any particular probability model; it considers the shortest program for a universal computer that outputs the sequence. A code that achieves the entropy rate of a sequence for a given model, plus the codebook (i.e. the probabilistic model), is one such program, but it may not be the shortest.
The Fibonacci sequence is 1, 1, 2, 3, 5, 8, 13, .... treating the sequence as a message and each number as a symbol, there are almost as many symbols as there are characters in the message, giving an entropy of approximately log 2( n). The first 128 symbols of the Fibonacci sequence has an entropy of approximately 7 bits/symbol, but the sequence can be expressed using a formula [ F( n) = F( n−1) + F( n−2) for n = 3, 4, 5, ..., F(1) =1, F(2) = 1] and this formula has a much lower entropy and applies to any length of the Fibonacci sequence.
Limitations of entropy in cryptography
[ edit]
In cryptanalysis, entropy is often roughly used as a measure of the unpredictability of a cryptographic key, though its real uncertainty is unmeasurable. For example, a 128-bit key that is uniformly and randomly generated has 128 bits of entropy. It also takes (on average) 2 127 {\displaystyle 2^{127}} 
guesses to break by brute force. Entropy fails to capture the number of guesses required if the possible keys are not chosen uniformly. [24] [25] Instead, a measure called guesswork can be used to measure the effort required for a brute force attack. [26]
Other problems may arise from non-uniform distributions used in cryptography. For example, a 1,000,000-digit binary one-time pad using exclusive or. If the pad has 1,000,000 bits of entropy, it is perfect. If the pad has 999,999 bits of entropy, evenly distributed (each individual bit of the pad having 0.999999 bits of entropy) it may provide good security. But if the pad has 999,999 bits of entropy, where the first bit is fixed and the remaining 999,999 bits are perfectly random, the first bit of the ciphertext will not be encrypted at all.
Data as a Markov process
[ edit]
A common way to define entropy for text is based on the Markov model of text. For an order-0 source (each character is selected independent of the last characters), the binary entropy is:
H ( S ) = − ∑ i p i log  p i , {\displaystyle \mathrm {H} ({\mathcal {S}})=-\sum {i}p{i}\log p_{i},} 
where p i is the probability of i. For a first-order Markov source (one in which the probability of selecting a character is dependent only on the immediately preceding character), the entropy rate is: [citationneeded]
H ( S ) = − ∑ i p i ∑ j p i ( j ) log  p i ( j ) , {\displaystyle \mathrm {H} ({\mathcal {S}})=-\sum {i}p{i}\sum {j}\ p{i}(j)\log p_{i}(j),} 
where i is a state (certain preceding characters) and p i ( j ) {\displaystyle p_{i}(j)} 
is the probability of j given i as the previous character.
For a second order Markov source, the entropy rate is
H ( S ) = − ∑ i p i ∑ j p i ( j ) ∑ k p i , j ( k ) log  p i , j ( k ) . {\displaystyle \mathrm {H} ({\mathcal {S}})=-\sum {i}p{i}\sum {j}p{i}(j)\sum {k}p{i,j}(k)\ \log p_{i,j}(k).} 
Efficiency (normalized entropy)
[ edit]
A source set X {\displaystyle {\mathcal {X}}} 
with a non-uniform distribution will have less entropy than the same set with a uniform distribution (i.e. the "optimized alphabet"). This deficiency in entropy can be expressed as a ratio called efficiency: [27]
η ( X ) = H H max = − ∑ i = 1 n p ( x i ) log b  ( p ( x i ) ) log b  ( n ) . {\displaystyle \eta (X)={\frac {H}{H_{\text{max}}}}=-\sum {i=1}^{n}{\frac {p(x{i})\log {b}(p(x{i}))}{\log _{b}(n)}}.} 
Applying the basic properties of the logarithm, this quantity can also be expressed as: η ( X ) = − ∑ i = 1 n p ( x i ) log b  ( p ( x i ) ) log b  ( n ) = ∑ i = 1 n log b  ( p ( x i ) − p ( x i ) ) log b  ( n ) = ∑ i = 1 n log n  ( p ( x i ) − p ( x i ) ) = log n  ( ∏ i = 1 n p ( x i ) − p ( x i ) ) . {\displaystyle {\begin{aligned}\eta (X)&=-\sum {i=1}^{n}{\frac {p(x{i})\log {b}(p(x{i}))}{\log _{b}(n)}}=\sum {i=1}^{n}{\frac {\log {b}\left(p(x{i})^{-p(x{i})}\right)}{\log _{b}(n)}}\[1ex]&=\sum {i=1}^{n}\log {n}\left(p(x{i})^{-p(x{i})}\right)=\log {n}\left(\prod {i=1}^{n}p(x{i})^{-p(x{i})}\right).\end{aligned}}} 
Efficiency has utility in quantifying the effective use of a communication channel. This formulation is also referred to as the normalized entropy, as the entropy is divided by the maximum entropy log b  ( n ) {\displaystyle {\log _{b}(n)}} 
. Furthermore, the efficiency is indifferent to the choice of (positive) base b, as indicated by the insensitivity within the final logarithm above thereto.
Entropy for continuous random variables
[ edit]
Differential entropy
[ edit]
Main article: Differential entropy
The Shannon entropy is restricted to random variables taking discrete values. The corresponding formula for a continuous random variable with probability density function f( x) with finite or infinite support X {\displaystyle \mathbb {X} } 
on the real line is defined by analogy, using the above form of the entropy as an expectation: [10] :224
H ( X ) = E [ − log  f ( X ) ] = − ∫ X f ( x ) log  f ( x ) d x . {\displaystyle \mathrm {H} (X)=\mathbb {E} [-\log f(X)]=-\int _{\mathbb {X} }f(x)\log f(x),\mathrm {d} x.} 
This is the differential entropy (or continuous entropy). A precursor of the continuous entropy h[ f] is the expression for the functional Η in the H-theorem of Boltzmann.
Although the analogy between both functions is suggestive, the following question must be set: is the differential entropy a valid extension of the Shannon discrete entropy? Differential entropy lacks a number of properties that the Shannon discrete entropy has – it can even be negative – and corrections have been suggested, notably limiting density of discrete points.
To answer this question, a connection must be established between the two functions:
In order to obtain a generally finite measure as the bin size goes to zero. In the discrete case, the bin size is the (implicit) width of each of the n (finite or infinite) bins whose probabilities are denoted by p n. As the continuous domain is generalized, the width must be made explicit.
To do this, start with a continuous function f discretized into bins of size Δ {\displaystyle \Delta } 
. By the mean-value theorem there exists a value x i in each bin such that f ( x i ) Δ = ∫ i Δ ( i + 1 ) Δ f ( x ) d x {\displaystyle f(x_{i})\Delta =\int _{i\Delta }^{(i+1)\Delta }f(x),dx} 
the integral of the function f can be approximated (in the Riemannian sense) by ∫ − ∞ ∞ f ( x ) d x = lim Δ → 0 ∑ i = − ∞ ∞ f ( x i ) Δ , {\displaystyle \int _{-\infty }^{\infty }f(x),dx=\lim _{\Delta \to 0}\sum {i=-\infty }^{\infty }f(x{i})\Delta ,} 
where this limit and "bin size goes to zero" are equivalent.
We will denote H Δ := − ∑ i = − ∞ ∞ f ( x i ) Δ log  ( f ( x i ) Δ ) {\displaystyle \mathrm {H} ^{\Delta }:=-\sum {i=-\infty }^{\infty }f(x{i})\Delta \log \left(f(x_{i})\Delta \right)} 
and expanding the logarithm, we have H Δ = − ∑ i = − ∞ ∞ f ( x i ) Δ log  ( f ( x i ) ) − ∑ i = − ∞ ∞ f ( x i ) Δ log  ( Δ ) . {\displaystyle \mathrm {H} ^{\Delta }=-\sum {i=-\infty }^{\infty }f(x{i})\Delta \log(f(x_{i}))-\sum {i=-\infty }^{\infty }f(x{i})\Delta \log(\Delta ).} 
As Δ → 0, we have
∑ i = − ∞ ∞ f ( x i ) Δ → ∫ − ∞ ∞ f ( x ) d x = 1 ∑ i = − ∞ ∞ f ( x i ) Δ log  ( f ( x i ) ) → ∫ − ∞ ∞ f ( x ) log  f ( x ) d x . {\displaystyle {\begin{aligned}\sum {i=-\infty }^{\infty }f(x{i})\Delta &\to \int {-\infty }^{\infty }f(x),dx=1\\sum {i=-\infty }^{\infty }f(x{i})\Delta \log(f(x{i}))&\to \int _{-\infty }^{\infty }f(x)\log f(x),dx.\end{aligned}}} 
Note; log(Δ) → −∞ as Δ → 0, requires a special definition of the differential or continuous entropy:
h [ f ] = lim Δ → 0 ( H Δ + log  Δ ) = − ∫ − ∞ ∞ f ( x ) log  f ( x ) d x , {\displaystyle h[f]=\lim _{\Delta \to 0}\left(\mathrm {H} ^{\Delta }+\log \Delta \right)=-\int _{-\infty }^{\infty }f(x)\log f(x),dx,} 
which is, as said before, referred to as the differential entropy. This means that the differential entropy is not a limit of the Shannon entropy for n → ∞. Rather, it differs from the limit of the Shannon entropy by an infinite offset (see also the article on information dimension).
Limiting density of discrete points
[ edit]
Main article: Limiting density of discrete points
It turns out as a result that, unlike the Shannon entropy, the differential entropy is not in general a good measure of uncertainty or information. For example, the differential entropy can be negative; also it is not invariant under continuous co-ordinate transformations. This problem may be illustrated by a change of units when x is a dimensioned variable. f( x) will then have the units of 1/ x. The argument of the logarithm must be dimensionless, otherwise it is improper, so that the differential entropy as given above will be improper. If Δ is some "standard" value of x (i.e. "bin size") and therefore has the same units, then a modified differential entropy may be written in proper form as: H = ∫ − ∞ ∞ f ( x ) log  ( f ( x ) Δ ) d x , {\displaystyle \mathrm {H} =\int _{-\infty }^{\infty }f(x)\log(f(x),\Delta ),dx,} 
and the result will be the same for any choice of units for x. In fact, the limit of discrete entropy as N → ∞ {\displaystyle N\rightarrow \infty } 
would also include a term of log  ( N ) {\displaystyle \log(N)} 
, which would in general be infinite. This is expected: continuous variables would typically have infinite entropy when discretized. The limiting density of discrete points is really a measure of how much easier a distribution is to describe than a distribution that is uniform over its quantization scheme.
Relative entropy
[ edit]
Main article: Generalized relative entropy
Another useful measure of entropy that works equally well in the discrete and the continuous case is the relative entropy of a distribution. It is defined as the Kullback–Leibler divergence from the distribution to a reference measure m as follows. Assume that a probability distribution p is absolutely continuous with respect to a measure m, i.e. is of the form p( dx) = f( x) m( dx) for some non-negative m-integrable function f with m-integral 1, then the relative entropy can be defined as D K L ( p ‖ m ) = ∫ log  ( f ( x ) ) p ( d x ) = ∫ f ( x ) log  ( f ( x ) ) m ( d x ) . {\displaystyle D_{\mathrm {KL} }(p|m)=\int \log(f(x))p(dx)=\int f(x)\log(f(x))m(dx).} 
In this form the relative entropy generalizes (up to change in sign) both the discrete entropy, where the measure m is the counting measure, and the differential entropy, where the measure m is the Lebesgue measure. If the measure m is itself a probability distribution, the relative entropy is non-negative, and zero if p = m as measures. It is defined for any measure space, hence coordinate independent and invariant under co-ordinate reparameterizations if one properly takes into account the transformation of the measure m. The relative entropy, and (implicitly) entropy and differential entropy, do depend on the "reference" measure m.
Use in number theory
[ edit]
Terence Tao used entropy to make a useful connection trying to solve the Erdős discrepancy problem. [28] [29]
Intuitively the idea behind the proof was if there is low information in terms of the Shannon entropy between consecutive random variables (here the random variable is defined using the Liouville function (which is a useful mathematical function for studying distribution of primes) X H = λ ( n + H ) {\displaystyle \lambda (n+H)} 
). And in an interval [n, n+H] the sum over that interval could become arbitrary large. For example, a sequence of +1's (which are values of X H could take) have trivially low entropy and their sum would become big. But the key insight was showing a reduction in entropy by non negligible amounts as one expands H leading inturn to unbounded growth of a mathematical object over this random variable is equivalent to showing the unbounded growth per the Erdős discrepancy problem.
The proof is quite involved and it brought together breakthroughs not just in novel use of Shannon entropy, but also it used the Liouville function along with averages of modulated multiplicative functions [30] in short intervals. Proving it also broke the "parity barrier" [31] for this specific problem.
While the use of Shannon entropy in the proof is novel it is likely to open new research in this direction.
Use in combinatorics
[ edit]
Entropy has become a useful quantity in combinatorics.
Loomis–Whitney inequality
[ edit]
A simple example of this is an alternative proof of the Loomis–Whitney inequality: for every subset A ⊆ Z d, we have | A | d − 1 ≤ ∏ i = 1 d | P i ( A ) | {\displaystyle |A|^{d-1}\leq \prod {i=1}^{d}|P{i}(A)|} 
where P i is the orthogonal projection in the i th coordinate: P i ( A ) = { ( x 1 , … , x i − 1 , x i + 1 , … , x d ) : ( x 1 , … , x d ) ∈ A } . {\displaystyle P_{i}(A)={(x_{1},\ldots ,x_{i-1},x_{i+1},\ldots ,x_{d}):(x_{1},\ldots ,x_{d})\in A}.} 
The proof follows as a simple corollary of Shearer's inequality: if X 1, ..., X d are random variables and S 1, ..., S n are subsets of {1, ..., d} such that every integer between 1 and d lies in exactly r of these subsets, then H [ ( X 1 , … , X d ) ] ≤ 1 r ∑ i = 1 n H [ ( X j ) j ∈ S i ] {\displaystyle \mathrm {H} [(X_{1},\ldots ,X_{d})]\leq {\frac {1}{r}}\sum {i=1}^{n}\mathrm {H} [(X{j}){j\in S{i}}]} 
where ( X j ) j ∈ S i {\displaystyle (X_{j}){j\in S{i}}} 
is the Cartesian product of random variables X j with indexes j in S i (so the dimension of this vector is equal to the size of S i).
We sketch how Loomis–Whitney follows from this: Indeed, let X be a uniformly distributed random variable with values in A and so that each point in A occurs with equal probability. Then (by the further properties of entropy mentioned above) Η( X) = log| A|, where | A| denotes the cardinality of A. Let S i = {1, 2, ..., i−1, i+1, ..., d}. The range of ( X j ) j ∈ S i {\displaystyle (X_{j}){j\in S{i}}} 
is contained in P i( A) and hence H [ ( X j ) j ∈ S i ] ≤ log  | P i ( A ) | {\displaystyle \mathrm {H} [(X_{j}){j\in S{i}}]\leq \log |P_{i}(A)|} 
. Now use this to bound the right side of Shearer's inequality and exponentiate the opposite sides of the resulting inequality you obtain.
Approximation to binomial coefficient
[ edit]
For integers 0 < k < n let q = k/ n. Then 2 n H ( q ) n + 1 ≤ ( n k ) ≤ 2 n H ( q ) , {\displaystyle {\frac {2^{n\mathrm {H} (q)}}{n+1}}\leq {\tbinom {n}{k}}\leq 2^{n\mathrm {H} (q)},} 
where [32] :43 H ( q ) = − q log 2  ( q ) − ( 1 − q ) log 2  ( 1 − q ) . {\displaystyle \mathrm {H} (q)=-q\log _{2}(q)-(1-q)\log _{2}(1-q).} 
show Proof (sketch)
Note that ( n k ) q q n ( 1 − q ) n − n q {\displaystyle {\tbinom {n}{k}}q^{qn}(1-q)^{n-nq}} 
is one term of the expression
∑ i = 0 n ( n i ) q i ( 1 − q ) n − i = ( q + ( 1 − q ) ) n = 1. {\displaystyle \sum _{i=0}^{n}{\tbinom {n}{i}}q^{i}(1-q)^{n-i}=(q+(1-q))^{n}=1.} 
Rearranging gives the upper bound. For the lower bound one first shows, using some algebra, that it is the largest term in the summation. But then, ( n k ) q q n ( 1 − q ) n − n q ≥ 1 n + 1 {\displaystyle {\binom {n}{k}}q^{qn}(1-q)^{n-nq}\geq {\frac {1}{n+1}}} 
since there are n + 1 terms in the summation. Rearranging gives the lower bound.
A nice interpretation of this is that the number of binary strings of length n with exactly k many 1's is approximately 2 n H ( k / n ) {\displaystyle 2^{n\mathrm {H} (k/n)}} 
. [33]
Use in machine learning
[ edit]
Machine learning techniques arise largely from statistics and also information theory. In general, entropy is a measure of uncertainty and the objective of machine learning is to minimize uncertainty.
Decision tree learning algorithms use relative entropy to determine the decision rules that govern the data at each node. [34] The information gain in decision trees I G ( Y , X ) {\displaystyle IG(Y,X)} 
, which is equal to the difference between the entropy of Y {\displaystyle Y} 
and the conditional entropy of Y {\displaystyle Y} 
given X {\displaystyle X} 
, quantifies the expected information, or the reduction in entropy, from additionally knowing the value of an attribute X {\displaystyle X} 
. The information gain is used to identify which attributes of the dataset provide the most information and should be used to split the nodes of the tree optimally.
Bayesian inference models often apply the principle of maximum entropy to obtain prior probability distributions. [35] The idea is that the distribution that best represents the current state of knowledge of a system is the one with the largest entropy, and is therefore suitable to be the prior.
Classification in machine learning performed by logistic regression or artificial neural networks often employs a standard loss function, called cross-entropy loss, that minimizes the average cross entropy between ground truth and predicted distributions. [36] In general, cross entropy is a measure of the differences between two datasets similar to the KL divergence (also known as relative entropy).
See also
[ edit]
 Mathematics portal
Approximate entropy (ApEn)
Entropy (thermodynamics)
Cross entropy – is a measure of the average number of bits needed to identify an event from a set of possibilities between two probability distributions
Entropy (arrow of time)
Entropy encoding – a coding scheme that assigns codes to symbols so as to match code lengths with the probabilities of the symbols.
Entropy estimation
Entropy power inequality
Fisher information
Graph entropy
Hamming distance
History of entropy
History of information theory
Information fluctuation complexity
Information geometry
Kolmogorov–Sinai entropy in dynamical systems
Levenshtein distance
Mutual information
Perplexity
Qualitative variation – other measures of statistical dispersion for nominal distributions
Quantum relative entropy – a measure of distinguishability between two quantum states.
Rényi entropy – a generalization of Shannon entropy; it is one of a family of functionals for quantifying the diversity, uncertainty or randomness of a system.
Randomness
Sample entropy (SampEn)
Shannon index
Theil index
Typoglycemia
Notes
[ edit]
^ This definition allows events with probability 0, resulting in the undefined log  ( 0 ) {\displaystyle \log(0)} . We do see lim x → 0 x log  ( x ) = 0 {\displaystyle \lim \limits _{x\rightarrow 0}x\log(x)=0} and it can be assumed that 0 log  ( 0 ) {\displaystyle 0\log(0)} equals 0 in this context. Alternatively one can define p : X → ( 0 , 1 ] {\displaystyle p\colon {\mathcal {X}}\to (0,1]}![{\displaystyle p\colon {\mathcal {X}}\to (0,1]}](https://wikimedia.org/api/rest_v1/media/math/render/svg/96938172ec33c0679fb1ffa61bd809fd9bb821bf) , not allowing events with probability equal to exactly 0.
References
[ edit]
^ Pathria, R. K.; Beale, Paul (2011). Statistical Mechanics (Third ed.). Academic Press. p. 51. ISBN 978-0123821881 .
^ Jump up to: a  b Shannon, Claude E. (July 1948). "A Mathematical Theory of Communication". Bell System Technical Journal. 27 (3): 379– 423. Bibcode: 1948BSTJ...27..379S. doi: 10.1002/j.1538-7305.1948.tb01338.x. hdl: 10338.dmlcz/101429. ( PDF, archived from here Archived 20 June 2014 at the Wayback Machine)
^ Jump up to: a  b Shannon, Claude E. (October 1948). "A Mathematical Theory of Communication". Bell System Technical Journal. 27 (4): 623– 656. Bibcode: 1948BSTJ...27..623S. doi: 10.1002/j.1538-7305.1948.tb00917.x. hdl: 11858/00-001M-0000-002C-4317-B. ( PDF, archived from here Archived 10 May 2013 at the Wayback Machine)
^ "Entropy (for data science) Clearly Explained!!!". 24 August 2021. Archived from the original on 5 October 2021. Retrieved 5 October 2021 – via YouTube.
^ MacKay, David J.C. (2003). Information Theory, Inference, and Learning Algorithms. Cambridge University Press. ISBN 0-521-64298-1 . Archived from the original on 17 February 2016. Retrieved 9 June 2014.
^ Shannon, Claude Elwood; Weaver, Warren (1998). The mathematical theory of communication. Urbana: Univ. of Illinois Press. p. 15. ISBN 978-0-252-72548-7 .
^ Schneier, B: Applied Cryptography, Second edition, John Wiley and Sons.
^ Borda, Monica (2011). Fundamentals in Information Theory and Coding. Springer. ISBN 978-3-642-20346-6 .
^ Han, Te Sun; Kobayashi, Kingo (2002). Mathematics of Information and Coding. American Mathematical Society. ISBN 978-0-8218-4256-0 .
^ Jump up to: a  b  c  d  e  f  g  h  i  j  k Thomas M. Cover; Joy A. Thomas (1991). Elements of Information Theory. Hoboken, New Jersey: Wiley. ISBN 978-0-471-24195-9 .
^ Entropy at the nLab
^ Carter, Tom (March 2014). An introduction to information theory and entropy (PDF). Santa Fe. Archived (PDF) from the original on 4 June 2016. Retrieved 4 August 2017. {{ [cite book](https://en.wikipedia.org/wiki/Template:Cite_book)}} : CS1 maint: location missing publisher ( link)
^ Chakrabarti, C. G., and Indranil Chakrabarty. "Shannon entropy: axiomatic characterization and application." International Journal of Mathematics and Mathematical Sciences 2005. 17 (2005): 2847-2854 url Archived 5 October 2021 at the Wayback Machine
^ Ellerman, David (October 2017). "Logical Information Theory: New Logical Foundations for Information Theory" (PDF). Logic Journal of the IGPL. 25 (5): 806– 835. doi: 10.1093/jigpal/jzx022. Archived (PDF) from the original on 25 December 2022. Retrieved 2 November 2022.
^ Jump up to: a  b  c Aczél, J.; Forte, B.; Ng, C. T. (1974). "Why the Shannon and Hartley entropies are 'natural'". Advances in Applied Probability. 6 (1): 131– 146. doi: 10.2307/1426210. JSTOR 1426210. S2CID 204177762.
^ Compare: Boltzmann, Ludwig (1896, 1898). Vorlesungen über Gastheorie : 2 Volumes – Leipzig 1895/98 UB: O 5262-6. English version: Lectures on gas theory. Translated by Stephen G. Brush (1964) Berkeley: University of California Press; (1995) New York: Dover ISBN 0-486-68455-5
^ Życzkowski, Karol (2006). Geometry of Quantum States: An Introduction to Quantum Entanglement. Cambridge University Press. p. 301.
^ Sharp, Kim; Matschinsky, Franz (2015). "Translation of Ludwig Boltzmann's Paper "On the Relationship between the Second Fundamental Theorem of the Mechanical Theory of Heat and Probability Calculations Regarding the Conditions for Thermal Equilibrium"". Entropy. 17: 1971– 2009. doi: 10.3390/e17041971.
^ Jaynes, E. T. (15 May 1957). "Information Theory and Statistical Mechanics". Physical Review. 106 (4): 620– 630. Bibcode: 1957PhRv..106..620J. doi: 10.1103/PhysRev.106.620. S2CID 17870175.
^ Landauer, R. (July 1961). "Irreversibility and Heat Generation in the Computing Process". IBM Journal of Research and Development. 5 (3): 183– 191. doi: 10.1147/rd.53.0183. ISSN 0018-8646. Archived from the original on 15 December 2021. Retrieved 15 December 2021.
^ Mark Nelson (24 August 2006). "The Hutter Prize". Archived from the original on 1 March 2018. Retrieved 27 November 2008.
^ Jump up to: a  b "The World's Technological Capacity to Store, Communicate, and Compute Information" Archived 27 July 2013 at the Wayback Machine, Martin Hilbert and Priscila López (2011), Science, 332(6025); free access to the article through here: martinhilbert.net/WorldInfoCapacity.html
^ Spellerberg, Ian F.; Fedor, Peter J. (2003). "A tribute to Claude Shannon (1916–2001) and a plea for more rigorous use of species richness, species diversity and the 'Shannon–Wiener' Index". Global Ecology and Biogeography. 12 (3): 177– 179. Bibcode: 2003GloEB..12..177S. doi: 10.1046/j.1466-822X.2003.00015.x. ISSN 1466-8238. S2CID 85935463.
^ Massey, James (1994). "Guessing and Entropy" (PDF). Proc. IEEE International Symposium on Information Theory. Archived (PDF) from the original on 1 January 2014. Retrieved 31 December 2013.
^ Malone, David; Sullivan, Wayne (2005). "Guesswork is not a Substitute for Entropy" (PDF). Proceedings of the Information Technology & Telecommunications Conference. Archived (PDF) from the original on 15 April 2016. Retrieved 31 December 2013.
^ Pliam, John (1999). "Selected Areas in Cryptography". International Workshop on Selected Areas in Cryptography. Lecture Notes in Computer Science. Vol. 1758. pp. 62– 77. doi: 10.1007/3-540-46513-8_5. ISBN 978-3-540-67185-5 .
^ Indices of Qualitative Variation. AR Wilcox - 1967 https://www.osti.gov/servlets/purl/4167340
^ Klarreich, Erica (1 October 2015). "A Magical Answer to an 80-Year-Old Puzzle". Quanta Magazine. Retrieved 18 August 2014.
^ Tao, Terence (28 February 2016). "The Erdős discrepancy problem". Discrete Analysis. arXiv: 1509.05363v6. doi: 10.19086/da.609. S2CID 59361755. Archived from the original on 25 September 2023. Retrieved 20 September 2023.
^ https://arxiv.org/pdf/1502.02374.pdf Archived 28 October 2023 at the Wayback Machine
^ "Open question: The parity problem in sieve theory". 5 June 2007. Archived from the original on 7 August 2023.
^ Aoki, New Approaches to Macroeconomic Modeling.
^ Probability and Computing, M. Mitzenmacher and E. Upfal, Cambridge University Press
^ Batra, Mridula; Agrawal, Rashmi (2018). "Comparative Analysis of Decision Tree Algorithms". In Panigrahi, Bijaya Ketan; Hoda, M. N.; Sharma, Vinod; Goel, Shivendra (eds.). Nature Inspired Computing. Advances in Intelligent Systems and Computing. Vol. 652. Singapore: Springer. pp. 31– 36. doi: 10.1007/978-981-10-6747-1_4. ISBN 978-981-10-6747-1 . Archived from the original on 19 December 2022. Retrieved 16 December 2021.
^ Jaynes, Edwin T. (September 1968). "Prior Probabilities". IEEE Transactions on Systems Science and Cybernetics. 4 (3): 227– 241. Bibcode: 1968IJSSC...4..227J. doi: 10.1109/TSSC.1968.300117. ISSN 2168-2887.
^ Rubinstein, Reuven Y.; Kroese, Dirk P. (9 March 2013). The Cross-Entropy Method: A Unified Approach to Combinatorial Optimization, Monte-Carlo Simulation and Machine Learning. Springer Science & Business Media. ISBN 978-1-4757-4321-0 .
This article incorporates material from Shannon's entropy on PlanetMath, which is licensed under the Creative Commons Attribution/Share-Alike License.
Further reading
[ edit]
Textbooks on information theory
[ edit]
Cover, T.M., Thomas, J.A. (2006), Elements of Information Theory – 2nd Ed., Wiley-Interscience, ISBN 978-0-471-24195-9
MacKay, D.J.C. (2003), Information Theory, Inference and Learning Algorithms, Cambridge University Press, ISBN 978-0-521-64298-9
Arndt, C. (2004), Information Measures: Information and its Description in Science and Engineering, Springer, ISBN 978-3-540-40855-0
Gray, R. M. (2011), Entropy and Information Theory, Springer.
Martin, Nathaniel F.G.; England, James W. (2011). Mathematical Theory of Entropy. Cambridge University Press. ISBN 978-0-521-17738-2 .
Shannon, C.E., Weaver, W. (1949) The Mathematical Theory of Communication, Univ of Illinois Press. ISBN 0-252-72548-4
Stone, J. V. (2014), Chapter 1 of Information Theory: A Tutorial Introduction Archived 3 June 2016 at the Wayback Machine, University of Sheffield, England. ISBN 978-0956372857 .
Tribus, Myron (1961). Thermodynamics and Thermostatics: An Introduction to Energy, Information and States of Matter, with Engineering Applications. University Series in Basic Engineering, vol. 1. Princeton: D. Van Nostrand. OCLC 1036889774.
External links
[ edit]
Wikibooks has a book on the topic of: An Intuitive Guide to the Concept of Entropy Arising in Various Sectors of Science
Library resources about
Entropy (information theory)
Online books
Resources in your library
Resources in other libraries
"Entropy", Encyclopedia of Mathematics, EMS Press, 2001 [1994]
"Entropy" Archived 4 June 2016 at the Wayback Machine at Rosetta Code—repository of implementations of Shannon entropy in different programming languages.
Entropy Archived 31 May 2016 at the Wayback Machine an interdisciplinary journal on all aspects of the entropy concept. Open access.
show
v
t
e
Data compression methods
Lossless
type
Lossy
type
Audio
Image
Video
Theory
Compressed data structures
Compressed suffix array
FM-index
Entropy
Information theory
Timeline
Kolmogorov complexity
Prefix code
Quantization
Rate–distortion
Redundancy
Symmetry
Smallest grammar problem
Community
Hutter Prize
People
Mark Adler
David A. Huffman
Phil Katz
Retrieved from " https://en.wikipedia.org/w/index.php?title=Entropy_(information_theory)&oldid=1349980670"
Categories:
Entropy and information
Information theory
Statistical randomness
Complex systems theory
Data compression
Hidden categories:
Webarchive template wayback links
CS1 maint: location missing publisher
Articles with short description
Short description is different from Wikidata
Articles that may contain original research from March 2026
All articles that may contain original research
Articles needing additional references from February 2019
All articles needing additional references
Use dmy dates from October 2023
Use American English from December 2024
All Wikipedia articles written in American English
All articles with unsourced statements
Articles with unsourced statements from April 2013
Wikipedia articles incorporating text from PlanetMath
This page was last edited on 19 April 2026, at 19:21 (UTC).
Text is available under the Creative Commons Attribution-ShareAlike 4.0 License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.
Privacy policy
About Wikipedia
Disclaimers
Contact Wikipedia
Legal & safety contacts
Code of Conduct
Developers
Statistics
Cookie statement
Mobile view
Search
Search [-]
Toggle the table of contents
Entropy (information theory)
46 languages Add topic 
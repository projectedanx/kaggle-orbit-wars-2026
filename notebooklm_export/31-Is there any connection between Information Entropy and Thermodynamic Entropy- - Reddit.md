> Source: https://www.reddit.com/r/askscience/comments/1wyfum/is_there_any_connection_between_information/

Is there any connection between Information Entropy and Thermodynamic Entropy? : r/askscience
Skip to main content Is there any connection between Information Entropy and Thermodynamic Entropy? : r/askscience
Open menu
Open navigation 
Go to Reddit Home 
r/askscience
TRENDING TODAY
Get App
Get the Reddit app
Log In
Log in to Reddit
Expand user menu
Open settings menu
Skip to Navigation Skip to Right Sidebar
Back
Go to askscience
r/askscience
•
12y ago
Megame50
Locked post
Stickied post
Archived post
Report
Is there any connection between Information Entropy and Thermodynamic Entropy?
Physics
I've been reading a lot about information theory lately and it is really interesting. But many of the equations I've seen remind me of physics so I'm curious:Is there any connection between Information Entropy and Thermodynamic Entropy or any other physical quantities? I'm somewhat familiar with digital physics, and I'm familiar with the microscopic definition of Thermodynamic Entropy, something gives me the feeling that'd be a good place to start.
Archived post. New comments cannot be posted and votes cannot be cast.
Upvote 22 Downvote 9 Go to comments Share
Sort by: Best
Open comment sort options
Best
Top
New
Controversial
Old
Q&A
Comments Section
The_Serious_Account
•
12y ago
The two things are related, but not exactly the same. The total information content of a closed system is constant, which is not true for entropy in thermodynamics. My preferred way of looking at it is to say that the thermodynamic entropy is the amount of information of a system that's hidden in the microscopic state when you know the macroscopic state.
As an example, if you mix coffee and milk, the total information required to perfectly describe the entire state(ie. position and movement of all particles) remains fixed over time, but the amount of information hidden in the microscopic state increases over time as the two mix. Put another way, the information you need to describe the macroscopic state decreases over time.
Upvote 5 Downvote Award Share
Report
Award
Share
super-zap
•
12y ago
I recently read a great comment (which I can't find) about how Huffman coding works. It is directly related to Information Entropy.
I will try to explain the basics here.
Imagine you have a text file with 4 letters in it. In a straightforward approach you can give each letter a code from 00 to 11 in binary.
a - 00
b - 01
c - 10
d - 11
Another approach would be to count how many times each letter appears and give the most commonly occurring letters a short code and the less commonly occurring letter a longer code. For example:
a - 0
b - 10
c - 110
d - 1110
Now imagine that the a letter comprises 50% of the text, b - 25%, c - 12.5% and d - 6.25%.
In the original case you needed an average of 2 bits of information to represent each letter in the file.
In the second version you need: 1 * 0.5 + 2 * 0.25 + 3 * 0.125 + 4 * 0.0625. This comes down to 1.625 bits per symbol on average.
Now, the way this is tied in with thermodynamic entropy is the following: both represent the orderliness of the system. A more ordered system has lower entropy and hence it need less information (per symbol) to describe it. To make another connection: the above example, there are more ways to arrange the system if all the symbols were evenly distributed (higher entropy) than if there if one symbol is predominant.
tl;dr: they both measure the same concept.
Upvote 2 Downvote Award Share
Report
Award
Share
The_Serious_Account
•
12y ago
Interesting post, but I'm not sure I understand the exact physical connection you're making here. As I mention in my answer, the information to fully describe a system does not change over time, whereas thermodynamic entropy can. When you say "need less information (per symbol) to describe it." what type of description are you referring to in a physical sense?
there are more ways to arrange the system if all the symbols were evenly distributed (higher entropy) than if there if one symbol is predominant.
This I don't understand. I can give you a probability distribution that would give few ways to arrange the symbols but high information entropy, eg.
22%, 25%, 26%, 27%.
Upvote 2 Downvote Award Share
Report
Award
Share
that-is-super-great
•
12y ago
They are different, but there is ongoing research about how the two are precisely related. For example, any computational procedure ought to produce thermodynamic entropy, but what's the 'in principle' minimum amount and how does this (or doesn't it) depend on the 'complexity' of the computation? Charles Bennett (an IBM research fellow) argued that using brownian motion machines we could theoretically perform a computation of any complexity at the price of an arbitrarily small amount of thermodynamic entropy, as along as we were willing to perform the computation very, very slowly (his 1981 "Thermodynamics of computation" is a good place to access this, but unfortunately you'll need access to the journal). Not very practical, and debated (e.g., see John Norton's "All shook up"), but to answer your question, yes, it seems there should be some way to characterize the relationship, but it's not clear exactly how.
Upvote 1 Downvote Award Share
Report
Award
Share
BoxAMu
•
12y ago
Since no one has mentioned it yet, one way to look at the similarity between the two entropies is that it is strictly formal. Both definitions of entropy come out of fairly straightforward combinatorics applied to random variables, resulting in the similar looking formulas.
The major difference is that thermodynamic entropy enumerates the true physical microstates, while information entropy enumerates the possible outcomes of some general random variables. This makes all the difference because there are no dynamical laws to supplement the states you've counted. If I am flipping a coin, the states used to calculate information entropy are heads and tails. In some prescribed scenario, where a human is there to tally the results of the coin toss, the information entropy obviously has meaning. But the thermodynamic entropy, which counts all the microscopic physical states of the particles comprising the coin, tells us about the actual physical processes that occur within the coin.
Upvote 1 Downvote Award Share
Report
Award
Share
quantumripple
•
12y ago
There is the classic paper by Jaynes, Information Theory and Statistical Mechanics that looks into exactly this connection.
Shannon's information entropy was named after statistical mechanical entropy, because the P log P equation had already shown up as statistical mechanical entropy.
The second law of thermodynamics is basically a statement that the information you have about an isolated system cannot just spontaneously increase over time. In statistical mechanics this is a trivial fact for P log P entropy: mechanical systems preserve information and evolve unitarily, meaning that two distinguishable states forever remain distinguishable states as they evolve in time, never merging into one state. On the other hand, the information you have about a system can "spontaneously" decrease, though this is not the fault of the system, but rather the lack of your ability to keep track of the fine details of the system.
Also, in the case of a system in thermodynamic equilibrium with its surroundings, the P log P entropy was shown (by Gibbs, in 1902) to be truly an exact analogy to thermodynamic entropy, since it is exactly this quantity that appears in the first law of thermodynamics derived in statistical mechanics.
Upvote 1 Downvote Award Share
Report
Award
Share
New to Reddit?
Create your account and connect with a world of communities.
Continue with Email
Continue With Phone Number
By continuing, you agree to our User Agreement and acknowledge that you understand the Privacy Policy.
Related Answers Section
Related Answers
Shannon entropy definition and formula
Entropy in information theory definition
Shannon entropy uncertainty and surprise
How does gravity affect time perception?
What causes the colors of a sunset?
More posts you may like
What is the relationship between information and thermodynamic entropy? r/askscience • 9y ago [
What is the relationship between information and thermodynamic entropy?
](https://www.reddit.com/r/askscience/comments/790bch/what_is_the_relationship_between_information_and/) 15 upvotes · 43 comments
Why does everyone hate Thermodynamics and find it so difficult? r/EngineeringStudents • 9mo ago [
Why does everyone hate Thermodynamics and find it so difficult?
](https://www.reddit.com/r/EngineeringStudents/comments/1lwtay3/why_does_everyone_hate_thermodynamics_and_find_it/) 10 upvotes · 16 comments
What's your understanding of information entropy? r/math • 1y ago [
What's your understanding of information entropy?
](https://www.reddit.com/r/math/comments/1krt65a/whats_your_understanding_of_information_entropy/) 132 upvotes · 68 comments
Mind blown.. if this is how the word 'entropy' came into Information Theory !! r/compsci • 15y ago [
Mind blown.. if this is how the word 'entropy' came into Information Theory !!
](https://www.reddit.com/r/compsci/comments/l2svh/mind_blown_if_this_is_how_the_word_entropy_came/) 86 upvotes · 48 comments
Whats the relation of entropy in physics and entropy in information theory? r/askscience • 7y ago [
Whats the relation of entropy in physics and entropy in information theory?
](https://www.reddit.com/r/askscience/comments/dz2fkw/whats_the_relation_of_entropy_in_physics_and/) 1.9K upvotes · 167 comments
After more than 100 years, the third law of thermodynamics has been proven mathematically. Interview with one of the researchers who did it r/Physics • 9y ago [
After more than 100 years, the third law of thermodynamics has been proven mathematically. Interview with one of the researchers who did it
](https://www.reddit.com/r/Physics/comments/62ebmh/after_more_than_100_years_the_third_law_of/)  chalkdustmagazine 1.6K upvotes · 112 comments
The second law of thermodynamics really messed with my intuition r/AskPhysics • 4mo ago [
The second law of thermodynamics really messed with my intuition
](https://www.reddit.com/r/AskPhysics/comments/1prnz6c/the_second_law_of_thermodynamics_really_messed/) 67 upvotes · 35 comments
How does the physical concept of entropy relates to the information theory concept of entropy? r/askscience • 9y ago [
How does the physical concept of entropy relates to the information theory concept of entropy?
](https://www.reddit.com/r/askscience/comments/5nz64j/how_does_the_physical_concept_of_entropy_relates/) 1.6K upvotes · 104 comments
What is information theory? explain it to me like I'm a ten-year-old. r/AskPhysics • 1mo ago [
What is information theory? explain it to me like I'm a ten-year-old.
](https://www.reddit.com/r/AskPhysics/comments/1rq8g7d/what_is_information_theory_explain_it_to_me_like/) 18 upvotes · 28 comments
If everything move towards entropy, why is the Universe more complexe and ordinate now (with complexes systems like stars, galaxies, even on a smaller scale life and volcanism) m than it was seconds after the big bang? r/askscience • 10mo ago [
If everything move towards entropy, why is the Universe more complexe and ordinate now (with complexes systems like stars, galaxies, even on a smaller scale life and volcanism) m than it was seconds after the big bang?
](https://www.reddit.com/r/askscience/comments/1lag9cn/if_everything_move_towards_entropy_why_is_the/) 318 upvotes · 91 comments
What is entropy ? r/Physics • 3mo ago [
What is entropy ?
](https://www.reddit.com/r/Physics/comments/1qjfvxv/what_is_entropy/) 80 upvotes · 60 comments
What is the opposite of entropy? r/AskPhysics • 7mo ago [
What is the opposite of entropy?
](https://www.reddit.com/r/AskPhysics/comments/1nhxol8/what_is_the_opposite_of_entropy/) 2 upvotes · 27 comments
Reversing Entropy - Theoretical ways to do it r/AskPhysics • 9mo ago [
Reversing Entropy - Theoretical ways to do it
](https://www.reddit.com/r/AskPhysics/comments/1mdwc79/reversing_entropy_theoretical_ways_to_do_it/) 47 comments
Why do we define entropy this way? r/Physics • 5y ago [
Why do we define entropy this way?
](https://www.reddit.com/r/Physics/comments/qltgfa/why_do_we_define_entropy_this_way/)  youtu 264 upvotes · 37 comments
What is the progress of making the theory of everything r/TheoreticalPhysics • 6mo ago [
What is the progress of making the theory of everything
](https://www.reddit.com/r/TheoreticalPhysics/comments/1oeuj93/what_is_the_progress_of_making_the_theory_of/) 12 upvotes · 30 comments
How do we know that Quantum interactions are truly random and not mediated by unknown deterministic rules? r/askscience • 7mo ago [
How do we know that Quantum interactions are truly random and not mediated by unknown deterministic rules?
](https://www.reddit.com/r/askscience/comments/1nc3pmk/how_do_we_know_that_quantum_interactions_are/) 485 upvotes · 88 comments
How do I decide between experimental and theoretical physics? r/Physics • 2mo ago [
How do I decide between experimental and theoretical physics?
](https://www.reddit.com/r/Physics/comments/1rmptou/how_do_i_decide_between_experimental_and/) 24 upvotes · 50 comments
Do two different atoms of the same element always have the same mass? r/askscience • 3mo ago [
Do two different atoms of the same element always have the same mass?
](https://www.reddit.com/r/askscience/comments/1qod0ab/do_two_different_atoms_of_the_same_element_always/) 745 upvotes · 131 comments
Why do atoms release energy when forming a chemical bond? r/askscience • 28d ago [
Why do atoms release energy when forming a chemical bond?
](https://www.reddit.com/r/askscience/comments/1s2r1dd/why_do_atoms_release_energy_when_forming_a/) 180 upvotes · 48 comments
Why do quantum computers look like that? r/askscience • 11d ago [
Why do quantum computers look like that?
](https://www.reddit.com/r/askscience/comments/1shlkzk/why_do_quantum_computers_look_like_that/) 449 upvotes · 138 comments
How do we know the universe is expanding due to internal forces, and not being stretched by something on the outside? r/askscience • 4mo ago [
How do we know the universe is expanding due to internal forces, and not being stretched by something on the outside?
](https://www.reddit.com/r/askscience/comments/1pzdepg/how_do_we_know_the_universe_is_expanding_due_to/) 131 upvotes · 42 comments
How does the brain "decide" what is language? r/askscience • 6mo ago [
How does the brain "decide" what is language?
](https://www.reddit.com/r/askscience/comments/1ofjy8v/how_does_the_brain_decide_what_is_language/) 133 upvotes · 23 comments
Why doesn't universe expansion affect local systems? r/AskPhysics • 10d ago [
Why doesn't universe expansion affect local systems?
](https://www.reddit.com/r/AskPhysics/comments/1si5uel/why_doesnt_universe_expansion_affect_local_systems/) 25 upvotes · 31 comments
Are there experimentally supported examples where quantum coherence influences biological function, and what molecular or structural features prevent immediate decoherence in these systems? r/askscience • 3mo ago [
Are there experimentally supported examples where quantum coherence influences biological function, and what molecular or structural features prevent immediate decoherence in these systems?
](https://www.reddit.com/r/askscience/comments/1qhg722/are_there_experimentally_supported_examples_where/) 212 upvotes · 12 comments
What is one theory you have a feeling is true but is not actually proven so r/AskPhysics • 4mo ago [
What is one theory you have a feeling is true but is not actually proven so
](https://www.reddit.com/r/AskPhysics/comments/1q4h18v/what_is_one_theory_you_have_a_feeling_is_true_but/) 75 upvotes · 49 comments
View Post in
日本語
简体中文
Русский
See more See fewer
Türkçe
Italiano
Nederlands
Community Info Section
r/askscience
Join
AskScience: Got Questions? Get Answers.
Ask a science question, get a science answer.
Show more
Public
Anyone can view, post, and comment to this community
Top Posts
Reddit reReddit: Top posts of February 4, 2014
Reddit reReddit: Top posts of February 2014
Reddit reReddit: Top posts of 2014
Reddit Rules Privacy Policy User Agreement Your Privacy Choices Accessibility Reddit, Inc. © 2026. All rights reserved.
Expand Navigation
Expand Navigation
Collapse Navigation
Collapse Navigation 
0cAFcWeA7xdHgoMfEV7oIcyirpPXDSSeWdt-YuRLl4oMvn_yCzobLTRAV-8cLhIq3cWe_pnEgKWXgvDz2h3GymrrAdjthvPRC6uVV6G-YbEvJ67slFQx20OPf09-AwIJN5mzQfTxCSxaF2N0qZm6V_S12hP6uFaWafPGgL4XjEoRteelIeUl7pRFU8mC1X3OckxaQEvQIpxdC8HuBvRcQ7ogGVXU2PIXAfoGA9iwd0QQwfE4J8bRovvQyZH7_shHQIuVCkFOop8bkli42gAmtRXC9ES1bwmI2XVyXAz_ijxpKrj206zc0ZfW9-MaJobPFnrJiwbp4_tz3jm0-u6xuPfaQVy-cKkBnRGse72e6A7WNz9x_Pxb89Cm7mV0mAa6pdFcOtgnOHcqRNpA3xk5_evYqHNe5cz1HaiSv1sYP5z5oOJCV4aYvDxGto2mSBPXezp1ldfdiWB9lH17_veAxUubAgLMD74uAdnIzassXeJ-uAJf5cL2DzJBwAiRQx1NkyEeJe1Rwsh_thQAwLa7BH8ddB3PHaj9BcND090F66NmX01a8fO43Wm0cPnP6aa903QuhqU1sjGV-Jg1Y6WLHbTSYBP7Z4rt2x0ktUkKWR0d58ftVKRCXZXa2-8omrHuCe8mfMBvDKZFowrKeYiUiXEyZgqcRJf_zLKHYxbErgzkITjjjVuqzCYpmwKrzqnE7ECkTOWzrZjb97puK73bgwOkJquGhRHspNKPEETP8TabByNTKcY5kYetOvsqCTLQ3XGsEQTsjLASLzZgm6fMFy_EZntOY951L2LumbsltqVQh0cezKWzrruSGHtYMPsxLLZyFe8-ytq_Fl4UDAH3_mGgwe1_Gl_URA_R2kli6aVfGnbBor19lhhZwk6EKaqT3zyKezUxr0unQ9Dw4jPIVYLisCO_ElHnkiEGHbznBcrVTzXtE8d2-I2KJpNZz5hm-lvogmwHJOjn_RvUEs8SJ3bf3Cs-nX-ThQBOnWMFWFchHVSNxw3t38-yXJUMauENkadZLxv3354pO9TzH7VhZaeUCjB_wVOx3JsOyzkvPylIQKYgHdd7rFa5HCwa-cGH6OUdA2X-UZ89ypqxHkxW9CnIcXgJ1dxxpRYDIj9_toa9kxRrq7ApUw3kn56vItDdliZQeidM_A4_Rxz5CJEzmlm-DikH3mrbp0EL73Yk4nHuLX-ozSkbDnEtDf2zV4WEorLek70c65IM4P3VFZGz4oG3mfJQP8Ll6Jt_9fxM3ymFq7vXI_RcGELZ33XA0IkGJiyIWuAWB0PIxYEXp7QJjI4khUkvKLwOxTU55RLJlG5XQJCvU7sOpvHvzsIXM9khXxLwtTzx3wgIdTgXqWWQx83eZ0V2Mjjt1x8oLcYO1pmz9Nd4ohzWCuzX5u_f83OnQYHqMtfsCjJ6OW0kBTIfyBHrx0JSSYoZ02a7l7UGCXfjPl1NjEwZcEuI6H3YquIxnhJZScqD6J92MixN3OPHeoVEDdhT84U109vZnouj615IZaPOFqMXnWEKegLoXO3Ch0ajM7q47P9O6rJTy6clSjulvYa1PisaguE0ix0huDjEEhSi_DT0kUJJB2Xpho-rHkBGvTkzTJlI6ywU-2NRmBKEX22gzYAe22qC2QDiZQ3i5uZqzkcJ41tyM1ipVPCYFoKVuq4mDJcMgJarnYcFdMouXWh69Daan50gFfHz1Sc-K6xh6Yy8crbmoqHNfOH3lXuhYDXOil93Rx9nG3tFlfqTOpyVvv8LIj29TQFqZonneCXQ12DKvciRG3WKejI5kLq274de3129PHvAeXtQttz3a8et2MqH0by5yRL1QWRvW1kHLSR8bFScUUlbsviOcN5DN9Wn9k2qcmVxL-57TP-rAnFuJxAdYr6nW_iwC_bhlGQPUTKOczUK8pElaEgjgX6i90EuhVo_vJyvRBhbEjvELfPT5gPKftIkbSvdEa0U-UIGlcj-c-0pJxgTBp9tShg7i0HP1MVQsJRLdAMWmQflcODP9wL_s-FO5ZJ0y0j1UNQYXEuuhVtf1FKg8A-iJAh8u2jFhtce0mpKUdCmw_Qt5zR67Khsl5oYd_AuCkDvEcUsgRVUR9ZQwRgRjP3lT5fNJWAFCZ85NR8X7dnV7E2clI0kPWKk4iMReP6RcIkxW956pg1eG4tdk
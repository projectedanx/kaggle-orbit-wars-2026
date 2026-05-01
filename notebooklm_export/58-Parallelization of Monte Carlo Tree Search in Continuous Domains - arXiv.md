> Source: https://arxiv.org/pdf/2003.13741

Parallelization of Monte Carlo Tree Search in Continuous Domains 
1st Karl Kurzer Karlsruhe Institute of Technology 
Karlsruhe, Germany kurzer@kit.edu 
2nd Christoph Hörtnagl Karlsruhe Institute of Technology 
Karlsruhe, Germany uyedd@student.kit.edu 
3rd J. Marius Zöllner Karlsruhe Institute of Technology 
Karlsruhe, Germany zoellner@kit.edu 
Abstract—Monte Carlo Tree Search (MCTS) has proven to be capable of solving challenging tasks in domains such as Go, chess and Atari. Previous research has developed parallel versions of MCTS, exploiting today’s multiprocessing architectures. These studies focused on versions of MCTS for the discrete case. Our work builds upon existing parallelization strategies and extends them to continuous domains. In particular, leaf parallelization and root parallelization are studied and two final selection strategies that are required to handle continuous states in root parallelization are proposed. The evaluation of the resulting parallelized continuous MCTS is conducted using a challenging cooperative multi-agent system trajectory planning task in the domain of automated vehicles. 
Index Terms—monte carlo tree search, continuous action spaces, parallelization, root parallelization, leaf parallelization, multi-threading, multi-agent systems 
I. INTRODUCTION 
Monte Carlo Tree Search (MCTS), based on the UCT (Upper Confidence Bound for Trees) selection policy [1], has demonstrated its strength on numerous occasions facing problems with large branching factors. AlphaGo, AlphaZero and their successor MuZero are among the most prominent examples, reaching super-human performance in the games of Go, chess, and Atari [2]–[4]. 
Prior work on parallelization has given insights with regard to benefits of using today’s multi-threaded processors to speed up MCTS [5]–[10]. However, due to its nature MCTS and the parallelization of it have been primarily studied for discrete state and action spaces. Our work extends prior research on MCTS in continuous domains [11]–[15] to the parallel case and develops novel final selection strategies for root parallelization that are required to address these domains. 
II. RELATED WORK 
A. Monte Carlo Tree Search 
An exhaustive tree search can find the optimal trajectory through any Markov decision process (MDP) with a finite set of states and actions. However, as the action space grows larger, so does the tree and it becomes prohibitively expensive 
We wish to thank the German Research Foundation (DFG) for funding the project Cooperatively Interacting Automobiles (CoInCar) within which the research leading to this contribution was conducted. The information as well as views presented in this publication are solely the ones expressed by the authors. 
to search for an optimal trajectory. Tree Search combined with Monte Carlo sampling addresses this issue, by approximating the optimal solution asymptotically through sampling. Monte Carlo Tree Search explores different trajectories (i.e. tuples of states st and actions at) through the MDP, with the goal of discovering the trajectory that maximizes the return R from the root state. 
The return R of a trajectory τ equals its accumulated discounted reward rt at time step t, taking action at in state st [16], see (1). 
R(τ) = ∑ 
(st,at)∈τ 
rt(st, at) (1) 
The mean of the returns over all trajectories T sampled from policy π(a|s), starting in state s and taking action a, is the Monte Carlo estimate of the action value Qπ(s, a) [16], see (2). 
Qπ(s, a) = 1 
|T | ∑ 
τ∈T ∼π R(τ) (2) 
Given an initial root state of the MDP, MCTS approximates the action value in four sequential steps for each iteration until a terminal condition is met (e.g. until a time budget or computational budget is exceeded). Since MCTS is an anytime algorithm [17], it returns an estimate after the first iteration. 
1) Selection: The UCT value [1] for all explored actions from the current state is calculated during the selection phase, see (3), and the state action tuple with the maximum UCT value is selected. This process repeats until a state is selected that has not been fully explored (i.e. not all available actions in the state have been expanded), see Fig. 1. 
The first term in (3) fosters exploitation of previously explored actions with high action values. The second term guarantees that all actions for a given state are being expanded at least once, with N(s) being the visit count for state s and N(s, a) the number of times action a has been chosen in that state. To balance the exploration-exploitation trade-off, a constant factor c is used. 
UCT (s, a) = Qπ(s, a) + c 
√ 2 logN(s) 
N(s, a) (3) 
 
 
 
 
 
 
 
 
 
 
 
Selection Expansion 
Fig. 1: Selection and Expansion in MCTS 
Simulation Backpropagation 
Fig. 2: Simulation and Backpropagation in MCTS 
2) Expansion: Once the selection policy encounters a state with untried actions left, it expands that state by randomly sampling an action from a uniform distribution over the action space, see (4), and executing the action reaching a successor state, see Fig. 1. 
a ∼ U [min(A),max(A)] (4) 
3) Simulation: After the expansion of an action completes, a simulation of subsequent random actions is conducted until a terminal condition is met (i.e. the planning horizon is reached or an action is sampled resulting in a terminal state) evaluating the action value of the previous expansion, see Fig. 2. 
4) Backpropagation: Lastly, the return R of the trajectory generated by the iteration is backpropagated to all states along the trajectory, see Fig. 2, and the action values and visit counts for all actions of the trajectory are updated, see (5) and (6), respectively. 
N(s, a) = N(s, a) + 1 (5) 
Qπ(s, a) = Qπ(s, a) + 1 
N(s, a) (R(s, a)−Qπ(s, a)) (6) 
B. Parallelization 
The parallelization of MCTS is a well researched topic. Most of this research focuses on the game of Go [5]– [10]. The baseline version of MCTS can be parallelized in 
Fig. 3: Leaf Parallelization of MCTS 
++ 
Fig. 4: Root Parallelization of MCTS 
multiple ways. Three different types of MCTS parallelizations are commonly referred to, namely leaf parallelization, root parallelization, and tree parallelization [6], [17]. 
1) Leaf Parallelization: The simplest form of paralleliza-tion is leaf parallelization. In this case all policies behave identical except for the simulation policy. Once a node gets expanded each thread creates a copy of the expanded node and runs a simulation on the copy until it terminates (i.e. reaches a terminal state or the planning horizon). The results of all simulations are combined and backpropagated along the traversed branch. One drawback of this method is the synchronization of threads before the backpropagation, as this implies that all threads must wait for the slowest to finish. By design, leaf parallelization fosters exploitation. 
2) Root Parallelization: Contrary to leaf parallelization root parallelization fosters exploration, even though not in a principled way. During root parallelization each thread creates a copy of the root node and builds up its own tree. Once the allotted time or computational budget is reached, the resulting trees are merged. Different methods on how to merge the resulting trees have been proposed. Some studies use a voting mechanism, where each tree votes for the best action it has explored [7] and the action with the majority of the votes gets selected. 
3) Tree Parallelization: Another variant is tree paralleliza-tion, which can be seen as a mixture of the previous methods, as the search tree is shared for all phases of the MCTS. However, as multiple threads build up the same tree it is essential to coordinate the threads properly ensuring efficiency as well as effectiveness of the parallel architecture. Thus, lock-free approaches have been developed to implement tree parallelization efficiently [8], [18]. In addition, measures such as virtual loss [6] improve the effectiveness of tree paral-lelization, by increasing the likelihood that multiple threads traverse different paths. While virtual loss has been an adopted concept [2], more recent studies suggest that the increase in effectiveness is merely a trade-off with time efficiency [19].
Even though the proposed parallelization strategies reach performance gains, the inherent dependence on previous sim-ulation results in UCT remains a key issue that hinders scalability. In order to reduce the dependence on previous it-erations, the visit count for incomplete expansions/simulations can be incorporated in the UCT formula. This avoids multiple threads working on identical unexplored actions and increases the information content of UCT prior to the result of the simulation [20]. 
As can be seen, extensive research on the parallelization of MCTS exists for discrete domains. However, to the best of our knowledge no research on the parallelization of MCTS with continuous action and state spaces has been performed. Hence, we propose respective extensions which are required by continuous domains. 
III. APPROACH 
A. Extensions to Continuous Action Spaces 
The application of the UCT in MCTS demands that every possible action in a given node must be explored at least once [1]. When actions are drawn from a continuous distribution, MCTS would be stuck indefinitely exploring a single node. Thus, standard MCTS is not directly applicable to continuous domains. 
1) Progressive Widening: To address the before mentioned issue during the expansion phase in continuous action do-mains, Progressive Unpruning [21] or Progressive Widening [22] have been proposed. Additional theoretical considerations have extended UCT for continuous domains [23]. 
These approaches gradually add actions during runtime to the action space of a node. Each node starts out with a sampled set of actions. Progressive Widening takes place once a node has sufficiently been explored by sampling an additional action and adding it to the action space of the node. The criteria is defined by a sub-linear function, see (7). 
|A(s)| = bc ·N(s)αc (7) 
The cardinality of the action set for any given state is depen-dent on the visit count of the state itself. The choice of the parameters c and α ∈ [0, 1] is adapted empirically. 
While progressive widening circumvents the problem of continuous action spaces during expansion, it does not solve the inefficiency in the update phase. 
2) Similarity Update: Since the update phase aggregates the statistics from consecutive simulations to generate accurate value estimates, it is critical to use as many simulations as possible for variance reduction. In continuous action spaces it regularly occurs that actions are sampled in close vicinity to one another. Actions that are close to each other are likely to generate similar trajectories and hence comparable returns. 
An example of this is depicted in Fig. 5, where action I has been sampled in close vicinity to action II, thus the return of action I might hold valuable information for action II and could be integrated in its statistics, to reduce its variance. 
∆ylat 
∆vlon 
I 
II 
K er 
ne l 
V al 
ue 
Fig. 5: Similarity update of action II given action I in the continuous space; In order to share information between actions that are similar, action II is updated with statistics gathered from action I weighted by the kernel value of action I and II. 
When the tree is traversed in reverse order during back-propagation, the similarity between the current action and all previously explored actions of a state is determined. The return and the visit count of the current action are weighted with the similarity to update comparable states. 
The similarity of two actions K(ai, aj) ∈ (0, 1] in the action space is determined by a distance measure based on a radial basis function, see (8). Lower values for γ ∈ R+, increase the influence of other actions, higher values decrease it. 
K(ai, aj) = exp ( −γ ‖ai − aj‖2 
) (8) 
B. Leaf Parallelization 
As mentioned, the simplest form of parallelization can be conducted on the leaves of the tree. The node to be simulated is copied once for each thread and the simulation is run until all threads reach the terminal condition. Finally, the result of the simulations is aggregated. 
rsim = 
T∑ t 
γtr(s, a) (9) 
1) Mean: The most obvious aggregation is the mean sim-ulation reward, which equals the cumulated sum of rewards over all time steps t over all threads ξ ∈ Ξ, see (10). 
rsim = 1 
|Ξ| 
Ξ∑ ξ 
rsim(ξ) (10) 
One issue arising with the mean is that environments requiring precise action selection become harder to solve [24]. As the majority of actions from a given state leads to an undesirable terminal state and only a fraction result in the desired state, averaging over all simulations will lead to a pessimistic evaluation of that node.
2) Maximum: To overcome the problem, the maximum of the simulation reward can be used, however, this cannot be generalized to adversarial multiplayer environments, as it might lead to traps [24]. The maximum simulation reward is calculated by choosing the value from the thread ξ that generated the maximum cumulated sum of rewards over all time steps t during simulation (11). 
r∗sim = max ξ rsim(ξ) (11) 
C. Root Parallelization 
Root parallelization grows multiple trees X originating from the same root. Once the MCTS terminates, the statistics of all resulting trees need to be merged. Merging the information for final action selection in the continuous domain requires different strategies, as actions that were explored in one tree are unlikely to be found in another. In the following two novel methods for aggregating the statistics are presented. 
1) Similarity Merge: Using the similarity update depicted in Fig. 5 multiple trees can be merged into a single tree, from which a final action can be chosen. 
The process is described in Algorithm 1. First, all actions of all trees are added to the final tree, line 2. Second, a pairwise similarity update is conducted between all actions of the final tree and the simulated trees. For this, the similarity visit count is determined, line 7, and the similarity action value is calculated based on the weighted visit count and similarity, line 8. Last, the action with the maximum action value from the final tree is returned. 
Algorithm 1 Similarity Merge 
Require: K 1 for x ∈ X do 2 Axfinal ← Axfinal +Ax 3 end for 4 for ai ∈ Axfinal do 5 for aj 6= ai ∈ Axfinal do 6 Kij ← exp 
( −γ ‖ai − aj‖2 
) 7 Nsim(s0, ai)← N(s0, ai) + KijN(s0, aj) 8 Qsim(s0, ai) ← 
1 Nsim 
(N(s0, ai)Q(s0, ai) + KijN(s0, aj)Q(s0, aj)) 9 end for 
10 end for 11 return afinal ← arg maxa∈Axfinal 
Qsim(s0, a) 
2) Similarity Vote: Inspired by a voting scheme for root parallelization which does not merely choose the action with the overall highest number of visits or action value, but rather lets each tree vote for an action [7], an extension for continuous domains was developed, see Algorithm 2. Analogous to [7] each tree submits its best action, line 2. Then a similarity matrix K is calculated, that stores the similarity of a chosen action from one tree to all actions from all trees, line 6. Weighted by the action values of the submitted actions, 
line 8, the final action is the one that maximizes the similarity vote. 
Algorithm 2 Similarity Vote 
Require: K,v 1 for x ∈ X do 2 A∗ ← A∗ ∪ arg maxaQx(s0, a) 3 end for 4 for ai ∈ A∗ do 5 for aj ∈ A∗ do 6 Kij ← exp 
( −γ ‖ai − aj‖2 
) 7 end for 8 vi ← Q(s0, ai) 9 end for 
10 return afinal ← ai ∈ A∗|i = arg maxiKv 
IV. EVALUATION 
To evaluate the impact of the proposed parallelization techniques, a challenging multi-agent environment, i.e. co-operative trajectory planning for automated vehicles [14] is employed. Using MCTS in conjunction with Decoupled-UCT, actions for each agent are evaluated in a decentralized manner, while respecting the interdependence of actions among traffic participants. 
Each parallelization technique is evaluated on every scenario for different numbers of iterations and threads. To generate statistically reliable results each setting is evaluated 50 times. The results for the scalability analysis are summarized in Fig. 6. The key evaluation metric is the success rate for the scenarios (the inverse of the collision rate, i.e. whether or not a vehicle collided). All parallelization strategies are compared to the performance of the average single-threaded baseline. Unless stated otherwise, the evaluation is conducted using scenarios SC07–SC15. This avoids skewing of the results as the single-threaded case already reaches a success rate of close to 100 percent for scenarios SC01–SC06, cf. Fig. 7a, allowing for no improvement through parallelization. Videos of all scenarios combined with a brief description can be found online 1. 
A. Leaf Parallelization Fig. 10a depicts the results of leaf parallelization with mean 
aggregation. No improvement and no scaling of threads can be seen. The slight gain in success rate over the 2σ region of the baseline at 2000 iterations is not consistent as it vanishes again for 4000 iterations. 
While the results for the maximum aggregation depicted in Fig. 10b indicate that it does not scale well with the number of threads, they demonstrate that there is relatively consistent improvement for 8 threads, as the success rate stays outside the 2σ region of the baseline. This implies that there is a benefit for multiple roll-outs when using their maximum. However, this might be due to the nature of the cooperative environment as explained in section III-B2. 
1http://url.fzi.de/PC-MCTS-COG
100 200 500 1000 2000 4000 Iterations 
0.1 
0.2 
0.3 
0.4 
0.5 
0.6 
0.7 Su 
cc es 
s R 
at e 
8 Threads 1 Threads 24 Threads 
(a) Leaf Parallelization: Mean 
100 200 500 1000 2000 4000 Iterations 
0.1 
0.2 
0.3 
0.4 
0.5 
0.6 
0.7 
Su cc 
es s 
R at 
e 
8 Threads 1 Threads 24 Threads 
(b) Leaf Parallelization: Maximum 
100 200 500 1000 2000 4000 Iterations 
0.1 
0.2 
0.3 
0.4 
0.5 
0.6 
0.7 
Su cc 
es s 
R at 
e 
8 Threads 1 Threads 24 Threads 
(c) Root Parallelization: Similarity Merge 
100 200 500 1000 2000 4000 Iterations 
0.1 
0.2 
0.3 
0.4 
0.5 
0.6 
0.7 
Su cc 
es s 
R at 
e 
8 Threads 1 Threads 24 Threads 
(d) Root Parallelization: Similarity Vote 
Fig. 6: Scalability of the different proposed parallelization strategies; The shaded region represents the deviation (2σ), 
100 200 500 1000 2000 4000 Iterations 
SC01 SC02 SC03 SC04 SC05 SC06 SC07 SC08 SC09 SC10 SC11 SC12 SC13 SC14 SC15 
Sc en 
ar io 
s 
0.98 0.98 0.98 0.99 0.99 1.00 0.59 0.66 0.84 0.91 0.93 0.95 1.00 1.00 1.00 1.00 1.00 1.00 0.96 0.94 0.98 0.99 0.99 0.97 0.82 0.92 0.97 0.97 0.98 0.96 0.93 0.96 0.99 1.00 0.99 1.00 0.13 0.16 0.28 0.40 0.39 0.58 0.09 0.20 0.28 0.39 0.50 0.65 0.56 0.90 0.96 0.94 0.90 0.90 0.28 0.46 0.74 0.75 0.77 0.81 0.04 0.10 0.26 0.53 0.69 0.80 0.01 0.03 0.13 0.25 0.56 0.85 0.02 0.01 0.03 0.07 0.10 0.11 0.00 0.01 0.05 0.10 0.14 0.24 0.00 0.02 0.02 0.02 0.01 0.00 
(a) 1 Thread 
100 200 500 1000 2000 4000 Iterations 
SC07 SC08 SC09 SC10 SC11 SC12 SC13 SC14 SC15 
Sc en 
ar io 
s 
0.16 0.22 0.40 0.44 0.36 0.44 0.10 0.24 0.38 0.50 0.52 0.80 0.90 0.98 1.00 0.98 0.92 0.98 0.74 0.70 0.88 0.90 0.92 0.92 0.16 0.18 0.42 0.64 0.82 0.74 0.02 0.16 0.40 0.68 0.74 0.84 0.04 0.02 0.08 0.14 0.20 0.18 0.00 0.00 0.12 0.18 0.24 0.32 0.00 0.02 0.04 0.02 0.08 0.00 
(b) 8 Threads 
100 200 500 1000 2000 4000 Iterations 
SC07 SC08 SC09 SC10 SC11 SC12 SC13 SC14 SC15 
Sc en 
ar io 
s 
0.16 0.28 0.36 0.52 0.44 0.42 0.28 0.24 0.44 0.62 0.68 0.76 0.96 1.00 1.00 1.00 1.00 0.92 0.58 0.74 0.80 0.88 0.92 0.92 0.20 0.30 0.56 0.80 0.90 0.86 0.06 0.06 0.58 0.64 0.80 0.86 0.02 0.02 0.08 0.26 0.20 0.18 0.00 0.00 0.06 0.28 0.24 0.44 0.00 0.02 0.08 0.14 0.10 0.00 
(c) 24 Threads 
Fig. 7: Evaluation of the success rate (i.e. 1 − collision rate) for the root parallelization with similarity vote for 1, 8 and 24 threads 
B. Root Parallelization 
Similarity merge does neither perform well, nor does it scale, see Fig. 10c. Different parameter values for γ, led to comparable results. 
Results for the similarity vote indicate a performance gain for lower iteration counts which seems to increase until 1000 iterations and tapers off afterwards, pictured in Fig. 10d. A detailed evaluation for the similarity vote is shown in Fig. 7. For lower numbers of iterations the improvement is
100 200 500 1000 2000 4000 Iterations 
0.1 
0.2 
0.3 
0.4 
0.5 
0.6 
0.7 Su 
cc es 
s R 
at e 
Leaf Max Leaf Mean Root Merge Root Vote Single Thread 
Fig. 8: Comparison of the different proposed parallelization strategies; The shaded region represents the deviation (2σ), of the mean success rate for the single-threaded baseline. The x-axis uses a logarithmic scale. 
considerable. At 100 iterations the success rate improves by approximately 100 percent, and keeps an improvement of roughly 45 percent until reaching 1000 iterations. 
V. CONCLUSION AND OUTLOOK 
The parallelization of MCTS in continuous domains creates novel challenges, which is especially true for root paralleliza-tion. Different solutions were demonstrated and evaluated to address these challenges. Standard leaf parallelization with mean selection, which has been shown to perform poorly in discrete domains seems to be less promising. However, the modification to maximum selection performed considerably better, which was to be expected in a cooperative multi-agent environment. Root parallelization with similarity merge yields no significant improvement. In combination with simi-larity voting the performance of root parallelization improved considerably, especially for lower iteration counts. Overall similarity voting performed best, cf. Fig. 8. 
While the proposed solutions achieve higher success rates, they need to be optimized in order to be more time efficient, as the allocation of threads does incur a considerable overhead, especially when the number of threads increases. 
In our future research we will look into additional tech-niques, promising a speed-up which scales better with the number of threads [20], as the standard techniques for par-allelization do not address the trade of between exploration and exploitation well enough [19], [20], [25]. 
APPENDIX 
For reasons of completeness the results for all scenarios are presented in Fig. 10 and Fig. 9. 
REFERENCES 
[1] L. Kocsis and C. Szepesvári, “Bandit based monte-carlo planning,” in Machine Learning: ECML 2006. Berlin, Heidelberg: Springer Berlin Heidelberg, 2006. 
[2] D. Silver, A. Huang et al., “Mastering the game of Go with deep neural networks and tree search,” Nature, 2016. 
[3] D. Silver, J. Schrittwieser et al., “Mastering the game of Go without human knowledge,” Nature, 2017. 
[4] J. Schrittwieser, I. Antonoglou et al., “Mastering atari, go, chess and shogi by planning with a learned model,” 2019. 
[5] T. Cazenave and N. Jouandeau, “On the Parallelization of UCT,” Monte Carlo Tree Search, 2007. 
[6] G. M. J. B. Chaslot, M. H. M. Winands et al., “Parallel monte-carlo tree search,” in Computers and Games. Berlin, Heidelberg: Springer Berlin Heidelberg, 2008. 
[7] Y. Soejima, A. Kishimoto et al., “Evaluating root parallelization in go,” IEEE Transactions on Computational Intelligence and AI in Games, vol. 2, no. 4, Dec 2010. 
[8] M. Enzenberger and M. Müller, “A lock-free multithreaded Monte-Carlo tree search algorithm,” in Lecture Notes in Computer Science. Springer, Berlin, Heidelberg, 2010, vol. 6048 LNCS. 
[9] A. Bourki, G. Chaslot et al., “Scalability and parallelization of monte-carlo tree search,” in Computers and Games. Berlin, Heidelberg: Springer Berlin Heidelberg, 2011. 
[10] K. Rocki and R. Suda, “Large-scale parallel monte carlo tree search on gpu,” in 2011 IEEE International Symposium on Parallel and Distributed Processing Workshops and Phd Forum, May 2011. 
[11] A. Couëtoux, J.-B. Hoock et al., “Continuous upper confidence trees,” in Learning and Intelligent Optimization. Berlin, Heidelberg: Springer Berlin Heidelberg, 2011. 
[12] P. Rolet, M. Sebag et al., “Optimal active learning through billiards and upper confidence trees in continous domains,” in Proceedings of the ECML conference, 2009. 
[13] T. Yee, V. Lisy et al., “Monte carlo tree search in continuous action spaces with execution uncertainty,” in Proceedings of the Twenty-Fifth International Joint Conference on Artificial Intelligence, ser. IJCAI’16. AAAI Press, 2016. 
[14] K. Kurzer, F. Engelhorn et al., “Decentralized Cooperative Planning for Automated Vehicles with Continuous Monte Carlo Tree Search,” in 2018 21st International Conference on Intelligent Transportation Systems (ITSC). IEEE, 2018. 
[15] T. M. Moerland, J. Broekens et al., “A0c: Alpha zero in continuous action space,” 2018. 
[16] R. S. Sutton and A. G. Barto, Reinforcement Learning: An Introduction. Cambridge, MA, USA: A Bradford Book, 2018. 
[17] C. B. Browne, E. Powley et al., “A survey of Monte Carlo tree search methods,” IEEE Transactions on Computational Intelligence and AI in Games, 2012. 
[18] S. A. Mirsoleimani., J. van den Herik. et al., “A lock-free algorithm for parallel mcts,” in Proceedings of the 10th International Conference on Agents and Artificial Intelligence - Volume 1: ICAART,, INSTICC. SciTePress, 2018. 
[19] S. A. Mirsoleimani., A. Plaat. et al., “An analysis of virtual loss in parallel mcts,” in Proceedings of the 9th International Conference on Agents and Artificial Intelligence - Volume 1: ICAART,, INSTICC. SciTePress, 2017. 
[20] A. Liu, J. Chen et al., “Watch the unobserved: A simple approach to parallelizing monte carlo tree search,” in International Conference on Learning Representations, 2020. 
[21] G. M. J.-B. Chaslot, M. H. M. Winands et al., “Progressive strategies for monte-carlo tree search,” New Mathematics and Natural Computation, vol. 04, no. 03, 2008. 
[22] R. Coulom, “Efficient selectivity and backup operators in monte-carlo tree search,” in Computers and Games. Berlin, Heidelberg: Springer Berlin Heidelberg, 2007. 
[23] Y. Wang, J. yves Audibert et al., “Algorithms for infinitely many-armed bandits,” in Advances in Neural Information Processing Systems 21. Curran Associates, Inc., 2009. 
[24] D. J. N. J. Soemers, C. F. Sironi et al., “Enhancements for real-time monte-carlo tree search in general video game playing,” in 2016 IEEE Conference on Computational Intelligence and Games (CIG), Sep. 2016. 
[25] P. Auer, “Using confidence bounds for exploitation-exploration trade-offs,” The Journal of Machine Learning Research, vol. 3, no. null, Mar. 2003.
100 200 500 1000 2000 4000 Iterations 
SC01 SC02 SC03 SC04 SC05 SC06 SC07 SC08 SC09 SC10 SC11 SC12 SC13 SC14 SC15 
Sc en 
ar io 
s 0.98 0.98 0.98 0.99 0.99 1.00 0.59 0.66 0.84 0.91 0.93 0.95 1.00 1.00 1.00 1.00 1.00 1.00 0.96 0.94 0.98 0.99 0.99 0.97 0.82 0.92 0.97 0.97 0.98 0.96 0.93 0.96 0.99 1.00 0.99 1.00 0.13 0.16 0.28 0.40 0.39 0.58 0.09 0.20 0.28 0.39 0.50 0.65 0.56 0.90 0.96 0.94 0.90 0.90 0.28 0.46 0.74 0.75 0.77 0.81 0.04 0.10 0.26 0.53 0.69 0.80 0.01 0.03 0.13 0.25 0.56 0.85 0.02 0.01 0.03 0.07 0.10 0.11 0.00 0.01 0.05 0.10 0.14 0.24 0.00 0.02 0.02 0.02 0.01 0.00 
(a) 1 Thread 
100 200 500 1000 2000 4000 Iterations 
SC01 SC02 SC03 SC04 SC05 SC06 SC07 SC08 SC09 SC10 SC11 SC12 SC13 SC14 SC15 
Sc en 
ar io 
s 
1.00 1.00 0.98 1.00 0.98 1.00 0.82 0.90 0.86 0.90 0.90 0.96 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 0.98 1.00 1.00 1.00 0.94 0.98 1.00 0.96 0.96 0.96 1.00 1.00 1.00 1.00 1.00 1.00 0.16 0.22 0.40 0.44 0.36 0.44 0.10 0.24 0.38 0.50 0.52 0.80 0.90 0.98 1.00 0.98 0.92 0.98 0.74 0.70 0.88 0.90 0.92 0.92 0.16 0.18 0.42 0.64 0.82 0.74 0.02 0.16 0.40 0.68 0.74 0.84 0.04 0.02 0.08 0.14 0.20 0.18 0.00 0.00 0.12 0.18 0.24 0.32 0.00 0.02 0.04 0.02 0.08 0.00 
(b) 8 Threads 
100 200 500 1000 2000 4000 Iterations 
SC01 SC02 SC03 SC04 SC05 SC06 SC07 SC08 SC09 SC10 SC11 SC12 SC13 SC14 SC15 
Sc en 
ar io 
s 
1.00 1.00 1.00 1.00 1.00 1.00 0.94 0.86 0.98 0.96 0.94 0.90 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 0.94 1.00 1.00 1.00 0.98 1.00 1.00 1.00 1.00 1.00 1.00 1.00 0.16 0.28 0.36 0.52 0.44 0.42 0.28 0.24 0.44 0.62 0.68 0.76 0.96 1.00 1.00 1.00 1.00 0.92 0.58 0.74 0.80 0.88 0.92 0.92 0.20 0.30 0.56 0.80 0.90 0.86 0.06 0.06 0.58 0.64 0.80 0.86 0.02 0.02 0.08 0.26 0.20 0.18 0.00 0.00 0.06 0.28 0.24 0.44 0.00 0.02 0.08 0.14 0.10 0.00 
(c) 24 Threads 
Fig. 9: Evaluation of the success rate (i.e. 1 − collision rate) for the root parallelization with similarity vote for 1, 8 and 24 threads 
100 200 500 1000 2000 4000 Iterations 
0.40 
0.45 
0.50 
0.55 
0.60 
0.65 
0.70 
0.75 
0.80 
Su cc 
es s 
R at 
e 
8 Threads 1 Threads 24 Threads 
(a) Leaf Parallelization: Mean 
100 200 500 1000 2000 4000 Iterations 
0.40 
0.45 
0.50 
0.55 
0.60 
0.65 
0.70 
0.75 
0.80 
Su cc 
es s 
R at 
e 
8 Threads 1 Threads 24 Threads 
(b) Leaf Parallelization: Maximum 
100 200 500 1000 2000 4000 Iterations 
0.40 
0.45 
0.50 
0.55 
0.60 
0.65 
0.70 
0.75 
0.80 
Su cc 
es s 
R at 
e 
8 Threads 1 Threads 24 Threads 
(c) Root Parallelization: Similarity Merge 
100 200 500 1000 2000 4000 Iterations 
0.40 
0.45 
0.50 
0.55 
0.60 
0.65 
0.70 
0.75 
0.80 
Su cc 
es s 
R at 
e 
8 Threads 1 Threads 24 Threads 
(d) Root Parallelization: Similarity Vote 
Fig. 10: Scalability of the different proposed parallelization strategies; The shaded region represents the deviation (2σ), of 
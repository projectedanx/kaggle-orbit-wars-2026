> Source: https://en.wikipedia.org/wiki/Monte_Carlo_tree_search

Monte Carlo tree search - Wikipedia
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
1 History Toggle History subsection
1.1 Monte Carlo method
1.2 Monte Carlo tree search (MCTS)
2 Principle of operation
3 Pure Monte Carlo game search
4 Exploration and exploitation
5 Advantages and disadvantages
6 Improvements
7 See also
8 References
9 Bibliography
10 External links [-]
Toggle the table of contents
Monte Carlo tree search
[-]
12 languages
Català
Español
فارسی
Français
Magyar
Italiano
日本語
한국어
Polski
Українська
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
Heuristic search algorithm for evaluating game trees
Monte Carlo tree search
In computer science, Monte Carlo tree search ( MCTS) is a heuristic search algorithm for some kinds of decision processes, most notably those employed in software that plays board games. In that context MCTS is used to solve the game tree.
MCTS was combined with neural networks in 2016 [1] and has been used in multiple board games like Chess, Shogi, [2] Checkers, Backgammon, Contract Bridge, Go, Scrabble, and Clobber [3] as well as in turn-based-strategy video games (such as Total War: Rome II's implementation in the high level campaign AI [4]) and applications outside of games. [5]
History
[ edit]
Monte Carlo method
[ edit]
The Monte Carlo method, which uses random sampling for deterministic problems which are difficult or impossible to solve using other approaches, dates back to the 1940s. [6] In his 1987 PhD thesis, Bruce Abramson combined minimax search with an expected-outcome model based on random game playouts to the end, instead of the usual static evaluation function. Abramson said the expected-outcome model "is shown to be precise, accurate, easily estimable, efficiently calculable, and domain-independent." [7] He experimented in-depth with tic-tac-toe and then with machine-generated evaluation functions for Othello and chess.
Such methods were then explored and successfully applied to heuristic search in the field of automated theorem proving by W. Ertel, J. Schumann and C. Suttner in 1989, [8] [9] [10] thus improving the exponential search times of uninformed search algorithms such as e.g. breadth-first search, depth-first search or iterative deepening.
In 1992, B. Brügmann employed it for the first time in a Go-playing program. [11] In 2002, Chang et al. [12] proposed the idea of "recursive rolling out and backtracking" with "adaptive" sampling choices in their Adaptive Multi-stage Sampling (AMS) algorithm for the model of Markov decision processes. AMS was the first work to explore the idea of UCB-based exploration and exploitation in constructing sampled/simulated (Monte Carlo) trees and was the main seed for UCT (Upper Confidence Trees). [13]
Monte Carlo tree search (MCTS)
[ edit] 
The rating of best Go-playing programs on the KGS server since 2007. Since 2006, all the best programs use Monte Carlo tree search. [14]
In 2006, inspired by its predecessors, [15] Rémi Coulom described the application of the Monte Carlo method to game-tree search and coined the name Monte Carlo tree search, [16] L. Kocsis and Cs. Szepesvári developed the UCT (Upper Confidence bounds applied to Trees) algorithm, [17] and S. Gelly et al. implemented UCT in their program MoGo. [18] In 2008, MoGo achieved dan (master) level in 9×9 Go, [19] and the Fuego program began to win against strong amateur players in 9×9 Go. [20]
In January 2012, the Zen program won 3:1 in a Go match on a 19×19 board with an amateur 2 dan player. [21] Google Deepmind developed the program AlphaGo, which in October 2015 became the first Computer Go program to beat a professional human Go player without handicaps on a full-sized 19x19 board. [1] [22] [23] In March 2016, AlphaGo was awarded an honorary 9-dan (master) level in 19×19 Go for defeating Lee Sedol in a five-game match with a final score of four games to one. [24] AlphaGo represents a significant improvement over previous Go programs as well as a milestone in machine learning as it uses Monte Carlo tree search with artificial neural networks (a deep learning method) for policy (move selection) and value, giving it efficiency far surpassing previous programs. [25]
The MCTS algorithm has also been used in programs that play other board games (for example Hex, [26] Havannah, [27] Game of the Amazons, [28] and Arimaa [29]), real-time video games (for instance Ms. Pac-Man [30] [31] and Fable Legends [32]), and nondeterministic games (such as skat, [33] poker, [34] Magic: The Gathering, [35] or Settlers of Catan [36]).
Principle of operation
[ edit]
The focus of MCTS is on the analysis of the most promising moves, expanding the search tree based on random sampling of the search space. The application of Monte Carlo tree search in games is based on many playouts, also called roll-outs. In each playout, the game is played out to the very end by selecting moves at random. The final game result of each playout is then used to weight the nodes in the game tree so that better nodes are more likely to be chosen in future playouts.
The most basic way to use playouts is to apply the same number of playouts after each legal move of the current player, then choose the move which led to the most victories. [11] The efficiency of this method—called Pure Monte Carlo Game Search—often increases with time as more playouts are assigned to the moves that have frequently resulted in the current player's victory according to previous playouts. Each round of Monte Carlo tree search consists of four steps: [37]
Selection: Start from root R and select successive child nodes until a leaf node L is reached. The root is the current game state and a leaf is any node that has a potential child from which no simulation (playout) has yet been initiated. The section below says more about a way of biasing choice of child nodes that lets the game tree expand towards the most promising moves, which is the essence of Monte Carlo tree search.
Expansion: Unless L ends the game decisively (e.g. win/loss/draw) for either player, create one (or more) child nodes and choose node C from one of them. Child nodes are any valid moves from the game position defined by L.
Simulation: Complete one random playout from node C. This step is sometimes also called playout or rollout. A playout may be as simple as choosing uniform random moves until the game is decided (for example in chess, the game is won, lost, or drawn).
Backpropagation: Use the result of the playout to update information in the nodes on the path from C to R. 
Step of Monte Carlo tree search.
This graph shows the steps involved in one decision, with each node showing the ratio of wins to total playouts from that point in the game tree for the player that the node represents. [38] In the Selection diagram, black is about to move. The root node shows there are 11 wins out of 21 playouts for white from this position so far. It complements the total of 10/21 black wins shown along the three black nodes under it, each of which represents a possible black move. Note that this graph does not follow the UCT algorithm described below.
If white loses the simulation, all nodes along the selection incremented their simulation count (the denominator), but among them only the black nodes were credited with wins (the numerator). If instead white wins, all nodes along the selection would still increment their simulation count, but among them only the white nodes would be credited with wins. In games where draws are possible, a draw causes the numerator for both black and white to be incremented by 0.5 and the denominator by 1. This ensures that during selection, each player's choices expand towards the most promising moves for that player, which mirrors the goal of each player to maximize the value of their move.
Rounds of search are repeated as long as the time allotted to a move remains. Then the move with the most simulations made (i.e. the highest denominator) is chosen as the final answer.
Pure Monte Carlo game search
[ edit]
This basic procedure can be applied to any game whose positions necessarily have a finite number of moves and finite length. For each position, all feasible moves are determined: k random games are played out to the very end, and the scores are recorded. The move leading to the best score is chosen. Ties are broken by fair coin flips. Pure Monte Carlo Game Search results in strong play in several games with random elements, as in the game EinStein würfelt nicht!. It converges to optimal play (as k tends to infinity) in board filling games with random turn order, for instance in the game Hex with random turn order. [39] DeepMind's AlphaZero replaces the simulation step with an evaluation based on a neural network. [2]
Exploration and exploitation
[ edit]
The main difficulty in selecting child nodes is maintaining some balance between the exploitation of deep variants after moves with high average win rate and the exploration of moves with few simulations. The first formula for balancing exploitation and exploration in games, called UCT ( Upper Confidence Bound 1 applied to trees), was introduced by Levente Kocsis and Csaba Szepesvári. [17] UCT is based on the UCB1 formula derived by Auer, Cesa-Bianchi, and Fischer [40] and the probably convergent AMS (Adaptive Multi-stage Sampling) algorithm first applied to multi-stage decision-making models (specifically, Markov Decision Processes) by Chang, Fu, Hu, and Marcus. [12] Kocsis and Szepesvári recommend to choose in each node of the game tree the move for which the expression w i n i + c ln  N i n i {\displaystyle {\frac {w_{i}}{n_{i}}}+c{\sqrt {\frac {\ln N_{i}}{n_{i}}}}} 
has the highest value. In this formula:
w i stands for the number of wins for the node considered after the i-th move
n i stands for the number of simulations for the node considered after the i-th move
N i stands for the total number of simulations after the i-th move run by the parent node of the one considered
c is the exploration parameter—theoretically equal to 2 {\displaystyle {\sqrt {2}}} ; in practice usually chosen empirically
The first component of the formula above corresponds to exploitation; it is high for moves with high average win ratio. The second component corresponds to exploration; it is high for moves with few simulations.
Most contemporary implementations of Monte Carlo tree search are based on some variant of UCT that traces its roots back to the AMS simulation optimization algorithm for estimating the value function in finite-horizon Markov Decision Processes (MDPs) introduced by Chang et al. [12] (2005) in Operations Research. (AMS was the first work to explore the idea of UCB-based exploration and exploitation in constructing sampled/simulated (Monte Carlo) trees and was the main seed for UCT. [13])
Advantages and disadvantages
[ edit]
Although it has been proven that the evaluation of moves in Monte Carlo tree search converges to minimax when using UCT, [17] [41] the basic version of Monte Carlo tree search converges only in so called "Monte Carlo Perfect" games. [42] However, Monte Carlo tree search does offer significant advantages over alpha–beta pruning and similar algorithms that minimize the search space.
In particular, pure Monte Carlo tree search does not need an explicit evaluation function. Simply implementing the game's mechanics is sufficient to explore the search space (i.e. the generating of allowed moves in a given position and the game-end conditions). As such, Monte Carlo tree search can be employed in games without a developed theory or in general game playing.
The game tree in Monte Carlo tree search grows asymmetrically as the method concentrates on the more promising subtrees. Thus [dubious–discuss] , it achieves better results than classical algorithms in games with a high branching factor.
A disadvantage is that in certain positions, there may be moves that look superficially strong, but that actually lead to a loss via a subtle line of play. Such "trap states" require thorough analysis to be handled correctly, particularly when playing against an expert player; however, MCTS may not "see" such lines due to its policy of selective node expansion. [43] [44] It is believed that this may have been part of the reason for AlphaGo's loss in its fourth game against Lee Sedol. In essence, the search attempts to prune sequences which are less relevant. In some cases, a play can lead to a very specific line of play which is significant, but which is overlooked when the tree is pruned, and this outcome is therefore "off the search radar". [45]
Improvements
[ edit]
Various modifications of the basic Monte Carlo tree search method have been proposed to shorten the search time. Some employ domain-specific expert knowledge, others do not.
Monte Carlo tree search can use either light or heavy playouts. Light playouts consist of random moves while heavy playouts apply various heuristics to influence the choice of moves. These heuristics may employ the results of previous playouts (e.g. the Last Good Reply heuristic [46]) or expert knowledge of a given game. For instance, in many Go-playing programs certain stone patterns in a portion of the board influence the probability of moving into that area. [18] Paradoxically, playing suboptimally in simulations sometimes makes a Monte Carlo tree search program play stronger overall. [47] 
Patterns of hane (surrounding opponent stones) used in playouts by the MoGo program. It is advantageous for both black and white to put a stone on the middle square, except the rightmost pattern where it favors black only. [18]
Domain-specific knowledge may be employed when building the game tree to help the exploitation of some variants. One such method assigns nonzero priors to the number of won and played simulations when creating each child node, leading to artificially raised or lowered average win rates that cause the node to be chosen more or less frequently, respectively, in the selection step. [48] A related method, called progressive bias, consists in adding to the UCB1 formula a b i n i {\displaystyle {\frac {b_{i}}{n_{i}}}} 
element, where b i is a heuristic score of the i-th move. [37]
The basic Monte Carlo tree search collects enough information to find the most promising moves only after many rounds; until then its moves are essentially random. This exploratory phase may be reduced significantly in a certain class of games using RAVE ( Rapid Action Value Estimation). [48] In these games, permutations of a sequence of moves lead to the same position. Typically, they are board games in which a move involves placement of a piece or a stone on the board. In such games the value of each move is often only slightly influenced by other moves.
In RAVE, for a given game tree node N, its child nodes C i store not only the statistics of wins in playouts started in node N but also the statistics of wins in all playouts started in node N and below it, if they contain move i (also when the move was played in the tree, between node N and a playout). This way the contents of tree nodes are influenced not only by moves played immediately in a given position but also by the same moves played later. 
RAVE on the example of tic-tac-toe. In red nodes, the RAVE statistics will be updated after the b1-a2-b3 simulation.
When using RAVE, the selection step selects the node, for which the modified UCB1 formula ( 1 − β ( n i , n ~ i ) ) w i n i + β ( n i , n ~ i ) w ~ i n ~ i + c ln  t n i {\displaystyle (1-\beta (n_{i},{\tilde {n}}{i})){\frac {w{i}}{n_{i}}}+\beta (n_{i},{\tilde {n}}{i}){\frac {{\tilde {w}}{i}}{{\tilde {n}}{i}}}+c{\sqrt {\frac {\ln t}{n{i}}}}} 
has the highest value. In this formula, w ~ i {\displaystyle {\tilde {w}}_{i}} 
and n ~ i {\displaystyle {\tilde {n}}_{i}} 
stand for the number of won playouts containing move i and the number of all playouts containing move i, and the β ( n i , n ~ i ) {\displaystyle \beta (n_{i},{\tilde {n}}_{i})} 
function should be close to one and to zero for relatively small and relatively big n i and n ~ i {\displaystyle {\tilde {n}}_{i}} 
, respectively. One of many formulas for β ( n i , n ~ i ) {\displaystyle \beta (n_{i},{\tilde {n}}_{i})} 
, proposed by D. Silver, [49] says that in balanced positions one can take β ( n i , n ~ i ) = n ~ i n i + n ~ i + 4 b 2 n i n ~ i {\displaystyle \beta (n_{i},{\tilde {n}}{i})={\frac {{\tilde {n}}{i}}{n_{i}+{\tilde {n}}{i}+4b^{2}n{i}{\tilde {n}}_{i}}}} 
, where b is an empirically chosen constant.
Heuristics used in Monte Carlo tree search often require many parameters. There are automated methods to tune the parameters to maximize the win rate. [50]
Monte Carlo tree search can be concurrently executed by many threads or processes. There are several fundamentally different methods of its parallel execution: [51]
Leaf parallelization, i.e. parallel execution of many playouts from one leaf of the game tree.
Root parallelization, i.e. building independent game trees in parallel and making the move basing on the root-level branches of all these trees.
Tree parallelization, i.e. parallel building of the same game tree, protecting data from simultaneous writes either with one, global mutex, with more mutexes, or with non-blocking synchronization. [52]
See also
[ edit]
AlphaGo, a Go program using Monte Carlo tree search, reinforcement learning and deep learning.
AlphaGo Zero, an updated Go program using Monte Carlo tree search, reinforcement learning and deep learning.
AlphaZero, a generalized version of AlphaGo Zero using Monte Carlo tree search, reinforcement learning and deep learning.
Leela Chess Zero, a free software implementation of AlphaZero's methods to chess, which is currently among the leading chess playing programs.
References
[ edit]
^ Jump up to: a  b Silver, David; Huang, Aja; Maddison, Chris J.; Guez, Arthur; Sifre, Laurent; Driessche, George van den; Schrittwieser, Julian; Antonoglou, Ioannis; Panneershelvam, Veda; Lanctot, Marc; Dieleman, Sander; Grewe, Dominik; Nham, John; Kalchbrenner, Nal; Sutskever, Ilya; Lillicrap, Timothy; Leach, Madeleine; Kavukcuoglu, Koray; Graepel, Thore; Hassabis, Demis (28 January 2016). "Mastering the game of Go with deep neural networks and tree search". Nature. 529 (7587): 484– 489. Bibcode: 2016Natur.529..484S. doi: 10.1038/nature16961. ISSN 0028-0836. PMID 26819042. S2CID 515925. 
^ Jump up to: a  b Silver, David (2017). "Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm". arXiv: 1712.01815v1 [ cs.AI].
^ Rajkumar, Prahalad. "A Survey of Monte-Carlo Techniques in Games" (PDF). cs.umd.edu. Archived (PDF) from the original on 2023-04-07.
^ "Monte-Carlo Tree Search in TOTAL WAR: ROME II's Campaign AI". AI Game Dev. Archived from the original on 13 March 2017. Retrieved 25 February 2017.
^ Kemmerling, Marco; Lütticke, Daniel; Schmitt, Robert H. (1 January 2024). "Beyond games: a systematic review of neural Monte Carlo tree search applications". Applied Intelligence. 54 (1): 1020– 1046. arXiv: 2303.08060. doi: 10.1007/s10489-023-05240-w. ISSN 1573-7497.
^ Nicholas, Metropolis; Stanislaw, Ulam (1949). "The monte carlo method". Journal of the American Statistical Association. 44 (247): 335– 341. doi: 10.1080/01621459.1949.10483310. PMID 18139350.
^ Abramson, Bruce (1987). The Expected-Outcome Model of Two-Player Games (PDF). Technical report, Department of Computer Science, Columbia University. Retrieved 23 December 2013.
^ Wolfgang Ertel; Johann Schumann; Christian Suttner (1989). "Learning Heuristics for a Theorem Prover using Back Propagation.". In J. Retti; K. Leidlmair (eds.). 5. Österreichische Artificial-Intelligence-Tagung. Informatik-Fachberichte 208, pp. 87-95. Springer. Archived from the original on 2021-04-15. Retrieved 2016-08-14.
^ Christian Suttner; Wolfgang Ertel (1990). "Automatic Acquisition of Search Guiding Heuristics.". CADE90, 10th Int. Conf. on Automated Deduction.pp. 470-484. LNAI 449. Springer. Archived from the original on 2021-04-15. Retrieved 2016-08-14.
^ Christian Suttner; Wolfgang Ertel (1991). "Using Back-Propagation Networks for Guiding the Search of a Theorem Prover". Journal of Neural Networks Research & Applications. 2 (1): 3– 16. Archived from the original on 2021-04-15. Retrieved 2016-08-14.
^ Jump up to: a  b Brügmann, Bernd (1993). Monte Carlo Go (PDF). Technical report, Department of Physics, Syracuse University.
^ Jump up to: a  b  c Chang, Hyeong Soo; Fu, Michael C.; Hu, Jiaqiao; Marcus, Steven I. (2005). "An Adaptive Sampling Algorithm for Solving Markov Decision Processes" (PDF). Operations Research. 53: 126– 139. doi: 10.1287/opre.1040.0145. hdl: 1903/6264. Archived from the original (PDF) on 2021-04-20. Retrieved 2016-02-25.
^ Jump up to: a  b Hyeong Soo Chang; Michael Fu; Jiaqiao Hu; Steven I. Marcus (2016). "Google DeepMind's Alphago: O.R.'s unheralded role in the path-breaking achievement". OR/MS Today. 45 (5): 24– 29.
^ "Sensei's Library: KGSBotRatings" (PDF). Archived from the original on 2009-06-25. Retrieved 2012-05-03.
^ Rémi Coulom (2008). "The Monte-Carlo Revolution in Go" (PDF). Japanese-French Frontiers of Science Symposium.
^ Rémi Coulom (2007). "Efficient Selectivity and Backup Operators in Monte-Carlo Tree Search". Computers and Games, 5th International Conference, CG 2006, Turin, Italy, May 29–31, 2006. Revised Papers. H. Jaap van den Herik, Paolo Ciancarini, H. H. L. M. Donkers (eds.). Springer. pp. 72– 83. CiteSeerX 10.1.1.81.6817. ISBN 978-3-540-75537-1 .
^ Jump up to: a  b  c Kocsis, Levente; Szepesvári, Csaba (2006). "Bandit based Monte-Carlo Planning". In Fürnkranz, Johannes; Scheffer, Tobias; Spiliopoulou, Myra (eds.). Machine Learning: ECML 2006, 17th European Conference on Machine Learning, Berlin, Germany, September 18–22, 2006, Proceedings. Lecture Notes in Computer Science. Vol. 4212. Springer. pp. 282– 293. CiteSeerX 10.1.1.102.1296. doi: 10.1007/11871842_29. ISBN 3-540-45375-X .
^ Jump up to: a  b  c Sylvain Gelly; Yizao Wang; Rémi Munos; Olivier Teytaud (November 2006). Modification of UCT with Patterns in Monte-Carlo Go (PDF). Technical report, INRIA.
^ Chang-Shing Lee; Mei-Hui Wang; Guillaume Chaslot; Jean-Baptiste Hoock; Arpad Rimmel; Olivier Teytaud; Shang-Rong Tsai; Shun-Chin Hsu; Tzung-Pei Hong (2009). "The Computational Intelligence of MoGo Revealed in Taiwan's Computer Go Tournaments" (PDF). IEEE Transactions on Computational Intelligence and AI in Games. 1 (1): 73– 89. Bibcode: 2009ITCIA...1...73L. CiteSeerX 10.1.1.470.6018. doi: 10.1109/tciaig.2009.2018703. S2CID 15266518.
^ Markus Enzenberger; Martin Mūller (2008). Fuego – An Open-Source Framework for Board Games and Go Engine Based on Monte Carlo Tree Search (PDF). Technical report, University of Alberta.
^ "The Shodan Go Bet". Retrieved 2012-05-02.
^ "Research Blog: AlphaGo: Mastering the ancient game of Go with Machine Learning". Google Research Blog. 27 January 2016.
^ "Google achieves AI 'breakthrough' by beating Go champion". BBC News. 27 January 2016.
^ "Match 1 - Google DeepMind Challenge Match: Lee Sedol vs AlphaGo". Youtube. 9 March 2016.
^ "Google AlphaGo AI clean sweeps European Go champion". ZDNet. 28 January 2016.
^ Broderick Arneson; Ryan Hayward; Philip Henderson (June 2009). "MoHex Wins Hex Tournament" (PDF). ICGA Journal. 32 (2): 114– 116. doi: 10.3233/ICG-2009-32218.
^ Timo Ewalds (2011). Playing and Solving Havannah (PDF). Master's thesis, University of Alberta.
^ Richard J. Lorentz (2008). "Amazons Discover Monte-Carlo". Computers and Games, 6th International Conference, CG 2008, Beijing, China, September 29 – October 1, 2008. Proceedings. H. Jaap van den Herik, Xinhe Xu, Zongmin Ma, Mark H. M. Winands (eds.). Springer. pp. 13– 24. ISBN 978-3-540-87607-6 .
^ Tomáš Kozelek (2009). Methods of MCTS and the game Arimaa (PDF). Master's thesis, Charles University in Prague.
^ Xiaocong Gan; Yun Bao; Zhangang Han (December 2011). "Real-Time Search Method in Nondeterministic Game – Ms. Pac-Man". ICGA Journal. 34 (4): 209– 222. doi: 10.3233/ICG-2011-34404.
^ Tom Pepels; Mark H. M. Winands; Marc Lanctot (September 2014). "Real-Time Monte Carlo Tree Search in Ms Pac-Man". IEEE Transactions on Computational Intelligence and AI in Games. 6 (3): 245– 257. doi: 10.1109/tciaig.2013.2291577.
^ Mountain, Gwaredd (2015). "Tactical Planning and Real-time MCTS in Fable Legends". Archived from the original on 2019-06-08. Retrieved 2019-06-08... we implemented a simulation based approach, which involved modelling the game play and using MCTS to search the potential plan space. Overall this worked well, ...
^ Michael Buro; Jeffrey Richard Long; Timothy Furtak; Nathan R. Sturtevant (2009). "Improving State Evaluation, Inference, and Search in Trick-Based Card Games". IJCAI 2009, Proceedings of the 21st International Joint Conference on Artificial Intelligence, Pasadena, California, USA, July 11–17, 2009. Craig Boutilier (ed.). pp. 1407– 1413. CiteSeerX 10.1.1.150.3077.
^ Jonathan Rubin; Ian Watson (April 2011). "Computer poker: A review". Artificial Intelligence. 175 ( 5– 6): 958– 987. doi: 10.1016/j.artint.2010.12.005.
^ C.D. Ward; P.I. Cowling (2009). "Monte Carlo Search Applied to Card Selection in Magic: The Gathering" (PDF). CIG'09 Proceedings of the 5th international conference on Computational Intelligence and Games. IEEE Press. Archived from the original (PDF) on 2016-05-28.
^ István Szita; Guillaume Chaslot; Pieter Spronck (2010). "Monte-Carlo Tree Search in Settlers of Catan" (PDF). In Jaap Van Den Herik; Pieter Spronck (eds.). Advances in Computer Games, 12th International Conference, ACG 2009, Pamplona, Spain, May 11–13, 2009. Revised Papers. Springer. pp. 21– 32. ISBN 978-3-642-12992-6 . Archived from the original (PDF) on 2016-03-04. Retrieved 2015-11-30.
^ Jump up to: a  b G.M.J.B. Chaslot; M.H.M. Winands; J.W.H.M. Uiterwijk; H.J. van den Herik; B. Bouzy (2008). "Progressive Strategies for Monte-Carlo Tree Search" (PDF). New Mathematics and Natural Computation. 4 (3): 343– 359. doi: 10.1142/s1793005708001094.
^ Bradberry, Jeff (2015-09-07). "Introduction to Monte Carlo Tree Search".
^ Peres, Yuval; Schramm, Oded; Sheffield, Scott; Wilson, David B. (2006). "Random-Turn Hex and other selection games". arXiv: math/0508580.
^ Auer, Peter; Cesa-Bianchi, Nicolò; Fischer, Paul (2002). "Finite-time Analysis of the Multiarmed Bandit Problem". Machine Learning. 47 (2/3): 235– 256. doi: 10.1023/a:1013689704352. S2CID 207609497.
^ Browne, Cameron B.; Powley, Edward; Whitehouse, Daniel; Lucas, Simon M.; Cowling, Peter I.; Rohlfshagen, Philipp; Tavener, Stephen; Perez, Diego; Samothrakis, Spyridon; Colton, Simon (2012). "A Survey of Monte Carlo Tree Search Methods". IEEE Transactions on Computational Intelligence and AI in Games. 4 (1): 1– 43. Bibcode: 2012ITCIA...4A6810B. doi: 10.1109/tciaig.2012.2186810. ISSN 1943-068X.
^ Althöfer, Ingo (2012). "On Board-Filling Games with Random-Turn Order and Monte Carlo Perfectness". Advances in Computer Games. Lecture Notes in Computer Science. Vol. 7168. pp. 258– 269. doi: 10.1007/978-3-642-31866-5_22. ISBN 978-3-642-31865-8 .
^ Ramanujan, Raghuram; Sabharwal, Ashish; Selman, Bart (May 2010). "On adversarial search spaces and sampling-based planning". ICAPS '10: Proceedings of the Twentieth International Conference on International Conference on Automated Planning and Scheduling. Icaps'10: 242– 245.
^ Ramanujan, Raghuram; Selman, Bart (March 2011). "Trade-Offs in Sampling-Based Adversarial Planning". Proceedings of the International Conference on Automated Planning and Scheduling. 21 (1): 202– 209. doi: 10.1609/icaps.v21i1.13472. S2CID 45147586.
^ "Lee Sedol defeats AlphaGo in masterful comeback - Game 4". Go Game Guru. Archived from the original on 2016-11-16. Retrieved 2017-07-04.
^ Drake, Peter (December 2009). "The Last-Good-Reply Policy for Monte-Carlo Go". ICGA Journal. 32 (4): 221– 227. doi: 10.3233/ICG-2009-32404.
^ Seth Pellegrino; Peter Drake (2010). "Investigating the Effects of Playout Strength in Monte-Carlo Go". Proceedings of the 2010 International Conference on Artificial Intelligence, ICAI 2010, July 12–15, 2010, Las Vegas Nevada, USA. Hamid R. Arabnia, David de la Fuente, Elena B. Kozerenko, José Angel Olivas, Rui Chang, Peter M. LaMonica, Raymond A. Liuzzi, Ashu M. G. Solo (eds.). CSREA Press. pp. 1015– 1018. ISBN 978-1-60132-148-0 .
^ Jump up to: a  b Gelly, Sylvain; Silver, David (2007). "Combining Online and Offline Knowledge in UCT" (PDF). Machine Learning, Proceedings of the Twenty-Fourth International Conference (ICML 2007), Corvallis, Oregon, USA, June 20–24, 2007. Zoubin Ghahramani (ed.). ACM. pp. 273– 280. ISBN 978-1-59593-793-3 . Archived from the original (PDF) on 2017-08-28.
^ David Silver (2009). Reinforcement Learning and Simulation-Based Search in Computer Go (PDF). PhD thesis, University of Alberta.
^ Rémi Coulom. "CLOP: Confident Local Optimization for Noisy Black-Box Parameter Tuning". ACG 2011: Advances in Computer Games 13 Conference, Tilburg, the Netherlands, November 20–22.
^ Guillaume M.J-B. Chaslot, Mark H.M. Winands, Jaap van den Herik (2008). "Parallel Monte-Carlo Tree Search" (PDF). Computers and Games, 6th International Conference, CG 2008, Beijing, China, September 29 – October 1, 2008. Proceedings. H. Jaap van den Herik, Xinhe Xu, Zongmin Ma, Mark H. M. Winands (eds.). Springer. pp. 60– 71. ISBN 978-3-540-87607-6 . {{ [cite book](https://en.wikipedia.org/wiki/Template:Cite_book)}} : CS1 maint: multiple names: authors list ( link)
^ Markus Enzenberger; Martin Müller (2010). "A Lock-free Multithreaded Monte-Carlo Tree Search Algorithm". In Jaap Van Den Herik; Pieter Spronck (eds.). Advances in Computer Games: 12th International Conference, ACG 2009, Pamplona, Spain, May 11–13, 2009, Revised Papers. Springer. pp. 14–20. CiteSeerX 10.1.1.161.1984. ISBN 978-3-642-12992-6 .
Bibliography
[ edit]
Cameron Browne; Edward Powley; Daniel Whitehouse; Simon Lucas; Peter I. Cowling; Philipp Rohlfshagen; Stephen Tavener; Diego Perez; Spyridon Samothrakis; Simon Colton (March 2012). "A Survey of Monte Carlo Tree Search Methods". IEEE Transactions on Computational Intelligence and AI in Games. 4 (1): 1– 43. Bibcode: 2012ITCIA...4A6810B. CiteSeerX 10.1.1.297.3086. doi: 10.1109/tciaig.2012.2186810. S2CID 9316331.
Maciej Świechowski, Konrad Godlewski, Bartosz Sawicki, Jacek Mańdziuk (July 2022). "Monte Carlo Tree Search: a Review of Recent Modifications and Applications". Springer Nature Artificial Intelligence Review. 56 (3): 497–2562 (66 pages). arXiv: 2103.04931. doi: 10.1007/s10462-022-10228-y. {{ [cite journal](https://en.wikipedia.org/wiki/Template:Cite_journal)}} : CS1 maint: multiple names: authors list ( link)
External links
[ edit]
Beginner's Guide to Monte Carlo Tree Search
hide
v
t
e
Graph and tree traversal algorithms
Search
α–β pruning
A*
IDA*
LPA*
SMA*
Best-first search
Beam search
Bidirectional search
Breadth-first search
Lexicographic
Parallel
B*
Depth-first search
Iterative deepening
D*
Fringe search
Jump point search
Monte Carlo tree search
SSS*
Shortest path
Bellman–Ford
Dijkstra's
Floyd–Warshall
Johnson's
Shortest path faster
Yen's
Minimum spanning tree
Borůvka's
Kruskal's
Prim's
Reverse-delete
List of graph search algorithms 
Retrieved from " https://en.wikipedia.org/w/index.php?title=Monte_Carlo_tree_search&oldid=1331518846"
Categories:
Combinatorial game theory
Heuristic algorithms
Monte Carlo methods
Optimal decisions
Computer Go
Hidden categories:
CS1: unfit URL
CS1 maint: multiple names: authors list
Articles with short description
Short description is different from Wikidata
All accuracy disputes
Articles with disputed statements from June 2019
This page was last edited on 6 January 2026, at 18:58 (UTC).
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
Monte Carlo tree search
12 languages Add topic 
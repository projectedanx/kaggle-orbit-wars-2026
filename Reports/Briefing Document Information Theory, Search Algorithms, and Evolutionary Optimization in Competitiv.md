# Briefing Document: Information Theory, Search Algorithms, and Evolutionary Optimization in Competitive AI

## Executive Summary

The synthesis of the provided research indicates a deep convergence between the physical laws of thermodynamics, information theory, and advanced computational search strategies. Central to this intersection is the principle that **information is physical**; every bit of data processed or erased incurs a thermodynamic cost, as defined by Landauer's Principle. This physical reality underpins the efficiency constraints of modern data centers and the metabolic costs of biological neural processing.

In the domain of Artificial Intelligence, **Monte Carlo Tree Search (MCTS)** has emerged as the premier heuristic search algorithm for complex decision processes, particularly in games with high branching factors like Go, Chess, and RTS simulations. While pure MCTS eliminates the need for explicit evaluation functions, its performance is significantly enhanced when combined with neural networks or optimized via **Evolutionary Algorithms (EAs)**. 

Recent breakthroughs highlight two critical optimization paths:
1.  **Adaptive Warm-Start Methodologies:** Solving the "cold-start" problem in AlphaZero-like reinforcement learning by using rollout-based enhancements that dynamically switch to neural network guidance based on performance.
2.  **Heuristic Parameter Tuning:** Using Genetic Algorithms to fine-tune the constants and weights of rule-based engines, as demonstrated by the **GeneBot** project, which outperformed human-coded baselines in Real-Time Strategy (RTS) environments.

---

## 1. The Thermodynamic Basis of Information

The relationship between thermodynamic entropy and information entropy is a cornerstone of modern physics and computation. 

### Core Concepts and Equivalence
*   **Statistical Mechanics:** Established by Boltzmann and Gibbs, thermodynamic entropy ($S$) is defined as $S = -k_B \sum p_i \ln p_i$.
*   **Information Theory:** Established by Claude Shannon, information entropy ($H$) uses a similar form: $H = -\sum p_i \log_b p_i$.
*   **The Physical Link:** G.N. Lewis noted in 1930 that "Gain in entropy always means loss of information." Physical entropy is essentially the amount of Shannon information required to define the detailed microscopic state of a system given its macroscopic description.

### Key Physical Principles
*   **Landauer's Principle:** Any logically irreversible operation, such as erasing a bit of information, must increase the entropy of the environment by at least $kT \ln 2$ of heat per bit. This has been experimentally confirmed and sets the fundamental lower bound for energy consumption in computing.
*   **Szilard’s Engine:** A thought experiment demonstrating that possessing a single bit of information about a particle's position can be converted into $k_B T \ln 2$ joules of useful work.
*   **Biological Efficiency:** Research on blowflies reveals that neural processing costs approximately $5 \times 10^{-14}$ Joules per bit. While far from the Landauer limit, biological systems remain significantly more efficient than modern silicon-based computers.

---

## 2. Monte Carlo Tree Search (MCTS) Fundamentals

MCTS is a search algorithm that balances exploration and exploitation to solve game trees without requiring a static evaluation function.

### The Four-Step Cycle
1.  **Selection:** Navigating from the root to a leaf node using a selection policy (typically UCT).
2.  **Expansion:** Adding one or more child nodes to the tree from the selected leaf.
3.  **Simulation (Playout/Rollout):** Completing a random or heuristic-driven game from the new node to a terminal state.
4.  **Backpropagation:** Updating the win/visit statistics of all ancestral nodes based on the simulation result.

### The UCT Algorithm
The **Upper Confidence Bound applied to Trees (UCT)** is the standard formula for balancing search depth:
$$\text{UCT} = \frac{w_i}{n_i} + c \sqrt{\frac{\ln N_i}{n_i}}$$
*   $w_i$: Number of wins for the node.
*   $n_i$: Number of simulations for the node.
*   $N_i$: Total simulations for the parent node.
*   $c$: Exploration parameter (theoretically $\sqrt{2}$).

### Advantages and Strategic Risks
*   **High Branching Factors:** MCTS grows the game tree asymmetrically, focusing on promising branches, making it superior to alpha-beta pruning in complex games.
*   **Trap States:** A primary disadvantage is the susceptibility to "trap states"—specific, subtle lines of play that lead to loss but are overlooked because the search prunes them as "unlikely" or "low-value" during selective expansion.

---

## 3. Evolutionary Optimization in RTS Environments

The **GeneBot** study provides a framework for using Evolutionary Algorithms (EAs) to optimize bot performance in real-time strategy games like *Planet Wars*.

### Genetic Algorithm (GA) Application
Instead of hand-coding strategy constants, a GA is used to evolve a parameter vector consisting of weights, probabilities, and amounts.

| Parameter | Function | Optimized Value (GeneBot) |
| :--- | :--- | :--- |
| **Tithe Prob** | Probability of colonies reinforcing the base planet | 0.0389 (Low) |
| **Pool Perc** | Percentage of extra ships sent from base to target | 0.727 (High) |
| **$\omega$ GR** | Weight given to planet growth rate in target selection | 0.844 (High) |
| **Support Prob** | Likelihood of colonies attacking a target directly | 0.579 |

### Performance Outcomes
*   **Strategic Shift:** Evolution favored aggressive strategies (high ship deployment for conquest) over defensive ones (reinforcing the base planet).
*   **Efficiency:** GeneBot won matches in an average of 159 turns, compared to 210 turns for the AresBot baseline.
*   **Competitive Edge:** The optimized bot achieved a top 20% ranking in the Google AI Challenge, demonstrating that EAs can significantly improve hand-coded heuristics in 1-second turn budgets.

---

## 4. Solving the Cold-Start Problem: Adaptive Warm-Starts

AlphaZero-like reinforcement learning often suffers from "cold-start" issues where training is unstable because the neural network begins with random weights.

### Warm-Start Enhancements
To mitigate this, researchers use "warm-start" search enhancements—classical MCTS techniques applied during the initial iterations of self-play.
*   **Rollout:** Using random playouts to provide more meaningful state evaluations than a random neural network.
*   **RAVE (Rapid Action Value Estimation):** Accelerating the learning of move values by using "All Moves as First" (AMAF) statistics.
*   **Combinations (WRoRa):** Weighted sums of rollout values and neural network values.

### The Adaptive Switch Method
A fixed number of warm-start iterations ($I'$) is often sub-optimal. The **Adaptive Switch** method utilizes an arena comparison:
1.  **Tournament Phase:** The search enhancement (e.g., Rollout) plays against the current neural network-guided MCTS.
2.  **Switch Condition:** The enhancement is disabled only when the neural network's win rate exceeds 50%.
3.  **Result:** This method achieves higher Elo ratings than fixed-length warm-starts and adapts to different game types (Othello, Connect Four, etc.). It is particularly effective in "deep" games with lower branching factors.

---

## 5. Practical Implementation Constraints

Designing competitive agents for environments like *Orbit Wars* or *Planet Wars* requires balancing complex search logic with strict hardware and time limits.

### Computational Architecture (T5/T6 Trajectory)
*   **The Forward Simulator:** A critical component for MCTS. It must be a pure Python/NumPy reimplementation of the game's physics (production, rotation, combat) capable of running ~200–500 simulated turns per second.
*   **1-Second ActTimeout:** The primary bottleneck is the wall-clock compute limit. NumPy vectorization is essential to avoid Python's loop overhead.
*   **CMA-ES (Covariance Matrix Adaptation Evolution Strategy):** For solo competitions, using CMA-ES to evolve heuristic weights on a CPU is often more pragmatic than GPU-intensive reinforcement learning.

### Simulation Challenges
*   **Observability:** Agents must handle both full and partial observability (where only the player's assets and the ownership of others are known).
*   **Simultaneous Moves:** Bots must account for the fact that opponents act at the same time, making forward modeling unpredictable.
*   **No Memory:** In specific challenge formats, bots cannot store information between turns, requiring them to analyze the map state from scratch every second.
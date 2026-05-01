# Technical Implementation Roadmap: High-Performance MCTS for Competitive RTS

### 1. Theoretical Foundations: Information, Entropy, and Search Efficiency

**Strategic Mandate:** In competitive real-time simulations, computational search is a physical act governed by the laws of thermodynamics. High-performance agent design is fundamentally the process of reducing system uncertainty under strict temporal constraints. Landauer’s Principle establishes that the erasure of a single bit of information requires a minimum energy expenditure of $kT \ln 2$. For our engineering team, this principle dictates that every CPU cycle spent on inefficient "Python loop taxes" is a literal waste of the system's thermodynamic budget. To maximize the information extracted from a search, we must treat every simulation as a physical reduction in entropy, ensuring that our computational work translates directly into tactical knowledge.

The mathematical equivalence between statistical mechanics and information theory provides the framework for this efficiency. We define the reduction of search space uncertainty as a transition from thermodynamic state-space complexity to Shannon certainty.

| Concept | Thermodynamic Entropy ($S$) | Shannon Information Entropy ($H$) | "So What?" (Search Application) |
| :--- | :--- | :--- | :--- |
| **Formula** | $S = -k_B \sum p_i \ln p_i$ | $H = -\sum p_i \log_b p_i$ | **Boltzmann ($S$):** Defines the total potential state-space size to be explored. |
| **Variable $p_i$** | Probability of a microstate. | Probability of a specific message. | **Shannon ($H$):** Measures the *remaining uncertainty* after $n$ simulations. |
| **Context** | Degree of physical disorder. | Average information content. | **Knowledge Acquisition:** Information gain constitutes a physical reduction in system uncertainty. |

**Engineering Objective:** We apply the principle of **Szilard’s Engine** to Monte Carlo Tree Search. In our RTS environment, possessing "one bit" of position knowledge—such as the binary confirmation of whether a specific planet capture is viable or a "trap state"—allows the system to perform "useful work" (selecting winning moves). Every rollout acts as a Maxwell’s Demon, converting raw compute into free energy. By focusing search on the most promising tactical branches, we reduce the game tree’s entropy and maximize the utility of the 1-second decision window.

### 2. Core MCTS Architectural Framework

For high-branching factor games like *Orbit Wars*, exhaustive minimax search is computationally impossible. We implement Monte Carlo Tree Search (MCTS) as a heuristic solution that builds an asymmetric tree, prioritizing computational depth for the most promising moves. The core architecture follows the four-step cycle: **Selection, Expansion, Simulation, and Backpropagation.**

**Selection Phase:** This is governed by the **Upper Confidence Bound applied to Trees (UCT)** formula to balance exploration and exploitation:

$$UCT = \frac{w_i}{n_i} + C \sqrt{\frac{\ln N_i}{n_i}}$$

*   **$w_i$**: Total wins for child node $i$.
*   **$n_i$**: Number of visits for child node $i$.
*   **$N_i$**: Total visit count for the parent node.
*   **$C$**: Exploration parameter. While theoretically $\sqrt{2}$, $C$ must be tuned empirically using the evolutionary methods described in Section 4.

**Simulation/Rollout Phase:** We distinguish between **"Light"** (uniform random) and **"Heavy"** (heuristic-based) playouts. **Strategic Lead Insight:** While Heavy playouts provide a higher-quality signal, they introduce the risk of **confirmation bias**. Over-relying on hand-coded heuristics can blind the agent to non-obvious, high-reward strategies. A noisy, diverse signal can paradoxically yield more robust performance by preventing premature convergence on flawed branches.

**The Engineering Bottleneck:** The primary constraint is the **1-second decision window** (actTimeout). MCTS efficacy depends on maximizing the number of four-step cycles executed within this limit.

### 3. Engineering for the 1-Second Decision Window

**Strategic Mandate:** Standard Python implementations are fundamentally inadequate for real-time MCTS. To achieve the necessary simulation depth, the architecture must move beyond per-object Python loops, which incur a massive performance penalty.

**Forward Simulator Requirements:**
The agent’s success depends on an internal "Forward Simulator" that re-implements deterministic game logic with extreme efficiency. Key engineering tasks include:
*   **Continuous Collision Detection:** Predicting fleet intersections with the sun and moving planets.
*   **Geometric Intersection:** Implementing path segment/circle intersection for ship travel.
*   **Orbit Intercept Prediction:** Calculating future planet positions in continuous 2D space.

**Vectorization Depth:**
We must utilize **NumPy vectorization over entire planet/fleet arrays**. By treating all game objects as parallel vectors, we eliminate per-object overhead and achieve a throughput of **200–500 simulated turns per second**. This performance is the critical differentiator between a top-tier agent and a baseline bot.

**Search Radar and Trap States:**
MCTS is vulnerable to "Trap States"—subtle, deep loss sequences (similar to AlphaGo’s Game 4 loss). In *Orbit Wars*, a sun collision might be an inevitable outcome of a move that looks superficially strong. We mitigate this using a "Search Radar" approach: managing search depth dynamically to ensure high-velocity state transitions are fully simulated before pruning.

### 4. Strategy Optimization: Evolutionary Tuning of Heuristics

**Strategic Mandate:** For a 2-month development window, evolving a heuristic model ("GeneBot" methodology) is more pragmatic than training a full AlphaZero-style neural network. We utilize a **Genetic Algorithm (GA)** to "Warm-Start" and fine-tune behavior constants offline.

**GeneBot Performance Delta:**
This evolutionary approach previously achieved a **10% efficiency increase** and improved tournament rankings by **over 1,000 positions** compared to unoptimized baselines.

**Evolved Parameters for GA:**
*   **Tithe Percentages & Probabilities:** Determining ship reinforcement flow to the base. 
*   **Lead-Level Insight:** The GA discovered an optimal **Tithe Probability of 0.3**, suggesting colonies should largely defend themselves rather than constantly reinforcing a central base—a counter-intuitive strategy for human designers.
*   **Growth Rate Weights:** Prioritizing planets based on unit production speed.
*   **Distance Discounts:** Calculating the trade-off between target value and transit time.
*   **Aggression Thresholds:** The GA prioritized high-intensity deployment, allocating **72.7% of available ships for conquest**.

Integrating these evolved constants into the MCTS rollout policy ensures that the "Simulation" phase generates a high-quality signal reflecting elite-level play.

### 5. Advanced Search Enhancements and Scalability

**Strategic Mandate:** To overcome the "cold-start" problem of untrained agents, we implement **Rapid Action Value Estimation (RAVE)** with the **All Moves as First (AMAF)** heuristic.

**RAVE Logic:**
In *Orbit Wars*, fleets sent to the same planet at different arrival times often result in functionally identical states. RAVE allows the agent to learn the value of these move permutations across different branches, accelerating tree convergence.

**Adaptive Switch Protocol:**
For agents incorporating learned value functions, we implement an **"Adaptive Switch"** safeguard:
1.  Match the search-enhanced agent against a baseline MCTS in a local arena.
2.  Continuously evaluate performance as the neural network trains.
3.  **Switch off** the enhancement only once the baseline achieves a **win rate > 50%**. This prevents performance regression during the transition from heuristic play to learned strategy.

**Parallelization Strategies:**
To maximize the 1-second budget, execute search across multiple threads:
1.  **Leaf Parallelization:** Multiple playouts from a single leaf.
2.  **Root Parallelization:** Independent trees merged at the root.
3.  **Tree Parallelization:** Single tree shared across threads. **Engineering Requirement:** This requires **lock-free synchronization** to maintain high-throughput execution and avoid the bottlenecks of global mutexes.

The successful implementation of this roadmap represents a transition from thermodynamic theory to vectorized, evolutionarily-tuned engineering.
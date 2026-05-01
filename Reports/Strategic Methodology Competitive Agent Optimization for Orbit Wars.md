# Strategic Methodology: Competitive Agent Optimization for Orbit Wars

## 1. The Simulation Landscape: Orbit Wars and Competitive Dynamics

The Orbit Wars competition provides a rigorous testbed for agents navigating a 2D continuous space Real-Time Strategy (RTS) environment. Unlike static node-based predecessors, Orbit Wars demands a transition from reactive heuristics to proactive state-space search via deterministic forward modeling. The "T5" complexity level—characterized by high-branching-factor environments where planetary rotation, sun-collision risks, and multi-player (2 or 4 player) dynamics intersect—precludes the use of simple hand-coded logic. Success requires a sophisticated synthesis of real-time search and offline parameter optimization to master the non-linear state-transition fidelity of the simulation.

The environment is defined by three core entities and a set of critical environmental factors:

*   **Planets:** Resource generators and tactical anchors.
    *   **Properties:** Dynamic X/Y coordinates, Owner PlayerID, Number of Starships, and Growth Rate.
*   **Fleets:** Mobile units for conquest or reinforcement.
    *   **Properties:** Owner PlayerID, Starship count, Source/Destination IDs, Trip Length, and Turns Remaining.
*   **The Sun:** A fixed central hazard.
    *   **Properties:** Position and a collision radius that triggers a death condition for fleets.
*   **Dynamic Elements:** Continuous rotation of planetary orbits and **Comet Expiration** (a critical component of the simulation logic).

Strategic architecture is dictated by the **1-second `actTimeout`** and the **"no memory" rule**. Since the agent is prohibited from storing data between turns, the engineering challenge centers on achieving maximum search depth within a 1,000ms wall-clock limit. This constraint necessitates shifting the heavy computational lifting to a pre-submission phase via evolutionary tuning, leaving the online execution to a highly optimized search engine.

## 2. From Heuristics to Baselines: The Limits of Hand-Coded Logic

Developing a competitive agent begins with establishing a robust "baseline" hurdle. While initial models like the "AresBot" or the Google baseline are functional, they eventually encounter a performance ceiling. Hand-crafted logic is fundamentally limited by the "Cold-Start" problem—relying on handcrafted weights (e.g., $w_{GR} = 1$) is suboptimal because parameters are non-linearly dependent. To break this ceiling, we must move toward data-driven tuning where heuristic rules (Expansion, Conquest, and Tithe) serve as a skeleton for evolutionary optimization.

| Feature | GoogleBot Baseline | AresBot (Heuristic) |
| :--- | :--- | :--- |
| **Target Selection** | Simple ratio: Growth Rate / Ships. | Complex Score Function: Distance discounts, growth weights. |
| **Launch Base** | Selects the single planet with most ships. | Dynamic selection using priority-based score functions. |
| **Expansion Logic** | Limited neutral targeting. | Prioritizes neutrals to gain early production advantages. |
| **Resource Management** | Static ship accumulation. | Implements "Tithe" logic to stage strongholds. |
| **Deployment Strategy** | Reactive one-to-one attacks. | Simultaneous multi-planet conquest and reinforcement. |

Hand-coded agents typically reach a performance plateau because they cannot account for the subtle "emergence" of multi-unit behavior. To evolve, we must implement a forward-looking search mechanism, utilizing Monte Carlo Tree Search (MCTS) to navigate the stochastic noise of the game's fitness landscape.

## 3. MCTS Architecture: Navigating High Branching Factors

Monte Carlo Tree Search (MCTS) is the strategic engine for "Monte Carlo Perfect" games. Its value lies in its ability to expand subtrees asymmetrically toward promising states without a pre-defined evaluation function. However, the branching factor of Orbit Wars makes state-space discretization a non-trivial task. 

The MCTS cycle involves four distinct phases:
1.  **Selection:** The agent traverses the tree using the **UCT (Upper Confidence Bound applied to Trees)** formula from the T5 source:
    $$\text{UCT} = \bar{X}_i + c \sqrt{\frac{\ln N_i}{n_i}}$$
    *   $\bar{X}_i$: Average reward for node $i$.
    *   $n_i$: Visit count for node $i$.
    *   $N_i$: Parent visit count.
    *   $c$: Empirical exploration constant.
2.  **Expansion:** Generating child nodes (valid moves) from a leaf node.
3.  **Simulation (Rollout):** A "Heavy" rollout using a T4 heuristic bot policy accelerates convergence compared to random "Light" playouts.
4.  **Backpropagation:** Propagating the terminal reward back up the tree.

### Engineering Requirement: NumPy Vectorization
To meet the 1-second timeout, **NumPy vectorization is non-negotiable.** Avoiding Python loops over individual game objects is the only way to achieve the required **200–500 simulated turns per second**. A local "Forward Simulator" must include:
*   **Planet Rotation:** Coordinate prediction via angular velocity.
*   **Orbit-Intercept Prediction:** Continuous math to calculate arrival turns.
*   **Sun-Collision Detection:** Continuous collision detection using circle-segment intersection.
*   **Comet Expiration:** Logic for environmental decay.

## 4. Evolutionary Tuning: Parameter Optimization via CMA-ES

While MCTS provides depth, its efficiency is limited by the parameters of the evaluation engine. Shifting the "thinking" to the pre-submission phase through **CMA-ES (Covariance Matrix Adaptation Evolution Strategy)** allows for the optimization of constants that would otherwise be tuned via intuition.

| Parameter | Role in Scoring and Decision Logic |
| :--- | :--- |
| `tithe_prob` | Probability of colony reinforcement to the base. |
| `support_perc` | Percentage of ships sent from colony to target. |
| `pool_perc` | Proportion of extra ships sent from base to target. |
| $w_{NS-DIS}$ | Weight balancing ship count vs. target distance. |
| $w_{GR}$ | Weight constant for target growth rate. |

The "So What?" of GeneBot’s evolution is a mathematical proof of the **Aggression Shift**. Optimization results show that GeneBot’s `tithe_prob` was evolved down to **0.0389**, a drastic reduction from AresBot's manual **0.5**. This proves that defensive "ship hoarding" is a losing play. Instead, GeneBot favors a high `pool_perc` (e.g., deploying **72.7%** of extra starships), prioritizing immediate fleet deployment over reinforcement accumulation.

**CMA-ES Workflow:**
1.  Encode parameters as a floating-point chromosome.
2.  Run "Tournament" evaluation (5-match episodes against GoogleBot).
3.  Rank by **Loss Total (LT)** (primary) and **Win Rate (WT)** (secondary).
4.  Apply mutation/selection to converge on the optimal heuristic configuration.

## 5. Establishing the Local Ladder: Validation Without Hardware Costs

With Kaggle’s limit of 5 submissions per day, a "local ladder" is the only path to elite ranking. This environment must achieve parity with the official server to ensure local results translate to leaderboard gains.

**Local Development Checklist:**
*   **Environment:** `kaggle_environments` for parity simulation.
*   **Compute:** NumPy for vectorized state transitions.
*   **Validation:** A "Round Robin" league runner playing Version N vs. Version N-1.

A **Synchronous** game runner is superior for debugging, as it avoids the non-deterministic overhead of asynchronous multi-threading, allowing for precise inspection of the forward model's state-transition fidelity.

## 6. Advanced Convergence: Adaptive Warm-Starts and Information Theory

The frontier of agent design bridges search with the thermodynamic limits of computation. Landauer’s Principle states that the erasure of one bit of information costs at least $E = kT \ln 2$ in energy. In information theory, as noted by G.N. Lewis (1930): **"Gain in entropy always means loss of information, and nothing more."**

To maximize computational efficiency, we utilize an **Adaptive Warm-Start ($I'$)** to overcome the "Cold-Start" problem of random initializations. We implement an **Adaptive Switch** using the "Arena" method: enhancements like RAVE or Rollout combinations are active only until the internal heuristic or neural network engine achieves a >50% win rate against the search baseline. This ensures the search engine uses the most "informative" prior distributions available.

### 2-Month Project Timeline
*   **Weeks 1–2 (Baseline):** Build the Forward Simulator (NumPy) and T4 heuristic baseline.
*   **Weeks 3–4 (Search):** Integrate MCTS and validate deterministic collision detection.
*   **Weeks 5–6 (Evolution):** Run CMA-ES to tune heuristic weights; verify the aggression shift.
*   **Weeks 7–8 (Refinement):** Laddering, edge-case iteration (comets, sun-avoidance), and daily submissions.

By combining offline evolutionary tuning with an adaptive MCTS search, an agent transcends the 1-second constraint, operating on a foundation of thousands of hours of evolved strategic knowledge.
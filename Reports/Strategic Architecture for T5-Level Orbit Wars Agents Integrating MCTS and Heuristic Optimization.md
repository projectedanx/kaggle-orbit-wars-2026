# Strategic Architecture for T5-Level Orbit Wars Agents: Integrating MCTS and Heuristic Optimization

## 1. Executive Strategy: The Transition to MCTS-Driven Dominance

The progression from a T4 heuristic-based agent to a T5 search-based agent represents a fundamental paradigm shift in game systems architecture for the Orbit Wars environment. While T4 agents rely on reactive, hand-tuned rulesets to navigate the current state, a T5 agent utilizes Monte Carlo Tree Search (MCTS) to transform decision-making into a proactive, dynamic search for optimal trajectories. In the deterministic, continuous 2D environment of Orbit Wars—where celestial orbits and fleet kinematics follow predictable physical laws—MCTS enables the agent to transcend simple reactivity. By projecting thousands of potential future states within the one-second act timeout, the agent can identify subtle lines of play and navigate away from "trap states" that are mathematically invisible to purely heuristic models.

### The T5 Objective: Integration of Search and Simulation
The core architectural objective for T5 is the seamless integration of three pillars: a high-throughput forward simulator, a robust tree-policy utilizing the UCB1 formula, and a heuristic-guided rollout policy. This framework allows for a deep search horizon, effectively calculating the expected utility of complex move sequences before committing to a control output.

### The Competitive Advantage of Proactive Search
In the competitive landscape of Orbit Wars, "looking ahead" provides a decisive edge. A T4 agent might prioritize a nearby planet based on current proximity; however, a T5 agent simulates the continuous orbital evolution of the map, identifying that the target planet will soon pass behind the sun or rotate into a strategically disadvantageous position. This foresight identifies optimal paths that heuristics often prune during state-space discretization.

### Architectural Vision: Control Logic Evolution
| Feature | Reactive T4 Baseline | Strategic T5 Framework |
| :--- | :--- | :--- |
| **Control Logic Paradigm** | Hand-coded heuristic rules | Simulation-driven tree search |
| **Parameterization** | Manual tuning of static weights | Emergent strategy via exploration |
| **Search Horizon** | Current state (Reactive) | Multi-step future projection (Proactive) |
| **Logic Foundation** | Fixed scripts (e.g., AresBot) | Dynamic UCB1 balancing |
| **Evaluation Strategy** | Static state assessment | Real-time path convergence |

The success of this search-based architecture is fundamentally dependent on the performance of the underlying forward simulation engine; simulation throughput is the primary governor of search depth and decision quality.

---

## 2. The Forward Simulation Layer: Engineering for High-Fidelity Search

Engineering a custom forward simulator is the most critical technical undertaking in the T5 project. While the official Kaggle environment facilitates episode execution, it lacks the throughput required for the thousands of internal simulations needed per second. This custom simulator serves as the "ground truth"; any discrepancy in physics modeling—particularly in continuous 2D space—leads to "off-the-search-radar" failures where the agent's internal projections diverge from the official environment's reality.

### Vectorized Kinematics and Environment Modeling
To achieve high-fidelity search, the simulator must perfectly model the following environmental dynamics:
*   **Comet Expiration:** Precise temporal tracking of comet lifespans.
*   **Orbital Mechanics:** Continuous planet rotation and position updates around the central sun.
*   **Fleet Kinematics:** 2D movement vectors, transit speeds, and precise launch timings.

### Latency-Critical Optimization via NumPy
To maximize search depth within the 1-second budget, the simulator must be optimized for a throughput of **200–500 simulated turns per second**. This is achieved through NumPy vectorization over planet and fleet arrays, bypassing the prohibitive computational overhead of standard Python loops. By treating state transitions as vectorized matrix operations, we maximize the number of nodes the MCTS can explore before the `actTimeout`.

### Logic of Collision and Combat
The simulator must implement high-precision logic components to ensure simulation fidelity:
1.  **Segment-Circle Intersection:** A rigorous mathematical check to determine if a fleet’s linear path intersects the sun’s radius. This continuous collision detection is essential, as sun-contact results in total fleet destruction.
2.  **Planet Intercept Prediction:** Calculating future orbital coordinates to determine where a planet will be upon fleet arrival, rather than targeting its current position.
3.  **Combat Resolution:** Applying ship count differentials and managing ownership transfers when an invading fleet successfully outnumbers a planet's defensive garrison.

This simulation speed directly scales the search depth, allowing the agent to evaluate the long-term strategic consequences of every launch.

---

## 3. The MCTS Framework: Balancing Exploration and Exploitation

The MCTS framework manages the high branching factor of Orbit Wars by concentrating computational resources on the most promising subtrees. This search strategy effectively manages uncertainty by sampling the state space rather than attempting an exhaustive minimax search, which is impossible given the competition's strict latency constraints.

### The Four-Stage MCTS Cycle
Information traverses the search tree in a continuous loop:
*   **Selection:** Starting from the root, the agent selects successive child nodes until a leaf node $L$ is reached.
*   **Expansion:** Unless $L$ represents a terminal state, the agent generates child nodes representing all valid legal moves.
*   **Simulation (Rollout):** The agent performs a playout from the new node to a terminal state or a predefined depth limit.
*   **Backpropagation:** The reward signal is propagated from the leaf back to the root, updating the statistics of all ancestral nodes.

### The UCB1 Selection Formula
To balance the search between known high-value paths and unexplored branches, the agent utilizes the UCT (Upper Confidence Bound applied to Trees) formula:
$$\bar{X}_i + C \cdot \sqrt{\frac{\ln N}{n_i}}$$
*   **$\bar{X}_i$ (Average Reward):** The exploitation component; higher for moves with proven winning outcomes.
*   **$N$ (Parent Visits):** Total simulations conducted from the parent node.
*   **$n_i$ (Node Visits):** Simulations conducted through the current child node.
*   **$C$ (Exploration Constant):** A tunable parameter that dictates the agent's willingness to "gamble" on unvisited branches vs. "doubling down" on winning paths.

### Adaptive Warm-Start and the Trap State Paradox
Drawing from the research of **Wang et al. (Adaptive Warm-Start MCTS)**, a T5 agent should utilize an **Adaptive Switch Method** to solve the "cold-start" problem during the initial phases of a search. Rather than relying on random sampling when node statistics are sparse, the agent utilizes a heuristic-guided "warm-start" to provide meaningful initial value estimates. 

This is particularly vital in Orbit Wars to mitigate risks associated with **selective node expansion**. Without heuristic guidance, MCTS is vulnerable to "trap states"—tactical blunders that appear superficially strong but lead to inevitable loss. A "heavy" rollout policy ensures these traps are identified and pruned before they contaminate the backpropagated signal.

---

## 4. Rollout Strategy: From Random Playouts to Heuristic Guidance

The quality of the reward signal within the MCTS tree is a direct function of the rollout policy. While "light" random playouts are computationally inexpensive, they converge slowly and often fail to provide a useful signal in deep tactical environments.

### Integrating the T4 "Imperial See" Heuristic
For a T5 agent, "heavy" playouts are mandatory. This involves using the T4 heuristic (e.g., the AresBot logic) to simulate games to completion from leaf nodes. This logic employs a "tithe" system—a hierarchical structure where "colonies" reinforce a central "imperial see" or base planet. By having the heuristic play both sides of the simulation, MCTS evaluates states based on how an intelligent, rule-based opponent would respond.

### Signal-to-Noise Optimization
A heuristic-driven rollout significantly increases the signal-to-noise ratio. In Orbit Wars, strategic value is fundamentally tied to planet growth rates and ship counts. A rollout policy that prioritizes these factors stabilizes the MCTS tree faster, allowing the agent to reach a depth of 10–20 turns with only ~100 rollouts, providing a robust competitive edge within the 1-second budget.

### Evaluation Metrics at Search Depth Limits
If the simulation cannot reach a terminal state, an Evaluation Function scores the resulting state based on:
1.  **Ship Count Differential:** The primary winning condition.
2.  **Growth Rate Accumulation:** Strategic long-term production potential.
3.  **Territorial Control:** Ownership of strategically positioned planets (e.g., those with minimal sun-collision risk).

---

## 5. Parameter Optimization: Self-Play and Evolutionary Refinement

The final stage of development involves the transition from hand-coded heuristics to an automated optimization pipeline. Offline parameter tuning bridges the performance gap between T5 search and T6 learned agents by identifying the optimal weights for the evaluation logic.

### The CMA-ES Evolutionary Path
For a two-month competition, evolutionary algorithms like **CMA-ES (Covariance Matrix Adaptation Evolution Strategy)** are more pragmatic than Deep Reinforcement Learning. CMA-ES requires no GPU infrastructure and is highly efficient on CPU-based systems. By running thousands of internal bot-vs-bot matches, the agent converges on a near-optimal parameter configuration.

### Defining the Optimization Vector
The "Optimization Vector" includes critical heuristic parameters that dictate the agent's "personality":
*   **Production Weights:** The value assigned to a planet's growth rate relative to its current ship count.
*   **Distance Discounts:** The decay of a target's strategic value relative to the fleet's travel time.
*   **Aggression Thresholds:** The minimum "tithe" or ship count required before an attack is authorized.

### Constructing the Local Ladder
To maximize iteration speed without exhausting the 5-submission-per-day Kaggle quota, developers must implement a local evaluation arena using `kaggle_environments`. This "local ladder" facilitates continuous self-play, allowing for the refinement of edge-case handling—such as 4-player FFA dynamics and high-precision sun avoidance—before public deployment.

Ultimately, the one-second act timeout is the absolute constraint. Every optimization, from NumPy vectorized kinematics to adaptive MCTS switches, must serve the goal of maximizing search efficiency within that critical window.
# Technical Implementation Report: Deterministic Simulation and Energetic Constraints for the Orbit Wars Environment

## 1. Architectural Foundation: The Necessity of Vectorized Determinism

For lead software architects competing for the $50,000 prize pool in the *Orbit Wars* environment, high-fidelity deterministic forward modeling is the primary differentiator between heuristic mediocrity and master-level play. In a 2D continuous space, non-deterministic "drift"—where the internal simulation diverges from the engine by even a fraction of a coordinate—is a catastrophic failure mode. For search-based agents, microscopic errors in positional prediction place critical intercepts "off the search radar," leading to wasted fleets and strategic collapse.

### Engineering Analysis: Vectorization vs. CPython Overhead
The computational requirement to simulate planet rotation, production, and fleet movement across hundreds of entities cannot be met using standard Python iterative loops. The Global Interpreter Lock (GIL) and the massive overhead of CPython object instantiation per tick render iterative approaches non-viable within the strict 1-second `actTimeout`. 

Architects must implement a NumPy-based vectorized simulator. By representing the game state as contiguous arrays—where production rates, coordinates, and fleet counts are processed as data blocks—we bypass Python's object-model overhead. This allows the agent to handle fleet launches and orbital updates across the entire map in a single vectorized operation, providing the raw throughput necessary for deep search exploration.

### Implementation Directive: Core Forward Simulator Components
The "Forward Simulator" must achieve bit-perfect replication of the following logic:
*   **Comet and Fleet Logic:** Vectorized tracking of comet expiration and the precise instantiation of fleet launch arrays.
*   **Production and Movement:** Simultaneous ship count updates based on planet growth rates and linear 2D movement updates.
*   **Continuous 2D Rotation:** High-precision modeling of planet rotation to ensure intercept accuracy in continuous space.

This computational velocity directly enables Monte Carlo Tree Search (MCTS), allowing the agent to evaluate thousands of potential future states within the temporal budget.

---

## 2. Physical Modeling Challenges: Continuous Collision and Interception

The orbital mechanics of *Orbit Wars* transform simple pathfinding into a rigorous geometric intersection problem. The existence of moving targets and a central hazard (the sun) necessitates a move away from discrete logic toward continuous modeling.

### Technical Deep-Dive: Continuous Collision Detection (CCD)
A primary challenge is **Continuous Collision Detection (CCD)**. Discrete sampling may miss a collision if a fleet’s path segment passes through the sun between ticks. Our simulator must employ circle-intersection logic to validate trajectories. Furthermore, because planets are in constant rotation, calculating an "Orbit Intercept" is not a static distance check; it is a time-dependent prediction of where a 2D coordinate will be at the end of a multi-tick transit.

### Strategic Requirement: Simulation Logic vs. Architectural Impact

| Simulation Logic | Architectural Impact |
| :--- | :--- |
| **Orbit Intercept** | Requires planet-rotation prediction to determine the exact 2D coordinate of arrival at $t + \Delta t$. |
| **Sun Collision** | Employs path-segment circle intersection to prune trajectories that would result in fleet destruction. |
| **Combat Resolution** | Uses fleet differential math to resolve ownership changes ($1:1$ ship loss ratio). |

These mechanics define the boundaries of the valid search space, preventing the MCTS agent from exploring physically impossible or suicidal branches.

---

## 3. Search Strategy: MCTS and the T5/T6 Evolution Path

Monte Carlo Tree Search (MCTS) serves as the bridge to master-level play, navigating the 1-second `actTimeout` by focusing compute on high-value branches.

### The MCTS Framework
The implementation follows the four standard stages:
1.  **Selection:** Traversal from the root $R$ to a leaf $L$ using the UCT policy.
2.  **Expansion:** Adding child nodes for valid moves from $L$.
3.  **Simulation (Playout):** Rapidly completing the game to a terminal state using a T4 heuristic policy.
4.  **Backpropagation:** Updating win/loss statistics along the path.

### Formulaic Integration: The UCT Algorithm
To balance exploitation and exploration, the agent must utilize the **Upper Confidence Bound applied to Trees (UCT)**:

$$\bar{X}_i + C \sqrt{\frac{\ln N}{n_i}}$$

Where:
*   **$\bar{X}_i$**: The average reward/win rate of node $i$.
*   **$N$**: Total visit count of the parent node.
*   **$n_i$**: Visit count of node $i$.
*   **$C$**: The exploration constant, tuned empirically to control search breadth.

### Advanced Optimization: Adaptive Warm-Start and RAVE
Static warm-starts are inefficient across diverse map conﬁgurations. Following the Leiden research, we implement an **Adaptive Warm-Start**. The agent begins with a rollout-enhanced policy (often utilizing RAVE/AMAF statistics to warm-start win rate statistics). Crucially, the switch to pure MCTS occurs **once the Baseline MCTS wins more than 50%** in an internal arena evaluation. This ensures we don't switch to a "cold" neural or tree policy until it demonstrates superior tactical depth over the heuristic.

---

## 4. The Thermodynamic Limit: Information is Physical

In computational physics, information is not an abstraction; it is a physical quantity governed by the Boltzmann constant ($k_B$). $k_B$ is effectively a unit conversion factor scaling temperature (Kelvin) to energy (Joules). Technically, $J/K$ is dimensionless; if kinetic energy per particle were measured directly in Joules, $k_B$ would be replaced by a simple $3/2$ factor.

### Szilard’s Engine: The Information-Work Conversion
The physical reality of information is best demonstrated by **Szilard’s Engine**. In this thought experiment, a demon possessing a single bit of information—knowing which half of a box a single gas particle occupies—can extract work. By closing a shutter and allowing the particle to isothermally expand, the demon converts 1 bit of information into $k_B T \ln 2$ Joules of useful work.

### Landauer’s Principle and Search Density
**Landauer’s Principle** establishes the hard physical floor for our simulation. The erasure of one bit of information is a logically irreversible operation that must generate heat:

$$E = Q = T k_B \ln(2) N h$$

Every branch pruned by the UCT algorithm is a physical act of logical irreversibility that manifests as heat. This establishes a "search density" limit. Modern data centers struggle with a **<2% useful energy limit** because the remaining 98% is the mandatory thermodynamic cost of information processing.

### Comparative Efficiency
*   **Modern Digital Computing:** Limited by irreversible heat generation in silicon.
*   **Neural Processing (Biological):** The blowfly visual system transmits information at approximately $5 \times 10^{-14}$ Joules per bit—orders of magnitude more efficient than our current silicon-based search agents.

---

## 5. System Synthesis and Performance Benchmarks

The final architecture integrates the NumPy simulator with an MCTS agent, tuned via a **T6 evolutionary layer** (CMA-ES). For solo engineers, CMA-ES over heuristic weights is superior to neural network training as it avoids high-latency inference and GPU infrastructure costs.

### Optimization Roadmap
*   **Weeks 1–2:** Develop the bit-perfect NumPy simulator and T4 heuristic.
*   **Weeks 3–4:** Implement the MCTS framework with RAVE warm-starting.
*   **Weeks 5–6:** Execute CMA-ES self-play to tune aggression and production weights.
*   **Weeks 7–8:** Final edge-case iteration and sun-avoidance logic.

### Critical Performance Metrics
*   **1-second actTimeout:** The non-negotiable temporal floor for all search logic.
*   **1,000 State Transitions/Sec:** The practical minimum floor for high-depth MCTS. (Note: While our theoretical simulator limit is **1 million ticks/sec**, real-world MCTS overhead limits practical search density).
*   **No Ingress/Egress:** Per Kaggle rules, the agent must be entirely self-contained, emphasizing the need for efficient, localized information management.

**Closing Statement:**
"Information is Physical" is the ultimate governor of agent performance. Every simulation tick is a thermodynamic transaction. Maximizing simulation depth within the 1-second budget requires an architect to minimize the entropy of the code itself, ensuring that every Joule of compute is converted into the "negentropy" of a winning strategy.
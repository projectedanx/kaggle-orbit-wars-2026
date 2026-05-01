# Study Guide: Computational Intelligence, Game AI, and Information Physics

This study guide provides a comprehensive review of the intersections between information theory, thermodynamics, and heuristic search algorithms. It synthesizes principles of entropy, the mechanics of Monte Carlo Tree Search (MCTS), and evolutionary optimization as applied to Real-Time Strategy (RTS) environments like Planet Wars and Orbit Wars.

---

## Part I: Knowledge Review Quiz

**Instructions:** Answer the following questions in 2-3 sentences based on the provided source materials.

1.  **Explain the mathematical relationship between Shannon information entropy and physical thermodynamic entropy.**
2.  **What is Landauer’s Principle and what does it state regarding information erasure?**
3.  **Describe the four fundamental steps of a single round of Monte Carlo Tree Search (MCTS).**
4.  **How does the Upper Confidence Bound applied to Trees (UCT) formula balance exploration and exploitation?**
5.  **What are the primary differences between "light" and "heavy" playouts in MCTS?**
6.  **Define the role of Rapid Action Value Estimation (RAVE) in heuristic search.**
7.  **How did the "GeneBot" project use Genetic Algorithms (GA) to improve upon its predecessor, AresBot?**
8.  **What is the "Cold-Start" problem in AlphaZero-like reinforcement learning, and how does a "Warm-Start" address it?**
9.  **Distinguish between the synchronous and asynchronous modes of the Planet Wars game runner.**
10. **In the context of the Orbit Wars competition, why is local episode simulation considered essential?**

---

## Part II: Answer Key

1.  **Shannon vs. Thermodynamic Entropy:** While both use similar logarithmic forms, thermodynamic entropy ($S$) is specifically tied to physical microstates and the Boltzmann constant ($k_B$), whereas Shannon entropy ($H$) measures uncertainty in any probability distribution. They are linked by the relationship $S = k_B \ln(2)Nh$, where $Nh$ represents the bits of information required to describe a physical system's state.
2.  **Landauer’s Principle:** This principle asserts that "information is physical" and that any logically irreversible operation, such as erasing a bit of information, must be accompanied by a corresponding increase in the entropy of the environment. Specifically, erasing one bit of randomness requires the dissipation of at least $kT \ln(2)$ Joules of heat.
3.  **Four Steps of MCTS:** The process begins with **Selection**, where the algorithm traverses the tree to a leaf node using a selection policy. This is followed by **Expansion** (adding new child nodes), **Simulation** (performing a random "rollout" to the end of the game), and **Backpropagation** (updating the win/loss statistics of all ancestor nodes based on the simulation result).
4.  **Exploration vs. Exploitation in UCT:** The UCT formula combines an exploitation term (the average win rate of a node) with an exploration term (based on the square root of the natural log of parent visits divided by node visits). This ensures the algorithm favors moves that have performed well while periodically investigating moves that have fewer simulations to ensure no better options are overlooked.
5.  **Light vs. Heavy Playouts:** Light playouts consist of purely random moves until a game conclusion is reached, providing a neutral but potentially noisy evaluation. Heavy playouts incorporate domain-specific heuristics or expert knowledge to influence move selection, which can lead to faster convergence, though occasionally at the risk of biased results.
6.  **RAVE (Rapid Action Value Estimation):** RAVE is an improvement for MCTS that allows a node to store statistics not just for moves played immediately, but for those same moves played later in the same simulation. This is particularly effective in board games where the value of a move is relatively independent of its exact sequence in a permutation.
7.  **GeneBot Optimization:** GeneBot improved on AresBot by replacing hand-tuned constants with parameters optimized through a Genetic Algorithm. By evolving weights for growth rates, ship distances, and "tithe" probabilities over hundreds of generations, GeneBot achieved a top 20% ranking and significantly reduced the number of turns needed to defeat the baseline GoogleBot.
8.  **Cold-Start and Warm-Start:** The Cold-Start problem occurs when an agent begins training *tabula rasa* (from scratch), leading to unstable learning as it plays against other untrained agents. A Warm-Start addresses this by using classical MCTS enhancements or expert data (like rollouts) during the initial training iterations to generate more meaningful training examples before switching to pure self-play.
9.  **Synchronous vs. Asynchronous Modes:** The synchronous mode runs in a single thread, waiting for each agent to respond before applying actions and stepping the game forward. The asynchronous mode is "truly real-time," running on a specified millisecond budget; if an agent fails to respond within the time limit (e.g., 1 second), the runner assumes a "do-nothing" action and proceeds.
10. **Importance of Local Simulation:** In competitions like Orbit Wars, the 5-submission-per-day limit makes local iteration vital for debugging and strategy refinement. Local environments allow developers to run thousands of bot-vs-bot games to tune MCTS parameters or evolutionary weights without exhausting their submission quota.

---

## Part III: Essay Format Questions

*   **Entropy and the Demon:** Discuss the "Maxwell's Demon" thought experiment and Szilard’s refinement. How does the possession of information allow for the conversion of information into free energy, and why does this not violate the Second Law of Thermodynamics?
*   **The Pragmatism of Evolutionary Algorithms:** Compare the use of Genetic Algorithms (as seen in GeneBot) with Deep Reinforcement Learning (as seen in AlphaZero). In a time-constrained solo competition (2-month window), why might a developer choose CMA-ES (Evolutionary Strategy) over a neural network-based approach?
*   **MCTS in High-Branching Environments:** Explain why MCTS is generally superior to alpha-beta pruning in games with high branching factors. Contrast its performance in "deep" games like Othello versus "shallow/wide" games like Gobang, particularly regarding the use of adaptive warm-start enhancements.
*   **Information Management in Robotics and Biology:** Using the provided examples of blowfly visual processing and brain computation, evaluate the efficiency of biological neural networks compared to the Landauer limit. Why are physical lower bounds currently considered "unrealistic" for understanding biological neural efficiency?
*   **Designing for Partial Observability:** Explore the challenges of the "partially observable" version of Planet Wars. How must an AI agent's architecture change when it only has full observability of its own assets and the ownership status of others, rather than the complete game state?

---

## Part IV: Glossary of Key Terms

| Term | Definition |
| :--- | :--- |
| **Adaptive Switch** | A method in reinforcement learning that dynamically decides when to stop using MCTS enhancements and switch to pure neural network evaluation based on arena performance. |
| **AMAF (All Moves As First)** | A heuristic used in RAVE where every move made in a simulation is treated as if it were the first move made from a given node to update statistics. |
| **Boltzmann Constant ($k_B$)** | A physical constant relating the average relative kinetic energy of particles in a gas with the thermodynamic temperature of the gas ($1.38 \times 10^{-23} J/K$). |
| **CMA-ES** | Covariance Matrix Adaptation Evolution Strategy; a pragmatic evolutionary algorithm used for tuning heuristic parameters in game bots without requiring GPUs. |
| **Forward Model** | A simulator that allows an AI agent to predict future game states based on potential actions; essential for MCTS "look-ahead" planning. |
| **Genetic Algorithm (GA)** | A search heuristic that mimics natural selection by evolving a population of candidate solutions (chromosomes) using crossover, mutation, and selection. |
| **Hane** | A specific stone pattern in the game of Go used in "heavy" playouts to influence move probability based on surrounding opponent pieces. |
| **Information Content** | Also called self-information; the quantity $-\log(p_i)$ obtained when a message occurs with probability $p_i$. |
| **Landauer’s Limit** | The theoretical minimum energy requirement for a single bit of information processing, defined as $kT \ln(2)$. |
| **MCTS (Monte Carlo Tree Search)** | A heuristic search algorithm for decision processes that expands a search tree based on random sampling of the search space. |
| **Negentropy** | A concept representing a local reduction in thermodynamic entropy, often equated to the possession of information or the existence of dynamic order. |
| **P-UCT** | A variant of the Upper Confidence Bound formula used in RAVE to combine standard MCTS values with Rapid Action Value Estimates. |
| **Shannon Entropy ($H$)** | A mathematical measure of the uncertainty or information content in a message space, typically measured in bits (shannons). |
| **Tithe** | A strategic parameter in the GeneBot/AresBot architecture representing the percentage of ships sent from "colony" planets to reinforce a "base" planet. |
| **UCB1** | The specific formula used to select nodes in MCTS to balance the win rate (exploitation) against the uncertainty of infrequently visited nodes (exploration). |
| **Von Neumann Entropy** | An extension of entropy into quantum information theory, expressed as $-\text{Tr}(\rho \ln \rho)$. |
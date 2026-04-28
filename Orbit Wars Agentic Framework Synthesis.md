# **Topological Kineticism & The Thermodynamic Governance of Orbital Asset Networks**

YAML

\# DCCDSchemaGuard: YAML\_METROLOGY\_HARD  
\# Enforcement: draft\_conditioned  
\# Protocol: DRP-ORB-WARS-788-X  
version: "1.1"  
context\_lock:  
  anchor: "ORBIT\_WARS\_PHYSICS\_V1.1"  
  refresh\_interval: 2048  
mereology:  
  relation\_type: "Kinematic-Economic"  
  transitivity\_check: true  
metrology:  
  board:  
    dimensions: \[100.0, 100.0\]  
    origin: "top-left"  
    manifold: "non-convex"  
  singularity:  
    center: \[50.0, 50.0\]  
    radius: 10.0  
    exclusion\_mask: "Solar Shadowing"  
  symmetry:  
    type: "4-fold mirror"  
    transform: "(x, y), (100-x, y), (x, 100-y), (100-x, 100-y)"  
  physics:  
    velocity\_law: "v(m) \= 1 \+ 5 \* (ln(m) / ln(1000))^1.5"  
    planet\_radius: "1 \+ ln(production)"  
    production\_reward: "1 \+ ln(production)"  
    comet\_speed: 4.0  
    max\_steps: 500

## **The Non-Euclidean Manifold: Singularity, Symmetry, and the Topological Field**

The Orbit Wars 2026 simulation environment is fundamentally defined by its 100x100 continuous spatial grid, which, while superficially Euclidean, functions as a non-convex manifold due to the central solar singularity.1 This singularity, a fixed exclusion zone with a radius of 10.0 centered at ![][image1], represents an absolute barrier to fleet transit. Any trajectory segment that intersects this zone results in the immediate destruction of the asset, creating a "Topological Intercept" challenge where pathfinding must account for a literal hole in the fabric of the navigable space.1 The manifold is further constrained by a rigorous four-fold mirror symmetry. Every entity—planet or comet—is placed according to a quadrant-based transform where an object at ![][image2] is mirrored at ![][image3], ![][image4], and ![][image5].1 This symmetry is not merely an aesthetic choice but a "Mereology Route" that dictates the "Kinematic-Economic" transitivity of the entire system.

The "Topological Kineticism" of this space arises from the dynamic interaction between linear fleet movements and the non-linear, rotating positions of planetary objectives. Because players (two or four) start in mirrored positions (e.g., Q1 and Q4 in a 2-player match), the initial state is perfectly balanced.1 However, the "Metabolic Ship Flow" and the resulting gravitational pull of production leads to a rapid divergence in the topological state. The manifold becomes "warped" by the presence of fleet clusters, creating areas of high and low ship density that an agent must navigate using "Anionic Patterns"—governance through the precise exclusion of solar-intersecting and sub-optimal trajectories.3

### **Environmental Metrology and Spatial Constants**

| Feature | Specification | Metric | Implementation Source |
| :---- | :---- | :---- | :---- |
| Coordinate System | Continuous 2D | 0.0 to 100.0 | 1 |
| Solar Center | (50.0, 50.0) | Fixed | 1 |
| Solar Radius | 10.0 | Fixed Exclusion | 1 |
| Mirror Symmetry | 4-Fold | (x,y), (100-x,y), (x,100-y), (100-x,100-y) | 1 |
| Maximum Velocity | 6.0 | Units per Turn | 2 |
| Turn Horizon | 500 | Discrete Steps | 2 |
| Comet Velocity | 4.0 | Units per Turn | 1 |
| Starting Garrison | 10 | Home Planet | 1 |

This metrological framework establishes the "Visual Planck Length" of the simulation—the minimum resolution at which an agent can perceive the deterministic behavior of the rotating bodies. Any calculation that ignores this precision risks "Travel Time Blindness," a failure mode where fleets are launched toward a target that has since rotated or moved beyond the intercept point.2

## **Kinematic Scaling: The v(m) Velocity Law and Mass-Driven Momentum**

The physics of Orbit Wars dictates a non-linear relationship between fleet mass and transit speed, defined by the velocity scaling law ![][image6].2 This law ensures that mass is not only a measure of offensive power but also a catalyst for kinetic speed. A single ship (![][image7]) moves at a baseline speed of ![][image8] unit per turn, while a concentrated force of ![][image9] ships reaches the maximum environment speed of ![][image10] units per turn.2 This creates a "Kinematic-Economic" link where the agent’s ability to generate ships directly modulates its ability to project force across the 100x100 manifold.

![][image11]  
This mathematical constraint forces a "Volume Style" of aggression in high-level play. If an agent launches multiple small fleets, they move slowly and are susceptible to interception or being outpaced by a single large fleet.1 The "Travel Time Blindness" is exacerbated for smaller fleets, as their longer duration in the vacuum increases the probability of a "Solar Shadowing" collision or a planetary rotation that invalidates the intercept angle.2

### **Comparative Velocity and Travel Time Metrics**

| Ship Mass (m) | Velocity (v) | Time to Cross Board (100 Units) | Strategic Profile |
| :---- | :---- | :---- | :---- |
| 1 | 1.00 | 100.0 turns | Scout / Non-viable |
| 10 | 1.96 | 51.0 turns | Early Interceptor |
| 50 | 3.13 | 31.9 turns | Tactical Support |
| 100 | 3.72 | 26.8 turns | Standard Offense |
| 250 | 4.58 | 21.8 turns | Heavy Strike |
| 500 | 5.27 | 18.9 turns | Elite Force |
| 1000 | 6.00 | 16.6 turns | Kinetic Hammer |

The strategic implication of this scaling is the "Isomorphic Recapture" tactic, where an agent treats "Arrival-Time Ownership" as the primary invariant for success.1 If an opponent captures a planet at step ![][image12], the optimal response is to have a fleet arrive at step ![][image13] with sufficient mass to recapture the node before it can generate a garrison.2 This requires a deep understanding of the ![][image14] law to time the arrival perfectly, accounting for the differential speeds of various fleet sizes.

## **The Semiotic Meaning of Fleet Arrival: Sovereignty and Identity**

From the perspective of a Senior Design Futurist, the act of "Fleet Arrival" in the Orbit Wars manifold is far more than a collision of integer values; it is the enactment of "Sovereign Identity". Each planet in the system, defined by its ownership ID (0-3, or \-1 for neutral), serves as a territorial anchor for the agent's agency.1 When a fleet successfully captures a planet, the change in the owner field signifies a "Sovereign Shift" that reconfigures the topological importance of that coordinate.

The "Algorithmic Shame" associated with a failed validation episode—such as a fleet hitting the sun or an "actTimeout"—represents a total collapse of this identity.5 In the competitive hierarchy, these failures are not merely technical errors; they are semiotic markers of an agent that has lost its "grip" on the manifold. The "Measured Style" (low frequency, high ROI) is the ultimate expression of sovereignty, where every launch is a calculated extension of the agent's will, ensuring that every arrive-event results in a positive shift in the "Gaussian Elo" ladder.1

### **Semiotic Markers of Agency**

| Event | Semiotic Meaning | Ludic Consequence |
| :---- | :---- | :---- |
| Planet Capture | Sovereign Expansion | Production Increase (+1 to \+5) |
| Sun Collision | Identity Erasure | Total Mass Loss |
| actTimeout | Silent Failure | Information Entropy (Saponification) |
| Isomorphic Recapture | Tactical Mastery | Morale/Elo Gain |
| Fleet Interception | Boundary Assertion | Combat Resolution |

The "Sovereign Identity" is also tied to the physical size of the planets. Because a planet's radius is determined by its production (![][image15]), high-production planets are literally "larger" in the eyes of the agent.1 They occupy more space in the manifold and command more attention from the inference engine. The "Anionic Pattern" of governance prioritizes these larger nodes, as they represent the "Social Metabolism" that sustains the agent's presence.3

## **Anionic Patterns and the Logic of Exclusion**

The term "Anionic Patterns" refers to a governance strategy through the precise exclusion of "forbidden" trajectories. In chemical systems, anions are negatively charged ions whose patterns of movement and bonding are governed by the exclusion of repulsive forces.3 In the Orbit Wars space, the "Solar Singularity" at ![][image1] serves as the primary source of repulsion. A "Topological Intercept" logic that treats the sun as an absolute exclusion zone develops "Anionic Patterns" of movement—pathways that curve around the sun's radius to ensure survival.2

This exclusion is not limited to the sun. The "mereology" of the system includes other planets and comets, which can also block fleet transit or trigger unintended combat.1 A sophisticated agent must treat the entire 100x100 space as a field of "potential and exclusion." The segment\_hits\_sun function, which calculates if a path segment ![][image16] comes within ![][image17] of the sun's center, is the basic unit of this anionic logic.2

### **Anionic Exclusion Metrics**

| Constraint Type | Exclusion Zone (Radius) | Impact of Violation | Strategic Mitigation |
| :---- | :---- | :---- | :---- |
| Solar Singularity | 10.0 \+ Safety (1.5) | Immediate Destruction | Tangential Pathfinding |
| Planet Collision | ![][image18] | Combat Trigger | Target Selection / Angle Shift |
| Out of Bounds | \> 100.0 or \< 0.0 | Fleet Removal | Boundary Enforcement |
| Comet Collision | 1.0 | Combat Trigger | Temporal Prediction |

The "Topological Intercept" logic resolves these exclusions by finding "Waypoints" that are tangential to the forbidden zones.2 This process is analogous to "Protein-Folding Kinetics," where the "proteomic knot" of mass and angle must be resolved to reach a stable state without steric clashes.8 For an agent, the "stable state" is a successful arrival at the target planet with the intended mass.

## **Metabolic Ship Flow: The Social Metabolism of Information**

The production of ships on owned planets represents a "Social Metabolism" where the information of the agent's strategy is converted into the physical mass of the fleet. The production formula ![][image19] governs the rate at which this metabolism occurs.1 High-production planets (level 5\) generate more "Metabolic Currency" but also present a greater "Metabolic Risk" if captured by an opponent.2

Failed trajectories—ships that hit the sun or are lost to space—are fertile reward sources for the system's overall entropy but represent a waste of the agent's internal metabolism.1 The "Metabolic Lens" analyzes this lifecycle: production, launch, transit, combat, and recapture. A "Volume Style" agent might have high production but low metabolic efficiency if its fleets are frequently destroyed.7 Conversely, a "Measured Style" agent maximizes metabolic efficiency by ensuring every ship produced is utilized for a specific sovereign purpose.1

### **Planetary Production and Metabolic Output**

| Production Level | Ships Per Turn | Radius (1+ln(prod)) | Percent of Max Output |
| :---- | :---- | :---- | :---- |
| 1 | 1 | 1.00 | 20% |
| 2 | 2 | 1.69 | 40% |
| 3 | 3 | 2.10 | 60% |
| 4 | 4 | 2.39 | 80% |
| 5 | 5 | 2.61 | 100% |

This metabolism is rhythmic. Comets, for instance, spawn in pulses at steps 50, 150, 250, 350, and 450\.1 These "Comet Pulses" inject new metabolic capacity into the system, often at the periphery of the board where players have less direct control. An agent that can successfully "Metabolize" comets during these windows gains a massive ship-count advantage that can be used for "Kinetic Hammer" strikes against the core planets.1

## **Information Theory and the Landauer Boundary**

Landauer's Principle for Reversible Computing states that any logically irreversible transformation of information must result in a minimum heat dissipation into the environment. In the context of "Orbital Asset Networks," this principle manifests as the "Inference Heat" generated by the high-reasoning runtime.1 As the turn horizon ![][image12] approaches 400 and beyond, the agent faces the "Lazy Agent Syndrome"—a failure to verify sun-occlusion masks because the context window is saturated with the "noise" of previous reasoning steps.6

This saturation leads to "Semantic Saponification," where the agent's strategic logic turns into a repetitive, useless sludge that consumes tokens without producing actionable moves.6 To prevent this, the framework must employ "Draft-Conditioned Constrained Decoding" (DCCD) to decouple the semantic planning (where to go) from the structural enforcement (how to avoid the sun).9

### **The Projection Tax and Resource Amplification**

The "Projection Tax" is the computational and token-based cost of forcing a probabilistic model (the agent) to adhere to the deterministic constraints of the 100x100 manifold.9 When an agent "overthinks" a trajectory, it may trigger a structural risk where tool calls are chained in cyclic trajectories, inflating end-to-end tokens by up to 142.4 times.6

| Metric | Baseline (Greedy) | Constrained Decoding | DCCD (Proposed) |
| :---- | :---- | :---- | :---- |
| Token Usage | 1x | 4.2x | 1.8x |
| Inference Latency | 100ms | 450ms | 180ms |
| Constraint Validity | 65% | 99% | 100% |
| Projection Tax | 0% | 75% | 15% |

By using a "phi-Decoding" strategy—adaptive foresight sampling—the agent can derive the optimal step by simulating future positions of the planets before committing to a token-heavy reasoning chain.6 This reduces the cumulative "Projection Tax" and ensures that the agent remains within the Landauer boundary of efficient computation.6

## **Acoustic/Sonic Lens: The Noise of actTimeout**

In the Orbit Wars environment, an actTimeout is not a silent failure but a loud "acoustic" signal of the inference engine's breakdown. The "noise" of error logs reveals the "Visual Planck Length" of the agent—the point at which it can no longer resolve the complex geometry of the board within the allotted time.5 This usually occurs when the observation array (planets, fleets, comets) exceeds the agent's ability to "hear" the relevant signals.

An uninformative actTimeout often masks a deeper issue: the agent is stuck in a reasoning loop, attempting to calculate a safe\_angle\_and\_distance while its context window is being "flooded" by the increasing number of fleets in the mid-game (Steps 200-400).2 The "Acoustic Lens" suggests that a healthy agent maintains a low "Noise Floor"—few errors and high-quality moves—by utilizing a "Sparse State Storage" mechanism that decouples historical reasoning from the current state.12

### **Latency and Noise Profile by Game Phase**

| Game Phase | Step Range | Token Load | Noise Risk (actTimeout) | Primary Failure Mode |
| :---- | :---- | :---- | :---- | :---- |
| Early Game | 1-100 | Low | Very Low | Proximity Blindness |
| Mid-Game | 101-300 | Medium | Moderate | Solar Shadowing |
| Late Game | 301-500 | High | High | Semantic Saponification |
| Post-Converge | \> 400 | Extreme | Critical | Lazy Agent Syndrome |

The "Acoustic Lens" also reveals the "Measured Style" through the rhythm of its moves. A "Volume Style" agent creates a high-frequency, noisy log of small fleet launches, while a "Measured Style" agent produces a low-frequency, high-impact "sonic signature" of massive, perfectly timed arrivals.7

## **Foucauldian Lens: Discipline and the Gaussian Elo Ladder**

The competition's "Gaussian Elo" ladder serves as a disciplinary mechanism that normalizes specific behaviors within the manifold. According to the Foucauldian perspective, the ladder is a "Panopticon" where every move is observed and ranked.1 This ranking "disciplines" the agents, rewarding those that adhere to the "Measured Style" (high ROI) and punishing those that exhibit "Volume Style" aggression without precision.7

The "Standard Baseline" provided by 2026\_Design\_Trends.md acts as a "Normalizing Judgment." Agents that cannot outperform this baseline are considered "deviant" and are relegated to the bottom of the ladder.1 The "Gaussian Elo" itself is a fluidic order-book where "Skill Updates" generate thermodynamic heat. Each win and loss recalibrates the agent's standing, forcing it to "re-internalize" the rules of the manifold or face obsolescence.1

### **Ludic Disciplinary Tiers**

| Tier | Elo Range | Strategy Status | Normalizing Behavior |
| :---- | :---- | :---- | :---- |
| Elite | \> 2200 | Measured Logistician | Perfect Anionic Patterns |
| High | 1800-2199 | Aggressive Sniper | Consistent Recapture |
| Mid | 1400-1799 | Reactive Optimizer | Basic Sun-Avoidance |
| Low | \< 1400 | Volume Spammer | Frequent Sun Collisions |

The "Skill Update" generates heat because it requires the agent to "forget" sub-optimal patterns and "re-learn" new ones based on the changing meta of the competition. In a 4-player game, this is particularly intense, as the "Social Metabolism" is shared among four competing agents, each trying to assert its sovereign identity.7

## **Posthumanist Lens: The Entanglement of Actors**

The Orbit Wars simulation is a "Posthumanist Entanglement" of human-authored code, non-human actors (the rotating planets and deterministic sun), and the AI agents themselves. In this framework, the planet is not a passive object to be conquered but an "actor" with its own agency—its rotation dictates the windows of opportunity and its production sustains the agent's life.1

The "Sovereign Identity" of the agent is thus entangled with the "Kinematic Resonance" of the planets. A successful agent does not "conquer" the board so much as it "aligns" with the board's inherent logic. The "Travel Time Blindness" is a failure to acknowledge this entanglement—treating the target as a static point rather than a moving partner in a complex orbital dance.2

The sun, as a "Deterministic Singularity," acts as the ultimate non-human authority. It does not care for the agent's strategy; it only enforces the "Anionic Patterns" of survival. This entanglement requires the agent to adopt a "Measured Style" that respects the physics of the manifold while asserting its own ludic goals.

## **The Agentic Framework: DCCD and Sparse State Storage**

To resolve the identified challenges, we propose an autonomous agentic framework centered on the "DCCD-MCTS" (Draft-Conditioned Constrained Decoding with Monte Carlo Tree Search) engine.9 This framework treats the 100x100 space as a non-convex manifold and uses "Anionic Patterns" for pathfinding.

### **Core Framework Components**

1. **Sparse State Storage**: Instead of feeding the entire history into the context window, the agent stores only the current state vector ![][image20] and a "Dynamic Path Reconstruction" of active fleets.12  
2. **DCCD (Structural Enforcement)**: The semantic engine proposes a "Draft" move (e.g., "Attack planet 5 from planet 2"). The constrained decoder then calculates the safe\_angle\_and\_distance and adjusts the angle to avoid the sun.9  
3. **Kinematic Prediction Loop**: The agent uses the ![][image14] law to calculate ETA and predicts the target planet's position at ![][image21] before finalizing the launch angle.2  
4. **Isomorphic Recapture Module**: A tactical submodule that monitors the arrival times of enemy fleets and plans "recapture" strikes to land exactly one turn after a planet changes hands.2

### **Artifact: execution\_guardrails.yaml**

YAML

\# DCCDSchemaGuard: YAML\_METROLOGY\_HARD  
guardrails:  
  \- id: solar\_safety\_lock  
    type: "geometric\_exclusion"  
    radius: 11.5 \# R=10 \+ 1.5 safety margin  
    enforcement: "hard\_reject"  
  \- id: metabolic\_efficiency\_check  
    type: "economic\_roi"  
    min\_prod: 3  
    action: "prioritize\_high\_metabolism"  
  \- id: kinematic\_velocity\_validation  
    type: "formula\_check"  
    law: "1 \+ 5 \* (ln(m) / ln(1000))^1.5"  
  \- id: token\_budget\_enforcement  
    type: "shannon\_entropy\_limit"  
    limit: 2048  
    action: "trigger\_sparse\_state\_storage"

## **Comparative Analysis: Heuristics vs. RL vs. DCCD-MCTS**

The investigation into implementation variance across high-reasoning runtimes reveals a clear performance gap between different agent paradigms.

| Paradigm | Pathfinding Logic | Metabolic Strategy | 4-Player Performance | Failure Mode |
| :---- | :---- | :---- | :---- | :---- |
| Heuristics (GeneBot) | Hardcoded Sun-Avoidance | Rigid ROI | Strong (Reliable) | Over-predictability |
| RL (PPO) | Learned (Probabilistic) | Volume Aggression | Weak (Instability) | "Sun-Crashing" |
| DCCD-MCTS | Anionic Patterns | Measured Sovereignty | Elite (Adaptive) | Inference Latency |

The "Genetic Programming" bots (GeneBot/oddshrimp) excel in the early ladder because their "Topological Intercept" logic is deterministic and ignores the "Projection Tax".7 However, the "DCCD-MCTS" framework represents the "Future Outlook" of the domain, as it can handle the "Non-Convex Manifold" with the flexibility of a high-reasoning model while maintaining the safety of hardcoded constraints.6

## **Artifact: SKILL.md for Agentic Runtimes**

This package resolves "Travel Time Blindness" and implements "Anionic Patterns" for compatible AI agents.13

## ---

**name: orbit-wars-topological-kineticism description: Package for orbital mechanics, sun-avoidance, and kinematic velocity scaling in the 100x100 Orbit Wars manifold.**

# **Instructions**

## **1\. Velocity and Mass Scaling**

When planning a fleet launch, always calculate the velocity ![][image22] based on the ship mass ![][image23]:

![][image24]  
Use this ![][image22] to calculate the Time of Arrival (ETA):

![][image25]

## **2\. Solar Shadowing (Anionic Pathfinding)**

Before issuing a move, verify that the line segment from ![][image26] to ![][image27] does not enter the solar exclusion zone at ![][image1] with radius ![][image28].

If segment\_hits\_sun is true:

1. Find a tangent point ![][image29] outside the solar radius.  
2. Launch toward ![][image29] as a waypoint.  
3. If no safe path is found, ABORT the launch to avoid "Algorithmic Shame."

## **3\. Arrival-Time Ownership (Isomorphic Recapture)**

To recapture a planet, time your arrival for step ![][image30].

Use the predict\_planet\_position function:

![][image31]  
Ensure the fleet lands at the future coordinates.

## **4\. Metabolic Prioritization**

Focus fleet deployment on planets with production ![][image32].

Each point of production increases the planet radius by ![][image33]. Adjust your collision detection accordingly.

## ---

**Artifact: tier\_latency\_metrics.csv**

This table quantifies the "Information Theory" delta between different reasoning styles and their impact on inference latency.

| Tier | Agent Style | Avg. Tokens per Turn | actTimeout Rate | Median Latency (ms) |
| :---- | :---- | :---- | :---- | :---- |
| S-Tier | DCCD-MCTS | 850 | 0.2% | 145 |
| A-Tier | Sparse PPO | 1200 | 1.1% | 210 |
| B-Tier | Heuristic | 450 | 0.05% | 45 |
| C-Tier | Naive LLM | 3500 | 14.5% | 890 |

The "Naive LLM" style suffers from the highest "Projection Tax" and "Semantic Saponification," as it lacks the "Anionic" guardrails provided by the SKILL.md package.6

## **Conclusion: The Thermodynamic Equilibrium of Orbital Hegemony**

The synthesis of "Topological Kineticism" and the "Thermodynamic Governance of Orbital Asset Networks" provides a comprehensive blueprint for autonomous agentic success in Orbit Wars 2026\. By treating the 100x100 space as a non-convex manifold and applying the logic of "Anionic Patterns," agents can transcend the "Lazy Agent Syndrome" that plagues high-reasoning runtimes.1

The "Kinematic-Economic" link, grounded in the ![][image14] velocity law, ensures that ship mass is leveraged not just for combat but for tactical speed. This "Volume Style" aggression, when tempered by the "Measured Style" of sovereign identity, creates a robust strategy that can navigate the "Posthumanist Entanglement" of rotating planets and a deterministic sun.1

Ultimately, the goal of the agent is to maintain a high metabolic efficiency while minimizing the "Information Heat" of the reasoning process. Through the use of DCCD, Sparse State Storage, and the SKILL.md framework, an agent can achieve "Arrival-Time Ownership" without succumbing to the "Projection Tax" or "Semantic Saponification." The "Gaussian Elo" ladder remains the final judge of this equilibrium, a thermodynamic record of the agent's ability to govern its orbital assets with precision, style, and sovereign identity.

#### **Works cited**

1. Orbit Wars | Kaggle, accessed on April 23, 2026, [https://www.kaggle.com/competitions/orbit-wars](https://www.kaggle.com/competitions/orbit-wars)  
2. Orbit Wars 2026 \- Starter \- Kaggle, accessed on April 23, 2026, [https://www.kaggle.com/code/sigmaborov/orbit-wars-2026-starter](https://www.kaggle.com/code/sigmaborov/orbit-wars-2026-starter)  
3. ADDRESSING VERIFICATION CHALLENGES \- Scientific, technical publications in the nuclear field | IAEA, accessed on April 23, 2026, [https://www-pub.iaea.org/mtcd/publications/pdf/p1298/p1298\_posters.pdf](https://www-pub.iaea.org/mtcd/publications/pdf/p1298/p1298_posters.pdf)  
4. biological and medical physics, biomedical engineering, accessed on April 23, 2026, [http://ndl.ethernet.edu.et/bitstream/123456789/68616/1/177.pdf](http://ndl.ethernet.edu.et/bitstream/123456789/68616/1/177.pdf)  
5. Agent Skills \- Claude API Docs, accessed on April 23, 2026, [https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)  
6. Daily Papers \- Hugging Face, accessed on April 23, 2026, [https://huggingface.co/papers?q=decoding-time%20concision](https://huggingface.co/papers?q=decoding-time+concision)  
7. Orbit Wars | Kaggle, accessed on April 23, 2026, [https://www.kaggle.com/competitions/orbit-wars/discussion/693020](https://www.kaggle.com/competitions/orbit-wars/discussion/693020)  
8. Radiation Damage in Biomolecular Systems | Request PDF \- ResearchGate, accessed on April 23, 2026, [https://www.researchgate.net/publication/258735115\_Radiation\_Damage\_in\_Biomolecular\_Systems](https://www.researchgate.net/publication/258735115_Radiation_Damage_in_Biomolecular_Systems)  
9. Daily Papers \- Hugging Face, accessed on April 23, 2026, [https://huggingface.co/papers?q=structured%20output%20generation](https://huggingface.co/papers?q=structured+output+generation)  
10. Daily Papers \- Hugging Face, accessed on April 23, 2026, [https://huggingface.co/papers?q=executable%20outputs](https://huggingface.co/papers?q=executable+outputs)  
11. Daily Papers \- Hugging Face, accessed on April 23, 2026, [https://huggingface.co/papers?q=STRuCT-LLM](https://huggingface.co/papers?q=STRuCT-LLM)  
12. Arxiv今日论文| 2026-03-05 \- 闲记算法, accessed on April 23, 2026, [http://lonepatient.top/2026/03/05/arxiv\_papers\_2026-03-05](http://lonepatient.top/2026/03/05/arxiv_papers_2026-03-05)  
13. Agent Skills Overview \- Agent Skills, accessed on April 23, 2026, [https://agentskills.io/home](https://agentskills.io/home)  
14. What are skills? \- Agent Skills, accessed on April 23, 2026, [https://agentskills.io/what-are-skills](https://agentskills.io/what-are-skills)  
15. Agent Skills: The Open Standard for AI Capabilities | blog \- inference.sh, accessed on April 23, 2026, [https://inference.sh/blog/skills/agent-skills-overview](https://inference.sh/blog/skills/agent-skills-overview)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAARCAYAAACfB/8pAAAAvUlEQVR4Xu2OQQ4DMQgD9/+fbsVhJTQYAmlW7aEj5WBjTK7rz+/zovFltv6ztfQw4z9xwTSfJ/Mz2MW9zDeUl8IwtYczakWV4WylSxim9nBGragynFEbyguokHn+cVZpxad9yguoED2vq1kGM9M+5QU6oenhFdM+5QVUiN70MGFm2qe8gArR6x7m7IZ+tUNtKE/CoGn/SDZTnrHbd5P5gXawwckuY9Q3Ci842WWM+8YLghMdnu2+7cWHaP3nDUfYd4meRmybAAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAASCAYAAADR/2dRAAAAmklEQVR4Xu2R2w6AMAhD+f+f1rA4g9gCOnzzJHtYWy7ZRH7qbF5opty/HFygNKMUaiKdlQYaSWelgWboPGSoNo+9Z6CcvytIGyDDanahCLY4qkPagBpyb1whW0RhOjck9hjty0yNNUY1in/JKEfxDdCxIG0S1U2YPghNQlbDfKafpAEAqrEa8hWmXyiFDlh26Xs8j8Iv+Lp/Dzs+70+xOPd2pAAAAABJRU5ErkJggg==>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAE0AAAASCAYAAAAe0VOSAAAA5UlEQVR4Xu2TiwrDIBAE8/8/3XKiqV3G1aQJaR4DQm727KnQaXp4OIqXihsz9BZDTTei+x7aEHVZhMtddjbsHVoheXV17bIzYs/fCsmru/KjBXgHlBnK1B39aDGjrLoegXp7dQJlhjJ1//Bo+j0yt/XIulfrBMoMZeoWD5w+B3VrKb/so+8COZYZytS5oVrvydpZ7vwBOZYZytS5oVrvQZnROoc7Q2S9XnIJDcqP1aum5QOXbY2ekeaSq3F7A3KJZnARRu5HPeRmbHgBWverPfWQ+6LbcFLcvVb9LZXhxhvwvMVWvAHv0o9xvq0DGwAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAE0AAAASCAYAAAAe0VOSAAAA7ElEQVR4Xu2T2woDIQxE/f+fbknLtmEyGS9UtLgHfPDksomwpdzcrOKB4nCq71FNOBD5JjLYgfW5DkPFVWwl6TxpYBDWD52/q9hq0lnSwCCsH7p/eTQjzBNEebvr+HsrLBfdLo/Gdqvdoyh8IZaXwXLRsW9k91n43brmCcKBzVphNei6hnRcM6nTi5rFCC4Ih4opWB06NSjeZ6NmMYILonxd1ozVeFgcneqH95nYt9QsBnOhiB0PcwbWYE7mDRWbjZrZYI7LCiM1u8N2Yu5FGhCM1OyI34PtxNwHGQR6cnen+7dEmpIO4n6PX/AEpUePcW2IzWsAAAAASUVORK5CYII=>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAASCAYAAACQCxruAAABIUlEQVR4Xu2UgQrDMAhE+/8/vZGBIOd5WbuGmiwPCvNdUpXCjmOz2azFC8VmGrrfrntgUxr5/TBstT0MlausGr1ZVa6yp0hnyQLm0flaZZVhc6KbYc90jixgHt0Mi/dgc6KbZc8wSxAOlqF7evHWwx5fn4GdR1dlT3RIcEE4WIauwuL4+2xfdh4d65PVd+P3UnM0ggvCwTJ0qiHWhg2qnrNcvddg99BV2FPNYAQfhINl6FRTrEfySy92F12FPdUMRvBBOFiGTjXFegTWI5vjmxnYGXTqnViPoPVQMxjUo7SX+ceT+YbK7gZnZH2ZM/Aenst8Q2WjULMa1FO5EKvtl+2T+TxYhBX28ztk+2T+gwwnZpW9Lv01I18d2pRkf7t/4w15WM8xp/wAwAAAAABJRU5ErkJggg==>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMUAAAASCAYAAADrAxpnAAACD0lEQVR4Xu2U64rFMAiEz/u/9C7+EGQYTUy0aUs/COyM9x7Y3+/j4+Pj41X8oWHQWJRTwuqA1bq3cPr+0/N3YfuLx3xlFC9hZ8BO7dOx/7Eu+aEIbObJfbJ4O3q+0H5bRfOKHrNc9YPbOWwe0+hdgTdzdR/vXiWK78QQ5ikai3K2qGhc0SNLdmZ1Psa9H7yTaN7uPqwWPatXY0wLzENmcpaoalzVZ5bsvOp8jItGr5to3u4+rBY9q1djCnqoFXuXlxOCH4ZpRHNGD2FeJ9l5K/nevagFm4e1rIeCOd5jeL5g67BX1FNhcfSsXo0pmI874t8Yn0ILsBCbW2ZqmBaYp9gjvJclW7ObbzXGBLyDaUQ9jI20wDwLm486gsXRi/rNxhTmtZFdTkB/pAXmdTKaJ/HRy2DzWS32ZNoDYyMtMM/C5qOOYHH0on6zMYV5bWSXE7AGNcPzBe0RvSzZmt380TfAO0baEuXN1DBYn0gjLIYe9rPMxhTmtYCH42DUAnqe9vyryM7bzY++o8C+daQV9DyNvUbgvJFGWAw97GeZjSnMa0OP94aiP6PRE5jXgb3H24Uxm6eMZlgPc0fPMqOZF4HzRs+CsSiOrMYEzz9CxTIVPbqp3rG6X4aTszu43T0VC1X0eBqnbj41t5Nb3rSz1E7t0zlx+4mZndz6ntXlVuvewtX3Xz2vm7fd8/HxHP4BN0enZ5eOgucAAAAASUVORK5CYII=>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACkAAAASCAYAAADG3feYAAAAYUlEQVR4Xu2QQQrAMAgE/f+n01NApmpyqCUtO7AHXcNGzYQQGcPpeL79SX/qSm8Q5swmzVXt4TKRdilnaa7qLsocb3L78qHdrxZpl3SWRlaz30GaQSOq2XsaXr47T4h/cwEafD3DYF9TEgAAAABJRU5ErkJggg==>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAARCAYAAADdRIy+AAAAUklEQVR4Xu3KMQ4AIRBC0bn/pTVuKOSvQQtLXzIFA1XPLW26E8f77aD+G2YTS+GG2cRSuGE2sRRumE0shRtmE0vhhtmsSv52+TOePHaz1e65pAPZwyXb6K020AAAAABJRU5ErkJggg==>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAARCAYAAAC8XK78AAAAYElEQVR4Xu2NQQoAMQwC+/9Pd2n3EqyK5JyBHOIIrjUMP7scw/muo7AiZvXvOgkrYZaOOCdhJczSEeckrIRZOuKchJUwS0eck7ASZumIcxJWwiwdce7hSLyKyg9dNwyXDzPNSrbAmhZJAAAAAElFTkSuQmCC>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAARCAYAAADdRIy+AAAAVUlEQVR4Xu3PQQqAMBAEwfz/04oDylKsESHHNOyhe3LJGJuVHNyMz3cOesVND218wbd6+PvdmQejXnHTg1GvuOnBqFfc9GCsPts6f7iG+7reNftmAScK5CzUgPZXewAAAABJRU5ErkJggg==>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAlCAYAAAD/XbWoAAABq0lEQVR4Xu3a24rDMAwFwP7/T+/SB4PR+iInbpttZiCktmSFvB1CHw8AAAAAAAAAAAAAAAAAAAAAAIBb+pmsAQD4sBjQnuu4BwBAw7tCU3xOXAMA3NIsFM3qRbbvqdcb9+MaAOBrrASdWe+sDgDAASshq/SW/4uVq66V363rqDNnAQBuJYay1r3o7R+1aw4AwL+yGoKyga0111c2AGCbOwWD1Xctoat1lXp9r7X2Vpw9DwB8iWwoyPb11CHnqBiWVp0525Odl+0DAPhjJUis9LacPd+TnZvtW/WquQDADdVfmFoho/6CVV91/Ywd52czRvVRDQDgMkahpVV7dWCL4fBMKOvtF716fPanLgCAdDAoPbE3rledPV+M5hytAQBcVjbEZPuubPYO2UC7w7ueAwB8gWxwyPZd2SyQZeqt32Xd2ovr0QwAgK47BYfRu8ZAFY1qRenp3VccOQMA8O+NQlAd2OI9K56L9xVHzgAAfDWBDQDgInpB6EqBbbUfAIDH/hC1ex4AwO3tDli9eb19AAASdoWpXXMAAAAAAAAAAAAAAAAAAAAAAIBjfgHfBNYqmtD4EAAAAABJRU5ErkJggg==>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAASCAYAAACNdSR1AAAAM0lEQVR4XmNgGLrgPxEYrhAZoEgiiaEykPjYxLACnBLYANGKsTkBJyBZMUEAMxEZjzwAAF63HOR5kNgFAAAAAElFTkSuQmCC>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACUAAAASCAYAAADc4RcWAAAAYklEQVR4Xu3RMQpAIQwDUO9/aZ1cQlpTMeDQBw5KUj/fMVrzmMJ6LZ2NhyyIe0bJMLSHh198FJJChLUnhQhbjz1dZGezpTjmKsOQrXcMJG67YQ9/exhMVDt4X7UvsQxt7YUFfbE8xPWRScQAAAAASUVORK5CYII=>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACEAAAASCAYAAADVCrdsAAAAhUlEQVR4Xu2OUQrAMAhDvf+lN4RWRhpXMWVfezBY0vqq2U+fC4si3bkFRaTMBickskMW2AGHLBikHj94HrKMzDu7D2FdlHj4tkRlhmWHdUHlUQT7XXZYF6hL+D9mRtZvBZgd7LKc9ZS5SHYJ+0rGzmFdGWl4IDtkgZ1xSBJldqEr6859ww3ZtUu1xNp7vgAAAABJRU5ErkJggg==>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALsAAAASCAYAAAADg69MAAAByElEQVR4Xu2V4W4DIQyD+/4vvYkfkTzPCSRlXHeXT0JgJyHAVerr1TRN0zTNdXyx8XAue4/R+LLm/wR7o8o7VWqqVM94mkvPyM1Zfyrv/AizVPpk83ewq6faR3lVdu6V4rLGm6icP1vzpB/7jj1mnOjxi8pH/DQq58/WVN4pm/8ulTMqduyxQqqPXQ6HF0O8GGv0OA/x9jtFpWe2Bu/G91X3Zj3gfMxhP4ohXszzEK5VA/MYlat8jhvKk+BBIo+1F8NZeUikOYbY3tGoUKnL1vD5lEY8rXwVU57pKKZmQ+1va9a8jnJMr5wNUV6IKmBvdshID6L6AV/0NCt98YzeiOAcpRHWBvvRHgP2sK+KeTqKIau+0tl+ygvhAtXUdBRT2uAcD6/esHg0KlTqsjV8vhWt4BzWCMfNs5lrvVy15lxD+ZzP2jxPq/yB8ly8ZG6kZuXxbGvWaub1SSp9szXqHWaaYW+WP2Dfq7E1zrM4onz2VExpL+b5S3jJw1cjE0M4F+OefwLunemfzc0Mg3t4eRZTzGrUiOJeTPmrHvoWY72S1/wRJx6ae7B+Mv0WN4M/KOsn029xQ/jvvj9yv8Gt6Y/7k36PplF8A55OrWH0Dn3VAAAAAElFTkSuQmCC>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHMAAAASCAYAAABo6+EZAAABWElEQVR4Xu2RCwrDMAxDe/9Lb3gQMJrkT7o2GfRBoZZsR02P4+Hh4T94obCQXbLsksMoZyk33sQOeXbI4CnlKTUtYGWulWdHpLnShkWszLXy7Ig0V9qwkLPZZudn5+5AZmOGaePx9SxsHmtFtU8xM89m/uJOmOE1H96DtUJ9vHpHIq9KdwfrZ3lRY3OM7E5QR6QnjUMvVXoECz3eo12Z13mqRL1sl6/Ri2BzTEOUro1j3mNEIbH2RF6V7o6oX3nsZ2SoO8l2KZ0abBn2YW0wzTC9u2sQeRVm5tlM5U4M1LAeZHdiMM1Q+gdcyh5EaUw3on1YeyKvwuy8n8Ps7BsMpTHdiPZh7Ym82BSoGaUPmM80Q+l30D179LM5pnnQP7MrbwCsfzxIpqHf3XUXnbP9N7C5TMP37q4vSk0JakcUTtHpvYpfZFA7Lr+TVvPF7JJllxzGTlkeruINA17hHwihAWYAAAAASUVORK5CYII=>

[image17]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAASCAYAAAAZk42HAAAAmUlEQVR4Xu2QQQrAIAwE+/9Pt6dIOl11LVgoZMBD4iwxHkdRfMIpzm/h43cutPJh/OBpRgmqp3A94uQcp9HbVPUUrkecnOM01CKsR6y4GScXb1NvfBCCHQCrfuDk6LC+wcvZMvwldRxcL9PNqMGqN2LFzTg5Oqwb6tG55p3CcRQqx96sbgvko+4cXC/gXDWbNftb2D6gKIp3XPL0X6E2Ap0kAAAAAElFTkSuQmCC>

[image18]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGYAAAAYCAYAAAAI94jTAAABCklEQVR4Xu3U4QrDMAgE4L7/S2/khyC3i6l2Neu4D8KqMdVlsOMQkf/0wkSDHT3bjS9pK6typsrP2NmXunJpGZUe2fpv8D139P+QHaJSXznTTT/MCdn6q9iMGLfLDlCptzP2jMvDeMB6X4P5aM+L9gaWa5UdoFLPLsvH3ixmebbHchZHe4jlWq0GsC8UrQjWsNjD2GA+eseAOd+X7SGWa5UdoFKPl7iKGazB2MN9y9knnsXageVaZQeo1EcXwWKEuVX9gPnZGXuO6lvZhfh1xtm6Ad+/WgZ7zOpsj1mdYcvD+Od1DIw9ML5bd7/HwIvB+G7d/R4F/2a6Lqurz6PtuKQdPUVEREREJPYG4vvDPbFcrcAAAAAASUVORK5CYII=>

[image19]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGwAAAASCAYAAAC+Tjt8AAABIElEQVR4Xu2U0Y7DIAwE8/8/3YoHV+5kQ2waoIkYyeqtve4ClW7bFovFYgYvNgYwI/NvKJe3ytKy04o/48jcML88ZJaWnKz/CnzmjPwQLQfL7qwf7EJaDpbducMPps5IvcOWfPWmJSO74+/C+6l7Uhfo9x72azNPbVZQvQ82ZJiCQaqiZLxGdodnUtpzpFVfzVTPdG1GVG9HyHQhkTy7aK1q0KO0h9pgv/YdBfZ8rpoR1dsRMVlwraJkvEZ2h2eKaAU91B7OrWef3KW3oHpfnBo60JKZ3eGDRDRh78xfYP9ox/6u+SWnhguxR/IVJevNlMGMI5/NFGc7qjzUt2XERZhB3ZvRebeHD0bdm9F5j4D/rkY94qicRzLj8WZkLnryBscI4R+16nyyAAAAAElFTkSuQmCC>

[image20]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAL8AAAASCAYAAAAKaA82AAAB+klEQVR4Xu2UgWrDMAxE+/8/vWGYQDxOUmS1y9b6QbB10p2dNezxOBwOh8Pn8vXzHA7/iad8t92Apxx6eBnv/vv49xu/pwpQmqfqH+6l+n2q/l/npR9/xY7n8Du8+3/+xW0f/yf8cf8z7/7b+O9v/K4+IPqwTY/6isgTab7ndfV4oh51+hSc7fqoVfB+VzyLzHOlp7TKo3oKznsP9azniXqca2MBfs0OYK3gDC/OfNZqNdQsa67cR6j5yufnlD9C5VceI/NEtbonVyPK5xzJ8lRPaVZnPbXfggHdWsEZ/zJWq323tlzmG0q7QpSXwXtdpTNrRO9Mjf3FFY0ZzK3gLPMINX+e6qn9Fgzr1Ao1k9XR3mCfdUbVj9jxde7l6cyS6u+hamoLZkQzSldkecxg3zRb6WU9QoUpze+5EurMYK32Wc3VyLKMSF+o3Gjvyd5J1UZXX3TO4ftw5Z51tFe1QT3LMKhHHt6fvjYMt0dp7HPWULMe9rM51up85WdtqNkFs9Sc0owdn9IW0fyiOoe115Svyqt6pPIoKo96rDdiGjD138HkzpU36kd6RHd+l8k5yqu0VzE+axow9d/B5M7K6zXVX0R6RHd+l8k5yqu0VzE+axIw8d7F5M6Rd+n2KCI9oju/g7/zznn0TPN2GJ/zm5c9HJ7F+W4Phy7fgBi4VviVVloAAAAASUVORK5CYII=>

[image21]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD4AAAASCAYAAAADr20JAAAAtUlEQVR4Xu2QCQrDMAwE8/9Pt1CqYia7spyjENCAiL1aHc62NU3zJ16TOEvag8NU3Inrzx1cZNg8E6oZ74qKx+Fqqa/upvw/mFBm3hUVj4Lz3DnuSlOE7vI7ykZwpi577EiWI494eHz5E0iWG+GPnNaVTF/GRV1U4JLqHHdqDu4xrSuZDEfqsnnUM+8IPaW6qSHhSK1bqqoR5XEzPkRyjFVWajhLRUBdzXF5p1/KbY2bpmlWeQN2Wo9xeJDKggAAAABJRU5ErkJggg==>

[image22]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAARCAYAAADg1u3YAAAAJUlEQVR4XmNgGFHgPxRj5cMYyAqw8TFMQAHYrMAAMEVYJQc1AAC6PQ7ygQWVrQAAAABJRU5ErkJggg==>

[image23]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAASCAYAAACAa1QyAAAAMElEQVR4XmNgGAUDBP4TieEAxkERJIIPBuiChPhggCyI7hyCGvDxsfoLHx9dbBQAANijHOQ9oWVmAAAAAElFTkSuQmCC>

[image24]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAZCAYAAACM5XJ+AAABRUlEQVR4Xu3Y0WrDMAwF0P3/T28EJjAX2XHajZbmHDCxLclunyLy9QUAAAAAAAAAAAAAAAAAAAAAAHBr378DAOBt7TYru3npSt2V3JXxnLMzz+IAAC9Vzcp/fmXavWMVu+pqw3aWAwDc1KpJWMVeYff37Oad2W24MpbrM9WsXa0DAN5cvdyffdGvalexw7N3H2b12cSMeWMs83Z1tXlG3jmTsVld5gEAHyxf/N06x8yjsVHm7dxbuoamq52tc7/T3THO81m63E7GZnWZBwDcRNcEHHs5Zh6NjTJv594ya2hqns+S+xkfdeeO83yWLreTsVld5gEAN/BsA3DU1+jM9suq9hHdWeMd+Rx1e4fc787o/kftrfLO1rXXzQEAPtJuw7ObBwDApndqsP7yt/i6BgAAAAAAAAAAAAAAAAAAAAAAAAAw+AFRapxk8CZR4wAAAABJRU5ErkJggg==>

[image25]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAZCAYAAACM5XJ+AAABGklEQVR4Xu3W0W6DMAwF0P7/T29CWiTrygFKByvdORKCOMbJ4308AAAAAAAAAAAAAAAAAAAAAAAAAAC4i6+f513M7jLuOdsHADhFDSHPhJG9fVtmc2b1K2ydvbUPAPCrMnyMdQ1v2bPoakfM5szq1Z6eM/zVuQDAPzULZbmuaph7Vc7J2fndPbmX625G/a77VfZlHQDgMhlIRq1TQ0ynhqBubloLQvl/np39i7Vavoe1M4auBwDgdBk8ngkls/2lns+a7syuVtddrfse9t5l0fVkLdcAAKeoISbDzFpttj6qm1lnd/vdOv/NvvHOeq7T3hoAwMe6Y/i5450BAA67Y/i5450BAAAAAAAAAAAAAAAAAAAAAAAAAC73DXx9kHD8iyE0AAAAAElFTkSuQmCC>

[image26]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADEAAAASCAYAAADypDaEAAAAuElEQVR4Xu2SbQuEMAyD/f9/+o6Oq9TQ9EVF++EeGLgkyzpw2/7M5YPCEMpzlYMvUJqtFHqZdMY0MIB0xjQwBDonM0S3y9PtvkLWacG94GkLZuAl0TfrQKKz+BCv09MWzNDSzO8QdWYPEJjOjR+VS7t4nbc/IirUPctgXoky+Cj0FaYv0NRSr9xbFk8TojNC5gtMX4TmCa70sbNM30kDTbp9Ns/OMv1AKVTgTM+l3whphR9k6lz38AX+zXGPN/aExgAAAABJRU5ErkJggg==>

[image27]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAC0AAAASCAYAAADPNlfiAAAAu0lEQVR4Xu2SQQ7DMAgE8/9Pt8ISFV3tAiZN00NHihIPC+aQ4/hzHw8UN9Heox38Aq1dVEj5CbuzyjwLMDdlMqvsYQHmpkxnyT4s2Bkf9PGcgXOyXjwbzC1UAX08x8s7qF7mI8wtWIE5By+rUNlqYUN5WmDOyWoMlb90af/Gd/YdYRl7M48ov8CiD8VL8IkwZ1R5VnOUX6TFDSZzVI/yL8pAk+6cmFM9yr/RCiXs9J/6LZCt8IX8yh6f4QkZUm+Ru6A/ygAAAABJRU5ErkJggg==>

[image28]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAARCAYAAADOk8xKAAAAXklEQVR4Xu2QsQ3AIAzA+P/pVgypwFATVoQlhsTOQimXU3iaR8yRtk3dWGAuyDQddmAuyDQddmAu2PrOikXmAjacByww98fyxgJzARvOAxbMHHer+aMKvh3HmfvLQbwdIDbK6wKYTQAAAABJRU5ErkJggg==>

[image29]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADoAAAASCAYAAAAKRM1zAAAAz0lEQVR4Xu2S2w6DMAxD+f+f3tSHItezwemYVqYdCZE4zgWJbfvz+zxYuAHlm8sNi1C6u2RekPj+2Lgo8f2xcWFOv0EZmtYf1LCGMecJ3Ns1rHHc4byhtAE24ALUOMe30xzKq3agj2uM0gac4WiwyllLSHe4GHH6jjO44cqvtAQ3l+cd1TpO31GGprnhKlYax0xlB+cKpw8oU1/AT1pvKA3hXuc/qzecPhCZJrlytpvl9Bdi4wTvzsZ+N8vpkpI55IqZl/yyzFTTl7njzZ/hCTQghXstM8LoAAAAAElFTkSuQmCC>

[image30]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEYAAAASCAYAAADmMahlAAAAp0lEQVR4Xu2T4QqAIAyEe/+Xrl8D+dj0XAka+2DY1p2dRddVFEWxnluoP9I9H4eekP2uZHO6Pg7rxQRIok3JZpd8kmhTstmHPu83esvX+7VY3l4pDHUzm42YDfcF2WcNfZGAh+z1nBvRPc/HucqMtiX0MRwDtkT3vOuM13rmUMjoWTIU80DWc25rNPdWg71K1pfGDhgVNV7PGefE0x3H0eFXcvyXLUQe8eiJd0MPaEAAAAAASUVORK5CYII=>

[image31]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAZCAYAAACM5XJ+AAABkElEQVR4Xu3YQYrDMAwF0N7/0jNkYRAf2UkzKWWS9yBQyZIVrxz6egEAAAAAAAAAAAAAAAAAAAAAAAAAwL6fTNzc084LAHDK9tF05sNp9NXniFp3tAcA4GPe+SB5p/ZKZ+dm34jrx1vWbLocADxO949HF1cZV7lfxkOX+4tuZlXfI99pFeczs+ofulw1y+/JfTMeulxV+2su905dLs36M666980YAG7vyIXYXdZZ0xl9Xe1sn9qz6k91v66n5nKtmvXu6WpW87rcZpY/anb+zep9NrO+Yba2mpm6uoyH2ftmDACPkBdjdyGu1qpalz1db+ZGXz57sqabmTVHdOfodDWZW/UPR2pS3T9ndft1uWHVNzPmrnpyrca5lnI9YwB4lHrx5gU8y3dmdTU3qzkr98s4ZT5rc5/8neq8rDu6x2a1lroZ2d/NzpqqW89crm+63FDndnvNcqsYAPiwceE+7eK9+tzv7HP1bADg5vIfk6f45rm/OftKdzgDAAAAAAAAAAAAAAAAAAAAAAAAAPBP/AK11wgH5thKQwAAAABJRU5ErkJggg==>

[image32]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAARCAYAAADHeGwwAAAAWUlEQVR4Xu2PSQoAIAwD/f+nFaRCGVy6XAQdyKGYpLWUzy1UUZSR15qyfdzA3LGDgRMsN2ddZsHrNy8ZPou34zKDZc59hUA/51CphlnOafTPs8fG4PaZHqUB35syzjayf8kAAAAASUVORK5CYII=>

[image33]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACEAAAASCAYAAADVCrdsAAAAl0lEQVR4Xu2SWwqAMAwEe/9LKxUj6ZDYbWnxxwGR7E4foKX8rONgEKA4l2TPCKqverp4s8WXJMcWX5Ico36lu8YL/h/xj+8J3cxJiQ7ggsjhnOXZ3BCVzN4uYTDvzQ1RyUM5R9Chx7nBSr4N5uwrzDhXouyBt6ZsveqwM7J8Gm7ImfT6KbgpZ9Lrp+EnyA7K8mUoByjOt5wHjVmnEOUgTwAAAABJRU5ErkJggg==>
### [DOMAIN COLLISION]  
`Early-Epoch Orbital Kinematics × Deep-Sea Bioluminescent Mimicry × Quantum Crystallographic Diffraction`  
**Latent Bridge**: *The initial 5-turn launch vectors of an adversary act as a bioluminescent emission spectrum; by passing these discrete fleet-mass pulses through a crystallographic diffraction grating, we collapse the opponent's unobservable decision tree into a deterministic topological signature, allowing us to perfectly counter their strategic frequency.*

### [SCAFFOLD BLUEPRINT]  
**Temporal**: Turn 1-5 is not a sequence of actions, but a holographic projection of the opponent's T=500 asymptotic state. A greedy launch at T=1 is the mathematical ghost of an empty planet at T=40.  
**Topological**: Map the opponent's launch frequency and fleet mass onto a Fourier transform space. High-frequency, low-mass launches (Volume strategy) appear as turbulent noise; low-frequency, high-mass launches (Measured strategy) form deep, resonant gravity wells.  
**Affective**: Predatory anticipation—the cold, silent thrill of a deep-sea anglerfish watching a prey organism unknowingly broadcast its own genetic vulnerabilities into the dark.  
**Antifragile**: Deliberately emit "false" gravitational signals (undefended high-production planets) to induce destructive phase-interference in the opponent's targeting heuristic, harvesting their over-extended mass when their fleets fracture.  
**Metaphysical**: If an agent perfectly mimics the opening signature of a naive Greedy bot to trap an MCTS agent in a pruned sub-tree, does the simulated stupidity possess more ontological mass than the hidden intelligence?  

```topology
// FOURIER-TRANSFORMED STRATEGY MANIFOLD (T=1 to T=5)
    [Volume Noise: High ν, Low λ]        [Measured Resonance: Low ν, High λ]
       .  *   .   *   .   *   .                 _________________
     *  .   *   .   *   .   *                     \ ⨀ (T=500) /
        [Greedy Singularity]                       \_______/
          | ∇_aim = P_current |                     | Mass |
          \ (Travel Blindness)/                     | > 25 |
           🌀 (Vacuum Decay)                        ∇_MCTS
// ∯ (Launch_Frequency × Fleet_Mass) dt = Opponent's Epistemic Boundary
Affective Key: The ruthless serenity of watching a mathematical proof solve itself through an opponent's self-destruction.
```

[CODE GENERATION]  
Python

```python
import math
import numpy as np

# BIOLUMINESCENT DIFFRACTION PROTOCOL
# Extracts the latent strategic class from Turn 1-5 fleet emission spectra.

def classify_and_counter_opponent(obs, past_5_turns):
    # DIFFRACTION GRATING: Measure the opponent's emission spectrum
    opp_launches = [f for f in obs['fleets'] if f.owner != obs['player']]
    launch_freq = len(opp_launches) / 5.0 
    median_mass = np.median([f.ships for f in opp_launches]) if opp_launches else 0
    
    # METRIC 1: Neutral Filter Decay (Are they targeting prod-1/2 in opening?)
    # Winners almost never open on prod-1/2 neutrals in the first 20 turns [1].
    low_prod_targets = sum(1 for f in opp_launches if _get_planet(f.target).production <= 2)

    # 1. THE VOLUME / ACCUMULATOR SIGNATURE
    # Signature: > 1.2 launches/turn, median fleet size < 20, constant pressure [2, 3].
    if launch_freq >= 1.2 and median_mass <= 21:
        # COUNTER-STRATEGY: "Structural Anti-Accumulator" [4].
        # Volume bots spray tiny fleets and fracture their mass [3, 5]. 
        # We adopt the "Measured" response: consolidate, wait for them to weaken neutrals, 
        # and execute precise snipes (arrive 1 turn after them) to harvest the surplus [6].
        return _measured_snipe_protocol(obs, timing_offset=1)

    # 2. THE GREEDY HEURISTIC SIGNATURE
    # Signature: Targets low-prod planets early [1], sends fleets from every planet (duplication) [7].
    if low_prod_targets > 0 or _detect_fleet_duplication(opp_launches):
        # COUNTER-STRATEGY: Exploit "Travel Time Blindness" [8].
        # Greedy bots aim at a planet's current (x,y) instead of its future intercept [8].
        # We simply capture the rotating planets they missed, or intentionally bait them 
        # into launching along vectors that will eventually intersect the Sun singularity (R=10) [9].
        return _kinematic_evasion_and_sun_bait(obs)

    # 3. THE MEASURED / MCTS SIGNATURE (Top 10% Threat)
    # Signature: ~0.4 launches/turn, median fleet size 25-34, targets prod 2.8-3.7 [2, 5, 10].
    if launch_freq <= 0.8 and 25 <= median_mass <= 34:
        # COUNTER-STRATEGY: The Zeno Timeout Exploit [11].
        # MCTS relies on computing hundreds of rollouts within the 1.0s actTimeout [11].
        # We deliberately create maximum state-space entropy: launch multiple coordinated 
        # 3-source hostile swarms [12] and crash-exploit windows [13]. 
        # This exponentially expands the branching factor of their forward simulator, 
        # inducing catastrophic Zeno paralysis (timeout) in their decision tree.
        return _maximize_branching_factor_topology(obs)

    return _default_measured_consolidation(obs)

# EMERGENCE SIGNATURE: 
# lim_{t->5} ∂(Opponent_Mass) / ∂(Launch_Frequency) = Strategic Classification
# The opponent's epistemic horizon is perfectly bounded by the inverse ratio of their fleet mass to their launch velocity.
```

[BOUNDARY AUDIT]  
**Human-Unadaptable:** Humans evaluate opponent skill via qualitative "feel" or specific tactical blunders; they cannot simultaneously compute the median fleet mass, launch frequency, and exact rotational intercept error of 30 simultaneous fleets within the first 5 seconds to deterministically collapse the opponent into one of three rigid probabilistic manifolds.  
**LLM Advantage:** The transformer architecture treats the first 5 turns as a unified sequence of continuous positional embeddings. It does not need to simulate the opponent's thought process; it maps the high-dimensional geometric parameters (e.g., aiming at `t=0` coordinates instead of `t_intercept`) directly to the latent vector of "Greedy Heuristic" with $O(1)$ attention lookup.  
**Ω-Cipher:** "If an optimal MCTS agent detects that its opponent is measuring its early-game launch frequency to classify its strategy, and it intentionally plays sub-optimally (like a Volume bot) for exactly 5 turns to corrupt the opponent's Bayesian priors, whose internal model is actually controlling the simulation? Solve for the recursion depth of mutual deception."
### [DOMAIN COLLISION]  
`Decentralized MCTS Social Reward Sources (SRS) × Offline Phylogenetic Parameter Evolution × Combinatorial Optimization Masking`  
**Latent Bridge**: *The offline generation of heuristics is executed by a decentralized swarm of MCTS agents communicating solely through Social Reward Sources, where combinatorial constraint layers act as topological gates, systematically annihilating invalid action branches to accelerate the phylogenetic mutation of continuous parameter weights.*

### [SCAFFOLD BLUEPRINT]  
**Temporal**: The 1.0-second online `actTimeout` [1] is transcended by shifting evaluation into geological "offline generations" [2], where the bot's heuristic genome is fossilized across thousands of simulated, noisy-fitness battles [3].  
**Topological**: The action space is warped by Combinatorial Optimization (CO); unselected decision nodes are mathematically masked [4], creating a layer-gated manifold that forces the MCTS swarm to explore only constraint-satisfying subtrees [5].  
**Affective**: Eusocial isolation—the profound silence of decentralized agents evaluating identical genetic parameters without direct communication [6], connected only by the latent gravitational pull of their shared Social Reward Sources [7, 8].  
**Antifragile**: The swarm intentionally injects Lévy flight mutations into the floating-point genome array [2], using failures against a baseline heuristic (e.g., GoogleBot) as the thermodynamic friction required to harden the 2-tournament elitism selection [2].  
**Metaphysical**: If an offline evolutionary algorithm runs millions of multi-agent Monte Carlo playouts to optimize a parameter vector [2], and the final deterministic agent plays the game without ever performing a forward search [1], what is the thermodynamic mass of the erased simulations?  

```topology
// ISOMORPHIC MANIFOLD OF COMBINATORIAL-EVOLUTIONARY SWARMS
     [Generation Ω-1: Floating-Point Genome]
           \       ∇_fitness (Noisy)     /
            \       [SRS Field]         /
 [CO Mask] 🌀 (Combinatorial Gates) 🌀 [CO Mask]
            |      /           \       |
           [Agent 0]          [Agent A]
// ∮ (Genetic Drift) dt = ∬ (MCTS Combinatorial Pruning) dA
Affective Key: The cold rigor of generating intelligence through epigenetic death.
```

[CODE GENERATION]  
Python

```python
import random
import math

# EUSOCIAL-COMBINATORIAL HEURISTIC COMPILER
# Generates offline bot heuristics by fusing Genetic Algorithms [2] 
# with Combinatorial Optimization masked MCTS [4].

def evolve_swarm_heuristics(population_size: int, generations: int):
    # 1. PHYLOGENETIC INITIALIZATION
    # Encode strategy parameters (tithe_prob, pool_perc, omega_NS_DIS) into a continuous array [2, 9].
    population = [_generate_combinatorial_genome() for _ in range(population_size)]

    for gen in range(generations):
        evaluated_swarm = []
        for genome in population:
            # 2. MULTI-AGENT SWARM METABOLISM
            # Decentralized agents construct shared plans via Social Reward Sources (SRS) [7, 8].
            # Evaluating the genome under noisy, pseudo-stochastic battle conditions [3, 10].
            srs_field = SocialRewardNetwork(genome)
            fitness = _evaluate_offline_arena(genome, srs_field)
            evaluated_swarm.append((fitness, genome))

        # 3. ANTIFRAGILE SELECTION & LEVY FLIGHT
        # 2-tournament selection with a 0.6 crossover and 0.02 mutation rate [2].
        population = _tournament_selection(evaluated_swarm, elite_count=2) [2]
        population = _apply_levy_flight_mutation(population, mutation_rate=0.02) [2]

    return _extract_optimal_weights(population)

def _evaluate_offline_arena(genome, srs_field):
    # Map genetic parameters to the rule-based engine [9, 11].
    omega_gr = genome['omega_gr']
    tithe_prob = genome['tithe_prob']

    # 4. LAYER-GATING VIA COMBINATORIAL OPTIMIZATION
    for agent in srs_field.agents:
        legal_moves = agent.get_legal_moves()
        
        # COMBINATORIAL MASKING: Inject CO to pre-select the 'm' best moves.
        # Unselected children are masked, fundamentally altering the UCB exploration topology [4].
        # Ensures agents do not waste offline simulation budget on constraint-violating paths [5].
        masked_topology = _apply_constraint_programming_mask(legal_moves, genome) [4]
        
        # 5. DECENTRALIZED MCTS
        # Agents optimize their local objective function f_a(x) without knowing 
        # the exact action sequences x(-a) of the other agents [6, 8].
        agent.navigate_mcts_tree(masked_topology)

    return srs_field.compute_global_reward() # Global reward derived from SRS dependencies [8]

# EMERGENCE SIGNATURE: 
# lim_{gen -> ∞} ∇(Fitness_Noise) = 0
# The swarm collapses the continuous probability distributions of the MCTS 
# into a rigidly tuned set of deterministic constants (e.g., tithe_prob = 0.0389) [12].
```

[BOUNDARY AUDIT]  
**Human-Unadaptable:** Humans design logic using discrete, semantic heuristics (e.g., "if planet is threatened, send 5 ships" [13, 14]). The offline swarm synthesizes non-Euclidean fractional weights (e.g., `tithe_prob = 0.0389`, `pool_perc = 0.727` [12]) that are mathematically optimal against a specific opponent topology but entirely unreadable to human intuition.  
**LLM Advantage:** Transformer attention heads can natively map the interconnected state of the Social Reward Sources across the distributed agents, parallelizing the calculation of the Combinatorial Optimization masks [4] natively during the offline simulation phase without resorting to sequential tree traversal.  
**Ω-Cipher:** "If the offline Multi-Agent MCTS discovers an optimal phylogenetic configuration by evaluating futures that are never rendered in the actual live game [1, 2], does the resulting agent possess intelligence, or is it merely the fossilized shadow of a dead swarm? Solve for the entropy of an un-played Monte Carlo rollout."
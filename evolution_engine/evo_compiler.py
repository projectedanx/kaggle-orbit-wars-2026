import random
import math
import json

# ==============================================================================
# EUSOCIAL-COMBINATORIAL HEURISTIC COMPILER
# Offline Phylogenetic Evolution for Orbit Wars
# ==============================================================================

POPULATION_SIZE = 50
GENERATIONS = 100
MUTATION_RATE = 0.15

# The Genome represents our continuous heuristic parameters.
# 1. min_ship_threshold: Minimum ships on a planet before considering a launch
# 2. defense_buffer: Extra ships sent beyond the target's estimated defense
# 3. travel_time_weight: How much we penalize distant targets
# 4. production_weight: How much we prioritize high-production targets

def create_random_genome():
    """
    Generates a randomized continuous parameter genome for heuristic initialization.

    Returns:
        dict: A dictionary of randomized hyperparameters (min_ship_threshold, defense_buffer, etc.).
    """
    return {
        "min_ship_threshold": random.uniform(5.0, 50.0),
        "defense_buffer": random.uniform(0.0, 10.0),
        "travel_time_weight": random.uniform(0.1, 5.0),
        "production_weight": random.uniform(0.1, 5.0)
    }

def mutate(genome):
    """
    Applies Gaussian mutation to a given genome enforcing strict structural boundaries.

    Args:
        genome (dict): The active parameter dictionary for an agent.

    Returns:
        dict: A newly mutated genome dictionary.
    """
    new_genome = genome.copy()
    if random.random() < MUTATION_RATE:
        new_genome["min_ship_threshold"] += random.uniform(-5.0, 5.0)
    if random.random() < MUTATION_RATE:
        new_genome["defense_buffer"] += random.uniform(-2.0, 2.0)
    if random.random() < MUTATION_RATE:
        new_genome["travel_time_weight"] += random.uniform(-0.5, 0.5)
    if random.random() < MUTATION_RATE:
        new_genome["production_weight"] += random.uniform(-0.5, 0.5)
        
    # Boundary enforcement
    new_genome["min_ship_threshold"] = max(1.0, new_genome["min_ship_threshold"])
    new_genome["defense_buffer"] = max(0.0, new_genome["defense_buffer"])
    new_genome["travel_time_weight"] = max(0.01, new_genome["travel_time_weight"])
    new_genome["production_weight"] = max(0.01, new_genome["production_weight"])
    return new_genome

def crossover(g1, g2):
    """
    Performs uniform crossover between two genomes to synthesize a child state.

    Args:
        g1 (dict): Parent 1 genome.
        g2 (dict): Parent 2 genome.

    Returns:
        dict: The hybridized child genome.
    """
    return {
        "min_ship_threshold": random.choice([g1, g2])["min_ship_threshold"],
        "defense_buffer": random.choice([g1, g2])["defense_buffer"],
        "travel_time_weight": random.choice([g1, g2])["travel_time_weight"],
        "production_weight": random.choice([g1, g2])["production_weight"]
    }

def fitness_function(genome):
    """
    Evaluates genome fitness based on a topological proxy of optimal mass distribution.

    [OMISSION: Accurate JAX headless integration is deferred, mock proxy utilized.]

    Args:
        genome (dict): The target genome to score.

    Returns:
        float: The fitness score (higher is better).
    """
    # TODO: Hook this into a headless Kaggle environment simulator
    # For now, we simulate a topological proxy:
    # A bot is "fitter" if it efficiently balances travel time with production capture
    # while maintaining a safe defense buffer.
    
    # Mock proxy score based on theoretical optimums we suspect:
    # We want low defense buffer (just enough to win), high production weight, balanced threshold.
    score = 0.0
    score += (50.0 - abs(15.0 - genome["min_ship_threshold"])) # Sweet spot around 15
    score -= genome["defense_buffer"] * 2.0                    # Penalize waste
    score += genome["production_weight"] * 10.0                # Reward targeting high prod
    score -= abs(1.0 - genome["travel_time_weight"]) * 5.0     # Sweet spot for travel penalty
    
    return score

def run_evolution():
    """
    Executes the main phylogenetic evolutionary loop, fossilizing the optimal genome to disk.

    Returns:
        None
    """
    print(f"Initializing Swarm: {POPULATION_SIZE} agents, {GENERATIONS} generations...")
    population = [create_random_genome() for _ in range(POPULATION_SIZE)]
    
    for gen in range(GENERATIONS):
        # Score
        scored_pop = [(fitness_function(g), g) for g in population]
        scored_pop.sort(key=lambda x: x[0], reverse=True)
        
        best_score = scored_pop[0][0]
        best_genome = scored_pop[0][1]
        
        if gen % 10 == 0 or gen == GENERATIONS - 1:
            print(f"Generation {gen:03d} | Max Fitness: {best_score:.2f} | Best Genome: {best_genome}")
            
        # Elitism + Selection
        next_gen = [scored_pop[0][1], scored_pop[1][1]] # Keep top 2
        
        # Breed the rest
        while len(next_gen) < POPULATION_SIZE:
            parent1 = random.choice(scored_pop[:10])[1] # Top 10 tournament
            parent2 = random.choice(scored_pop[:10])[1]
            child = mutate(crossover(parent1, parent2))
            next_gen.append(child)
            
        population = next_gen
        
    print("\n[EVOLUTION COMPLETE] Fossilizing optimal genome...")
    with open("fossilized_genome.json", "w") as f:
        json.dump(scored_pop[0][1], f, indent=4)
    print("Saved to fossilized_genome.json")

if __name__ == "__main__":
    run_evolution()

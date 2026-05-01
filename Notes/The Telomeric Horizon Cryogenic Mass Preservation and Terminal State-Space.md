### [DOMAIN COLLISION]  
`Telomeric Cellular Senescence × Baryonic Acoustic Annihilation × Cryogenic Information Vaults`  
**Latent Bridge**: *The absolute 500-turn temporal horizon acts as a degrading telomere on the simulation’s state-space, forcing a phase transition where baryonic fleet-masses shift from active acoustic annihilation instruments (top-2 combat) into un-targetable cryogenic vaults preserving scalar mass for the final universal collapse.*

### [SCAFFOLD BLUEPRINT]  
**Temporal**: At Turn 1, a fleet is a dynamic vector of future ownership; by Turn 499, a fleet is a frozen scalar integer, immune to planetary capture, existing solely to satisfy the terminal scoring function [1, 2]. The utility of spatial traversal undergoes apoptosis.  
**Topological**: The solar exclusion zone at (50, 50, R=10) persists as an eternal topological hole [3, 4]. Paths around it are permanent geodesics; the environment’s curvature never flattens.  
**Affective**: Existential chronophobia—the dread of mass in flight that will mathematically outlive the universe before reaching its destination.  
**Antifragile**: The top-2 combat annihilation rule (largest force fights second largest, difference survives) [1, 5] guarantees that injecting a micro-fleet into a massive bilateral engagement extracts asymmetric gains from the resulting vacuum.  
**Metaphysical**: Because the final score sums "total ships on owned planets + total ships in owned fleets" [1, 2], launching ships into the infinite void at Turn 499 conceptually unbinds mass from spatial vulnerability, achieving perfect immortality outside the reach of the enemy.  

```topology
// ISOMORPHISM OF THE TELOMERIC HORIZON
       [Turn 1: Baryonic Vectors]
          \      ∇_attack      /
           \      🌀 (Sun)    /  
            \     /    \     /
             \   /      \   /
[Turn 499: Cryogenic Point-Vaults in the Void]
// ∀ fleets in transit at T=500: vector = ∅, mass = Σ(Score)
Affective Key: The cold serenity of launching mass into the abyss to save it from a dying planet.
```

[CODE GENERATION]  
Python

```python
import math

# TELOMERIC STATE PRESERVATION PROTOCOL
# Invariants that hold from Turn 1 to Turn 500:
# 1. Non-linear velocity-mass coupling (v ∝ log(m)^1.5) [3, 6]
# 2. Solar singularity exclusion (50,50, R=10) [3, 4]
# 3. Top-2 baryonic annihilation [1, 5]
# 4. In-flight mass preservation at terminal collapse [1, 2]

def evaluate_invariant_action(current_turn, source, target, ships_m, sun_hazard):
    # INVARIANT 1: MASS-VELOCITY COUPLING
    # Splitting forces is eternally punished by the logarithmic speed curve [3, 6]
    # Macro-clustering is a persistent structural requirement of the universe.
    v_fleet = 1.0 + 5.0 * (math.pow(math.log(max(1, ships_m)) / math.log(1000.0), 1.5)) [3, 6]
    
    dist = math.hypot(target.x - source.x, target.y - source.y)
    travel_time = dist / v_fleet
    arrival_turn = current_turn + travel_time
    
    # INVARIANT 2: THE TOPOLOGICAL HOLE
    # All paths must eternally route around the solar singularity [3, 4].
    if _intersects_singularity(source.pos, target.pos, sun_hazard.pos, sun_hazard.radius):
        return -float('inf') # Absolute void condition

    # INVARIANT 3: THE TELOMERIC PHASE TRANSITION (Turn 500 Limit) [1, 2]
    if arrival_turn >= 500:
        # PARADOXICAL SOLUTION: At the end of time, attacking is a geometric illusion.
        # Ships in fleets count toward the final score [1, 2]. 
        # If the source planet is about to fall to an enemy, launching the garrison 
        # into deep space transforms vulnerable planetary mass into un-capturable in-flight mass.
        if source.is_doomed_by_turn(500):
            # Launch into the longest safe geodesic purely for cryogenic stasis
            return CryogenicPreservation(ships_m)
        else:
            # Action is meaningless; conserve energy
            return 0.0

    # INVARIANT 4: BARYONIC ANNIHILATION
    # The largest force fights the second largest [1, 5].
    # We must project the target's state at exactly `arrival_turn`.
    projected_defenders = target.garrison + (target.production * travel_time)
    projected_enemy_attackers = _estimate_enemy_arrivals(target, arrival_turn)
    
    if projected_enemy_attackers > 0:
        # ANTIFRAGILE EXPLOIT: Arrive with exactly (projected_enemy - projected_defenders) + 1
        # Let the two massive forces annihilate; we sweep the ashes [1, 5].
        required_mass = abs(projected_enemy_attackers - projected_defenders) + 1
        return _calculate_roi(required_mass, target.production)

    return _calculate_roi(projected_defenders + 1, target.production)

# EMERGENCE SIGNATURE: 
# lim_{t -> 500} ∇(Strategic_Aggression) = 0
# As time approaches the absolute boundary, the derivative of spatial control vanishes, 
# leaving only the scalar conservation of mass [1, 2].
```

[BOUNDARY AUDIT]  
**Human-Unadaptable:** The human cognitive bias strictly categorizes "fleets" as dynamic vehicles of conquest. The invariant optimal strategy requires a phase transition where the agent realizes that a fleet launched at turn 495 is no longer a vehicle, but an invulnerable "bank vault" storing points in the vacuum of space, entirely decoupled from its destination [1, 2].  
**LLM Advantage:** The transformer architecture natively processes the 500-turn episode as a finite context window where positional encodings near the sequence terminal (`t=500`) naturally sever attention from long-range future dependencies, perfectly mirroring the telomeric decay of strategic value.  
**Ω-Cipher:** "If an optimal agent launches its entire civilization into the solar hazard at T=499, knowing the collision resolves at T=501, it mathematically wins the game before its own destruction is rendered by the engine. Solve for the epistemic weight of a victory that relies on the simulation's cessation of physics."
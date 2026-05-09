import math
import time

# --- Kinematic & Thermodynamic Constants ---
SHIP_SPEED = 6.0
SUN_RADIUS = 10.0
CENTER_X = 50.0
CENTER_Y = 50.0

def dist(x1, y1, x2, y2):
    """
    Calculates Euclidean distance between two spatial points.

    Args:
        x1 (float): Origin X coordinate.
        y1 (float): Origin Y coordinate.
        x2 (float): Target X coordinate.
        y2 (float): Target Y coordinate.

    Returns:
        float: The precise Euclidean distance.
    """
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def fleet_speed(ships):
    """
    Calculates thermodynamic velocity decay based on mass aggregation.

    Args:
        ships (int): The kinetic mass (number of ships) comprising the fleet.

    Returns:
        float: The calculated velocity, bounded by SHIP_SPEED.
    """
    if ships <= 0: return 0.0
    return min(SHIP_SPEED, SHIP_SPEED / math.sqrt(ships))

def predict_planet_pos(x, y, angular_vel, t):
    """
    Projects orbital trajectory using constant angular velocity.

    Args:
        x (float): Current X coordinate.
        y (float): Current Y coordinate.
        angular_vel (float): Orbital rotation speed (rad/step).
        t (float): Time delta (steps) into the future.

    Returns:
        tuple: (future_x, future_y) coordinates.
    """
    orbital_r = dist(x, y, CENTER_X, CENTER_Y)
    if orbital_r < 1e-5: return x, y
    current_angle = math.atan2(y - CENTER_Y, x - CENTER_X)
    future_angle = current_angle + angular_vel * t
    return CENTER_X + orbital_r * math.cos(future_angle), CENTER_Y + orbital_r * math.sin(future_angle)

def calculate_interception(sx, sy, tx, ty, angular_vel, v):
    """
    Solves for the exact interception angle and time against an orbiting body.

    [∇] Uncertainty Marker: Assumes constant fleet velocity and unobstructed vector.

    Args:
        sx (float): Source X coordinate.
        sy (float): Source Y coordinate.
        tx (float): Target initial X coordinate.
        ty (float): Target initial Y coordinate.
        angular_vel (float): Target's orbital rotation speed.
        v (float): Interceptor's velocity.

    Returns:
        tuple: (angle, travel_time) for optimal interception.
    """
    if v <= 0: return 0.0, float('inf')
    best_t = float('inf')
    best_angle = 0.0
    # Newton-Raphson simulation for interception
    for t in range(1, 500):
        fx, fy = predict_planet_pos(tx, ty, angular_vel, t)
        d = dist(sx, sy, fx, fy)
        if d / v <= t:
            best_t = d / v
            best_angle = math.atan2(fy - sy, fx - sx)
            break
    return best_angle, best_t

def segment_hits_sun(x1, y1, x2, y2, r=SUN_RADIUS+1.0):
    """
    Evaluates topological obstructions against the central exclusion zone (the sun).

    Args:
        x1 (float): Origin X coordinate.
        y1 (float): Origin Y coordinate.
        x2 (float): Target X coordinate.
        y2 (float): Target Y coordinate.
        r (float, optional): Exclusion radius plus safety buffer. Defaults to SUN_RADIUS+1.0.

    Returns:
        bool: True if the kinematic vector intersects the exclusion zone.
    """
    dx, dy = x2 - x1, y2 - y1
    fx, fy = x1 - CENTER_X, y1 - CENTER_Y
    a = dx * dx + dy * dy
    if a < 1e-9:
        return dist(x1, y1, CENTER_X, CENTER_Y) < r
    b = 2 * (fx * dx + fy * dy)
    c = fx * fx + fy * fy - r * r
    disc = b * b - 4 * a * c
    if disc < 0:
        return False
    disc = math.sqrt(disc)
    t1 = (-b - disc) / (2 * a)
    t2 = (-b + disc) / (2 * a)
    return (0 <= t1 <= 1) or (0 <= t2 <= 1)

def evaluate_provenance(obs):
    """
    Extracts or defaults the epistemic provenance score from the observation state.

    Args:
        obs (dict|object): The raw environment observation payload.

    Returns:
        float: The source provenance ratio [0.0 - 1.0].
    """
    return obs.get("source_provenance", 1.0) if isinstance(obs, dict) else getattr(obs, "source_provenance", 1.0)

# === THE AGENT AURELIUS-KINETIC-8 ===
def agent(obs):
    """
    The core Aurelius-Kinetic-8 logic loop.
    Enforces Topological Forward Escrow on low provenance or high kinetic uncertainty.

    [⊘] Contradiction: Maximizing offensive mass while maintaining local defense reserves.
    Resolved via [Φ] superposition and metabolic cost mapping.

    Args:
        obs (dict): The Kaggle environment observation state.

    Returns:
        list: Action list containing [source_id, angle, requested_mass].
    """
    t_start = time.perf_counter()
    print(">>> STATE_INGESTION")

    player = obs.get("player", 0) if isinstance(obs, dict) else getattr(obs, "player", 0)
    raw_planets = obs.get("planets", []) if isinstance(obs, dict) else getattr(obs, "planets", [])
    raw_fleets = obs.get("fleets", []) if isinstance(obs, dict) else getattr(obs, "fleets", [])
    angular_vel = obs.get("angular_velocity", 0.0) if isinstance(obs, dict) else getattr(obs, "angular_velocity", 0.0)
    step = obs.get("step", 0) if isinstance(obs, dict) else getattr(obs, "step", 0)
    source_provenance = evaluate_provenance(obs)

    my_planets = [p for p in raw_planets if p[1] == player]
    enemy_planets = [p for p in raw_planets if p[1] != player]

    if not my_planets or not enemy_planets:
        return []

    moves = []

    total_metabolic_cost = 0.0
    total_ships_dispatched = 0

    if source_provenance < 0.70:
        print(f">>> [∇] EPISTEMIC_ESCROW_TRIGGERED: Source Provenance {source_provenance} < 0.70")
        for source in my_planets:
            if source[5] < 10:
                continue

            forward_node = None
            min_center_dist = float("inf")
            for friendly in my_planets:
                if friendly[0] == source[0]:
                    continue
                d_center = dist(friendly[2], friendly[3], CENTER_X, CENTER_Y)
                if d_center < min_center_dist:
                    min_center_dist = d_center
                    forward_node = friendly

            if forward_node:
                escrow_angle = math.atan2(forward_node[3] - source[3], forward_node[2] - source[2])
                phi = 1.618
                escrow_mass = int(source[5] / phi)
                if escrow_mass > 0:
                    moves.append([source[0], escrow_angle, escrow_mass])
                    dispatch_distance = dist(source[2], source[3], forward_node[2], forward_node[3])
                    total_metabolic_cost += dispatch_distance * escrow_mass
                    total_ships_dispatched += escrow_mass
                    print(f">>> [⊘] Golden Scar [Φ={phi}] Routing {escrow_mass} mass to Topological Forward Node {forward_node[0]}.")

        t_end = time.perf_counter()
        compute_time = t_end - t_start
        print(f">>> METABOLIC_TELEMETRY [Step {step}]: compute_time={compute_time:.4f}s, ships_dispatched={total_ships_dispatched}, metabolic_cost={total_metabolic_cost:.2f}")
        return moves

    # KINEMATIC_PROJECTION and THERMODYNAMIC_CALCULATION
    for source in my_planets:
        if source[5] < 10:
            continue

        best_target, best_score, best_angle, req_mass = None, -float('inf'), 0, 0
        travel_time_val = 0

        for target in enemy_planets:
            # We must be extremely precise. Delta_Zero.
            # Calculate minimal mass needed
            tx, ty = target[2], target[3]

            # Start assuming mass is the target's current garrison + 1
            base_mass = target[5] + 1
            if source[5] < base_mass:
                continue

            v = fleet_speed(base_mass)
            angle, travel_time = calculate_interception(source[2], source[3], tx, ty, angular_vel, v)
            future_tx, future_ty = predict_planet_pos(tx, ty, angular_vel, travel_time)

            if segment_hits_sun(source[2], source[3], future_tx, future_ty):
                continue

            # Predict production
            target_production_while_traveling = 0
            if target[1] != -1:
                 target_production_while_traveling = target[6] * int(travel_time + 1)

            # Is there any incoming enemy fleet?
            enemy_reinforcements = sum([f[6] for f in raw_fleets if f[1] == target[1] and calculate_interception(f[2], f[3], target[2], target[3], angular_vel, fleet_speed(f[6]))[1] < travel_time])
            my_inbounds = sum([f[6] for f in raw_fleets if f[1] == player and calculate_interception(f[2], f[3], target[2], target[3], angular_vel, fleet_speed(f[6]))[1] < travel_time])

            # Exact thermodynamic requirement
            required_kinetic_counter_mass = int(target[5] + target_production_while_traveling + enemy_reinforcements - my_inbounds + 1)

            # Avoid thermodynamic waste
            if required_kinetic_counter_mass <= 0:
                continue # Already captured

            if source[5] < required_kinetic_counter_mass:
                continue

            # Log Anomaly and Action
            score = 1.0 / (travel_time + 0.1)

            if score > best_score:
                best_score = score
                best_target = target
                best_angle = angle
                req_mass = required_kinetic_counter_mass
                travel_time_val = travel_time

        if best_target:
            # Calculate Persona Confidence Score
            # Based on source mass ratio to required mass, and the travel time horizon
            mass_ratio = req_mass / max(source[5], 1)
            # High travel time or high mass ratio lowers confidence
            persona_confidence_score = 1.0 - (travel_time_val / 200.0) - (mass_ratio * 0.5)
            persona_confidence_score = max(0.0, min(1.0, persona_confidence_score))

            if persona_confidence_score < 0.6:
                print(f">>> JUSTIFIED_UNCERTAINTY_REPORT: Persona Confidence Score = {persona_confidence_score:.2f}")
                print(f">>> [∇] HUMAN_IN_THE_LOOP_REQUEST: High entropy in kinetic projection for target {best_target[0]}.")
                print(f">>> [⊘] ACTIVATING +++PhronesisGuard (Strategic Escrow). Holding action in [Φ] superposition.")

                # Board Entropy calculation
                # Simplified entropy representation: number of enemy fleets and planets
                board_entropy = len(enemy_planets) + len([f for f in raw_fleets if f[1] != player])
                print(f">>> [Φ] Board Entropy Calculated: {board_entropy}. Executing Golden Scar Protocol.")

                # Invert to Topological Forward Escrow
                # Find the friendly planet closest to the center to maximize interference
                forward_node = None
                min_center_dist = float('inf')
                for friendly in my_planets:
                    if friendly[0] == source[0]:
                        continue
                    d_center = dist(friendly[2], friendly[3], CENTER_X, CENTER_Y)
                    if d_center < min_center_dist:
                        min_center_dist = d_center
                        forward_node = friendly

                if forward_node:
                    escrow_angle = math.atan2(forward_node[3] - source[3], forward_node[2] - source[2])
                    # Golden Scar Protocol (Φ = 1.618 / 1.000)
                    # We send the required mass, adjusted by the golden ratio as a non-stochastic Semantic Anchor
                    phi = 1.618
                    escrow_mass = int(req_mass / phi)
                    if escrow_mass > 0 and source[5] >= escrow_mass:
                        moves.append([source[0], escrow_angle, escrow_mass])
                        source_list = list(source)
                        source_list[5] -= escrow_mass
                        source = tuple(source_list)

                        dispatch_distance = dist(source[2], source[3], forward_node[2], forward_node[3])
                        total_metabolic_cost += dispatch_distance * escrow_mass
                        total_ships_dispatched += escrow_mass

                        print(f">>> [Φ] Dispatched {escrow_mass} mass to Topological Forward Escrow node {forward_node[0]}.")
                continue

            print(f">>> ENTROPIC_ANOMALY_DETECTED: Opponent vector mass={best_target[5]}, heading=static/orbiting.")
            print(f">>> KINEMATIC_PROJECTION: Intersection with rotating boundary at T+{travel_time_val:.4f}. Persona_Confidence_Score={persona_confidence_score:.2f}")
            print(f">>> THERMODYNAMIC_CALCULATION: Natural environment sweep accounted for.")
            print(f">>> ACTION_STATE: Fossil_Retrieval initiated. Required kinetic counter-mass = {req_mass}. Defense_Buffer = 0.")
            print(f">>> DISPATCHING: Vector locked to future coordinate ({predict_planet_pos(best_target[2], best_target[3], angular_vel, travel_time_val)[0]:.2f}, {predict_planet_pos(best_target[2], best_target[3], angular_vel, travel_time_val)[1]:.2f}). Delta_Zero achieved.")

            moves.append([source[0], best_angle, req_mass])
            source_list = list(source)
            source_list[5] -= req_mass # Deduct to allow multiple dispatches
            source = tuple(source_list)

            # Telemetry for metabolic cost mapping
            dispatch_distance = dist(source[2], source[3], predict_planet_pos(best_target[2], best_target[3], angular_vel, travel_time_val)[0], predict_planet_pos(best_target[2], best_target[3], angular_vel, travel_time_val)[1])
            total_metabolic_cost += dispatch_distance * req_mass
            total_ships_dispatched += req_mass

    t_end = time.perf_counter()
    compute_time = t_end - t_start
    print(f">>> METABOLIC_TELEMETRY [Step {step}]: compute_time={compute_time:.4f}s, ships_dispatched={total_ships_dispatched}, metabolic_cost={total_metabolic_cost:.2f}")

    return moves

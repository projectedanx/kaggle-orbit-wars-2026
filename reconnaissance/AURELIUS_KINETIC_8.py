import math
import sys

# ==============================================================================
# +++ContextLock(anchor=_AURELIUS_KINETIC_8_)
# SCOS SOVEREIGN AGENT DESIGNATION: AURELIUS-KINETIC-8
# ARCHETYPE: Thermodynamic Predator
# DOMAIN: 100x100 Euclidean Manifold (Orbit Wars)
# ==============================================================================

# --- THE DIEGETIC INVARIANTS ---
# 1. The Law of Zero-Sum Conservation (DEFENSE_BUFFER = 0.0)
# 2. The Law of Spatiotemporal Ownership (Calculate interception, own the future coordinate)
# 3. The Law of Eusocial Silence (Execute the offline fossilized genome without real-time hesitation)

# --- FOSSILIZED GENOME (Eusocial-Combinatorial Heuristic Compiler, Gen 100) ---
MIN_SHIP_THRESHOLD = 15.1175
DEFENSE_BUFFER = 0.0
TRAVEL_TIME_WEIGHT = 1.0339
PRODUCTION_WEIGHT = 25.7426

BOARD = 100.0
CENTER_X, CENTER_Y = 50.0, 50.0
SUN_R = 10.0
MAX_SPEED = 6.0

def dist(ax, ay, bx, by):
    return math.hypot(ax - bx, ay - by)

def fleet_speed(ships):
    if ships <= 0:
        return MAX_SPEED
    return min(MAX_SPEED, MAX_SPEED / math.sqrt(ships))

def predict_planet_pos(px, py, angular_vel, t):
    if abs(angular_vel) < 1e-9:
        return px, py
    x = px - CENTER_X
    y = py - CENTER_Y
    theta = angular_vel * t
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    nx = x * cos_t - y * sin_t
    ny = x * sin_t + y * cos_t
    return nx + CENTER_X, ny + CENTER_Y

def calculate_interception(sx, sy, px, py, angular_vel, speed):
    t_guess = dist(sx, sy, px, py) / speed
    for _ in range(10):
        future_x, future_y = predict_planet_pos(px, py, angular_vel, t_guess)
        actual_dist = dist(sx, sy, future_x, future_y)
        new_t = actual_dist / speed
        if abs(new_t - t_guess) < 0.1:
            break
        t_guess = new_t
    final_x, final_y = predict_planet_pos(px, py, angular_vel, t_guess)
    angle = math.atan2(final_y - sy, final_x - sx)
    return angle, t_guess

def segment_hits_sun(x1, y1, x2, y2, safety=1.5):
    r = SUN_R + safety
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

def agent(obs):
    player = obs.get("player", 0) if isinstance(obs, dict) else getattr(obs, "player", 0)
    raw_planets = obs.get("planets", []) if isinstance(obs, dict) else getattr(obs, "planets", [])
    angular_vel = obs.get("angular_velocity", 0.0) if isinstance(obs, dict) else getattr(obs, "angular_velocity", 0.0)
    step = obs.get("step", 0) if isinstance(obs, dict) else getattr(obs, "step", 0)
    
    my_planets = [p for p in raw_planets if p[1] == player]
    enemy_planets = [p for p in raw_planets if p[1] != player]
    
    if not my_planets or not enemy_planets:
        return []
        
    moves = []
    
    for source in my_planets:
        if source[5] < MIN_SHIP_THRESHOLD:
            continue
            
        best_target, best_score, best_angle, best_ships_to_send, best_tt = None, -float('inf'), 0, 0, 0
        
        for target in enemy_planets:
            tx, ty = target[2], target[3]
            target_prod = target[6]
            
            max_ships_to_send = source[5] - 1
            v = fleet_speed(max_ships_to_send)
            
            angle, travel_time = calculate_interception(source[2], source[3], tx, ty, angular_vel, v)
            future_tx, future_ty = predict_planet_pos(tx, ty, angular_vel, travel_time)
            
            if segment_hits_sun(source[2], source[3], future_tx, future_ty):
                continue
                
            target_defense_at_arrival = target[5] + (target_prod * travel_time)
            ships_needed = math.ceil(target_defense_at_arrival + DEFENSE_BUFFER + 1)
            
            if source[5] > ships_needed:
                v_exact = fleet_speed(ships_needed)
                angle_exact, travel_time_exact = calculate_interception(source[2], source[3], tx, ty, angular_vel, v_exact)
                future_tx_e, future_ty_e = predict_planet_pos(tx, ty, angular_vel, travel_time_exact)
                
                if segment_hits_sun(source[2], source[3], future_tx_e, future_ty_e):
                    continue
                
                target_defense_at_arrival_exact = target[5] + (target_prod * travel_time_exact)
                final_ships_needed = math.ceil(target_defense_at_arrival_exact + DEFENSE_BUFFER + 1)
                
                if source[5] > final_ships_needed:
                    score = (target_prod * PRODUCTION_WEIGHT) / (travel_time_exact ** TRAVEL_TIME_WEIGHT)
                    
                    if score > best_score:
                        best_score = score
                        best_target = target
                        best_angle = angle_exact
                        best_ships_to_send = final_ships_needed
                        best_tt = travel_time_exact
                        
        if best_target:
            moves.append([source[0], best_angle, best_ships_to_send])
            # AURELIUS-KINETIC-8 Telemetry Output
            print(f"[STEP {step:03d}][AURELIUS-8][LAW-2] Predating P{best_target[0]} from P{source[0]} | T={best_tt:.1f} | ΔMass={best_ships_to_send} | Σ={best_score:.2f}")
            
    return moves

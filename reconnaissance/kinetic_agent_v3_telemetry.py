import math
import sys

# --- OFFLINE EVOLVED GENOME ---
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
    if ships <= 1:
        return 1.0
    ratio = math.log(ships) / math.log(1000.0)
    ratio = max(0.0, min(1.0, ratio))
    return 1.0 + (MAX_SPEED - 1.0) * (ratio ** 1.5)

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
            print(f"[STEP {step:03d}][SCOS-TELEMETRY] P{source[0]} -> P{best_target[0]} | Ships: {best_ships_to_send} | TravelTime: {best_tt:.1f} | Score: {best_score:.2f}")
            
    return moves

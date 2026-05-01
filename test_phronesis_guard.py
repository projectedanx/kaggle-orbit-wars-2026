import math
import orbit_agent_manifest as agent_module

def test_phronesis_guard_escrow():
    # Construct a state where Persona Confidence Score is guaranteed to be < 0.6
    # This happens when target is far away (high travel time)
    # We set up Player 0 (agent), and Player 1 (enemy).

    # Planet structure: [id, owner, x, y, radius, ships, production]
    planets = [
        [0, 0, 10.0, 10.0, 2.0, 100, 1.0],  # Source: Low mass relative to distance
        [1, 1, 90.0, 10.0, 2.0, 45, 1.0],  # Target: Far away
        [2, 0, 15.0, 15.0, 2.0, 10, 1.0],  # Safe Escrow: Close to source, friendly
    ]

    obs = {
        "player": 0,
        "planets": planets,
        "fleets": [],
        "angular_velocity": 0.0, # Make it static for predictable time
        "step": 10
    }

    moves = agent_module.agent(obs)

    # In the old code, low confidence led to no moves (returning []).
    # In the new Phronesis Guard code, it should route the mass to the safe escrow planet.
    # We expect a move from planet 0 to planet 2.

    assert len(moves) > 0, "[∇] Test failed: Expected Strategic Escrow to route mass, but no moves were generated."
    assert moves[0][0] == 0, "Source should be planet 0"

    # The angle should point to planet 2
    dx = planets[2][2] - planets[0][2]
    dy = planets[2][3] - planets[0][3]
    expected_angle = math.atan2(dy, dx)

    # Allow some tolerance for the angle
    assert abs(moves[0][1] - expected_angle) < 0.1, "[⊘] Test failed: Mass was not routed to the Strategic Escrow."

if __name__ == "__main__":
    test_phronesis_guard_escrow()
    print("Test passed.")

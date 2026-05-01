import math
import orbit_agent_manifest as agent_module

def test_phronesis_guard_escrow():
    # Construct a state where Persona Confidence Score is guaranteed to be < 0.6
    # This happens when target is far away (high travel time) and mass_ratio is high.

    # Center of board is 50.0, 50.0. Sun is there. Avoid passing through center.
    planets = [
        [0, 0, 10.0, 50.0, 2.0, 100, 1.0],  # Source
        [1, 1, 90.0, 10.0, 2.0, 45, 1.0],   # Target (far enough, avoids sun)
        [2, 0, 5.0, 50.0, 2.0, 10, 1.0],    # Rear Escrow
        [3, 0, 40.0, 40.0, 2.0, 10, 1.0],   # Forward Escrow: Closer to center
    ]

    obs = {
        "player": 0,
        "planets": planets,
        "fleets": [],
        "angular_velocity": 0.0, # Make it static for predictable time
        "step": 10
    }

    moves = agent_module.agent(obs)

    # Under Topological Forward Escrow, the agent should route mass to the
    # node closest to the center (planet 3), not the safest rear node (planet 2).
    # We expect a move from planet 0 to planet 3.

    assert len(moves) > 0, "[∇] Test failed: Expected Strategic Escrow to route mass, but no moves were generated."
    assert moves[0][0] == 0, "Source should be planet 0"

    # The angle should point to planet 3
    dx = planets[3][2] - planets[0][2]
    dy = planets[3][3] - planets[0][3]
    expected_angle = math.atan2(dy, dx)

    # Allow some tolerance for the angle
    assert abs(moves[0][1] - expected_angle) < 0.1, "[⊘] Test failed: Mass was not routed to the Topological Forward Node."

if __name__ == "__main__":
    test_phronesis_guard_escrow()
    print("Test passed.")

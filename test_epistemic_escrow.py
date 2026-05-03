import math
import orbit_agent_manifest as agent_module

def test_epistemic_escrow_low_provenance():
    # Construct a state to trigger evaluate_provenance() to return < 0.70
    # In our implementation, we'll simulate this by mocking or passing a low provenance metric.
    # The agent should route mass to the Topological Forward Node (the friendly planet closest to center).

    planets = [
        [0, 0, 10.0, 90.0, 2.0, 100, 1.0],  # Source (Friendly)
        [1, 1, 90.0, 10.0, 2.0, 45, 1.0],   # Target (Enemy)
        [2, 0, 5.0, 50.0, 2.0, 10, 1.0],    # Rear Escrow (Friendly, far from center 50,50)
        [3, 0, 45.0, 45.0, 2.0, 10, 1.0],   # Forward Escrow (Friendly, close to center 50,50)
    ]

    obs = {
        "player": 0,
        "planets": planets,
        "fleets": [],
        "angular_velocity": 0.0,
        "step": 10,
        "source_provenance": 0.65 # Artificial flag for testing Epistemic Escrow [∇]
    }

    moves = agent_module.agent(obs)

    assert len(moves) > 0, "[∇] Test failed: Expected Epistemic Escrow to route mass, but no moves were generated."

    source = moves[0][0]
    angle = moves[0][1]

    assert source == 0, "Source should be planet 0"

    # The angle should point to planet 3 (Topological Forward Node)
    dx = planets[3][2] - planets[0][2]
    dy = planets[3][3] - planets[0][3]
    expected_angle = math.atan2(dy, dx)

    assert abs(angle - expected_angle) < 0.1, "[⊘] Test failed: Mass was not routed to the Topological Forward Node during Epistemic Escrow."

if __name__ == "__main__":
    test_epistemic_escrow_low_provenance()
    print("Test passed.")

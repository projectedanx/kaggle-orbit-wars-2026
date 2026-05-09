from orbit_agent_manifest import agent
import pytest

def test_phronesis_guard_escrow():
    """
    Validates that a low Source Provenance triggers Topological Forward Escrow
    instead of standard kinematic engagement, maintaining the Mereological Mandate.

    Returns:
        None
    """
    # Create a mock observation payload with low provenance
    obs_mock = {
        "player": 0,
        "step": 0,
        "source_provenance": 0.50, # Below 0.70 threshold
        "planets": [
            [0, 0, 10, 10, 1, 50, 5], # source planet, player 0
            [1, 0, 40, 40, 1, 10, 2], # friendly topological forward node
            [2, 1, 90, 90, 1, 20, 5]  # enemy planet
        ],
        "fleets": []
    }

    moves = agent(obs_mock)

    # We expect 2 moves because both planets 0 and 1 belong to player 0 and > 10 ships
    # They route to each other as the "Topological Forward Node" since they are the only other friendly nodes
    assert len(moves) == 2

    source_id, target_angle, mass = moves[0]

    assert source_id == 0
    # Mass should be scaled by phi (50 / 1.618 = 30.9 => 30)
    assert mass == int(50 / 1.618)

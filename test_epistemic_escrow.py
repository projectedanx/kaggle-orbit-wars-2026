from symbolic_scar_registry import SymbolicScarRegistry, EpistemicEscrowException
import pytest

def test_epistemic_escrow_low_provenance():
    """
    Validates the Golden Scar Protocol triggers EpistemicEscrowException
    when the CFDI threshold exceeds established limits.

    Returns:
        None
    """
    registry = SymbolicScarRegistry()
    claim = {
        "architecture": "Betti-1 Loop: Unverified Kinetic Trajectory",
        "agent": "P5-Implementer"
    }

    # Simulate a CFDI score higher than the 0.15 threshold
    high_cfdi = 0.85

    with pytest.raises(EpistemicEscrowException):
        registry.evaluate_claim(claim, high_cfdi)

    # Verify the failure was recorded in the registry as an active scar
    active_scars = registry.get_active_scars()
    assert len(active_scars) == 1
    assert active_scars[0]["pattern"] == claim["architecture"]
    assert active_scars[0]["status"] == "Active_Escrow"

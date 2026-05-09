import pytest
from symbolic_scar_registry import SymbolicScarRegistry, EpistemicEscrowException

def test_scar_registry_halt_on_uncertainty():
    """
    Validates that evaluating a claim with a CFDI > 0.15 enforces execution halting.

    Returns:
        None
    """
    registry = SymbolicScarRegistry()
    claim = {"architecture": "Undefined_Latent_Space"}

    with pytest.raises(EpistemicEscrowException):
        registry.evaluate_claim(claim, 0.25)

def test_scar_registry_weaponize_failure():
    """
    Verifies that halted executions generate a structural scar enforcing superposition weights.

    Returns:
        None
    """
    registry = SymbolicScarRegistry()
    claim = {"architecture": "Undefined_Latent_Space"}

    try:
        registry.evaluate_claim(claim, 0.25)
    except EpistemicEscrowException:
        pass

    scars = registry.get_active_scars()
    assert len(scars) == 1
    assert scars[0]["pattern"] == "Undefined_Latent_Space"
    assert scars[0]["superposition_weight"] == 1.618

import pytest
from symbolic_scar_registry import SymbolicScarRegistry, EpistemicEscrowException

def test_scar_registry_halt_on_uncertainty():
    registry = SymbolicScarRegistry()

    # Simulate a condition where CFDI > 0.15
    cfdi_score = 0.18
    claim = {"architecture": "shared_database_between_contexts"}

    with pytest.raises(EpistemicEscrowException) as excinfo:
        registry.evaluate_claim(claim, cfdi_score)

    assert "CFDI threshold breached" in str(excinfo.value)

def test_scar_registry_weaponize_failure():
    registry = SymbolicScarRegistry()

    cfdi_score = 0.20
    claim = {"architecture": "2pc_xa_transaction"}

    try:
        registry.evaluate_claim(claim, cfdi_score)
    except EpistemicEscrowException:
        pass

    # The registry should have recorded the scar with Golden Scar Protocol details
    scars = registry.get_active_scars()
    assert len(scars) == 1
    assert scars[0]["pattern"] == "2pc_xa_transaction"
    assert scars[0]["superposition_weight"] == 1.618  # Phi
    assert scars[0]["status"] == "Active_Escrow"

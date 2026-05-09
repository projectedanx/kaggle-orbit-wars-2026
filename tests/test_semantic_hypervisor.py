import pytest
from symbolic_scar_registry import SymbolicScarRegistry, EpistemicEscrowException
from semantic_hypervisor import SemanticHypervisor, EpistemicPheromone

def test_successful_stigmergic_lock():
    """Validates that a node can be locked and unlocked correctly."""
    registry = SymbolicScarRegistry()
    hypervisor = SemanticHypervisor(registry)

    pheromone = EpistemicPheromone(agent_id="agent_alpha", intent_hash="hash_123")

    # Acquire lock
    assert hypervisor.lock_ast_node("node_A", pheromone) is True

    # Cannot unlock with wrong agent
    assert hypervisor.unlock_ast_node("node_A", "agent_beta") is False

    # Correct unlock
    assert hypervisor.unlock_ast_node("node_A", "agent_alpha") is True

def test_semantic_mutex_conflict_triggers_escrow():
    """
    Validates that a race condition (lock conflict) triggers an EpistemicEscrowException
    and records a Betti-1 scar via the Golden Scar Protocol.
    """
    registry = SymbolicScarRegistry()
    hypervisor = SemanticHypervisor(registry)

    pheromone_1 = EpistemicPheromone(agent_id="agent_alpha", intent_hash="hash_123")
    pheromone_2 = EpistemicPheromone(agent_id="agent_beta", intent_hash="hash_456")

    # Agent Alpha locks the node
    assert hypervisor.lock_ast_node("node_B", pheromone_1) is True

    # Agent Beta attempts to lock the same node, which should trigger Escrow
    with pytest.raises(EpistemicEscrowException) as excinfo:
        hypervisor.lock_ast_node("node_B", pheromone_2)

    assert "CFDI threshold breached" in str(excinfo.value)

    # Verify the scar was recorded in the registry
    scars = registry.get_active_scars()
    assert len(scars) == 1
    assert "Betti-1 Loop: Conflict at node_B" in scars[0]["pattern"]
    assert scars[0]["superposition_weight"] == 1.618  # Golden Ratio applied

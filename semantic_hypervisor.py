import time
from typing import Dict, Optional
from symbolic_scar_registry import SymbolicScarRegistry, EpistemicEscrowException

class EpistemicPheromone:
    """
    Machine-readable signal representing an agent's intent to operate on a topological space.
    Used for Stigmergic Concurrency.
    """
    def __init__(self, agent_id: str, intent_hash: str, strength: float = 1.0):
        """
        Initializes an EpistemicPheromone to declare spatial intent on the AST.

        Args:
            agent_id (str): The unique identifier of the agent leaving the pheromone.
            intent_hash (str): A cryptographic hash of the agent's intended operation.
            strength (float, optional): The relative strength of the intent. Defaults to 1.0.

        Returns:
            None
        """
        self.agent_id = agent_id
        self.intent_hash = intent_hash
        self.strength = strength
        self.timestamp = time.time()

class SemanticHypervisor:
    """
    The Semantic Hypervisor Daemon physically locks Abstract Syntax Tree (AST) nodes
    (represented here by node keys) to prevent Logic Shearing.
    """
    def __init__(self, scar_registry: SymbolicScarRegistry):
        """
        Initializes the SemanticHypervisor with a reference to the global Scar Registry.

        Args:
            scar_registry (SymbolicScarRegistry): The registry for logging Epistemic Escrows.

        Returns:
            None
        """
        self.scar_registry = scar_registry
        self.active_locks: Dict[str, EpistemicPheromone] = {}

    def lock_ast_node(self, node_key: str, pheromone: EpistemicPheromone) -> bool:
        """
        Attempts to lock a node. If a conflict occurs, it applies the Golden Scar Protocol
        via the SymbolicScarRegistry rather than auto-resolving.

        [⊘] Contradiction: Auto-merging concurrent agent intents homogenizes architecture.
        We hold collisions in superposition (Betti-1 Loop) instead.

        Args:
            node_key (str): The specific AST node identifier to lock.
            pheromone (EpistemicPheromone): The agent's intent signal.

        Returns:
            bool: True if the lock is successfully acquired; False otherwise.

        Raises:
            EpistemicEscrowException: If a Logic Shear (collision) is detected.
        """
        if node_key in self.active_locks:
            existing_pheromone = self.active_locks[node_key]

            # The Mereological Mandate + Golden Scar Protocol
            # Conflict detected. Halt and evaluate via Paraconsistent Logic.

            # We construct a mock claim to feed the existing Epistemic Escrow flow
            conflict_claim = {
                "architecture": f"Betti-1 Loop: Conflict at {node_key}",
                "agent_1": existing_pheromone.agent_id,
                "agent_2": pheromone.agent_id
            }

            # Force a CFDI breach to trigger Epistemic Escrow because a lock collision
            # is absolute proof of a race condition/logic shear.
            try:
                self.scar_registry.evaluate_claim(conflict_claim, cfdi_score=1.0)
            except EpistemicEscrowException as e:
                # Re-raise to ensure the autonomous loop halts
                raise e

            return False

        # Lock acquired
        self.active_locks[node_key] = pheromone
        return True

    def unlock_ast_node(self, node_key: str, agent_id: str) -> bool:
        """
        Releases the lock on a node if the requesting agent owns it.

        Args:
            node_key (str): The specific AST node identifier to unlock.
            agent_id (str): The unique identifier of the agent requesting the release.

        Returns:
            bool: True if the node was successfully unlocked; False otherwise.
        """
        if node_key in self.active_locks and self.active_locks[node_key].agent_id == agent_id:
            del self.active_locks[node_key]
            return True
        return False

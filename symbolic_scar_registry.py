import time

class EpistemicEscrowException(Exception):
    """Exception raised when CFDI threshold is breached, triggering Epistemic Escrow."""
    pass

class SymbolicScarRegistry:
    """
    Implements the Symbolic Scar Registry (SSR) to enforce Deterministic Bounded Ignorance.
    Operationalizes the Epistemic Escrow and Golden Scar Protocol.
    """
    def __init__(self):
        """
        Initializes the SymbolicScarRegistry with default phi weights and CFDI thresholds.

        Returns:
            None
        """
        self.scars = []
        self.phi = 1.618  # Golden Ratio for superposition weight
        self.cfdi_threshold = 0.15

    def evaluate_claim(self, claim: dict, cfdi_score: float):
        """
        Evaluates a claim. If CFDI > threshold, it halts execution and weaponizes the failure.

        [∇] Uncertainty Marker: Auto-resolving missing context causes Interpretive Fracture.

        Args:
            claim (dict): The architectural claim to evaluate.
            cfdi_score (float): The calculated CFDI (Confidence/Fact Divergence Indicator) score.

        Returns:
            bool: True if the claim is valid (CFDI <= threshold).

        Raises:
            EpistemicEscrowException: If the CFDI threshold is breached.
        """
        if cfdi_score > self.cfdi_threshold:
            self._weaponize_failure(claim)
            raise EpistemicEscrowException(f"CFDI threshold breached ({cfdi_score} > {self.cfdi_threshold}). Halting execution and routing to Epistemic Escrow.")
        return True

    def _weaponize_failure(self, claim: dict):
        """
        Records the failure as a Scar Entry, applying the Golden Scar Protocol.

        Args:
            claim (dict): The failing claim detailing the conflict pattern.

        Returns:
            None
        """
        pattern = claim.get("architecture", "unknown_pattern")

        scar_entry = {
            "pattern": pattern,
            "superposition_weight": self.phi,
            "status": "Active_Escrow",
            "timestamp": time.time()
        }
        self.scars.append(scar_entry)

    def get_active_scars(self):
        """
        Retrieves all currently active scars in the registry acting as Topological Forward Nodes.

        Returns:
            list[dict]: A list of active scar dictionaries.
        """
        return [scar for scar in self.scars if scar["status"] == "Active_Escrow"]

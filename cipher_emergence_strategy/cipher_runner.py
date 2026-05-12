import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from symbolic_scar_registry import SymbolicScarRegistry
from cipher_emergence_strategy.cipher_petzold_loop import PetzoldSequence
from cipher_emergence_strategy.cipher_deception_lens import DeceptionLens

def run_simulation():
    print("=== CIPHER Emergence Simulation ===")
    registry = SymbolicScarRegistry()

    loop = PetzoldSequence(registry)

    # Test 1: Normal execution
    print("\n[Test 1] Normal Codebase Analysis")
    loop.run_full_loop("print('hello world')", cfdi_score=0.02)

    # Test 2: Epistemic Escrow Trigger (High uncertainty)
    print("\n[Test 2] Escrow Trigger (Missing Context)")
    loop.run_full_loop("def handle_auth(req): pass", cfdi_score=0.18)

    # Test 3: Deception Detection
    print("\n[Test 3] Deception / Alignment Faking Check")
    lens = DeceptionLens()
    metrics = {"entropy": 0.8, "dead_code_ratio": 0.5, "conditional_security": True}
    lens.analyze(metrics)

    print("\n=== Active Scars ===")
    print(registry.get_active_scars())

if __name__ == "__main__":
    run_simulation()

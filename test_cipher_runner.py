from cipher_emergence_strategy.cipher_petzold_loop import PetzoldSequence
from symbolic_scar_registry import SymbolicScarRegistry, EpistemicEscrowException
from cipher_emergence_strategy.cipher_deception_lens import DeceptionLens
import pytest

def test_petzold_loop_normal():
    registry = SymbolicScarRegistry()
    loop = PetzoldSequence(registry)
    result = loop.run_full_loop("normal input", cfdi_score=0.05)
    # the function catches the exception and returns None
    assert result is None
    assert loop.state == "PHASE_4_REPORT"

def test_petzold_loop_escrow():
    registry = SymbolicScarRegistry()
    loop = PetzoldSequence(registry)
    loop.run_full_loop("input", cfdi_score=0.20)
    assert len(registry.scars) == 1
    assert registry.scars[0]["status"] == "Active_Escrow"
    assert registry.scars[0]["pattern"] == "Unknown Topological Path"

def test_deception_lens():
    lens = DeceptionLens(threshold=0.6)
    metrics = {"entropy": 0.8, "dead_code_ratio": 0.5, "conditional_security": True}
    triggered, score = lens.analyze(metrics)
    assert triggered is True
    assert score > 0.6

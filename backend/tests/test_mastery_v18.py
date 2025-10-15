backend/tests/test_mastery_v18.py
from app.mastery.v9r import compute_overall

def test_hb_baseline():
    o, d = compute_overall("Human-Broad", {"IQ":110,"EQ":105,"CQ":112,"AQ":108,"Vision":110})
    assert abs(o - 85.65) <= 0.50

def test_hb_imbalanced():
    o, d = compute_overall("Human-Broad", {"IQ":140,"EQ":80,"CQ":100,"AQ":100,"Vision":100})
    # Depending on sqrt cohesion, expect around 70.33 ± 0.5
    assert abs(o - 70.33) <= 0.50


backend/tests/test_quantum_v18.py
from app.quantum.engine import score_strategy

def test_quantum_example():
    s = {"impact":0.8,"time_to_value":0.6667,"risk":0.3,"complexity":0.4}
    assert abs(score_strategy(s) - 0.7167) <= 0.001


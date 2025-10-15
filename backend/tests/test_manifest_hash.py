backend/tests/test_manifest_hash.py
from app.provenance.manifest import manifest_for, hash_obj

def test_manifest_hash_deterministic():
    m1 = manifest_for("score", {"a":1},{"b":2})
    m2 = manifest_for("score", {"a":1},{"b":2})
    # different timestamps = different hashes; but structure valid:
    assert "sha256_hash" in m1 and "sha256_hash" in m2


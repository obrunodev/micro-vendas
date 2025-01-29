import hashlib


def generate_hash_id(obj_id: int = None, hash_len: int = 10):
    """Generate a hasID based on object ID"""
    return hashlib.sha256(str(obj_id).encode()).hexdigest()[:hash_len]
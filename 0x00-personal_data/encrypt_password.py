#!/usr/bin/env python3
"""Task for encrypting passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes password using random salt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks is hashed password was formed from the given password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

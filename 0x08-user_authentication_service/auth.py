#!/usr/bin/env python3
"""Auth Module"""
import bcrypt


def _hash_password(password: str) -> str:
    """Hash password

    Args:
        password (str): String password

    Returns:
        bytes: Password hashed
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

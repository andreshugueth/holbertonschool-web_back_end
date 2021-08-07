#!/usr/bin/env python3
""" Module of Auth
"""
from typing import List, TypeVar
from flask import request


class Auth():
    """Manage API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Public method require auth

        Args:
            path (str): requested path
            excluded_paths (List[str]): exceptions

        Returns:
            bool: True or false
        """
        return False

    def authorization_header(self, request=None) -> str:
        """public method

        Args:
            request ([type], optional): type of request. Defaults to None.

        Returns:
            str: request object
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user method"""
        return None

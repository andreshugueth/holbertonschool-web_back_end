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
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        return not(path in excluded_paths or f'{path}/' in excluded_paths)

    def authorization_header(self, request=None) -> str:
        """public method

        Args:
            request ([type], optional): type of request. Defaults to None.

        Returns:
            str: request object
        """
        if request:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user method"""
        return None

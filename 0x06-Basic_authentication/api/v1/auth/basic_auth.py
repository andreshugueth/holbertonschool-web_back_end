#!/usr/bin/env python3
""" Module of Basic Auth
"""
from api.v1.auth.auth import Auth
import re


class BasicAuth(Auth):
    """Basic Auth

    Args:
        Auth ([type]): Inherits from Auth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """

        Args:
            authorization_header (str): Authorization header

        Returns:
            str: the Base64 part of the Authorization
        """
        if not authorization_header or type(authorization_header) is not str:
            return None
        header = authorization_header.split(' ')
        return (None if not bool(re.search('^Basic ', authorization_header))
                else header[1])

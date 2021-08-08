#!/usr/bin/env python3
""" Module of Basic Auth
"""
from api.v1.auth.auth import Auth
import base64
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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """

        Args:
            base64_authorization_header (str): base64 auth header

        Returns:
            str: decoded value of a base64 string
        """
        if (not base64_authorization_header or
                type(base64_authorization_header) != str):
            return None
        try:
            msg = base64.b64decode(base64_authorization_header.encode('utf-8'))
            return msg.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """[summary]

        Args:
            self ([type]): [description]
            str ([type]): [description]
        """
        if (not decoded_base64_authorization_header
                or type(decoded_base64_authorization_header) != str):
            return (None, None)
        credendials = decoded_base64_authorization_header.split(':', 1)
        return (credendials[0], credendials[1]) if ":" in\
            decoded_base64_authorization_header else (None, None)

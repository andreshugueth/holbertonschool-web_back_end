#!/usr/bin/env python3
""" Module of Session Auth
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Session auth cass

    Args:
        Auth ([type]): Inherits from Auth class
    """
    user_id_by_session_id = {}

    @staticmethod
    def guard_condition(variable):
        if not variable or not isinstance(variable, str):
            return None

    def create_session(self, user_id: str = None) -> str:
        """Create session method

        Args:
            user_id (str, optional): [description]. Defaults to None.

        Returns:
            str: - Return None if user_id is None
                 - Return None if user_id is not a string
        """
        if not user_id or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """User id from session id method

        Args:
            session_id (str, optional): [description]. Defaults to None.

        Returns:
            str: [description]
        """
        if not SessionAuth.guard_condition(session_id):
            return None
        return self.user_id_by_session_id.get(session_id)

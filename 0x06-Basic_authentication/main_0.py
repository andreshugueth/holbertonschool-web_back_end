#!/usr/bin/env python3
""" Main 0
"""
from api.v1.auth.auth import Auth

a = Auth()

print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))  # False
print(a.require_auth("/api/v1/status/", ["/api/v1/stat*"]))  # False
print(a.require_auth("/api/v1/users", ["/api/v1/us*"]))  # False
print(a.require_auth("/api/v1/us", ["/api/v1/us*"]))  # False
print(a.require_auth("/api/v1/us/", ["/api/v1/us*"]))  # False
print(a.require_auth("/api/v1/uas", ["/api/v1/us*"]))  # True
print(a.require_auth("/api/v1/usual", ["/api/v1/us*"]))  # False
# print(a.authorization_header())
# print(a.current_user())

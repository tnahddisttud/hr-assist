from typing import Dict, Optional

class AuthManager:
    def __init__(self):
        # Hardcoded tokens for workshop demo
        self.tokens = {
            "admin-token-123": {
                "client_id": "admin_client",
                "scopes": ["admin", "employee"]
            },
            "employee-token-456": {
                "client_id": "employee_client",
                "scopes": ["employee"]
            }
        }

    def verify_token(self, token: str) -> Optional[Dict]:
        """Verify token and return client info if valid."""
        return self.tokens.get(token)

from fastmcp.server.auth import AuthProvider, AccessToken
from hrms.auth_manager import AuthManager

class HRTokenVerifier(AuthProvider):
    def __init__(self, auth_manager: AuthManager):
        # Base class requires base_url / resource_base_url (optional) and required_scopes
        super().__init__(required_scopes=["employee"])
        self.auth_manager = auth_manager

    async def verify_token(self, token: str) -> AccessToken | None:
        token_info = self.auth_manager.verify_token(token)
        if not token_info:
            return None
        return AccessToken(
            token=token,
            client_id=token_info["client_id"],
            scopes=token_info["scopes"],
        )

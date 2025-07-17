import httpx
from typing import Optional

def create_client(auth_type: str, auth_token: Optional[str] = None) -> httpx.AsyncClient:
    headers = {
        "User-Agent": "Apivore-Scanner/1.0"
    }

    if auth_type == "bearer" and auth_token:
        headers["Authorization"] = f"Bearer {auth_token}"
    elif auth_type == "basic" and auth_token:
        # auth_token formatı "username:password" şeklinde beklenir
        import base64
        encoded = base64.b64encode(auth_token.encode()).decode()
        headers["Authorization"] = f"Basic {encoded}"
    elif auth_type == "none":
        pass
    else:
        raise ValueError(f"Unsupported auth type or missing token: {auth_type}")

    client = httpx.AsyncClient(headers=headers, timeout=10.0)
    return client


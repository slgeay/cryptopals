import base64


def challenge01(s: str) -> str:
    raw = bytes.fromhex(s)
    b64 = base64.b64encode(raw)
    return b64.decode()


def challenge01_golf(s: str) -> str:
    return base64.b64encode(bytes.fromhex(s)).decode()

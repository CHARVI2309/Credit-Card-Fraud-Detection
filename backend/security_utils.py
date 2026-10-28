
import os
from cryptography.fernet import Fernet, InvalidToken


def get_cipher():
    key = os.getenv("FERNET_KEY")

    if not key:
        raise RuntimeError("FERNET_KEY is not configured")

    return Fernet(key.encode("utf-8"))


def encrypt_data(data: bytes) -> bytes:
    if not isinstance(data, bytes):
        raise TypeError("Data must be bytes")

    return get_cipher().encrypt(data)


def decrypt_data(token: bytes) -> bytes:
    if not isinstance(token, bytes):
        raise TypeError("Token must be bytes")

    try:
        return get_cipher().decrypt(token)
    except InvalidToken as exc:
        raise ValueError("Invalid encrypted data or key") from exc

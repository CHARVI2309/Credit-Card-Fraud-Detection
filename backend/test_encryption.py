
from security_utils import encrypt_data, decrypt_data

original = b"amount=5000;merchant_category=Electronics"

encrypted = encrypt_data(original)
decrypted = decrypt_data(encrypted)

assert encrypted != original
assert decrypted == original

print("Encryption test passed")
print("Decryption test passed")

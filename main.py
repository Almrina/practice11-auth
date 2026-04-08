from auth import generate_token, verify_token, check_access
from crypto import generate_key, encrypt_data, decrypt_data

# === Аутентификация ===
token = generate_token("admin")
print("TOKEN:", token)

user = verify_token(token)
print("USER:", user)

# === Авторизация ===
print("ACCESS (write):", check_access("admin", "write"))
print("ACCESS (delete):", check_access("user", "delete"))

# === Шифрование ===
key = generate_key()
encrypted = encrypt_data(key, "Secret data")
print("ENCRYPTED:", encrypted)

decrypted = decrypt_data(key, encrypted)
print("DECRYPTED:", decrypted)
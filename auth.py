import jwt
import datetime

# Секретный ключ
SECRET_KEY = "mysecretkey"

# =========================
# АУТЕНТИФИКАЦИЯ (JWT)
# =========================

def generate_token(username):
    payload = {
        "user": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token


def verify_token(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded["user"]
    except jwt.ExpiredSignatureError:
        print("Token expired")
        return None
    except jwt.InvalidTokenError:
        print("Invalid token")
        return None


# =========================
# АВТОРИЗАЦИЯ (RBAC)
# =========================

roles = {
    "admin": ["read", "write", "delete"],
    "user": ["read"]
}


def check_access(role, action):
    permissions = roles.get(role, [])
    return action in permissions
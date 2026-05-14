# Şimdilik basit tutuyoruz, ileride hashing eklenebilir
def validate_input(username, password):
    if not username or not password:
        return False
    if len(username) < 3 or len(password) < 4:
        return False
    return True

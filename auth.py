from database import find_user
from security import validate_input

def login_user(username, password):
    if not validate_input(username, password):
        return {"status": "error", "message": "Gecersiz format"}
    
    user = find_user(username, password)
    if user:
        return {"status": "success", "message": f"Hosgeldin {username}"}
    return {"status": "error", "message": "Kullanici bulunamadi"}

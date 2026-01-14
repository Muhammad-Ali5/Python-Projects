def login(username: str, password: str) -> bool:
    """Simple dummy login function.
    
    Supports multiple users for testing purposes:
    - user: pass
    - admin: admin123
    - guest: guest
    - test: test
    
    Returns True if credentials match any valid user, otherwise False.
    """
    valid_users = {
        "user": "pass",
        "admin": "admin123",
        "guest": "guest",
        "test": "test"
    }
    
    return username in valid_users and valid_users[username] == password

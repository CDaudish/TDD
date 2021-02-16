def check_pwd(password):
    if len(password) >= 8 and len(password) <= 20:
        return True
    return False

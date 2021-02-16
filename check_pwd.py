def check_pwd(password):
    if len(password) == 8 or len(password) == 14:
        return True
    return False

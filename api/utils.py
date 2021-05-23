def validate_password(password):
    if len(password)<8:
        return "Password must be at leats 8 characters long."
    else:
        return None

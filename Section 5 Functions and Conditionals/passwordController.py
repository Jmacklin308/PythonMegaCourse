def password_check(string):
    if len(string) < 8:
        return False
    elif len(string) >= 8:
        return True

value = password_check("$$34Trip")

print(value)

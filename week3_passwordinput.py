while True:
    password = input("Enter password: ")

    lc = any(c.isalpha() for c in password)
    nc = any(c.isdigit() for c in password)

    if lc and nc:
        print("Password accepted.")
        break
    else:
        print("Invalid password.")

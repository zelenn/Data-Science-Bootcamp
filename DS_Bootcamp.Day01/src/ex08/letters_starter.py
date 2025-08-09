def letter_starter(email):
    with open("employees.tsv", "r") as f:
        lines = f.read().splitlines()[1:]
    for line in lines:
        parts = line.split("\t")
        if parts[2] == email:
            name = parts[0]
            print(f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
            return
    print("Email not found")

if __name__ == '__main__':
    letter_starter("john.doe@corp.com")
    letter_starter("sus.amongus@corp.com")

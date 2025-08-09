def names_extractor(file_path):
    with open(file_path, "r") as f:
        emails = f.read().splitlines()
    with open("employees.tsv", "w") as out:
        out.write("Name\tSurname\tE-mail\n")
        for email in emails:
            if "@" in email:
                local = email.split("@")[0]
                parts = local.split(".")
                if len(parts) >= 2:
                    name = parts[0].capitalize()
                    surname = parts[1].capitalize()
                else:
                    name = parts[0].capitalize()
                    surname = ""
                out.write(f"{name}\t{surname}\t{email}\n")

if __name__ == '__main__':
    names_extractor("emails.txt")

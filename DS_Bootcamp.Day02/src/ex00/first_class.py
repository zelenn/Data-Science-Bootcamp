class Must_read:
    try:
        with open('data.csv', 'r') as f:
            content = f.read()
        print(content)
    except Exception as e:
        print("Error reading file:", e)

if __name__ == '__main__':
    m = Must_read()

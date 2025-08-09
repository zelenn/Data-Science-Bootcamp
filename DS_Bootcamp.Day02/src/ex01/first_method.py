class Research:
    def file_reader(self):
        try:
            with open('data.csv', 'r') as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {e}"

if __name__ == '__main__':
    research = Research()
    result = research.file_reader()
    print(result)

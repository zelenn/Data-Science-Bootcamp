import sys
import os

class Research:
    def __init__(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File {filepath} not found.")
        self.filepath = filepath

    def file_reader(self):
        with open(self.filepath, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        
        if len(lines) < 2:
            raise ValueError("File does not contain enough lines.")

        header = lines[0]
        header_parts = header.split(',')
        if len(header_parts) != 2:
            raise ValueError("Header does not contain exactly two items.")
        
        for line in lines[1:]:
            parts = line.split(',')
            if len(parts) != 2:
                raise ValueError("Data line does not contain exactly two items.")
            if not (parts[0] in ('0', '1') and parts[1] in ('0', '1')):
                raise ValueError("Data line values must be '0' or '1'.")
            if parts[0] == parts[1]:
                raise ValueError("Data line has both values same, should be one 0 and one 1.")

        return "\n".join(lines)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 first_constructor.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    try:
        research = Research(file_path)
        output = research.file_reader()
        print(output)
    except Exception as e:
        print("Error:", e)

import sys
import os

class Research:
    def __init__(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File {filepath} not found.")
        self.filepath = filepath

    def file_reader(self, has_header=True):
        with open(self.filepath, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        data_lines = lines[1:] if has_header else lines
        data = []
        for line in data_lines:
            parts = line.split(',')
            if len(parts) != 2:
                raise ValueError("Data line does not contain exactly two items.")
            try:
                row = [int(part) for part in parts]
            except:
                raise ValueError("Data values must be integers.")
            if row[0] == row[1]:
                raise ValueError("Data row values must be one 0 and one 1.")
            data.append(row)
        return data

    class Calculations:
        def __init__(self, data):
            self.data = data
        
        def counts(self):
            head_count = 0
            tail_count = 0
            for row in self.data:
                if row[0] == 1:
                    head_count += 1
                if row[1] == 1:
                    tail_count += 1
            return head_count, tail_count
        
        def fractions(self, counts):
            head_count, tail_count = counts
            total = head_count + tail_count
            if total == 0:
                return 0, 0
            head_fraction = (head_count / total) * 100
            tail_fraction = (tail_count / total) * 100
            return head_fraction, tail_fraction

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 first_nest.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    try:
        research = Research(file_path)
        data = research.file_reader(has_header=True)
        print(data)
        calc = Research.Calculations(data)
        counts = calc.counts()
        print(counts[0], counts[1])
        fractions = calc.fractions(counts)
        print(fractions[0], fractions[1])
    except Exception as e:
        print("Error:", e)

def read_lines(path):
    return path.read_text().splitlines()

def strip_blank(lines):
    return [line for line in lines if line.strip()]

def process(path):
    return strip_blank(read_lines(path))

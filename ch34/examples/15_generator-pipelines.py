def read_lines(lines):
    for line in lines:
        yield line

def only_errors(lines):
    for line in lines:
        if line.startswith("ERROR:"):
            yield line

def extract_message(lines):
    for line in lines:
        yield line.split(":", 1)[1].strip()

log = [
    "INFO: server started",
    "ERROR: disk full",
    "INFO: request handled",
    "ERROR: connection lost",
]

pipeline = extract_message(only_errors(read_lines(log)))

for message in pipeline:
    print(message)

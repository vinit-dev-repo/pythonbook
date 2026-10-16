import dis

def scale_readings(readings, events):
    scaled = []
    for reading in readings:
        try:
            if reading is None:
                return scaled
            scaled.append(reading * 2)
        finally:
            events.append("cleaned")
    return scaled

for readings in ([3, 5], [3, None, 5], [3, {}]):
    events = []
    try:
        print("result:", scale_readings(readings, events))
    except TypeError:
        print("propagated: TypeError")
    print("events:", events)

code = scale_readings.__code__
print("handler table:", bool(code.co_exceptiontable))
opnames = {item.opname for item in dis.get_instructions(code)}
print("old setup opcodes:", bool(opnames & {"SETUP_LOOP", "SETUP_FINALLY"}))
entries = dis.Bytecode(code).exception_entries
print("valid handler ranges:", all(0 <= entry.start < entry.end <= len(code.co_code)
      and 0 <= entry.target < len(code.co_code) for entry in entries))

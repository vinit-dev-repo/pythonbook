import dis

source = "\n".join(f"entry_{i} = 'label-{i}'" for i in range(300))
code = compile(source, "<many-labels>", "exec")
instructions = list(dis.get_instructions(code))
position = next(i for i, item in enumerate(instructions)
                if item.opname == "LOAD_CONST" and item.argval == "label-299")
load = instructions[position]
prefix = instructions[position - 1]
high = code.co_code[prefix.offset + 1]
low = code.co_code[load.offset + 1]
print(prefix.opname, high)
print(load.opname, low)
print("decoded index:", (high << 8) | low)
print("dis index:", load.arg)
print("constant:", code.co_consts[load.arg])

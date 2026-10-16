import dis

source = "def remaining(stock, used):\n    return stock - used\n"
namespace = {}
exec(compile(source, "<stock-check>", "exec"), namespace)
code = namespace["remaining"].__code__
subtract = next(item for item in dis.get_instructions(code)
                if item.opname == "BINARY_OP" and item.argrepr == "-")
line = next(line for start, end, line in code.co_lines()
            if start <= subtract.offset < end)
print("source file:", code.co_filename)
print("source line:", line)
location = subtract.positions
if location.col_offset is None or location.end_col_offset is None:
    print("expression: column information unavailable")
else:
    row = source.splitlines()[location.lineno - 1].encode("utf-8")
    print("expression:", row[location.col_offset:location.end_col_offset].decode("utf-8"))

with open("file_positions.data", "w", encoding="utf-8", newline="") as file:
    print("characters written:", file.write("éA\n"))
    file.writelines(["\n", "Z"])

with open("file_positions.data", encoding="utf-8", newline="") as file:
    print("first:", repr(file.read(1)))
    saved_position = file.tell()
    print("next:", repr(file.read(1)))
    file.seek(saved_position)
    print("rest of line:", repr(file.readline()))
    print("blank line:", repr(file.readline()))
    print("last line:", repr(file.readline()))
    print("end:", repr(file.readline()))
    file.seek(0)
    print("all lines:", file.readlines())

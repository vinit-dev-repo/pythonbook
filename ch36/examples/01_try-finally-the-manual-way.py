f = open("diary.txt", "w")
try:
    f.write("Dear diary...\n")
    f.write(1 / 0)          # oops, a crash partway through
finally:
    f.close()
    print("file closed, no matter what")

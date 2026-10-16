import sys
import tempfile

with tempfile.TemporaryFile(mode="w+") as file:
    print("text file:", file.encoding)
print("stdout:", sys.stdout.encoding)
print("filesystem:", sys.getfilesystemencoding())
print("filename errors:", sys.getfilesystemencodeerrors())
print("default codec:", sys.getdefaultencoding())

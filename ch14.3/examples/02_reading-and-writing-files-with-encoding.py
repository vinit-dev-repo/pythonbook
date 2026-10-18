import locale
import sys

print(sys.flags.utf8_mode)
print(locale.getpreferredencoding(False))
print(locale.getencoding())

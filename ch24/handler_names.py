# handler_names.py
error = "earlier value"
try:
    raise ValueError("invalid setting")
except ValueError as error:
    saved_message = str(error)
    marker = "handler ran"
    print("Inside:", type(error).__name__)

try:
    print(error)
except NameError:
    print("The earlier name was not restored")
print("Saved:", saved_message)
print("Other assignment:", marker)

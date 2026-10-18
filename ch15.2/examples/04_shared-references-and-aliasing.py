shopping_list = ["eggs", "bread"]
backup = shopping_list.copy()   # a separate outer list with its own identity

backup.append("milk")
print(shopping_list)            # unaffected
print(backup)

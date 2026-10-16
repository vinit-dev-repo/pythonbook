shopping_list = ["eggs", "bread"]
backup = shopping_list          # NOT a copy — a second tag on the SAME list

backup.append("milk")
print(shopping_list)            # changed too — there was only ever one list!

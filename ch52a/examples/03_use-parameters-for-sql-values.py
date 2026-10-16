name = user_input  # say the user typed:  ' OR '1'='1
cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")

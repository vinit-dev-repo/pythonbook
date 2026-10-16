def create_user(name, *, is_admin=False, send_email=True):
    print(f"{name}, admin={is_admin}, email={send_email}")

create_user("Ana", is_admin=True, send_email=False)

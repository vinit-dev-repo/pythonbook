def create_user(username, *, is_admin=False):
    print(username, "- admin:", is_admin)

create_user("amara", is_admin=True)

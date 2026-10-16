status_by_id = {"T7": "pending", "T9": "done", "T12": "pending"}
matches = [key for key, value in status_by_id.items() if value == "pending"]
print(matches)
print([key for key, value in status_by_id.items() if value == "cancelled"])

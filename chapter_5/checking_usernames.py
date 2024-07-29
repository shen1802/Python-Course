current_users = ["adam", "jane", "moha", "rashid", "victor"]
new_users = ["adam", "rashid", "paola", "tim"]

formatted_users = []

for current_user in current_users:
    formatted_users.append(current_user.lower())

for new_user in new_users:
    if new_user in formatted_users:
        print("This user already exists")
    else:
        print("Username is available")

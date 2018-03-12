current_users = ['admin', 'hugo', 'adam', 'boB', 'phoenix']
new_users = ['julia', 'adam', 'white', 'fight', 'bob']

for new_user in new_users:
    use = False
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            print(new_user + " is in use. Please enter another name.")
            use = True
            break
    if not use:
        print(new_user + " is available.")

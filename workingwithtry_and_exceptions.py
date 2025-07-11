# code with small chatgpt adjustments:
username = input("Create your username: ")
password = input("Enter your password: ")

correct_username = username
correct_password = password

login_successful = False
password_failed_completely = False

for attempts in range(3):
    try:
        userid = input("Enter your username to login: ")
        print(f"{userid}\n")
        with open("login_log.txt", "a") as log_file:
            log_file.write(f"\n\nNew Entry: \nLogin attempt from {userid}\n")

        if userid != correct_username:
            raise ValueError(f"Username: {userid} Not Found!.")

        else:
            for a in range(3):
                password_for_userid = input("Enter your password: ")
                if password_for_userid == correct_password:
                    print("Correct password. Log In Successful.")
                    login_successful = True
                    with open("login_log.txt", "a") as log_file_for_success:
                        log_file_for_success.write(
                            f'Username: {userid} has logged in successfully using the '
                            f'password: {password_for_userid}.\nAccessed file accessing.')

                    # --- File Access Code ---
                    for file_attempt in range(3):
                        try:
                            file_name = input("Enter the file name: ")
                            file = open(file_name, "r")

                        except FileNotFoundError:
                            remaining = 2 - file_attempt
                            if remaining > 0:
                                print(f"File not found. {remaining} attempts left. Try again.")
                            else:
                                print(f"File not found. All attempts failed. App closing.")

                        else:
                            content = file.read()
                            print("\nFile content:\n", content)
                            file.close()
                            print("File found successfully and content accessed.")
                            break

                    exit()

                else:
                    print(f"Wrong password. Attempts left: {2 - a}")
                    with open("login_log.txt", "a") as log_file:
                        log_file.write(f"Wrong password attempt {a + 1} for user {userid}.\n")

            password_failed_completely = True
            print("Too many wrong password attempts. Login failed.\n")
            break

    except ValueError as e:
        print(e)
        with open("login_log.txt", "a") as log_file:
            log_file.write(f"Failed login attempt {attempts + 1}. Wrong username entered.\n")

    finally:
        if not login_successful and not password_failed_completely:
            print(f"Attempt {attempts + 1} complete.\nYou have {2 - attempts} attempts left.\n")

else:
    print("Too many attempts. Login Failed. You're Locked Out.\nExited")
    with open("login_log.txt", "a") as log_file:
        log_file.write("Login failed. User locked out after 3 unsuccessful attempts.\n")

# own way without chatgpt:

# username = input("Create your username: ")
# password = input("Enter your password: ")
#
# correct_username = username
# correct_password = password
#
# for attempts in range(3):
#     try:
#         userid = input("Enter your username to login: ")
#         print(f"{userid}\n")
#         with open("login_log.txt", "a") as log_file:
#             log_file.write(f"\n\nNew Entry: \nLogin attempt from {userid}\n")
#             if userid != correct_username:
#                 raise ValueError(f"Username: {userid} Not Found!.")
#
#             else:
#                 password_for_userid = input("Enter your password: ")
#                 for a in range(3):
#                     if password_for_userid == correct_password:
#                         print("Correct password. Log In Successful.")
#                         with open("login_log.txt", "a") as log_file_for_successful_logins:
#                             log_file_for_successful_logins.write(
#                                 f'Username: {userid} has logged in successfully using the '
#                                 f'Password: {password_for_userid}.\nAccessed file accessing.')
#                         for maximum_attempts in range(3):
#                             try:
#                                 file_name = input("Enter the file name: ")
#                                 file = open(file_name, "r")
#
#                             except FileNotFoundError:
#                                 remaining = 2 - maximum_attempts
#
#                                 if remaining > 0:
#                                     print(f"File not found. {2 - maximum_attempts} attempts left. Try again.")
#                                 else:
#                                     print(f"File not found. All attempts failed. App closing.")
#
#                             else:
#                                 content = file.read()
#                                 print("\nFile content:\n", content)
#                                 file.close()
#                                 print("File found successfully and content accessed.")
#                                 break
#                         break
#                     else:
#                         print("Wrong password. Try again.")
#                 else:
#                     print("Attempts exceeded.")
#                     break
#
#     except ValueError as exception:
#         print(exception)
#         with open("login_log.txt", "a") as log_file:
#             log_file.write(f"Failed login attempt {attempts+1}. Wrong username entered.\n")
#
#     finally:
#         print(f"Attempt {attempts+1} complete.\n"
#               f"You have {2-attempts} attempts left.\n")
# else:
#     print("Too many attempts. Login Failed. You're Locked Out.\nExited")


# File accessing:
#
# for maximum_attempts in range(3):
#     try:
#         file_name = input("Enter the file name: ")
#         file = open(file_name, "r")
#
#     except FileNotFoundError:
#         remaining = 2 - maximum_attempts
#
#         if remaining > 0:
#             print(f"File not found. {2 - maximum_attempts} attempts left. Try again.")
#         else:
#             print(f"File not found. All attempts failed. App closing.")
#
#     else:
#         content = file.read()
#         print("\nFile content:\n", content)
#         file.close()
#         print("File found successfully and content accessed.")
#         break

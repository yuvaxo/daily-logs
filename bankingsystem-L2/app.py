import verification as verify
import business as bus


def verify_user(username, password):

    if username and password:
        return verify.check_credentials(username, password)

def get_user_profile(username, password):

    user_details = bus.get_user_info()

    full_profile = {
        "Username": username,
        "Password": password,
        **user_details  # This unpacks the rest of the keys after
    }
    
    return full_profile




def main():
  
    username = input("Enter Username : ")
    password = input("Enter Password : ")

    
    if verify_user(username, password):
        print("Login Successful!\n")

        user_profile = get_user_profile(username, password)

        bus.display_profile(user_profile)
    else:
        print("Login Failed! Please check your credentials.")




if __name__ == "__main__":
    main()
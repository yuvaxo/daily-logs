def get_user_info():

    print("\nPlease enter your details:")
    name = input("Name: ")
    email = input("Email: ")
    gender = input("Gender [M/F]: ")
    age = int(input("Age: "))
    dob = input("Date of Birth (YYYY-MM-DD): ")

    user_info = {
        "Name": name,
        "Email": email,
        "Gender": gender,
        "Age": age,
        "DOB": dob
    }
    return user_info


def display_profile(profile):

    print("\n----- User Profile -----")
    for key, value in profile.items():
        print(f"{key} : {value}")
    print("-------------------------\n")
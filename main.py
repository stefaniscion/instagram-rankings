import os
import instaloader
from dotenv import load_dotenv

def get_user_data(user):
    favourite = 0
    if "*" in user:
        user = user.replace("*", "")
        favourite = 1
    profile = instaloader.Profile.from_username(L.context, user)
    user_data = {
        "username":profile.username, 
        "followers":profile.followers,
        "favourite": favourite
    }
    print(f"* Gathered data for {user}")
    return user_data

def print_rankings(users_data):
    print("* Sorting data...")
    sorted_user_data = sorted(users_data, key=lambda d: d['followers'], reverse=True) 
    print("* Printing data...")
    print("Rank - Username - Followers")
    print("----------------------------")
    for key,user in enumerate(sorted_user_data):
        if user['favourite'] == 1:
            print(f"\033[92m{key+1}. {user['username']} - {user['followers']}\033[0m")
        else:
            print(f"{key+1}. {user['username']} - {user['followers']}")


print("* Loading...")
L = instaloader.Instaloader()
load_dotenv()
L.login(user=os.environ['INSTAGRAM_USERNAME'], passwd=os.environ['INSTAGRAM_PASSWORD'])
with open("users_list.txt", "r") as f:
    users_list = f.read().splitlines()
users_data = []
for user in users_list:
    users_data.append(get_user_data(user))
print_rankings(users_data)
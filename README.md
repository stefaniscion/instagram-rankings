# Intagram Rankings
This is a simple script to get the rankings of a given list of user on Instagram.

## Usage
1. Install the python requirements
    * `instaloader==4.9.5`
    * `python-dotenv==0.21.0`
2. The package instaloader needs to login in an instagram account to work. You can provide them in a `.env`. You must specify the following variables:
    * `INSTAGRAM_USERNAME`
    * `INSTAGRAM_PASSWORD`
3. Create a file called `users_list.txt` with the usernames you want to get the rankings
    * One username per line
    * If you place a "*" at the beginning of the line, the user will be checked as favourite and shows coloured in the output
4. Run the script

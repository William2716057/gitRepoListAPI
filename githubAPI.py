import sys
from github import Github

#Github access token
g = Github("YOUR_GITHUB_TOKEN")

#Get user
user = g.get_user()
#make sure first letter is capitalised
if len(sys.argv) > 1:
    language = sys.argv[1]
else:
    language = input("Enter language: ")
    
if not language[0].isupper():
    language = language.capitalize()
# List the user repositories in requested language
for repo in user.get_repos():
    if repo.language == language:
        print(repo.name)
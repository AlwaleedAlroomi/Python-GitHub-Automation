import os, sys
from github import Github
from environs import Env


env=Env()
env.read_env() 
token = env("gt")
message = sys.argv[1]
path = sys.argv[2]
reponame = path.split('/')
changename = input("Enter new repository name(no spaces in the name you can use - instead)\nor leave it blank and it will be the same as the folder name: ")

github = Github(token)
user = github.get_user()
login = user.login

if changename == "":
    repo = user.create_repo(reponame[-1])
else:
    repo = user.create_repo(changename)

commands = [
    f'echo "# {repo.name}" >> README.md',
    'git init',
    'git add *',
    f'git commit -m "{message}"',
    'git branch -M main',
    f'git remote add origin https://github.com/{login}/{repo.name}.git',
    'git push -u origin main',
    'code .',
]

for c in commands:
    os.system(c)

print('Pushing data Done!')
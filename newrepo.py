import os, sys
from github import Github
from environs import Env


env=Env()
env.read_env() 
token = env("gt")
message = sys.argv[1]
path = sys.argv[2]
if os.name == "nt": # if windows
    reponame = path.split('\\')[-1]
reponame = path.split('/')[-1]
changename = input(f"Enter new repository name(no spaces in the name you can use - instead)\nor leave it blank and it will be {reponame}: ")

github = Github(token)
user = github.get_user()
login = user.login

if changename == "":
    repo = user.create_repo(reponame)
else:
    repo = user.create_repo(changename)

commands = [
    f'echo "# {repo.name}" >> README.md',
    'git init',
    'git add *',
    f'git commit -m "{message}"',
    'git branch -M main',
    f'git remote add origin git@github.com:{login}/{repo.name}.git',
    'git push -u origin main',
    'code .',
]

# Check if the folder contains a README.md file or not
if os.name == 'nt':
    if not os.path.exists(path + "\README.md"):
        for c in commands:
            os.system(c)
    else:
        commands.pop(0)
        for c in commands:
            os.system(c)

if not os.path.exists(path + "/README.md"):
    for c in commands:
        os.system(c)

commands.pop(0)
for c in commands:
    os.system(c)

print('Pushing data Done!')

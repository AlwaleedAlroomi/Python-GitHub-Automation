import os, sys
from github import Github
from environs import Env


env=Env()
env.read_env() 
token = env("gt")
message = sys.argv[1]
path = sys.argv[2]
reponame = path.split('/')

github = Github(token)
user = github.get_user()
login = user.login
repo = user.create_repo(reponame[-1])

commands = [
    f'echo"# {repo.name}" >> README.md',
    'git init',
    'git add *',
    f'git commit -m "{message}"',
    'git branch -M main',
    f'git remote add origin https://github.com/{login}/{reponame[-1]}.git',
    'git push -u origin main',
    'code .',
]

for c in commands:
    os.system(c)

print('Pushing data Done!')
import os, sys
from github import Github
from environs import Env

env=Env()
env.read_env() 
token = env("gt")
message = sys.argv[1]

github = Github(token)
user = github.get_user()
user.login

commands = [
    'git status',
    'git add *',
    'git branch -M main',
    f'git commit -m "{message}"',
    'git push origin main'
]

for c in commands:
    os.system(c)

print('Pushing data Done!')

@echo off

set pa=%CD%
set "msg=%~1"
rem it will check if the user entered a folder msg 
if "%msg%" == "" (
    rem if there is no msg it will print error
    echo "error you did not enter a message for the commit"
rem if the user entered a msg it will skip the if condition and enter else condition
) else (
    rem if the user want to make a new repo from zero he will only enter the msg
    if "%2" == "" (
        python D:\Programming\python\Python-GitHub-Automation\newrepo.py "%msg%" "%pa%"
    ) else (
        rem if he wants to make a repo from a local file on the pc he will enter 'l' at the end
        if "%2" == "-l" (
            python D:\Programming\python\Python-GitHub-Automation\localrepo.py "%msg%"
        )
    )
)

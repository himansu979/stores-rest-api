# stores-rest-api
Rest API creation using stores database

### commands to commit files from local to empty github repo

```
git init
dir /ah --> you will see .git directory
git status --> modified files are in red
git add * --> to add all files
git status --> all are in green
git commit -m "added some files"
git status
git remote add origin https://github.com/xxx/stores-rest-api.git
git push -u origin master --> this will give error
>>> this this is a new repo, first pull it
git pull https://github.com/xxx/stores-rest-api.git --allow-unrelated-histories
git push -u origin master
git status
rm-rf .git
```


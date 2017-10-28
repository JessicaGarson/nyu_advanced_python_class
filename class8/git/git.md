# Advanced Git!

## Fetch and Diff Method!
`$ git fetch <remote> <branch>`
`$ git diff <remote>/<branch>`

## How to Do a Rebase
Grab the necessary changes with `git pull --rebase <remote> <branch>`, fix any merge conflicts, run git add then resolve with `git rebase --continue`.

## Deleting Branches 
`git branch -d <branch> Deletes`local branch 

`git branch -D <branch>` Forces delete for un-merged branches`

Remote...

`git push origin :<branch>` Deletes Remote Branch

## Resources
[How to undo everything with git](https://github.com/blog/2019-how-to-undo-almost-anything-with-git)

[Resolving merge conflicts](https://about.gitlab.com/2016/09/06/resolving-merge-conflicts-from-the-gitlab-ui/)

[Should I Merge or Rebase?](https://raw.githubusercontent.com/gitforteams/diagrams/master/flowcharts/rebase-or-merge.png)

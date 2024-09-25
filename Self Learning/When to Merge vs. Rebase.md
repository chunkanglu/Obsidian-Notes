# Merge
- When wanting to combine your work from another branch to the current branch via a new commit
- For adding changes to a branch that many others use
# Rebase
- When wanting to restructure the commit history with a new starting point for your changes on the current branch
- Destructive operation, hard to revert
- Should only be done when you are the only one working on this branch (ie. in feature branch), otherwise it causes a lot of pain for others
	- Don't rebase for `main` branch
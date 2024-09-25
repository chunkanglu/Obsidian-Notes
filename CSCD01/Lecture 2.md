# Contributing to a Project
- fork
- branch
- do stuff
- pull request
	- request made by a dev to a maintainer of an upstream repository to pull in their contributions

# Bring new upstream changes
`git remote add upstream [upstreamRepoUrl]`
- add the upstream repo that is not your own fork

1. fetch upstream remote `git fetch upstream`
2. checkout local main `git checkout main`
3. merge upstream/main into main `git merge upstream/main main`
4. checkout local feature branch
5. 2 options
	1. Merge local main into feature branch
	2. Rebase feature branch to main

# Learning a codebase
1. Why does software exist? What problem does it solve?
	1. Provides abstractions for common use cases or core components for using LLMs in projects
	2. Makes things easier to use without re-inventing the wheel every time
2. Understand the core features and what it does
3. Understand core objects involved
4. Learn how to use the library basics

# Langchain
- build around "standard interfaces"
- used as basis for core components
	- `BaseChatModel`, `PromptTemplates`, Output Parsers
- many things are under the `Runnable` interface so that they can be chained together
- Evaluating this would be a tree structure, with branching happening when there are multiple options
- Idea is to perform BFS on this tree
- Use 3-tape multitape TM where
	1. Contains configurations we've seen but not expanded
	2. Current configuration
	3. Configurations we've fully searched (This may not be needed as graph is a tree so we don't need to check if we have already seen a node)

- Fill initial config in first tape using $\#$ as delimiter
- Keep running BFS steps until accepting config or all exhausted
	- Move first available config in first tape to second tape
	- Cross out moved config in first tape & advance first head to next available
	- perform TM actions on second tape, append all possible next transitions to tape 1, and evaluate result (halt if needed)
	- append second tape to tape 3
	- erase tape 2

- **How do we copy next configs to the end of the string**
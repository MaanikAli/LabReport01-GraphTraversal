#LabReport01-GraphTraversal


## Overview
This project generates an `N×N` grid (where `N` is between 4 and 7) with obstacles (`0` for blocks and `1` for paths). It then performs Depth-First Search (DFS) to find a path from a randomly selected source to a goal and outputs the results.

## Features
- Generates a random grid with obstacles (`0`) and paths (`1`).
- Selects a random non-obstacle source and goal.
- Implements DFS to find a path from the source to the goal.
- Prints the grid, DFS path, and topological order of traversal.

## Installation & Usage
### Prerequisites
- Python 3.x

### Running the Program

1. Run the script:
   ```bash
   LabReport01-GraphTraversal.py
   ```

## Example Output
```
Generated Grid:
S 1 0 1 1
1 0 1 0 1
1 1 1 1 1
0 1 0 1 G
1 1 1 0 1

Source: (0, 0)
Goal: (3, 4)
DFS Path: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4)]
Topological Order of Traversal: [(0, 0), (1, 0), (2, 0), ...]
```




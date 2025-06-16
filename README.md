# Cell Tower Optimizer

This project solves the problem of finding the minimum number of cell towers needed to cover all houses along a road, where each tower has a 4-mile coverage radius.

## Problem Description
- Each dash "-" represents a mile marker along the road
- Each "H" represents a house located next to a mile marker
- Cell towers can cover houses within a 4-mile radius
- Goal is to find the minimum number of towers needed to cover all houses

## Algorithm
The solution uses a greedy algorithm approach where:
1. We sort the house positions
2. For each uncovered house, we place a tower at the rightmost position that can cover it
3. We then skip all houses that are covered by this tower
4. Repeat until all houses are covered

This is a variation of the interval covering problem, which is a classic greedy algorithm problem.

## References
- Interval Covering Problem: https://en.wikipedia.org/wiki/Interval_scheduling
- Greedy Algorithms: https://en.wikipedia.org/wiki/Greedy_algorithm

## Setup
1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the main script:
```bash
python src/main.py
```

The output will be a single integer representing the minimum number of towers needed.

## Testing
Run tests:
```bash
pytest tests/
``` 
# Cell Tower Optimizer

This project solves the problem of finding the minimum number of cell towers needed to cover all houses along a road, where each tower has a 4-mile coverage radius.

## Problem Description
- Each dash "-" represents a mile marker along the road
- Each "H" represents a house located next to a mile marker
- Cell towers can cover houses within a 4-mile radius
- Goal is to find the minimum number of towers needed to cover all houses

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

## Testing
Run tests:
```bash
pytest tests/
``` 
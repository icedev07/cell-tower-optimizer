import requests
import re

def download_reference_file(url, output_path):
    # Google Drive direct download workaround
    file_id = re.findall(r"/d/([\w-]+)", url)[0]
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    response = requests.get(download_url)
    response.raise_for_status()
    with open(output_path, 'wb') as f:
        f.write(response.content)

def parse_road_layout(file_path):
    with open(file_path, 'r') as f:
        lines = [line.rstrip('\n') for line in f if line.strip()]
    # Find the road line (with dashes)
    road_idx = next(i for i, line in enumerate(lines) if '-' in line)
    road = lines[road_idx]
    house_positions = []
    for i, line in enumerate(lines):
        if i == road_idx:
            continue
        for m in re.finditer('H', line):
            house_positions.append(m.start())
    return road, sorted(house_positions)

def min_cell_towers(house_positions, coverage_radius):
    if not house_positions:
        return 0
    towers = 0
    i = 0
    n = len(house_positions)
    while i < n:
        # Place tower at the farthest house within coverage_radius of the current house
        loc = house_positions[i] + coverage_radius
        # Move to the rightmost house within coverage
        while i < n and house_positions[i] <= loc:
            i += 1
        towers += 1
    return towers

def main():
    url = "https://drive.google.com/file/d/1YzjvOf8vHj5KYrfw2nbVh8t78leD6jB7/view?usp=sharing"
    ref_file = "reference.txt"
    download_reference_file(url, ref_file)
    road, house_positions = parse_road_layout(ref_file)
    # Each tower covers 4 miles to the left and right (8 miles total)
    coverage_radius = 4
    result = min_cell_towers(house_positions, coverage_radius)
    print(result)

if __name__ == "__main__":
    main() 
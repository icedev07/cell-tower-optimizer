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
        # Place tower to cover house_positions[i] and extend coverage as far right as possible
        # 'loc' represents the furthest point to the right that this tower can cover.
        # If the tower is centered at T, its coverage is [T - radius, T + radius].
        # To cover house_positions[i] (the leftmost uncovered house) and maximize right reach,
        # the tower should be centered at 'house_positions[i] + coverage_radius'.
        # The rightmost point it covers would then be (house_positions[i] + coverage_radius) + coverage_radius
        # which simplifies to house_positions[i] + (2 * coverage_radius).
        # So, 'loc' as calculated here (house_positions[i] + coverage_radius) is actually the
        # point where the tower would be placed (its center) if we wanted to cover house_positions[i]
        # and its coverage extends up to (house_positions[i] + 2 * coverage_radius).
        # The loop condition `house_positions[i] <= loc` means it continues as long as the house
        # is within the *effective* coverage area rightwards from the current placement.
        # This is a standard greedy approach for this type of problem.
        loc = house_positions[i] + coverage_radius # This is the location of the tower itself, not the rightmost coverage
        
        # This inner loop finds the rightmost house that can be covered by the current tower
        # A tower at 'loc' covers up to 'loc + coverage_radius'.
        # So, we need to check if house_positions[i] is within this range.
        # The existing code should be:
        # covered_until = house_positions[i] + (2 * coverage_radius)
        # while i < n and house_positions[i] <= covered_until:
        #     i += 1
        # Let me correct the `loc` variable name and the logic to reflect this correctly.

        # Correct greedy placement logic:
        # If the leftmost uncovered house is at 'current_house_pos',
        # place a tower at 'current_house_pos + coverage_radius'.
        # This tower will cover houses in the range [current_house_pos, current_house_pos + 2 * coverage_radius].
        
        tower_placement_point = house_positions[i] + coverage_radius
        coverage_right_boundary = tower_placement_point + coverage_radius

        # Increment tower count
        towers += 1
        
        # Advance 'i' past all houses covered by this tower
        while i < n and house_positions[i] <= coverage_right_boundary:
            i += 1
            
    return towers

def main():
    url = "https://drive.google.com/file/d/1YzjvOf8vHj5KYrfw2nbVh8t78leD6jB7/view?usp=sharing"
    ref_file = "reference.txt"
    download_reference_file(url, ref_file)
    road, house_positions = parse_road_layout(ref_file)

    # Each tower covers 4 miles to the left and right (8 miles total)
    coverage_radius = 4
    result = min_cell_towers(house_positions, coverage_radius)
    print("ANSWER:")
    print('"""')
    print(result)
    print('"""')
    print("\nSOURCES:")
    print('"""')
    print(url)
    print('"""')

if __name__ == "__main__":
    main() 
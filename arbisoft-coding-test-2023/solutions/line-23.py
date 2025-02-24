import sys


def merge_floors(merges_allowed, buildings):
    """
    Merge floors of buildings based on the total weight of above floors & merges allowed
    Return the buildings after merges
    """
    total_merges = 0
    buildings = buildings
    for i in range(0, len(buildings)):
        building = buildings[i]
        print(f"Building {i} is: ", building)
        for j in range(0, len(building)):
            print(f"Floor {j} is: ", building[j])
            total_weight_of_above_floors = sum([building[k] for k in range(j + 1, len(building))])
            print(f"Total weight of above floors: {total_weight_of_above_floors}")
            if total_weight_of_above_floors > building[j]:
                if j-1 > 0:
                    building[j-1] += building[j]
                    building.pop(j)
                total_merges += 1
                print(f"Building after merge {total_merges}: ", building)
                if total_merges == merges_allowed:
                    break
    return buildings


def run_simulator(steps, merges_allowed, buildings):
    """
    Run the simulator X times & print the remaining height of each bulding
    """
    buildings = buildings
    for i in range(0, steps):
        buildings = merge_floors(merges_allowed, buildings)
        print(f"Building after step {i+1}: ", buildings)
    # Print the remaining height of each building
    buildings_remaining_height = ",".join([str(len(building)) for building in buildings])
    print(buildings_remaining_height)


if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
        steps = int(file.readline().strip())
        merges_allowed = int(file.readline().strip())
        rows = int(file.readline().strip())
        buildings = []
        for i in range(0, rows):
            building = file.readline().strip().split(",")
            building = [int(x) for x in building]
            buildings.append(building)
    print("Buildings: ", buildings)
    run_simulator(steps, merges_allowed, buildings)

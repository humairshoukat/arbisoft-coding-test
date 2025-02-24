import sys


def get_all_ballons(pattern, end_position):
    """
    Get the list of all the ballons by iterating till end position
    """
    ballons = []
    pattern_index = 0
    for i in range(end_position + 1):
        if pattern_index == len(pattern):
            pattern_index = 0
        ballons.append(pattern[pattern_index])
        pattern_index += 1
    return ballons


def print_ballon_count(ballons, start_position, end_position):
    """
    Print the ballon count for each color
    """
    blue = 0
    orange = 0
    white = 0
    for i in range(start_position, end_position + 1):
        if ballons[i] == 'b':
            blue += 1
        elif ballons[i] == 'o':
            orange += 1
        elif ballons[i] == 'w':
            white += 1
    print(f"b{blue}o{orange}w{white}")


if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
        pattern = file.readline().strip()
        start_position = int(file.readline().strip())
        end_position = int(file.readline().strip())
    ballons = get_all_ballons(pattern, end_position)
    print_ballon_count(ballons, start_position, end_position)

import sys


def minimum_cars_required(tourists, seats):
    """
    Calculate & return the min number of cars required for all tourists 
    """
    total_tourists = sum(tourists)
    seats.sort(reverse=True)

    cars_with_max_seats = []

    for seat in seats:
        cars_with_max_seats.append(seat)
        if sum(cars_with_max_seats) > total_tourists:
            return(len(cars_with_max_seats))


if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
        tourists = file.readline().strip()
        seats = file.readline().strip()
        # Convert strings to lists of integers
        tourists = eval(tourists)
        seats = eval(seats)
        print(minimum_cars_required(tourists, seats))
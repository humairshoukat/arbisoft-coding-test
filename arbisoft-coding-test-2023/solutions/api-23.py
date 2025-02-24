import sys
import requests


def calculate_commission_on_driver_earnings(driver_id, month_joined, rides):
    """
    Calculate and return the total commission that has to paid by the driver to the company
    """
    commission = 0
    for ride in rides:
        if ride['driver_id'] == driver_id:
            trip_month = ride['trip_date'].strip().split('/')[0]
            if trip_month == month_joined:
                continue  # Skip the ride if it was in the month when the driver joined
            if int(trip_month) - int(month_joined) == 1:
                # Calculate 10% commission if the ride was in the next month
                commission += ride['trip_details']['fare'] * 0.1
            else:
                # Calculate 20% commission if the ride was in the month after the next month
                commission += ride['trip_details']['fare'] * 0.2
    return commission


def calculate_driver_payments(driver_id, payments):
    """
    Calculate and returns the total payment made to the company by the driver
    """
    driver_payments = 0
    for payment in payments:
        if payment['driver_id'] == driver_id:
            driver_payments += payment['amount']
    return driver_payments


def calculate_driver_balance(drivers, rides, payments):
    """
    Calculate the prints the balance of each driver
    """
    rides = rides.json()
    payments = payments.json()
    for driver in drivers:
        driver_id = driver['driver_id']
        month_joined = driver['month_joined']
        driver_payments = calculate_driver_payments(driver_id, payments)
        total_commission = calculate_commission_on_driver_earnings(driver_id, month_joined, rides)
        driver_balance = driver_payments - total_commission
        print("Driver ID: ", driver_id, " Month Joined: ", month_joined)
        print("Driver Payments: ", driver_payments, " Total Commision: ", total_commission)
        print("Driver Balance: ", round(driver_balance, 1))


if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
        test_cases = int(file.readline().strip())
        drivers = []
        for i in range(0, test_cases):
            driver = file.readline().strip().split(',')
            drivers.append({
                "driver_id": int(driver[0]),
                "month_joined": driver[1].strip().split('/')[0],
            })
    print("Test Cases: ", test_cases)
    print("Drivers: ", drivers)
    rides_api_url = "https://www.jsonkeeper.com/b/DM5F"
    payments_api_url = "https://www.jsonkeeper.com/b/9QRZ"
    rides = requests.get(rides_api_url)
    payments = requests.get(payments_api_url)
    calculate_driver_balance(drivers, rides, payments)
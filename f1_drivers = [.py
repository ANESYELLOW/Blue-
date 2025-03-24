f1_drivers = [
    {"Name": "Lewis Hamilton", "Team": "Mercedes", "Championships": 7, "Country": "UK"},
    {"Name": "Max Verstappen", "Team": "Red Bull", "Championships": 3, "Country": "Netherlands"},
    {"Name": "Charles Leclerc", "Team": "Ferrari", "Championships": 0, "Country": "Monaco"},
    {"Name": "Lando Norris", "Team": "McLaren", "Championships": 0, "Country": "UK"},
    {"Name": "Fernando Alonso", "Team": "Aston Martin", "Championships": 2, "Country": "Spain"},
    {"Name": "Carlos Sainz", "Team": "Ferrari", "Championships": 0, "Country": "Spain"},
    {"Name": "Sergio Perez", "Team": "Red Bull", "Championships": 0, "Country": "Mexico"},
    {"Name": "George Russell", "Team": "Mercedes", "Championships": 0, "Country": "UK"},
    {"Name": "Oscar Piastri", "Team": "McLaren", "Championships": 0, "Country": "Australia"},
    {"Name": "Pierre Gasly", "Team": "Alpine", "Championships": 0, "Country": "France"}
]

def filter_drivers(data, key, value):
    """Filters a list of dictionaries by a key-value pair."""
    return [driver for driver in data if driver.get(key) == value]

def sort_drivers(data, key, reverse=False):
    """Sorts a list of dictionaries by a specified key."""
    sorted_data = data.copy()  # Create a copy of the original list
    n = len(sorted_data)

    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if sorted_data[j][key] > sorted_data[j + 1][key]:
                # Swap the elements if they are in the wrong order
                sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]

    # If reverse is True, reverse the sorted list
    if reverse:
        sorted_data.reverse()

    return sorted_data


def aggregate_drivers(data, key):
    """Groups data by a key and calculates the average of 'Championships' for each group."""
    aggregation = {}
    for driver in data:
        group = driver[key]
        championships = driver.get("Championships", 0)
        if group not in aggregation:
            aggregation[group] = {"count": 0, "total": 0}
        aggregation[group]["count"] += 1
        aggregation[group]["total"] += championships
    
    return {group: values["total"] / values["count"] for group, values in aggregation.items()}

def print_drivers(drivers):
    """Prints the drivers in a formatted way."""
    for driver in drivers:
        print(f"Name: {driver['Name']}, Team: {driver['Team']}, Championships: {driver['Championships']}, Country: {driver['Country']}")

def main():
    while True:
        print("\nF1 Driver Data Analysis")
        print("1. Filter drivers")
        print("2. Sort drivers")
        print("3. Aggregate driver data")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            key = input("Enter the key to filter by (Name/Team/Championships/Country): ")
            value = input(f"Enter the value for {key}: ")
            filtered_drivers = filter_drivers(f1_drivers, key, value)
            print("\nFiltered Drivers:")
            print_drivers(filtered_drivers)
        
        elif choice == '2':
            key = input("Enter the key to sort by (Name/Team/Championships/Country): ")
            order = input("Sort in ascending (a) or descending (d) order? ").lower()
            reverse = order == 'd'
            sorted_drivers = sort_drivers(f1_drivers, key, reverse)
            print("\nSorted Drivers:")
            print_drivers(sorted_drivers)
        
        elif choice == '3':
            key = input("Enter the key to aggregate by (Team/Country): ")
            aggregated_data = aggregate_drivers(f1_drivers, key)
            print(f"\nAverage Championships by {key}:")
            for group, avg in aggregated_data.items():
                print(f"{group}: {avg:.2f}")
        
        elif choice == '4':
            print("Thank you for using the F1 Driver Data Analysis tool. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

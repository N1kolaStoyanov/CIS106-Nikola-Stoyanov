def load_data_from_file(file_path):
    player_names = []
    batting_averages = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                player_name = data[0]
                batting_average = float(data[1])
                player_names.append(player_name)
                batting_averages.append(batting_average)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"Error loading data: {e}")

    return player_names, batting_averages

def display_player_data(player_names, batting_averages):
    print("Player Data:")
    for i in range(len(player_names)):
        print(f"Player: {player_names[i]}, Batting Average: {batting_averages[i]}")

def search_player_by_last_name(player_names, batting_averages, target_last_name):
    for i in range(len(player_names)):
        if player_names[i].lower() == target_last_name.lower():
            return player_names[i], batting_averages[i]
    return None, None

def main():
    file_path = "player_data.txt"  # Replace with the path to your file
    player_names, batting_averages = load_data_from_file(file_path)

    # Display player data
    display_player_data(player_names, batting_averages)

    while True:
        target_last_name = input("\nEnter a last name to search (or 'exit' to quit): ")
        if target_last_name.lower() == 'exit':
            break

        found_player_name, found_batting_average = search_player_by_last_name(player_names, batting_averages, target_last_name)

        if found_player_name is not None:
            print(f"\nPlayer Found - Last Name: {found_player_name}, Batting Average: {found_batting_average}")
        else:
            print(f"\nPlayer with last name '{target_last_name}' not found.")

if __name__ == "__main__":
    main()

import pandas as pd
import sys

def load_map(file_path):
    try:
        # We can read the file line by line and then create a DataFrame
        with open(file_path, 'r') as f:
            lines = [list(line.strip()) for line in f]
        return pd.DataFrame(lines)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python pandas_map_viewer.py <path_to_map_file>")
        sys.exit(1)

    map_file_path = sys.argv[1]
    game_map_df = load_map(map_file_path)

    print("Map:")
    # We can print the DataFrame without the index and header
    print(game_map_df.to_string(index=False, header=False))

    # Example of using a pandas function: describe()
    # This will give us some basic statistics about the characters in the map.
    print("\\nMap Description:")
    print(game_map_df.describe())


if __name__ == "__main__":
    main()

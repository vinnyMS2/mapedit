import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python map_viewer.py <path_to_map_file>")
        sys.exit(1)

    map_file_path = sys.argv[1]
    load_map(map_file_path)

def load_map(file_path):
    try:
        with open(file_path, 'r') as f:
            map_data = f.read()
        print(map_data)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()

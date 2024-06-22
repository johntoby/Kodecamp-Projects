import os

# Define the directory names
directories = [
    "Finance Budgets",
    "Contract Documents",
    "Business Projections",
    "Business Models",
    "Employee Data",
    "Company Vision and Mission Statement",
    "Server Configuration Script"
]

# Function to create directories
def create_directories(dir_list, base_path="."):
    for directory in dir_list:
        path = os.path.join(base_path, directory)
        try:
            os.makedirs(path, exist_ok=True)
            print(f"Created directory: {path}")
        except OSError as e:
            print(f"Error creating directory {path}: {e}")

# Function to create a file in a specified directory
def create_file_in_directory(file_name, directory, base_path="."):
    if directory not in directories:
        print(f"Error: {directory} is not a valid company directory.")
        return

    dir_path = os.path.join(base_path, directory)
    file_path = os.path.join(dir_path, file_name)

    try:
        with open(file_path, 'w') as file:
            file.write("This is a placeholder file.")
        print(f"Created file: {file_path}")
    except OSError as e:
        print(f"Error creating file {file_path}: {e}")

# Create directories
create_directories(directories)

# Get user input for file creation
file_name = input("Enter the name of the file to create: ")
directory = input("Enter the directory to create the file in: ")

# Create the file in the specified directory
create_file_in_directory(file_name, directory)


import subprocess

# Define users and their groups
users = {
    "Andrew": "IT",
    "Julius": "Legal",
    "Chizi": "HR",
    "Jeniffer": "Sales",
    "Adeola": "Business",
    "Bach": "Management",
    "Gozie": "Intern",
    "Ogochukwu": "Finance"
}

# Function to create a group
def create_group(group):
    try:
        subprocess.run(['groupadd', group], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error creating group {group}: {e}")

# Function to create a user and assign to a group
def create_user(username, group):
    try:
        subprocess.run(['useradd', '-m', '-G', group, username], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error creating user {username}: {e}")

# Create groups and users
for user, group in users.items():
    create_group(group)
    create_user(user, group)

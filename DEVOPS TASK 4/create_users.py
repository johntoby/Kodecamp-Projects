import subprocess

# Define users and their groups
users = {
    "Andrew": "System Administrator",
    "Julius": "Legal",
    "Chizi": "Human Resource Manager",
    "Jeniffer": "Sales Manager",
    "Adeola": "Business Strategist",
    "Bach": "CEO",
    "Gozie": "IT intern",
    "Ogochukwu": "Finance Manager"
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
S
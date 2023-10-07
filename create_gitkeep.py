import os

def create_gitkeep(root_dir):
    for subdir, _, _ in os.walk(root_dir):
        gitkeep_path = os.path.join(subdir, '.gitkeep')
        with open(gitkeep_path, 'a') as file:
            pass  # This creates an empty file if it doesn't exist, and does nothing if it does exist

# Usage:
project_root = "E:\\Moneymad"  # Replace with the path to your project root
create_gitkeep(project_root)

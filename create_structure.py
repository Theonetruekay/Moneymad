import os

def create_directory_structure(root):
    directories = [
        "Assets/Animations",
        "Assets/Audio/Music",
        "Assets/Audio/SFX",
        "Assets/Prefabs",
        "Assets/Scenes/Main",
        "Assets/Scenes/Office",
        "Assets/Scenes/Market",
        "Assets/Scripts/Entities",
        "Assets/Scripts/Gameplay",
        "Assets/Scripts/Managers",
        "Assets/Scripts/UI",
        "Assets/Sprites/Characters",
        "Assets/Sprites/Furniture",
        "Assets/Sprites/OfficeTiles",
        "Assets/Sprites/UI",
        "Assets/Plugins",
        "Assets/Libraries",
        "Documentation/DesignDocuments",
        "Documentation/TechnicalDocuments",
        "ProjectSettings"
    ]

    for directory in directories:
        path = os.path.join(root, directory)
        os.makedirs(path, exist_ok=True)
        gitkeep_path = os.path.join(path, ".gitkeep")
        with open(gitkeep_path, "w") as gitkeep_file:
            pass  # This creates an empty file

    # Create .gitignore, README.md, and LICENSE files at the root level
    for filename in [".gitignore", "README.md", "LICENSE"]:
        filepath = os.path.join(root, filename)
        with open(filepath, "w") as file:
            pass  # This creates empty files

# Usage:
project_root = "E:\\Moneymad"  # replace with the path to your project root
create_directory_structure(project_root)
 
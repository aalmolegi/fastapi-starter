import os
from pathlib import Path

def create_structure():
    
    # Define the structure
    structure = {
        "app": [
            "__init__.py",
            "main.py",
        ],
        "app/core": [
            "__init__.py",
            "config.py",
            "security.py",
        ],
        "app/db": [
            "__init__.py",
            "base.py",
            "session.py",
        ],
        "app/models": [
            "__init__.py",
            "user.py",
            "item.py",
        ],
        "app/schemas": [
            "__init__.py",
            "user.py",
            "item.py",
        ],
        "app/repositories": [
            "__init__.py",
            "user_repo.py",
            "item_repo.py",
        ],
        "app/api": [
            "__init__.py",
            "deps.py",
        ],
        "app/api/routes": [
            "__init__.py",
            "auth.py",
            "users.py",
            "items.py",
        ],
        "alembic": [
            "env.py",
            "script.py.mako",
        ],
        "alembic/versions": [],  # This is just a directory, no files to create
        "tests": [
            "test_health.py",
            "test_auth_items.py",
        ],
    }
    
    # Create directories and files
    for directory, files in structure.items():
        dir_path = Path(directory)  # Convert string to Path object
        dir_path.mkdir(parents=True, exist_ok=True)
        
        for file in files:
            filepath = dir_path / file
            filepath.touch()
            print(f"Created: {filepath}")
    
    # Create additional root files
    additional_files = [
        ".env.example",
        ".gitignore", 
        "alembic.ini",
        "requirements.txt",
        "README.md"
    ]
    
    for file in additional_files:
        filepath = Path(file)  # These are in the current directory
        filepath.touch()
        print(f"Created: {filepath}")

if __name__ == "__main__":
    create_structure()

import os
import shutil
from pathlib import Path
from datetime import datetime

# Change this to the folder you want to organize.
# For a safe first test, create a folder named "Organizer_Test" in Downloads.
SOURCE_DIR = Path.home() / "Downloads" / "Organizer_Test"

EXTENSION_MAP = {
    # Documents
    ".pdf": "Documents", ".doc": "Documents", ".docx": "Documents",
    ".txt": "Documents", ".rtf": "Documents", ".odt": "Documents",
    ".xls": "Documents", ".xlsx": "Documents", ".ppt": "Documents",
    ".pptx": "Documents", ".csv": "Documents",

    # Images
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images",
    ".gif": "Images", ".bmp": "Images", ".webp": "Images",
    ".svg": "Images", ".tif": "Images", ".tiff": "Images",

    # Videos
    ".mp4": "Videos", ".mov": "Videos", ".avi": "Videos",
    ".mkv": "Videos", ".wmv": "Videos", ".webm": "Videos",

    # Archives
    ".zip": "Archives", ".rar": "Archives", ".7z": "Archives",
    ".tar": "Archives", ".gz": "Archives",

    # Code
    ".py": "Code", ".js": "Code", ".html": "Code",
    ".css": "Code", ".java": "Code", ".c": "Code",
    ".cpp": "Code", ".h": "Code", ".json": "Code",
    ".xml": "Code", ".sql": "Code", ".ipynb": "Code"
}

def unique_destination(path):
    """Choose a non-existing filename instead of overwriting a file."""
    if not path.exists():
        return path

    counter = 1
    while True:
        candidate = path.with_name(f"{path.stem}_{counter}{path.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1

def organize_directory(source_dir):
    if not source_dir.exists() or not source_dir.is_dir():
        print(f"Folder not found: {source_dir}")
        print("Create Downloads/Organizer_Test, put a few test files in it, and run again.")
        return

    moved = 0
    skipped = 0
    errors = 0

    print("\n===== DESKTOP FILE ORGANIZER =====")
    print(f"Folder: {source_dir}\n")

    try:
        entries = list(os.scandir(source_dir))
    except PermissionError:
        print("Permission denied: cannot access this folder.")
        return

    for entry in entries:
        # Only handle files in this folder; don't process category folders.
        if not entry.is_file(follow_symlinks=False):
            continue

        file_path = Path(entry.path)
        category = EXTENSION_MAP.get(file_path.suffix.lower())

        if category is None:
            print(f"Skipped (unknown file type): {file_path.name}")
            skipped += 1
            continue

        target_dir = source_dir / category

        try:
            target_dir.mkdir(exist_ok=True)
            destination = unique_destination(target_dir / file_path.name)
            shutil.move(str(file_path), str(destination))
            print(f"Moved: {file_path.name} -> {category}/{destination.name}")
            moved += 1
        except (PermissionError, FileExistsError, OSError) as exc:
            print(f"Could not move {file_path.name}: {exc}")
            errors += 1

    print("\n===== EXECUTION SUMMARY =====")
    print(f"Files relocated : {moved}")
    print(f"Files skipped   : {skipped}")
    print(f"Errors          : {errors}")
    print("Organization complete.")

if __name__ == "__main__":
    organize_directory(SOURCE_DIR)


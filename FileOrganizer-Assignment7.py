import os
import shutil
from pathlib import Path


FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico"],
    "Documents": [
        ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
        ".txt", ".csv", ".md", ".odt",
    ],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"],
    "Code": [
        ".py", ".js", ".ts", ".html", ".css", ".java", ".c", ".cpp",
        ".h", ".json", ".xml", ".yaml", ".yml", ".toml", ".sh", ".sql",
    ],
    "Executables": [".exe", ".msi", ".deb", ".rpm", ".appimage", ".dmg"],
    "Others": [],
}


def organize_downloads(download_path=None):
    if download_path is None:
        download_path = str(Path.home() / "Downloads")

    if not os.path.exists(download_path):
        print(f"Error: Path '{download_path}' does not exist.")
        return

    print(f"Organizing: {download_path}")
    print("-" * 50)

    created_folders = {}

    for category in FILE_CATEGORIES:
        folder_path = os.path.join(download_path, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            created_folders[category] = True

    moved_count = 0
    skipped_count = 0

    for item in os.listdir(download_path):
        item_path = os.path.join(download_path, item)

        if os.path.isdir(item_path):
            continue

        ext = os.path.splitext(item)[1].lower()
        target_category = "Others"

        for category, extensions in FILE_CATEGORIES.items():
            if ext in extensions:
                target_category = category
                break

        target_path = os.path.join(download_path, target_category, item)

        if os.path.exists(target_path):
            base, ext = os.path.splitext(item)
            counter = 1
            while os.path.exists(
                os.path.join(download_path, target_category, f"{base}_{counter}{ext}")
            ):
                counter += 1
            target_path = os.path.join(
                download_path, target_category, f"{base}_{counter}{ext}"
            )

        shutil.move(item_path, target_path)
        moved_count += 1
        print(f"  Moved: {item} -> {target_category}/")

    print("-" * 50)
    print(f"Total files organized: {moved_count}")
    print("Done!")


if __name__ == "__main__":
    organize_downloads()

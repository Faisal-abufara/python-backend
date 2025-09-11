import os
import shutil

EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
}

def get_folder_name(extension):
    """Return the folder name for a given file extension."""
    for folder, extensions in EXTENSION_MAP.items():
        if extension.lower() in extensions:
            return folder
    return "Others"

def organize_directory(target_dir):
    """Organize files in the given directory based on file type."""
    if not os.path.isdir(target_dir):
        print("The specified path is not a directory.")
        return


    with os.scandir(target_dir) as entries:
        for entry in entries:
            if entry.is_file():
                file_path = entry.path
                file_name = entry.name
                _, extension = os.path.splitext(file_name)

                
                folder_name = get_folder_name(extension)
                destination_folder = os.path.join(target_dir, folder_name)

                
                os.makedirs(destination_folder, exist_ok=True)

                
                destination_path = os.path.join(destination_folder, file_name)
                shutil.move(file_path, destination_path)

                print(f"Moved '{file_name}' to '{folder_name}/'")

def main():
    target_dir = input("Enter the full path of the directory to organize: ").strip()

    if os.path.exists(target_dir):
        organize_directory(target_dir)
    else:
        print("That directory does not exist.")

if __name__ == "__main__":
    main()

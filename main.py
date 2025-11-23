import os
import shutil

# === SCRIPT ===
def sort_images_by_type(source_dir):
    if not os.path.exists(source_dir):
        print(f"❌ The folder '{source_dir}' does not exist.")
        return

    # Go through each file in the directory
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        # Extract file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower().lstrip(".")  # e.g. "jpg"

        # Skip files with no extension
        if not ext:
            continue

        # Create a folder named after the file type
        folder_name = ext.upper()  # e.g. "JPG"
        folder_path = os.path.join(source_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Move file into its type folder
        dest_path = os.path.join(folder_path, filename)
        shutil.move(file_path, dest_path)
        print(f"Moved: {filename} → {folder_name}/")

    print("\n✅ Done! Images are now organized by type.")


if __name__ == "__main__":
    # Ask the user for the folder path
    source_dir = input("Enter the full path of the folder you want to sort: ").strip()
    sort_images_by_type(source_dir)

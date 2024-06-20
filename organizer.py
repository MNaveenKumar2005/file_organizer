import os
import shutil

# Prompt user to enter the directory path
path = input("Enter Path: ")

# Check if the provided path is valid
if not os.path.isdir(path):
    print("The specified path is not valid.")
else:
    # List all files in the directory
    files = os.listdir(path)

    for file in files:
        # Construct full file path
        file_path = os.path.join(path, file)

        # Check if the current item is a file (skip directories)
        if os.path.isfile(file_path):
            # Split the file name and its extension
            filename, extension = os.path.splitext(file)
            # Remove the leading dot from the extension
            extension = extension[1:]

            if extension:  # Only process if there is an extension
                # Construct the new directory path for this extension
                extension_dir = os.path.join(path, extension)

                # Create the extension directory if it doesn't exist
                if not os.path.exists(extension_dir):
                    os.makedirs(extension_dir)

                # Move the file to the new directory
                shutil.move(file_path, os.path.join(extension_dir, file))

    print("Files have been organized by extension.")

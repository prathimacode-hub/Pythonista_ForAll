import os
import shutil

# Define the path to your desktop
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# Define categories and their respective file extensions
categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.tiff'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Audio': ['.mp3', '.wav', '.aac'],
    # Add more categories and file extensions as needed
}

# Create folders for each category on the desktop if they don't exist
for category in categories:
    folder_path = os.path.join(desktop_path, category)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize files
for file in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, file)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(file)[1].lower()
        for category, extensions in categories.items():
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(desktop_path, category))
                break

print("Desktop organized successfully!")

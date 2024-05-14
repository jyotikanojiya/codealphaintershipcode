import os
import shutil

# Source directory containing files to be organized
source_dir = 'k:\\Camera Roll'

# Iterate over files in the source directory
for file_name in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file_name)
    
    # Check if the file is a regular file
    if os.path.isfile(file_path):
        # Get file extension
        file_extension = file_name.split('.')[-1]
        
        # Define destination directory based on file types
        if file_extension in ['jpg', 'png']:
            destination_dir = os.path.join(source_dir, 'photos')
        elif file_extension == 'mp3':
            destination_dir = os.path.join(source_dir, 'music')
        elif file_extension == 'doc':
            destination_dir = os.path.join(source_dir, 'documents')
        else:
            destination_dir = os.path.join(source_dir, 'other')
        
        # Create destination directory if it doesn't exist
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        
        # Move file to the appropriate directory
        shutil.move(file_path, destination_dir)

print("File organization completed.")

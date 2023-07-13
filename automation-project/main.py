import os
import shutil

# Function to create a new folder
def create_folder(folder_name):
    """
    Create a new folder with the specified name.
    """
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created successfully.")

# Function to handle a deleted user
def handle_deleted_user(deleted_user, user_folder, temp_folder):
    """
    Move the documents of a deleted user to a temporary folder.
    """
    if os.path.exists(user_folder):
        if not os.path.exists(temp_folder):
            os.mkdir(temp_folder)
        shutil.move(user_folder, temp_folder)
        print(f"User '{deleted_user}' has been deleted and their documents moved to the temporary folder.")

# Function to sort documents into appropriate folders
def sort_documents(source_folder):
    """
    Sort the documents in the source folder into additional folders based on their file type.
    """
    file_types = {
        ".txt": "text_files",
        ".pdf": "pdf_files",
        ".docx": "word_files",
        ".xlsx": "excel_files"
    }

    for file_name in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, file_name)):
            file_extension = os.path.splitext(file_name)[1].lower()
            if file_extension in file_types:
                destination_folder = file_types[file_extension]
                destination_path = os.path.join(source_folder, destination_folder)
                if not os.path.exists(destination_path):
                    os.mkdir(destination_path)
                shutil.move(os.path.join(source_folder, file_name), destination_path)
    
    print("Documents sorted successfully.")

# Function to parse a log file for errors and warnings
def parse_log_file(log_file):
    """
    Parse the log file for errors and warnings, and create separate log files for each.
    """
    errors = []
    warnings = []

    with open(log_file, "r") as file:
        for line in file:
            if "ERROR" in line:
                errors.append(line)
            elif "WARNING" in line:
                warnings.append(line)
    
    with open("errors.log", "w") as error_file:
        error_file.write("\n".join(errors))
    with open("warnings.log", "w") as warning_file:
        warning_file.write("\n".join(warnings))
    
    print("Log file parsed successfully.")

# Main menu-driven application
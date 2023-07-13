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
def handle_deleted_user(deleted_user, user_folder, temp_user_folder):
    """
    Move the documents of a deleted user to a temporary folder.
    """
    # Check if the user folder exists
    if os.path.exists(user_folder):
        # Check if the temporary folder exists, create it if not
        if not os.path.exists(temp_user_folder):
            os.mkdir(temp_user_folder)

        # Move the user's documents to the temporary folder
        shutil.move(user_folder, temp_user_folder)
        print(f"User '{deleted_user}' has been deleted and their documents moved to the temporary folder.")

# Function to sort documents into appropriate folders
def sort_documents(source_folder):
    """
    Sort the documents in the source folder into additional folders based on their file type.
    """
    file_types = {
        ".txt": "text_files",
        ".pdf": "pdf_files",
        ".docx": "word_files"
    }

    # Iterate over the files in the source folder
    for file_name in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, file_name)):
            file_extension = os.path.splitext(file_name)[1].lower()

            # Check if the file extension is recognized
            if file_extension in file_types:
                destination_folder = file_types[file_extension]
                destination_path = os.path.join(source_folder, destination_folder)

                # Create the destination folder if it doesn't exist
                if not os.path.exists(destination_path):
                    os.mkdir(destination_path)

                # Move the file to the destination folder
                shutil.move(os.path.join(source_folder, file_name), destination_path)
    
    print("Documents sorted successfully.")

# Function to parse a log file for errors and warnings
def parse_log_file(log_file):
    """
    Parse the log file for errors and warnings, and create separate log files for each.
    """
    errors = []
    warnings = []

    # Open the log file for reading
    with open(log_file, "r") as file:
        for line in file:
            if "ERROR" in line:
                errors.append(line)
            elif "WARNING" in line:
                warnings.append(line)
    
    # Create separate log files for errors and warnings
    with open("errors.log", "w") as error_file:
        error_file.write("\n".join(errors))
    with open("warnings.log", "w") as warning_file:
        warning_file.write("\n".join(warnings))
    
    print("Log file parsed successfully.")

# Main menu-driven application
def main_menu():
    """
    Display the main menu and execute the selected automation task.
    """
    while True:
        print("Main Menu")
        print("1. Create a new folder")
        print("2. Handle a deleted user")
        print("3. Sort documents into appropriate folders")
        print("4. Parse a log file for errors and warnings")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            folder_name = input("Enter the folder name: ")
            create_folder(folder_name)
        elif choice == "2":
            deleted_user = input("Enter the name of the deleted user: ")
            user_folder = input("Enter the path to the user's folder: ")
            temp_user_folder = input("Enter the path to the temporary folder: ")
            handle_deleted_user(deleted_user, user_folder, temp_user_folder)
        elif choice == "3":
            source_folder = input("Enter the path to the source folder: ")
            sort_documents(source_folder)
        elif choice == "4":
            log_file = input("Enter the path to the log file: ")
            parse_log_file(log_file)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main_menu()

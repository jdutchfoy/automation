import unittest
import os
import shutil
from main import create_folder, handle_deleted_user, sort_documents, parse_log_file, main_menu

class TestAutomationProject(unittest.TestCase):

    def setUp(self):
        # Set up a temporary folder for testing
        self.temp_folder = "temp_test_folder"
        os.mkdir(self.temp_folder)

    def tearDown(self):
        # Clean up the temporary folder after testing
        shutil.rmtree(self.temp_folder)

    def test_create_folder(self):
        # Test the create_folder function

        # Prepare the necessary data
        folder_name = "NewFolder"

        # Call the function to be tested
        create_folder(folder_name)

        # Check the expected outcome
        self.assertTrue(os.path.exists(folder_name))  # Assert that the folder has been created

    def test_handle_deleted_user(self):
        # Test the handle_deleted_user function

        # Prepare the necessary data
        deleted_user = "user2"
        user_folder = os.path.join(self.temp_folder, deleted_user)
        temp_user_folder = os.path.join(self.temp_folder, "temp_user_folder")
        os.mkdir(user_folder)

        # Call the function to be tested
        handle_deleted_user(deleted_user, user_folder, temp_user_folder)

        # Check the expected outcome
        self.assertFalse(os.path.exists(user_folder))  # Assert that the user folder has been deleted
        self.assertTrue(os.path.exists(temp_user_folder))  # Assert that the documents have been moved to the temporary folder

    def test_sort_documents(self):
        # Test the sort_documents function

        # Prepare the necessary data
        source_folder = "test_documents"
        os.mkdir(source_folder)
        test_files = ["document1.txt", "document2.pdf", "document3.docx"]
        for file in test_files:
            with open(os.path.join(source_folder, file), "w"):
                pass

        # Call the function to be tested
        sort_documents(source_folder)

        # Check the expected outcome
        self.assertTrue(os.path.exists(os.path.join(source_folder, "text_files")))  # Assert that the text files have been sorted correctly
        self.assertTrue(os.path.exists(os.path.join(source_folder, "pdf_files")))  # Assert that the PDF files have been sorted correctly
        self.assertTrue(os.path.exists(os.path.join(source_folder, "word_files")))  # Assert that the Word files have been sorted correctly

    def test_parse_log_file(self):
        # Test the parse_log_file function

        # Prepare the necessary data
        log_file = "test_log.log"
        test_log_data = "This is an ERROR message.\nThis is a WARNING message.\n"
        with open(log_file, "w") as file:
            file.write(test_log_data)

        # Call the function to be tested
        parse_log_file(log_file)

        # Check the expected outcome
        self.assertTrue(os.path.exists("errors.log"))  # Assert that the errors log file has been created
        self.assertTrue(os.path.exists("warnings.log"))  # Assert that the warnings log file has been created

    def test_main_menu(self):
        # TODO: Implement tests for the main_menu function
        pass

if __name__ == '__main__':
    unittest.main()

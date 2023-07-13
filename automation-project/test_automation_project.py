import unittest
import os
import shutil
from main import create_folder, handle_deleted_user, sort_documents, parse_log_file

class TestAutomationProject(unittest.TestCase):

    def setUp(self):
        self.temp_folder = "temp_test_folder"
        os.mkdir(self.temp_folder)

    def tearDown(self):
        shutil.rmtree(self.temp_folder)

    def test_create_folder(self):
        folder_name = "NewFolder"
        create_folder(folder_name)
        self.assertTrue(os.path.exists(folder_name))

    def test_handle_deleted_user(self):
        deleted_user = "user2"
        user_folder = os.path.join(self.temp_folder, deleted_user)
        temp_user_folder = os.path.join(self.temp_folder, "temp_user_folder")
        os.mkdir(user_folder)

        handle_deleted_user(deleted_user, user_folder, temp_user_folder)

        self.assertFalse(os.path.exists(user_folder))
        self.assertTrue(os.path.exists(temp_user_folder))

    def test_sort_documents(self):
        source_folder = "test_documents"
        os.mkdir(source_folder)
        test_files = ["document1.txt", "document2.pdf", "document3.docx"]
        for file in test_files:
            with open(os.path.join(source_folder, file), "w"):
                pass

        sort_documents(source_folder)

        self.assertTrue(os.path.exists(os.path.join(source_folder, "text_files")))
        self.assertTrue(os.path.exists(os.path.join(source_folder, "pdf_files")))
        self.assertTrue(os.path.exists(os.path.join(source_folder, "word_files")))

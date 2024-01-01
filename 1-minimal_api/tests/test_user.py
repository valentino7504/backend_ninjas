#!/usr/bin/python3
'''
tests fot the user class
'''
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    class to test the user model
    """
    def test_user_creation(self):
        """
        tests user initialisation
        """
        user_1 = User("Edwin Ade", "Male", "https://github.com/valentino7504")
        self.assertEqual(user_1.name, "Edwin Ade")
        self.assertEqual(user_1.gender.lower(), "male")
        self.assertEqual(
            user_1.github_url,
            "https://github.com/valentino7504"
        )

    def test_empty_name(self):
        """
        Test user creation with an empty name
        """
        with self.assertRaises(ValueError):
            user = User("", "Male", "https://github.com/valentino7504")

    def test_invalid_name(self):
        """
        tests creation with invalid name
        """
        with self.assertRaises(ValueError):
            user_2 = User("Edwin2 Ade", "Male", "github.com/valentino7504")

    def test_name_wrong_type(self):
        """
        tests with wrong name type
        """
        with self.assertRaises(TypeError):
            user_3 = User(3.5, "Male", "https://github.com/valentino7504")

    def test_invalid_gender(self):
        """
        tests creation with invalid gender
        """
        with self.assertRaises(ValueError):
            user = User("Edwin", "", "github.com/valentino7504")

    def test_wrong_gender_type(self):
        """
        tests if gender is of the right type
        """
        with self.assertRaises(TypeError):
            user_2 = User("Edwin", 445, "https://github.com/valentino7504")

    def test_github_url_type(self):
        """
        tests invalid github url type
        """
        with self.assertRaises(TypeError):
            user_4 = User("Edwin", "Male", None)

    def test_invalid_github_url(self):
        """
        tests with invalid values for the url
        """
        with self.assertRaises(ValueError):
            user_5 = User("Robin", "Female", "ghub.com/yuri")
        with self.assertRaises(ValueError):
            user_6 = User("Luffy", "Male", "github.com/valentino7504/first-lhc")
        with self.assertRaises(ValueError):
            user = User("Edwin", "Male", "not_a_valid_url")
        with self.assertRaises(ValueError):
            user = User("Edwin", "Male", "")

#!/usr/bin/python3
'''
This module contains the Info class
'''
import re


class User:
    '''
    User class
    '''
    def __init__(self, name: str, gender: str, github_url: str):
        '''
        Constructor
        '''
        self.name = name
        self.gender = gender
        self.github_url = github_url

    @property
    def name(self):
        """
        getter method for name attribute
        """
        return self.__fname

    @name.setter
    def name(self, value: str):
        """
        setter method for name attribute
        """
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        pattern = re.compile(r"\A[a-zA-Z\s]+\Z")
        if pattern.match(value) is None or len(value.strip()) == 0:
            raise ValueError("name must consist of letters and spaces only")
        self.__fname = value

    @property
    def gender(self):
        """
        getter method
        """
        return self.__gender

    @gender.setter
    def gender(self, value: str):
        """
        setter method for gender attribute
        """
        if not isinstance(value, str):
            raise TypeError("gender must be a string")
        if len(value.strip()) == 0:
            raise ValueError("gender cannot be an empty string")
        self.__gender = value

    @property
    def github_url(self):
        """
        getter method for github url
        """
        return self.__github_url

    @github_url.setter
    def github_url(self, value: str):
        """
        setter method for github url
        """
        if not isinstance(value, str):
            raise TypeError("github url must be a string")
        pattern = re.compile(r'^(?:https?://)?(?:www\.)?github\.com/[a-zA-Z0-9_-]+$')
        if pattern.match(value) is None or len(value.strip()) == 0:
            raise ValueError("url is not a valid github username url")
        self.__github_url = value

"""
The setup.py file is essential part of packaging and destributing python project.
 It is used by setuptools to define the configuration of your proect, 
 such as its metadata, dependencies, and more.
"""

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    '''
        This file will return the list of requirements
    '''
    requirement_lst : List[str] =[]
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement= line.strip()
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst


setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Ayush Bhatt",
    author_email = "ayushbhatt.ml@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()

)
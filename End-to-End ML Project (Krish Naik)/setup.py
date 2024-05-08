# Writing all the code required in setup.py

# setuptools, a commonly used library for building and distributing Python packages.
from setuptools import find_packages, setup

HYPHEN_E_DOT = "-e ."  # ---> constant


def get_requirements(file_path: str) -> list(str):
    """
    This function will fetch the requirements for this project and return them in a list.
    """
    requirements = []
    with open(file_path, "r") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        # removing the '-e .' to get into libraries to isntall in setup.py
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="End-To-End ML Project",
    version="0.0.1",
    author="GyanDev",
    author_email="ramved.2018@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)


# Explainations ------>
# find_packages ----> gonna find all the packages used in your project you are making.
# It is really powerfull.

# install_requires ----> install all the packages, lib needed automatically.
# Now, in "install_requires" you cant possibly manually fill all the libaraies used in the project.
# Thats,why we are going to use "requirements.txt" file to do that for us by making a function named
# get_requirements().

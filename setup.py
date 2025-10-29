from pkg_resources import Requirement
from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    Requirements=[]
    with open(file_path) as file_obj:
        Requirements=file_obj.readlines()
        [req.replace("\n","") for req in Requirements]

        if HYPEN_E_DOT in Requirements:
            Requirements.remove(HYPEN_E_DOT)
setup(
    name="machine learning project",
    version="0.0.1",
    author="mounika veerapaga",
    author_gmail="veerapagamounika2@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")


)
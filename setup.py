from setuptools import setup , find_packages,Setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","")for req in requirements]
    

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)


    return requirements

setup(
    name="census-income",
       version="0.0.1",
       author="jyoti kapoor",
       author_email="jyotikpr999@gmail.com",
       packages=find_packages(),
       install_requires=get_requirements('requirements.txt')
      )
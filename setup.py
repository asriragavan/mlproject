from setuptools import find_packages,setup
from typing import List


Hypen_E_Dot="-e ."
def get_requirement(file_path:str)->List[str]:
    '''
    this will list of requirements
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if Hypen_E_Dot in requirements:
            requirements.remove(Hypen_E_Dot)

    return requirements

setup(

    name='MLPROJECT',
    version='0.0.1',
    author='sri',
    author_email='asriragavan86@gmail.com',
    packages=find_packages(),
    install_requires = get_requirement('requirements.txt')
)

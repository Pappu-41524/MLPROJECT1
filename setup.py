from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    
    requitements=[]
    with open(file_path) as file_obj:
        requitements=file_obj.readlines()
        requitements=[req.replace("\n","") for req in requitements]
        
        if HYPEN_E_DOT in requitements:
            requitements.remove(HYPEN_E_DOT)
    return requitements        
          
setup(
    name='MLProject',
    version='0.1.0',
    author='Pappu',
    author_email='pappu41524@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
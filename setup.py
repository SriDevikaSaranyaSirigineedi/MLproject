from setuptools import find_packages,setup

hypen_e_dot ='-e .'
def get_requirements(file_path:str):
    '''
    this function will return the list of requiements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements= [req.strip() for req in requirements]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements

setup(
name = 'MLproject',
version = '0.0.1',
author = 'Saranya',
author_email = 'devikasaranya1827@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)
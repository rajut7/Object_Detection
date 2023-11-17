from setuptools import setup, find_packages

setup(
    name='object_detection',
    version='0.0.0',
    author='Tadisetti Raju',
    author_email='tadisettiraju72@gmail.com',
    packages=find_packages(),
    install_requires=[
        'flask',
        'tqdm',
        'requests',  
    ],
   
)

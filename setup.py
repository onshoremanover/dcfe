
from setuptools import setup
setup(
        name = 'dcfe',
        version = '0.1.1',                
        packages = ['dcfe'],
        entry_points = {
            'console_scripts': [
                'dcfe = dcfe.__main__:main'
                ]
            })


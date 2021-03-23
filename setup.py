from setuptools import setup

setup(
    name='skribblio-cheater',
    version='0.1',
    py_modules=['skribblio-cheater'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts':[
        'cheater=skribblio_cheater:main',
        ],
    }
)
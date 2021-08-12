### NOT RUN YET #####
from setuptools import setup

setup(
    name="gg",
    version='0.1',
    py_modules=['gscli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        gg=gscli:gscli
    ''',
)
import setuptools
import distutils.core

setuptools.setup(
    name='json-leaves',
    version="1.2.1",
    author='@readwithai',
    long_description_content_type='text/markdown',
    author_email='talwrii@gmail.com',
    description='Extract the leaves from a JSON file and show the paths to said leaves',
    license='MIT',
    keywords='JSON,leaves,cli',
    url='https://github.com/talwrii/json-leaves',
    packages=["json_leaves"],
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts': ['json-leaves=json_leaves.main:main']
    },
)

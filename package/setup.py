from setuptools import setup, find_packages

setup(
    name='myproject',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A sample Python project',
    packages=find_packages(),
    install_requires=[
        'requests',
        'numpy',
        # Add other dependencies here
    ]
)


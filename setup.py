from setuptools import setup

setup(
    name='foxypool-docs',
    version='1.0.0',
    url='https://foxypool.io',
    license='GPLv3',
    author='Felix Brucker',
    author_email='contact@foxypool.io',
    description='Documentation for Foxy related services and tools',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires='>=3.11, <4',
    install_requires=[
        "mkdocs==1.6.1",
        "mkdocs-material==9.5.44",
        "mkdocs-minify-plugin==0.8.0",
        "mkdocs-redirects==1.2.2",
    ],
)

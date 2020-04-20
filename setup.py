from setuptools import find_packages, setup

with open('README.md', 'r') as fh:
    long_description = fh.read()


setup(
    name="notes_to_trello-snpardy", # Replace with your own username
    version="0.0.1",
    author="Sam Pardy",
    author_email="snpardy@gmail.com",
    description="A package to extract Trello cards from meeting notes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

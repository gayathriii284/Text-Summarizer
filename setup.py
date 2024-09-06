import setuptools

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()
    

# this information is used while publishing the package to PyPi.    
__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "gayathriii284"
SRC_REPO = "text-summarizer"
AUTHOR_EMAIL = "gayathripvt284@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A simple text summarizer using huggingface api",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"" : "src"},
    packages=setuptools.find_packages(where='src'),
    
)
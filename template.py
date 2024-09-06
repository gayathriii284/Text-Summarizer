import os
from pathlib import Path
import logging

# create the project name
project_name = "text-summarizer"

# set the configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# create a list of files that indicate the project structure
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

# now execute the template inorder to estabilish the project structure
for filepath in list_of_files:
    # since we need to ensure that the path specified is proper and for windows, use the Path library
    # here the windows path will be initialized with a forward slash instead of backwards
    path = Path(filepath)
    
    # get the file directory and the file name
    file_dir, file_name = os.path.split(path)
    logging.info(f"file_dir : {file_dir}, file_name : {file_name}")
    
    # check if the directory is non-empty
    if file_dir:
        # create the file directory
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory : {file_dir}")
        
    # after creating the directory, create the file if it does not exist
    if (not os.path.exists(filepath)):
        # create the file
        with open(filepath, "w") as f:
            logging.info(f"Creating file : {file_name}")
    else:
        logging.info(f"File {file_name} already exists")





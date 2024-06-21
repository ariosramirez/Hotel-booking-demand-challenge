#!/bin/bash

echo "Setting readonly /app..."
readonly ROOT_DIRECTORY="/app"
echo "Setting readonly /app DONE!"

# Init
echo "cd to ROOT_DIRECTORY..."
cd $ROOT_DIRECTORY
echo "cd to ROOT_DIRECTORY... DONE!"


echo "Installing pip dependencies..."
touch requirements.txt
pip install -v -r requirements.txt
echo "Installing pip dependencies Done!"


echo "Config JupyterLab..."
# Config JupyterLab
jupyter-lab --generate-config
echo $CONFIG >> ~/.jupyter/jupyter_notebook_config.py
echo "Config JupyterLab... Done!"

echo "Building JupyterLab..."
jupyter lab build
echo "Building JupyterLab... Done!"

# Run Lab
echo "Running Lab"
jupyter lab --ip=0.0.0.0 --NotebookApp.allow_origin='*' --NotebookApp.quit_button='False' \
  --NotebookApp.notebook_dir=$ROOT_DIRECTORY/ --no-browser --allow-root

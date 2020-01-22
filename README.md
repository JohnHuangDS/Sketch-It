# Sketch It! A Machine Learning Drawing Game

## Overview
Sketch It is a machine learning drawing game that I made for my capstone project during my Data Science Diploma program at BrainStation.  The inspiration comes from Quick Draw by Google ([https://quickdraw.withgoogle.com/](https://quickdraw.withgoogle.com/)).  

In Sketch It, the player is tasked with drawing a certain object on paper for each level.  The player places the drawing infront of a camera.  If the object is correctly drawn, the player will be able to move onto the next level.  

## Jupyter Notebooks
There are 4 Jupyter Notebooks to explain the workflow/thought processes behind creating the game.  
1. Exploring the Data set - A look at the data set that will use to train classification models  
2. Logistic Regression - The first classification model, used for its simplicity.  
3. CNN - Convolutional Neural Networking using Keras to achieve higher test accuracy (95.6%).  
From this notebook, we create the models that will be used in the Demo (CNN_model.json, CNN_model.h5)


## Demo Folder
To run Sketch It on your own computer, download the demo folder.  
Create a virtual enviroment and install the requirements with the following command in terminal:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; pip install -r requirements.txt  
Run the game with:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; python sketch_it.py  

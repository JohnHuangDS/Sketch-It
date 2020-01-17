# Sketch It! A Machine Learning Drawing Game

## Overview
Sketch It is a machine learning drawing game that I made for my capstone project during my Data Science Diploma program at BrainStation.  The inspiration comes from Quick Draw by Google ([https://quickdraw.withgoogle.com/](https://quickdraw.withgoogle.com/)).  

In Sketch It, the player is tasked with drawing a certain object on paper for each level.  The player places the drawing infront of a camera.  If the object is correctly drawn, the player will be able to move onto the next level.

## Jupyter Notebooks
There are 4 Jupyter Notebooks to explain the workflow/thought processes behind creating the game.
1. Exploring the Data set - A look at the data set that will use to train classification models
2. Logistic Regression - Logistic Regression, used for its simplicity and computational speed
3. CNN - CNN using Keras to achieve higher test accuracy (95.6%)
4. Building Functions - Functions used to track images through a webcam, and to process and predict images drawn by the user.

## Demo Folder
There are 4 files in this folder.
1. demo_game.py - running this file will start the game
2. test_functions.py - this file contains all the functions that are used in demo_game.py
3. CNN_model.json -CNN model stored as a json file, loaded when demo_game.py is run
4. CNN_model.h5 - weights of the CNN model, loaded when demo_game.py is run

### to be completed
1. Instructions on how to install packages and dependencies to work on other computers

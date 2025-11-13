# FlowQ
This repo contains the code for my MLOPs experiments using DVC to track data and Mlflow for model registry.

# What's MLOPs
When building machine learning models, at scale, isn't enough to build jupyter notebook and export the model. You need tracking every parameter, keep improving the model performance, to prevent the lost of performance.

<img width="705" height="311" alt="image" src="https://github.com/user-attachments/assets/9f5a8893-73c7-41b7-ba79-d435b0819cb8" />

MLOPs set the rules, so we can make this process efficient, for exemplo, run the pipeline (process data, train, evaluate) all your code. Each one of those, play a different and importat role on your project.

## DVC
DVC plays the role of tracking every variation of data we can possible create. In your case, this data are data_00, data_01. We cambine both on combined_data, finally you need a preprocessed version of our Yahoo-Question data.

## MLFLOW
With the help of Mlflow we can tracking every experiment we can possibly make. It provides a UI where we can label and visualize and metrics, model and most efficient parameters.

# NLP modeling


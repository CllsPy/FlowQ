# FlowQ
This repo contains the code for my MLOPs experiments using DVC to track data and Mlflow for model registry.

## What's MLOPs
When building machine learning models, at scale, isn't enough to build jupyter notebook and export the model. You need tracking every parameter, keep improving the model performance, to prevent the lost of performance. MLOPs set the rules, so we can make this process efficient, for exemplo, run the pipeline (process data, train, evaluate) all your code. Each one of those, play a different and importat role on your project.

<img width="705" height="311" alt="image" src="https://github.com/user-attachments/assets/9f5a8893-73c7-41b7-ba79-d435b0819cb8" />

The process of developing an ML system looks more like a cycle with a lot of back and forth between steps (src: ML systems - Chip Huyen)


### DVC
DVC plays the role of tracking every variation of data we can possible create. In your case, this data are data_00, data_01. We cambine both on combined_data, finally you need a preprocessed version of our Yahoo-Question data.

<img width="320" height="288" alt="image" src="https://github.com/user-attachments/assets/77c4975f-d595-425a-a263-d114a20b4a62" />

### MLFLOW
With the help of Mlflow we can tracking every experiment we can possibly make. It provides a UI where we can label and visualize and metrics, model and most efficient parameters.

<img width="612" height="513" alt="image" src="https://github.com/user-attachments/assets/350aacdd-2a47-40bf-be54-41191f78aed7" />

## NLP 

### Exploratory Data Analysis
I start exploring all data, checking for stranger charcteres, emojis, null values. Eda help us with understanting the data we have, so we can make better decisions, latter.

### Modeling
I start with MutinominalNB, which is great for text classifical, but before deep dive into modeling. A went trought each step on NLP projects. For exemplo, after plotting every class a really we don't have any problem with class imbalanced.

- data cleaning
- tokenização
- lemmatization or stemming

<img width="556" height="435" alt="image" src="https://github.com/user-attachments/assets/4b0696e9-b52d-4203-83b8-985d98513a3a" />

All those steps help us improve data quality, so it implies better result. At the end we got a classification report like this:

<img width="511" height="359" alt="image" src="https://github.com/user-attachments/assets/9aeba9fc-52aa-4480-b254-008442c7a240" />

To build the model I used scit-learning and for hyperparamenter otimization gridsearch. Didn't search for too long, since my focus was on enhace data quality and avoid tweeking models.

## Citation

```
@misc{Carlos2025FlowQ,
  author = {Lima, Carlos},
  title = {FlowQ},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/CllsPy/FlowQ}},
}
```


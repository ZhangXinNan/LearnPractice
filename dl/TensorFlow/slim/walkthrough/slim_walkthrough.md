TF-Slim Walkthrough


## 0 Table of contents
* Installation and setup
* Creating your first neural network with TF-Slim
* Reading Data with TF-Slim
* Training a convolutional neural network (CNN)
* Using pre-trained models

## 1 Installation and setup
自从TF 1.0后，slim已经在tf.contrib.slim中获取到。
```
python -c "import tensorflow.contrib.slim as slim; eval = slim.evaluation.evaluate_once"
```

## 2 Creating your first neural network with TF-Slim

### 2.1 Let's create the model and examine its structure.
### 2.2 Let's create some 1d regression data .
### 2.3 Let's fit the model to the data
### 2.4 Training with multiple loss functions.
### 2.5 Let's load the saved model and use it for prediction.
### 2.6 Let's compute various evaluation metrics on the test set.


## 3 Reading Data with TF-Slim
### 3.1 Dataset

### 3.2 DatasetDataProvider

### 3.3 Demo: The Flowers Dataset

### 3.4 Download the Flowers Dataset

### 3.5 Display some of the data


## 4 Training a convolutional neural network (CNN)
### 4.1 Define the model.
### 4.2 Apply the model to some randomly generated images.
### 4.3 Evaluate some metrics.
### 4.4 

## 5 Using pre-trained models
### 5.1 Download the Inception V1 checkpoint
### 5.2 Apply Pre-trained Inception V1 model to Images.
### 5.3 Download the VGG-16 checkpoint
### 5.4 Apply Pre-trained VGG-16 model to Images.
### 5.5 Fine-tune the model on a different set of labels.
### 5.6 Apply fine tuned model to some images.

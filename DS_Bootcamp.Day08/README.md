# Intro to Machine Learning  

**Summary** – This repository contains a series of practical exercises that introduce the basic concepts and tasks in machine‑learning using Python.

## Contents  

1. [Exercise 00 – Binary classifier](#exercise-00---binary-classifier)  
2. [Exercise 01 – Decision boundaries](#exercise-01---decision-boundaries)  
3. [Exercise 02 – Multiclass classification](#exercise-02---multiclass-classification)  
4. [Exercise 03 – Overfitting & validation](#exercise-03---overfitting--validation)  
5. [Exercise 04 – Regression](#exercise-04---regression)  
6. [Exercise 05 – Clustering](#exercise-05---clustering)  


---  

### Exercise 00 – Binary classifier  

**Turn‑in directory:** `ex00/`  
**File to submit:** `00_binary_classifier_logreg.ipynb`  
**Allowed functions:** no restrictions  

In this task you will build a binary classifier that predicts whether a commit was made on a working day or on a weekend.  
You will practice **feature engineering** by extracting useful information from timestamps (e.g., number of commits before/after midday).  
The exercise covers:

* Supervised learning basics – features (`X`) and target (`y`).  
* Difference between classification (categorical target) and regression (continuous target).  
* Simple logistic‑regression model training and evaluation.  



### Exercise 01 – Decision boundaries  

**Turn‑in directory:** `ex01/`  
**File to submit:** `01_binary_classifier_svm_tree.ipynb`  
**Allowed functions:** no restrictions  

Now you will compare three algorithms:

* Logistic regression  
* Support‑Vector Machine (SVM)  
* Decision tree  

The notebook visualises the decision boundaries of each model, letting you see how they separate the classes and how model complexity influences performance.



### Exercise 02 – Multiclass classification  

**Turn‑in directory:** `ex02/`  
**File to submit:** `02_multiclassi_one-hot.ipynb`  
**Allowed functions:** no restrictions  

Real‑world problems often have more than two classes. In this exercise you will:

* Train a multiclass classifier (e.g., using one‑vs‑rest or softmax).  
* Encode categorical features with one‑hot encoding.  
* Explore feature importance for several algorithms, including a random‑forest model.  

The goal is to predict the weekday of a commit using a richer set of predictors (author, time, laboratory, number of attempts, etc.).



### Exercise 03 – Overfitting & validation  

**Turn‑in directory:** `ex03/`  
**File to submit:** `03_split_crossval.ipynb`  
**Allowed functions:** no restrictions  

You will learn how to obtain reliable performance estimates:

* **Train‑test split** – keep a hold‑out set for final evaluation.  
* **Cross‑validation** – repeatedly split the data to assess model stability.  

The notebook demonstrates how overfitting can inflate accuracy when the same data is used for training and testing, and shows techniques to mitigate it.



### Exercise 04 – Regression  

**Turn‑in directory:** `ex04/`  
**File to submit:** `04_regression.ipynb`  
**Allowed functions:** no restrictions  

Switching to a regression problem, you will predict the average time delta between task deadlines and the first commit for each user.  
Features include user activity metrics such as news‑feed views and number of commits.  
You will experiment with linear regression and other regression models, evaluate them with appropriate metrics (RMSE, MAE), and interpret the results.



### Exercise 05 – Clustering  

**Turn‑in directory:** `ex05/`  
**File to submit:** `05_clustering.ipynb`  
**Allowed functions:** no restrictions  

The final exercise introduces unsupervised learning. You will:

* Apply clustering algorithms (e.g., K‑means, hierarchical clustering) to segment users into homogeneous groups.  
* Analyse cluster characteristics to inform possible future engagement strategies.  

The focus is on interpreting the clusters rather than predicting a target variable.

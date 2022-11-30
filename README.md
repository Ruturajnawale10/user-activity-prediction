# user-activity-prediction

## Team members:
### Rajat Prashant Masurkar
### Utkarsh Pant
### Roshan Chokshi
### Ruturaj Nawale

## Project Description:
#### The objective of the project is to predict the activity of a user from the sensors attached to the user’s torso, hands, and legs. There are 19 user activities such as walking, running on a treadmill, sitting, rowing, jumping, playing basketball, etc. There are 9 sensors from which the data is captured. Each of total of 8 users performs each activity for 5 minutes. There will be many features of all the activities, and the goal would be to minimize these features to achieve maximum efficiency in the prediction models.

## Proposed Methodology:
#### Firstly we scanned the input data and put appropriate activity labels to the training dataset. We standardized the data using StandardScaler. Then we tried using Dimensional reduction techniques such as PCA, but the performance did not improve by that. Further, we would apply classifiers such as Naive Bayes, KNN, Random Forest to train the model. This model can then be used to predict a user’s activity such as running or walking based on the data captured from the sensors attached to the user.

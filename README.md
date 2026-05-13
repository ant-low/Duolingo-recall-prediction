# Duolingo-recall-prediction

This project models memory decay in English language learners using a dataset of 13 million learning traces. It compares Logistic Regression and Random Forest algorithms to predict word recall success based on the "Spacing Effect".  
# Key Engineering Highlights
Big Data Processing: 
Implemented a chunking strategy to process 13 million rows of raw data in blocks of 500,000.  
Feature Engineering: 
* Applied Logarithmic Transformations to handle extreme right-skewness in time-gap data.
* Calculated history_success_rate to compress historical sightings into a bounded range.
Class Imbalance Mitigation:
Addressed a significant success bias (83.7% success rate) by using Balanced Class Weights and Hyperparameter Tuning.

# Technical Implementation
The core prediction uses a Sigmoid function mapping for probability:$$f(x) = \frac{1}{1 + e^{-(c_1 x + c_2)}}$$  

# Results
The tuned Random Forest model was able to proactively identify nearly 40% of all memory failures, outperforming the linear baseline which struggled with the imbalanced nature of the dataset.
This project models memory decay in English language learners using a dataset of 13 million learning traces.  

📊 Data AccessDue to GitHub's file size limits, the raw Duolingo dataset is not included here.
* Download: Duolingo Dataset on Kaggle * Setup: Place learning_traces.zip in the /data folder to run the analysis.

# Duolingo Language Recall Prediction

This project presents a predictive model on student recall of English language vocabulary. It utilizes approximately 13 million learning traces from the Duolingo spaced-repetition dataset to estimate the probability that a learner will successfully recall a word.

---

## Key Engineering Highlights

* **Big Data Processing:** Implemented a chunking strategy with a size of 500,000 to process 13 million rows of raw data efficiently.
* **Feature Engineering:**
    * **Logarithmic Transformations:** Applied `delta_log` to normalize the "delta" feature, addressing extreme right-skewness and outliers in the time-gap data.
    * **History Success Rate:** Developed a `history_success_rate` feature (ratio of successful past reviews to total sightings) to compress practice history into a bounded range.
* **Class Imbalance Mitigation:** Addressed a success bias where 83.7% of traces were successful recalls. This was managed using **Balanced Class Weights** to penalize misclassifications of the minority (Forgot) class.

---

## Technical Implementation

The project contrasts a linear baseline (**Logistic Regression**) against a non-linear algorithm (**Random Forest**). 

### Logistic Regression
Used as a benchmark for interpretability. It utilizes a Sigmoid Function to map real-valued features into a recall probability:

$$f(x) = \frac{1}{1 + e^{-(c_1 x + c_2)}}$$





### Random Forest
Selected for its ability to capture non-linear nuances discovered during exploratory data analysis.





---

## Results

* **Baseline Performance:** Logistic Regression achieved 84.1% test accuracy but failed to identify nearly every case where a student forgot a word.
* **Tuned Random Forest:** The optimized model was significantly more effective, proactively identifying nearly **40% of all memory failures**.
* **Generalization:** By tuning tree depth to 12, the gap between training and testing accuracy was closed, ensuring the model's ability to generalize to unseen data.

---

## Data Access

Due to GitHub's file size limits, the raw dataset is not included in this repository.

* **Download:** [Duolingo Spaced Repetition Data (Kaggle)](https://www.kaggle.com/datasets/aravinii/duolingo-spaced-repetition-data)
* **Setup:** Place the `learning_traces.zip` file inside the `/data` folder to run the notebook analysis.

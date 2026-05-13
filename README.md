# Duolingo Language Recall Prediction

[cite_start]This project presents a predictive model on student recall of English language vocabulary[cite: 931, 933]. [cite_start]It utilizes approximately 13 million learning traces from the Duolingo spaced-repetition dataset to estimate the probability that a learner will successfully recall a word[cite: 934, 978].

---

## 🛠️ Key Engineering Highlights

* [cite_start]**Big Data Processing:** Implemented a chunking strategy with a size of 500,000 to process 13 million rows of raw data efficiently[cite: 21, 978].
* **Feature Engineering:**
    * [cite_start]**Logarithmic Transformations:** Applied `delta_log` to normalize the "delta" feature, addressing extreme right-skewness and outliers in the time-gap data[cite: 568, 1044].
    * [cite_start]**History Success Rate:** Developed a `history_success_rate` feature (ratio of successful past reviews to total sightings) to compress practice history into a bounded range[cite: 570, 1050].
* [cite_start]**Class Imbalance Mitigation:** Addressed a success bias where 83.7% of traces were successful recalls[cite: 1032]. [cite_start]This was managed using **Balanced Class Weights** to penalize misclassifications of the minority (Forgot) class[cite: 1123, 1157].

---

## 💻 Technical Implementation

[cite_start]The project contrasts a linear baseline (**Logistic Regression**) against a non-linear algorithm (**Random Forest**)[cite: 935]. 

### Logistic Regression
[cite_start]Used as a benchmark for interpretability[cite: 1108]. It utilizes a Sigmoid Function to map real-valued features into a recall probability:

$$f(x) = \frac{1}{1 + e^{-(c_1 x + c_2)}}$$



[Image of Basic Sigmoid Function]


### Random Forest
[cite_start]Selected for its ability to capture non-linear nuances discovered during exploratory data analysis[cite: 965, 1122].



[Image of Random Forest diagram]


---

## 📈 Results

* [cite_start]**Baseline Performance:** Logistic Regression achieved 84.1% test accuracy [cite: 1151] [cite_start]but failed to identify nearly every case where a student forgot a word[cite: 1152].
* [cite_start]**Tuned Random Forest:** The optimized model was significantly more effective, proactively identifying nearly **40% of all memory failures**[cite: 1182].
* [cite_start]**Generalization:** By tuning tree depth to 12 [cite: 1177][cite_start], the gap between training and testing accuracy was closed, ensuring the model's ability to generalize to unseen data[cite: 1181].

---

## 📥 Data Access

Due to GitHub's file size limits, the raw dataset is not included in this repository.

* **Download:** [Duolingo Spaced Repetition Data (Kaggle)](https://www.kaggle.com/datasets/aravinii/duolingo-spaced-repetition-data)
* **Setup:** Place the `learning_traces.zip` file inside the `/data` folder to run the notebook analysis.
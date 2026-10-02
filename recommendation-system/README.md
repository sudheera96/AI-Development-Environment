# SmartMovie Recommender

A course project that implements a movie recommendation system as a Flask web application. The system recommends movies based on the content of a selected movie and incorporates a popularity component into the final ranking.

## Project Overview

The application allows a user to enter or select a movie title. The recommendation engine:

1. Reads the movie dataset.
2. Combines movie title, genres, and overview into a text representation.
3. Converts the text into numerical features using TF-IDF.
4. Calculates cosine similarity between movies.
5. Adds a normalized popularity component based on the available movie rating.
6. Produces a hybrid ranking.
7. Displays the top six recommendations through a Flask web interface.

## Recommendation Approach

This project uses a **content-based recommendation approach with a popularity component**.

### Content Representation

Title, genres, and overview are combined and processed with scikit-learn's `TfidfVectorizer`.

The implementation uses:
- English stop-word removal
- Unigrams and bigrams
- TF-IDF weighting

### Cosine Similarity

Cosine similarity measures how similar the TF-IDF representations of movies are. Movies with more similar textual descriptions receive higher content-similarity scores.

### Popularity Component

The dataset contains a `rating` field rather than direct behavioral measures such as views, users, or purchases. Therefore, the movie rating is used as a **proxy for popularity**. The rating values are normalized before being incorporated into the ranking.

### Hybrid Ranking

```text
Final Score = 0.82 × Content Similarity + 0.18 × Popularity
```

The 82% and 18% weights are manually selected design parameters for this course project; they are not learned from a training process. The selected movie itself is excluded from the recommendation results.

## Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Cosine similarity
- HTML/CSS

## Dataset

The project uses a small, reproducible movie dataset at `data/movies.csv`.

Fields:
- `title`
- `genres`
- `overview`
- `year`
- `rating`

Because the dataset is intentionally small, this project demonstrates the recommendation workflow rather than production-scale recommendation quality.

## Project Modifications and Original Work

The project was informed by the course lecture and the public examples listed below. The implementation was adapted rather than copied as a complete solution.

Project-specific work includes:
- Flask/browser interface
- Dedicated `Recommender` class
- TF-IDF over title, genre, and overview
- Unigram and bigram features
- Cosine similarity
- Normalized popularity component
- Hybrid 82/18 ranking
- Exact and partial title matching
- Unknown-title handling
- Browser required-field validation
- Reproducible local movie dataset

## Project Structure

```text
recommendation-system/
├── app.py
├── recommender.py
├── requirements.txt
├── README.md
├── data/
│   └── movies.csv
├── templates/
│   └── index.html
└── .gitignore
```

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```text
.venv\\Scripts\\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Example Results

For **The Matrix**, the system returned:
1. Inception
2. The Dark Knight
3. Interstellar
4. The Matrix Reloaded
5. Batman Begins
6. The Martian

The ranking is generated from the hybrid recommendation score.

## Testing Performed

The application was tested with:
- The Matrix — recommendations returned
- Inception — recommendations returned
- Interstellar — recommendations returned
- Matrix — partial title successfully matched The Matrix
- Avatar — unknown title handled with a clear message
- Empty input — browser required-field validation
- Direct Python Recommender test — results matched the Flask workflow

## Evaluation

The project uses functional testing rather than claiming a statistical accuracy percentage. The dataset is small and does not contain historical user interactions or labeled user preferences that could provide reliable ground truth.

Formal measures such as Precision@K, Recall@K, Hit Rate, NDCG, diversity, and behavioral acceptance could be added with a larger dataset and appropriate interaction data.

## Limitations

1. Small dataset.
2. Rating is a proxy for popularity rather than a direct behavioral popularity measure.
3. No collaborative filtering or user-history personalization.
4. Hybrid weights are manually selected rather than learned.
5. Limited production-scale evaluation.

## Future Improvements

Future versions could:
- Use a larger movie dataset.
- Add user viewing/rating histories.
- Add collaborative filtering.
- Add explicit behavioral popularity measures.
- Learn ranking weights from validation data.
- Add Precision@K, Recall@K, Hit Rate, or NDCG evaluation.
- Measure recommendation diversity.
- Add conversational recommendation.
- Incorporate additional context such as user preferences and viewing history.

## Attribution and Learning Resources

### Course Lecture

MSI 631 course lecture on recommendation systems and AI HCI:
https://youtu.be/INhSJsnoUgk

### Example GitHub Project

shyam1998, **Movie-Recommendation-System-GUI**:
https://github.com/shyam1998/Movie-Recommendation-System-GUI

### Medium Part 1

Gabriele Albini, **Building a movie recommender web app from scratch with SVD and Flask — Part 1**:
https://gabri-albini.medium.com/building-a-movie-recommender-web-app-from-scratch-with-svd-and-flask-part-1-ff4d39b837ea

### Medium Part 2

Gabriele Albini, **Building a movie recommender web app from scratch with SVD and Flask — Part 2**:
https://gabri-albini.medium.com/building-a-movie-recommender-web-app-from-scratch-with-svd-and-flask-part-2-ba8a7b34b020

### Apriori Resource

Chonyy, **Apriori — Association Rule Mining In-depth Explanation and Python Implementation**:
https://towardsdatascience.com/apriori-association-rule-mining-explanation-and-python-implementation-290b42afdfc6

## Academic Integrity and Project Attribution

The external resources above were used as learning references and examples. The repository documents the specific modifications made for this course project rather than presenting an external implementation as original work.

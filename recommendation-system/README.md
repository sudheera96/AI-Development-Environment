# SmartMovie Recommender

Course project: an independent Flask movie recommender inspired by the course resources.

## Foundation and attribution
- shyam1998, Movie-Recommendation-System-GUI: https://github.com/shyam1998/Movie-Recommendation-System-GUI
- Gabriele Albini, Building a movie recommender web app from scratch with SVD and Flask, Parts 1 and 2:
  - https://gabri-albini.medium.com/building-a-movie-recommender-web-app-from-scratch-with-svd-and-flask-part-1-ff4d39b837ea
  - https://gabri-albini.medium.com/building-a-movie-recommender-web-app-from-scratch-with-svd-and-flask-part-2-ba8a7b34b020
- Chonyy, Apriori — Association Rule Mining In-depth Explanation and Python Implementation:
  - https://towardsdatascience.com/apriori-association-rule-mining-explanation-and-python-implementation-290b42afdfc6

This implementation is not a copy of the source implementation. It changes the interface to Flask/web, uses TF-IDF across title/genre/overview, and blends content similarity with a normalized popularity signal.

## Run

```bash
python -m venv .venv
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in a browser.

## Project files
- `app.py` — Flask interface and request handling
- `recommender.py` — TF-IDF, cosine similarity, and hybrid ranking
- `data/movies.csv` — small reproducible movie dataset
- `templates/index.html` — browser interface
- `requirements.txt` — Python dependencies

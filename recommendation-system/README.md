# SmartMovie Recommender

Course project: an independent Flask movie recommender inspired by the course references.

## Foundation and attribution
- shyam1998, Movie-Recommendation-System-GUI: https://github.com/shyam1998/Movie-Recommendation-System-GUI
- Gabriele Albini, Building a movie recommender web app from scratch with SVD and Flask, Parts 1 and 2.

This implementation is not a copy of the source implementation. It changes the interface to Flask/web, uses TF-IDF across title/genre/overview, and blends content similarity with a normalized popularity signal.

## Run
python -m venv .venv
pip install -r requirements.txt
python app.py

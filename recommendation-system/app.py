from flask import Flask, render_template, request
from recommender import Recommender

app = Flask(__name__)
recommender = Recommender("data/movies.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    query = ""
    recommendations = []
    message = "Choose a movie to see recommendations."
    if request.method == "POST":
        query = request.form.get("movie", "").strip()
        recommendations = recommender.recommend(query, top_n=6)
        if not recommendations:
            message = "Movie not found. Try another title."
        else:
            message = f"Recommendations based on “{query}”."
    return render_template(
        "index.html",
        movies=recommender.titles,
        query=query,
        recommendations=recommendations,
        message=message,
    )

if __name__ == "__main__":
    app.run(debug=True)

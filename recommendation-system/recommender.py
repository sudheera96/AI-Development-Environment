import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Recommender:
    def __init__(self, path):
        self.df = pd.read_csv(path)
        self.df["genres"] = self.df["genres"].fillna("")
        self.df["overview"] = self.df["overview"].fillna("")
        self.df["year"] = self.df["year"].fillna(0).astype(int)

        # Modified design:
        # combine title + genre + overview text with TF-IDF.
        text = (
            self.df["title"]
            + " "
            + self.df["genres"].str.replace("|", " ", regex=False)
            + " "
            + self.df["overview"]
        )
        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2),
            min_df=1,
        )
        self.matrix = self.vectorizer.fit_transform(text)
        self.sim = cosine_similarity(self.matrix)

        # Small popularity component for the final hybrid ranking.
        pop = self.df["rating"].fillna(self.df["rating"].median())
        self.popularity = (
            (pop - pop.min()) / (pop.max() - pop.min() + 1e-9)
        )

        self.titles = self.df["title"].tolist()
        self.lookup = {title.lower(): i for i, title in enumerate(self.titles)}

    def recommend(self, title, top_n=6):
        idx = self.lookup.get(title.lower())

        if idx is None:
            matches = [
                i for i, value in enumerate(self.titles)
                if title.lower() in value.lower()
            ]
            if not matches:
                return []
            idx = matches[0]

        scores = 0.82 * self.sim[idx] + 0.18 * self.popularity.to_numpy()
        scores[idx] = -1

        order = np.argsort(scores)[::-1]
        results = []

        for i in order[:top_n]:
            row = self.df.iloc[i]
            results.append(
                {
                    "title": row["title"],
                    "genres": row["genres"].replace("|", ", "),
                    "year": int(row["year"]),
                    "rating": round(float(row["rating"]), 1),
                    "score": round(float(scores[i]), 3),
                }
            )

        return results

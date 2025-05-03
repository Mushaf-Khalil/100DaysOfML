import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import re
from sklearn.metrics.pairwise import cosine_similarity # You might need this if not directly in loaded data

app = Flask(__name__)
CORS(app)

MODEL_PATH = 'backend/movie_recommendation_model.pkl'  # Adjust the path to your model file

model_data = None
try:
    with open(MODEL_PATH, 'rb') as file:
        model_data = pickle.load(file)
    print("Model data loaded successfully!")
except FileNotFoundError:
    print(f"Error: Model file not found at {MODEL_PATH}")
except Exception as e:
    print(f"Error loading model data: {e}")

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    if not model_data:
        return jsonify({"error": "Model data not loaded"}), 500

    try:
        data = request.get_json()
        if not data or 'movie_title' not in data:
            return jsonify({"error": "Missing 'movie_title' in request body"}), 400
        movie_title = data['movie_title']

        cosine_sim = model_data.get('cosine_sim')
        movies_list = model_data.get('movies')
        indices_dict = model_data.get('indices')

        if cosine_sim is None or movies_list is None or indices_dict is None:
            return jsonify({"error": "Incomplete model data loaded"}), 500

        movies_df = pd.DataFrame(movies_list)
        indices = pd.Series(indices_dict)

        processed_title = re.sub(r'[- ]', '', movie_title).lower()

        if processed_title not in indices:
            return jsonify({"error": f"Movie '{movie_title}' not found. Please try a different spelling."}), 404

        idx = indices[processed_title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]  # Get the top 10 most similar movies (excluding the movie itself)
        movie_indices = [i[0] for i in sim_scores]
        recommendations = movies_df['title'].iloc[movie_indices].tolist()

        return jsonify({"recommendations": recommendations})

    except Exception as e:
        return jsonify({"error": f"Error generating recommendations: {e}"}), 500

if __name__ == '__main__':
    # --- Simple test within the API ---
    if model_data:
        test_title = "spiderman"
        processed_test_title = re.sub(r'[- ]', '', test_title).lower()
        if processed_test_title in model_data.get('indices', {}):
            idx = model_data['indices'][processed_test_title]
            cosine_sim = model_data['cosine_sim']
            movies_df = pd.DataFrame(model_data['movies'])
            sim_scores = list(enumerate(cosine_sim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            top_indices = [i[0] for i in sim_scores[1:6]] # Top 5 recommendations
            test_recommendations = movies_df['title'].iloc[top_indices].tolist()
            print("\n--- API Test ---")
            print(f"Recommendations for '{test_title}': {test_recommendations}")
            print("--- End of API Test ---")
        else:
            print("\n--- API Test ---")
            print(f"Test movie '{test_title}' not found in indices.")
            print("--- End of API Test ---")
    else:
        print("\n--- API Test ---")
        print("Model data not loaded, skipping API test.")
        print("--- End of API Test ---")

    app.run(debug=True)
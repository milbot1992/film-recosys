from flask import Flask
from users import user_api
from recommendations import recommendation_api
from top_movies import top_movies_api
from ..utils.preprocess_utils import load_and_preprocess_data

app = Flask(__name__)

# Load and preprocess data
processed_data, collab_df = load_and_preprocess_data()

# Register blueprints
app.register_blueprint(user_api)
app.register_blueprint(recommendation_api)
app.register_blueprint(top_movies_api)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask_cors import CORS
from api.users import create_user_api
from api.recommendations import create_recommendation_api
from api.trending_now import trending_now_api
from utils.preprocess_utils import load_and_preprocess_data

app = Flask(__name__)
CORS(app)

# Load and preprocess data
collab_df = load_and_preprocess_data()

# Register blueprints
app.register_blueprint(create_user_api(collab_df))
app.register_blueprint(create_recommendation_api(collab_df))
app.register_blueprint(trending_now_api)

if __name__ == '__main__':
    app.run(debug=True)

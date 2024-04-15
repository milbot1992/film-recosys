from flask import Blueprint, jsonify
from models.collab_recommendation import user_based_collaborative_filtering

recommendation_api_blueprint = Blueprint('recommendation_api', __name__)

def create_recommendation_api(collab_df):
    users_choice, common = user_based_collaborative_filtering(collab_df)

    @recommendation_api_blueprint.route('/recommendations/<int:user_id>', methods=['GET'])
    def get_recommendations(user_id):
        try:
            user_favourite_films_df = users_choice(user_id)
            user_favourite_films = user_favourite_films_df.to_dict(orient='records')
            recommended_films = common(user_id)
            return jsonify({'user_favourite_films': user_favourite_films, 'recommended_films': recommended_films})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return recommendation_api_blueprint

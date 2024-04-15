from flask import Blueprint, jsonify

user_api_blueprint = Blueprint('user_api', __name__)

def create_user_api(collab_df):
    @user_api_blueprint.route('/user_ids', methods=['GET'])
    def get_user_ids():
        try:
            user_ids = collab_df['userId'].unique().tolist()
            return jsonify({'user_ids': user_ids})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return user_api_blueprint

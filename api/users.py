from flask import Blueprint, jsonify
import pandas as pd

user_api = Blueprint('user_api', __name__)

@user_api.route('/user_ids', methods=['GET'])
def get_user_ids():
    try:
        user_ids = collab_df['userId'].unique().tolist()
        return jsonify({'user_ids': user_ids})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
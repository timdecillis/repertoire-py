# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     print('Visited localhost:3000')
#     return 'Hello, World!'

# if __name__ == '__main__':
#     print('Starting the Flask server')
#     app.run(port=3000)


from flask import Flask, render_template, request, jsonify, send_from_directory
import os

app = Flask(__name__)


# from controllers import get_songs, add_song, delete_song, create_user

import logging
logger = logging.getLogger(__name__)

# # Serve static files from the 'client/dist' directory


@app.route('/')
def serve_index():
    dist_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'client', 'dist'))
    return send_from_directory(dist_dir, 'index.html')

# @app.route('/findBand', methods=['POST'])
# def find_band():
#     try:
#         data = request.get_json()
#         result = find_band(data)
#         return jsonify(result)
#     except Exception as e:
#         return jsonify({'error': str(e)})

# @app.route('/users', methods=['POST'])
# def create_user():
#     try:
#         data = request.get_json()
#         create_user(data)
#         return '', 201  # HTTP 201 Created
#     except Exception as e:
#         return jsonify({'error': str(e)})

# @app.route('/addSong', methods=['POST'])
# def add_song():
#     try:
#         data = request.get_json()
#         add_song(data)
#         return '', 201  # HTTP 201 Created
#     except Exception as e:
#         return jsonify({'error': str(e)})

# @app.route('/getSongs', methods=['GET'])
# def get_songs():
#     try:
#         result = get_songs()
#         return jsonify(result)
#     except Exception as e:
#         return jsonify({'error': str(e)})

# @app.route('/deleteSong', methods=['DELETE'])
# def delete_song():
#     try:
#         data = request.get_json()
#         delete_song(data)
#         return '', 203  # HTTP 203 Non-Authoritative Information
#     except Exception as e:
#         return jsonify({'error': str(e)})

# @app.route('/updateSong', methods=['PUT'])
# def update_song():
#     try:
#         data = request.get_json()
#         update_song(data)
#         return '', 202  # HTTP 202 Accepted
#     except Exception as e:
#         return jsonify({'error': str(e)})

# @app.route('/updateNotes', methods=['PUT'])
# def update_notes():
#     try:
#         data = request.get_json()
#         update_notes(data)
#         return '', 202  # HTTP 202 Accepted
#     except Exception as e:
#         return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.debug = True
    print('Starting the Flask server')
    app.run(port=3000)
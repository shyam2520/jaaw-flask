from flask import Blueprint, jsonify , request
import requests
routes_blueprint = Blueprint('routes', __name__)

API_BASE_URL = "https://animetize-api.vercel.app/"

@routes_blueprint.route('/')
def index():
    return jsonify({'message': 'server is running!'}),200 


@routes_blueprint.route('/healthz')
def healthz():
    return jsonify({'message': 'server is healthy!'}),200


@routes_blueprint.route('/search')
def searchAnime():
    anime_name = request.args.get('character') # get the character query parameter
    try:
        if(anime_name == None):
            return jsonify({'error': 'character query parameter is required'}),400
        response = requests.get(API_BASE_URL+anime_name)
        return jsonify(response.json()),200
    except Exception as e:
        return jsonify({'error': str(e )}),500 

@routes_blueprint.route('/info/<anime_id>')
def getAnimeInfo(anime_id):
    try:
        response = requests.get(API_BASE_URL+"info/"+anime_id)
        return jsonify(response.json()),200
    except Exception as e:
        return jsonify({'error': str(e)}),500

@routes_blueprint.route('/topairing')
def getTopAiring():
    try:
        response = requests.get(API_BASE_URL+"top-airing")
        return jsonify(response.json()),200
    except Exception as e:
        return jsonify({'error': str(e)}),500


@routes_blueprint.route('/watch/<episode_id>')
def getWatchLink(episode_id):
    try:
        response = requests.get(API_BASE_URL+"watch/"+episode_id)
        return jsonify(response.json()),200
    except Exception as e:
        return jsonify({'error': str(e)}),500

@routes_blueprint.route('/popular')
def getPopular():
    try:
        response = requests.get(API_BASE_URL+"popular")
        return jsonify(response.json()),200
    except Exception as e:
        return jsonify({'error': str(e)}),500

@routes_blueprint.route('/recent')
def getRecent():
    try:
        response = requests.get(API_BASE_URL+"recent-episodes")
        return jsonify(response.json()),200
    except Exception as e:
        return jsonify({'error': str(e)}),500

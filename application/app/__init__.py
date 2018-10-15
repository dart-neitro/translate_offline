from flask import Flask, request
from flask_restplus import Api, Resource

from .core.db_utils import MongoDB


app = Flask(__name__)
app.config.from_object('config')
api = Api(app)


@api.route('/translate')
class Translate(Resource):

    def get(self):
        if (not app.config.get('MONGODB_HOST') or
                not app.config.get('MONGODB_PORT')):
            return {'error': 1, 'msg': 'Wrong application config'}

        if request.args.get('keyword'):
            return {
                'error': 0,
                'msg': '',
                'result': request.args.get('keyword')}

        return {'error': 1, 'msg': 'No keyword'}

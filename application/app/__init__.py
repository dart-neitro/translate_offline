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
            client = MongoDB(
                host=app.config.get('MONGODB_HOST'),
                port=app.config.get('MONGODB_PORT')
            )

            words = client.get_collection('translate_offline', 'words')

            result = words.find_one({"key": request.args.get('keyword')}) or {}
            if not result:
                return {
                    'error': 1,
                    'msg': 'The word "%s" is missing in the database' % (
                        request.args.get('keyword')
                    )
                }

            return {
                'error': 0,
                'msg': '',
                'result': result.get('translate')}

        return {'error': 1, 'msg': 'No keyword'}


def render_error(msg):
    return '<h1 style="color: red">%s</h1>' % msg


@app.route('/translate_show')
def translate_show():
    if (not app.config.get('MONGODB_HOST') or
            not app.config.get('MONGODB_PORT')):
        return render_error('Wrong application config')

    if request.args.get('keyword'):
        client = MongoDB(
            host=app.config.get('MONGODB_HOST'),
            port=app.config.get('MONGODB_PORT')
        )

        words = client.get_collection('translate_offline', 'words')

        result = words.find_one({"key": request.args.get('keyword')}) or {}
        if not result:
            return render_error(
                'The word "%s" is missing in the database' % (
                    request.args.get('keyword')
            ))

        return """
        <h1> Перевод слова {} </h1>
        {}
        """.format(request.args.get('keyword'), result.get('translate'))

    return render_error('No keyword')
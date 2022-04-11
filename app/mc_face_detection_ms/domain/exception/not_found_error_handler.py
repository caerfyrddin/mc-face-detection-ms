import flask

def not_found_error_handler(e):
    return flask.jsonify(error = 404, text = str(e)), 404
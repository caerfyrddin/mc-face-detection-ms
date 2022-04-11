import flask

def internal_server_error_error_handler(e):
    return flask.jsonify(error = 500, text = str(e)), 500
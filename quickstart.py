import logging
import uuid
 
from flask import Flask, render_template, request, redirect, session, abort, jsonify
 
CSRF_TOKEN = '_csrf_token'
 
app = Flask(__name__)
app.secret_key = 'hogehoge'
 
# @app.route('/', methods=['GET'])
# def redirect_ui_index_with_crsftoken():
#     response = app.make_response(redirect("main.html"))
#     # response.set_cookie('XSRF-TOKEN', value=generate_csrf_token()) 
#     # return response
#     return render_template('main.html',res= response)
 
@app.route('/api/hello', methods=['POST'])
def api_hello():
    name = request.json['params']['name']
    return jsonify({"result":{"name":name}})
 
# @app.errorhandler(403)
# @app.errorhandler(500)
# def server_error(e):
#     logging.exception(e)
#     return 'an error occurred.', e.code
 
# @app.before_request
# def csrf_protect():
#     if request.method == "POST":
#         token = session[CSRF_TOKEN]
#         if not token or token != request.headers.get('X-XSRF-TOKEN'):
#             abort(403)
 
# def generate_csrf_token():
#     if CSRF_TOKEN not in session:
#         session[CSRF_TOKEN] = str(uuid.uuid4())
#     return session[CSRF_TOKEN]
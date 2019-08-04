from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/python_says_hello', methods=['POST'])
def python_says_hello(message = 'Hello!'):
	message = 'Python says: {}'.format(request.form['message'])
	return jsonify(result=message)

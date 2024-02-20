from flask import Flask, jsonify
import randomname

app = Flask(__name__)

@app.route('/getname', methods=['GET'])
def get_random_name():
    name = randomname.get_name()
    return jsonify({'random_name': name})

# Health check endpoint
@app.route('/healthcheck', methods=['GET'])
def health_check():
    return '', 200

if __name__ == '__main__':
    app.run(debug=False)
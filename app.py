from flask import Flask, jsonify
import randomname
import os

app = Flask(__name__)

@app.route('/getname', methods=['GET'])
def get_random_name():
    name = randomname.get_name()
    print(f"This name is funny: {name}")
    return jsonify({'random_name': name})

@app.route('/hello',methods=['GET'])
def say_hello():
    name = os.getenv('MYNAME')
    return jsonify({'your_name': name})

# Health check endpoint
@app.route('/healthcheck', methods=['GET'])
def health_check():
    return '', 200

if __name__ == '__main__':
    app.run(debug=False)

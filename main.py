from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"


@app.route('/oddeven/<int:n>')
def oddeven(n):
    if n%2 == 0:
        return "True"
    else:
        return "False"
    
    
if __name__ == "__main__":
    app.run(debug=True)



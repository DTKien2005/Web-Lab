from flask import Flask

app = Flask(__name__)

@app.route('/reverse_string/<string>')

def reverse_string(string):
    try:
        reverse = string[::-1]

        return f"Reverse string: {reverse}"
    except ValueError:
        return "Please provide string"

if __name__ == '__main__':
    app.run(debug=True)
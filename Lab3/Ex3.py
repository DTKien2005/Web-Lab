from flask import Flask, render_template

app = Flask(__name__)

@app.route('/table')

def display_table():
    data = [
        {'name': 'Alice', 'age': 22},
        {'name': 'Bob', 'age': 19},
        {'name': 'Charlie', 'age': 25},
        {'name': 'David', 'age': 24},
        {'name': 'Eve', 'age': 21}
    ]

    return render_template('table.html', students=data)


if __name__ == '__main__':
    app.run(debug=True)
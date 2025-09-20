from flask import Flask
import math

app = Flask(__name__)

@app.route('/factorial/<int:num>')

def factorial(num):
    try:
        if num < 0:
            return f"Factorial is not defined for negative numbers"
        
        result = math.factorial(num)
        return f"The factorial of {num} is {result}"
    
    except Exception as e:
        return "Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
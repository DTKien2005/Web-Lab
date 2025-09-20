from flask import Flask

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

@app.route('/isprime/<int:num>')

def check_prime(num):
    if is_prime(num):
        return f"{num} is Prime"
    else:
        return f"{num} is Not Prime"

if __name__ == '__main__':
    app.run(debug=True)

#Exercise 6: Flask Function to Sort a Numerical Array
#  Write a Flask route that accepts a list of numbers (via URL query
# parameters) and returns the sorted array.
#  Example URL: /sort?numbers=4,2,9,1
#  Return the sorted array in ascending order.

from flask import Flask

app = Flask(__name__)

@app.route('/sort/<numbers>')
def sort_array(numbers):
    # Convert the numbers (comma-separated string) into a list of integers
    try:
        num_list = list(map(int, numbers.split(',')))
        # Sort the list in ascending order
        num_list.sort()
        return f"Sorted Array: {num_list}"
    except ValueError:
        return "Please provide a valid comma-separated list of numbers."

if __name__ == '__main__':
    app.run(debug=True)

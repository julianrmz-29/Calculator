from flask import Flask, render_template, request, jsonify
from FunctionCalculator.CalculatorOperations import add, sub, mul, div
app = Flask(__name__)


@app.route('/')
def calculator():
    return render_template("calculator.html")


@app.route('/Calculate',methods=['POST'])
def calculator_post():
    try:
        data = request.get_json()
        operation = data['operation']
        a = float(data['a'])
        b = float(data['b'])

        if operation == '+':
            result = add(a,b)
        elif operation == '-':
            result = sub(a,b)
        elif operation == '*':
            result = mul(a,b)
        elif operation == '/':
            result = div(a,b)
        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({"result": result}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__app__':
    app.run(debug=True)

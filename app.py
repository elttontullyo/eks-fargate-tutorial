from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("Hello guys")
    return 'Hello guys! This application converts Dollar in brazilian Real currency. \\n I can make change at route: /change'

@app.route('/conversion', methods=['POST'])
def changeroute():
    print(f"Make Change for  to Real")
    dollar = float(request.json['dollar'])
    conversion_day = 4.97
    result = float(dollar * conversion_day)
    return jsonify({'real':result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
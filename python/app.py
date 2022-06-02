from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/menu")
def hello_world():
    '''
    Method
    '''
    return "<p>Hello, World!</p>"


@app.route('/swati')
def swati():
    '''
    Returns Swati
    '''
    return ("Swati")


@app.route('/index')
def index():
    '''
    Index
    '''
    return render_template('index.html')


@app.route('/sum')
def sum():
    '''
    Returns the sum
    '''
    args = request.args
    # print (args)
    a = int(args.get('a'))
    b = int(args.get('b'))
    sum = (a + b)
    return (str(sum))


@app.route('/subtract')
def subtract():
    '''
    Returns the subtract
    '''
    args = request.args
    # print (args)
    a = int(args.get('a'))
    b = int(args.get('b'))
    result = (a - b)
    return (str(result))


@app.route('/product')
def product():
    '''
    Returns the product
    '''
    args = request.args
    # print (args)
    a = int(args.get('a'))
    b = int(args.get('b'))
    result = (a * b)
    return (str(result))


@app.route('/divide', methods=['GET'])
def divide():
    '''
    Returns the divide
    '''
    args = request.args
    # print (args)
    a = int(args.get('a'))
    b = int(args.get('b'))
    result = (a / b)
    return (str(result))


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8087, debug=True)
    
    
    

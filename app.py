from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/product_inquiry')
def product_inquiry():
    return render_template("product_inquiry.html")
    
if __name__=='__main__':
    app.run(debug=True)
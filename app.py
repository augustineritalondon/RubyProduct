from flask import Flask, render_template, request
# from flask_mail import Mail, Message
# import smtplib

app = Flask(__name__)

# app.config['DEBUG'] = True
# app.config['TESTING'] = False
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False
# app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
# app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
# app.config['MAIL_USERNAME'] = 'itskeldon@gmail.com'
# app.config['MAIL_PASSWORD'] = 'google.com/keldon'
# app.config['MAIL_DEFAULT_SENDER'] = 'itskeldon@gmail.com'
# app.config['MAIL_MAX_EMAILS'] = None
# app.config['MAIL_ASCII_ATTACHMENTS'] = False

# mail = Mail(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/product_inquiry')
def product_inquiry():
    return render_template("product_inquiry.html")

@app.route('/send_message', methods=['GET', 'POST'])
def send_message():
    return "Message sent"

# @app.route('/new')
# def new():
#     msg = Message('Hey there', recipients=['itskeldon@gmail.com'])
#     mail.send(msg)
#     return 'Message sent'

@app.route('/CCTV_AnalogCameras')
def CCTV_AnalogCameras():
    return render_template("CCTV_AnalogCameras.html")

@app.route('/CCTV_IpCameras')
def CCTV_IpCameras():
    return render_template("CCTV_IpCameras.html")

@app.route('/CCTV_CovertCameras')
def CCTV_CovertCameras():
    return render_template("CCTV_CovertCameras.html")

@app.route('/CCTV_DVRS')
def CCTV_DVRS():
    return render_template("CCTV_DVRS.html")

@app.route('/Pabx_intercom')
def Pabx_intercom():
    return render_template("Pabx_intercom.html")

@app.route('/Access_Control')
def Access_Control():
    return render_template("Access_Control.html")

@app.route('/Fire_Alarm')
def Fire_Alarm():
    return render_template("Fire_Alarm.html")

@app.route('/Inverter_SolarSystem')
def Inverter_SolarSystem():
    return render_template("Inverter_SolarSystem.html")

@app.route('/Permitter')
def Permitter():
    return render_template("Permitter.html")

if __name__=='__main__':
    app.run(debug=True)
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('button.html')

@app.route('/login')
def login():
    return render_template('index.html')


@app.route('/submit')
def submit():
    return render_template('submit.html')

# @app.route('/test1')
# def abc():
#     return'<h1>안녕하세요 저는 김민지 입니다.</h1><input type = "textbox"/>'

if __name__ == '__main__':
    app.run(host='192.168.1.175', port=2323, debug=True)

   
   
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    name = request.form['name']
    id = request.form['id']
    emailAddress = request.form['emailAddress']
    return render_template('result.html',name=name,id=id,emailAddress=emailAddress)


if __name__ == '__main__':
    app.run(debug=True)


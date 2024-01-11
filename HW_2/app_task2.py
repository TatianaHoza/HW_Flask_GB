from flask import Flask,request,render_template,make_response,redirect,url_for,session

app = Flask(__name__)
app.secret_key = '5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if (name := request.form.get('name')) and (email := request.form.get('e-mail')):
            response = make_response(redirect(url_for('submit')))
            response.set_cookie('username', name)
            response.set_cookie('email', email)
            return response
    return render_template('base.html')


@app.route('/submit/', methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        response = make_response(redirect(url_for('index')))
        response.delete_cookie('username')
        response.delete_cookie('email')
        return response
    username = request.cookies.get('username')
    return render_template('hello.html', name=username)

@app.route('/logout/')
def logout():
    session.pop('name',None)
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)

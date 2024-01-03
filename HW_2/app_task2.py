from flask import Flask,request,render_template,make_response,redirect,url_for,session

app = Flask(__name__)
app.secret_key = '5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'

@app.route('/')
def index():
    if 'name' in session:
        return f'Привет, {session["name"]}'
        #return redirect(url_for('hello.html'))
    else:
        return redirect(url_for('submit'))
    response = make_response("Cookie установлен")
    response.set_cookie('username', 'admin')
    return response


@app.route('/submit/', methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        session['name'] = request.form.get('name') or 'NoName'
        return redirect(url_for('index'))
    return render_template('base.html')

@app.route('/logout/')
def logout():
    session.pop('name',None)
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)

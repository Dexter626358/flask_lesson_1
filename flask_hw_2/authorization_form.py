"""
Создать страницу, на которой будет форма для ввода имени
и электронной почты
При отправке которой будет создан cookie файл с данными
пользователя
Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка "Выйти"
При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.
"""

from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        resp = make_response(redirect('/getcookie'))
        resp.set_cookie('user_name', name)
        resp.set_cookie('user_email', email)
        return resp
    return render_template('email.html')


@app.route('/getcookie/')
def get_cookies():
    # получаем значение cookie
    name = request.cookies.get('user_name')
    if not name:
        return redirect('/')
    return render_template('greetings.html', name=name)


@app.route('/logout')
def logout():
    respons = make_response(redirect('/'))
    respons.set_cookie('user_name', '', expires=0)
    respons.set_cookie('user_email', '', expires=0)
    return respons



if __name__ == '__main__':
    app.run(debug=True)

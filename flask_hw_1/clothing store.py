"""Создать базовый шаблон для интернет-магазина,
содержащий общие элементы дизайна (шапка, меню,
подвал), и дочерние шаблоны для страниц категорий
товаров и отдельных товаров.
Например, создать страницы "Одежда", "Обувь" и "Куртка",
используя базовый шаблон.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/main/')
def main():
    context = {'title': 'Главная'}
    return render_template('main.html', **context)


@app.route('/cloth/')
def cloth():
    context = {'title': 'Одежда'}
    return render_template('cloth.html', **context)


@app.route('/jackets/')
def jackets():
    context = {'title': 'Куртки'}
    return render_template('jackets.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    return render_template('shoes.html', **context)



if __name__ == "__main__":
    app.run(debug=True)


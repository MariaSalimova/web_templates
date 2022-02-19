from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/trainig/<prof>')
def training(prof):
    if 'инженер' or 'строитель' in prof.lower():
        return render_template('trainig.html', title='Инженерные тренажеры',
                               image=url_for('static', filename='pictures/eng.jpg'))
    return render_template('trainig.html', title='Научные симуляторы',
                           image=url_for('static', filename='pictures/sci.jpg'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

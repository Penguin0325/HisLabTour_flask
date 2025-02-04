from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/title')
def title():
    return render_template('title.html')

@app.route('/preface')
def preface():
    return render_template('preface.html')

@app.route('/intro_story1')
def intro_story1():
    return render_template('intro_story1.html')

@app.route('/intro_story2')
def intro_story2():
    return render_template('intro_story2.html')

@app.route('/intro_story3')
def intro_story3():
    return render_template('intro_story3.html')

@app.route('/intro_story4')
def intro_story4():
    return render_template('intro_story4.html')

@app.route('/intro_story5')
def intro_story5():
    return render_template('intro_story5.html')

@app.route('/movie_0523')
def movie_0523():
    return render_template('movie_0523.html')

@app.route('/character')
def character():
    return render_template('character.html')

@app.route('/movie_0530')
def movie_0530():
    return render_template('movie_0530.html')

@app.route('/mystery1')
def mystery1():
    return render_template('mystery1.html')

@app.route('/movie_0613')
def movie_0613():
    return render_template('movie_0613.html')

@app.route('/movie_0711')
def movie_0711():
    return render_template('movie_0711.html')

@app.route('/movie_0725')
def movie_0725():
    return render_template('movie_0725.html')

@app.route('/movie_1128')
def movie_1128():
    return render_template('movie_1128.html')

@app.route('/movie_0111')
def movie_0111():
    return render_template('movie_0111.html')

@app.route('/mystery2')
def mystery2():
    return render_template('mystery2.html')

@app.route('/movie_0130')
def movie_0130():
    return render_template('movie_0130.html')

@app.route('/before_last_story1')
def before_last_story1():
    return render_template('before_last_story1.html')

@app.route('/mystery3')
def mystery3():
    return render_template('mystery3.html')

@app.route('/movie_ending')
def movie_ending():
    return render_template('movie_ending.html')

@app.route('/ending_story1')
def ending_story1():
    return render_template('ending_story1.html')

@app.route('/ending_story2')
def ending_story2():
    return render_template('ending_story2.html')

@app.route('/ending_story3')
def ending_story3():
    return render_template('ending_story3.html')

if __name__ == '__main__':
    app.run(debug=True)
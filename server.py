from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('checkerboard.html')

@app.route('/<times1>/<times2>')
def checkerboard2(times1,times2):
    return render_template('checkerboard2.html', box1 = int(times1), box2 = int(times2))

app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('valentine.html')

@app.route('/forgiveness')
def forgiveness():
    return render_template('forgiveness.html')

if __name__ == '__main__':
    app.run(debug=True)
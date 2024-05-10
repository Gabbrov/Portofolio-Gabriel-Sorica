from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return render_template('result.html', name=name, email=email)
    return render_template('cvBuild.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return render_template('cvBuild.html', name=name, email=email)
    return "Form submission failed."

if __name__ == '__main__':
    app.run(debug=True)

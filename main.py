from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/me')
def me():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        text = request.form['text']
        print(text)
        return render_template('kontakt.html')
    return render_template('kontakt.html')

if __name__ == '__main__':
    app.run()

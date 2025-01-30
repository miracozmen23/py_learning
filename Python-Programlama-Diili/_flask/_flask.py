from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Ana Sayfa"

@app.route('/about')
def about():
    return "Hakkında Sayfası"

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']
        return f"Hoşgeldiniz, {username}!"
    return '''
        <form method="POST">
        Adınızı girin : <input type="text" name="username">
        <input type="submit" value="Gönder">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)

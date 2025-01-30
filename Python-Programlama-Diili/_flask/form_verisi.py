from flask import Flask, request

app = Flask(__name__)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        username = request.form['username']
        age = request.form['age']
        return f"Kullanıcı adınız: {username}, Yaşınız:{age}"
    
    return '''
        <form method="POST">
        Adınızı girin : <input type="text" name="username"><br>
        Yaşınızı girin : <input type="number" name="age"><br>
        <input type="submit" value="Gönder">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
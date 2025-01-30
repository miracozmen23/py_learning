from flask import Flask, request, render_template
import requests  

app = Flask(__name__)

API_KEY = 'f44bcfa9aa6cb0baef29aebe2e5557d2'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form['city']
        
        complete_url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
        
        # API'ye istek yapmak için requests.get kullanıyoruz
        response = requests.get(complete_url)  # Burada requests.get kullanmalısınız
        data = response.json()
        
        if data['cod'] == 200:
            main = data['main']
            weather = data['weather'][0]
            wind = data['wind']
            city_name = data['name']
            country = data['sys']['country']
            
            temperature = main['temp']
            pressure = main['pressure']
            humidity = main['humidity']
            description = weather['description']
            wind_speed = wind['speed']
            
            # Hava durumu bilgilerini şablona gönderiyoruz
            return render_template('index2.html', city=city_name, country=country, temperature=temperature, 
                                   pressure=pressure, humidity=humidity, description=description, 
                                   wind_speed=wind_speed)
        else:
            error_message = "Geçersiz şehir adı veya API hatası"
            return render_template('index2.html', error=error_message)
    
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)

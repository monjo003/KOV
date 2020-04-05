from flask import Flask, render_template
import requests

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    country = "ethiopia"
    url = "https://coronavirus-19-api.herokuapp.com/countries/" + country
    
    req_data = requests.get(url.format(country)).json()
    country = req_data['country']
    cases  = req_data['cases']
    todayCases = req_data['todayCases']
    deaths = req_data['deaths']
    todayDeaths = req_data['todayDeaths']
    recovered = req_data['recovered']
    active = req_data['active']
    critical = req_data['critical']
    casesPerOneMillion = req_data['casesPerOneMillion']
    deathsPerOneMillion = req_data['deathsPerOneMillion']
    totalTests = req_data['totalTests']
    testsPerOneMillion = req_data['testsPerOneMillion']

    print(cases)

    return render_template('index.html', country = country, cases = cases, todayCases = todayCases, deaths = deaths, todayDeaths = todayDeaths, recovered = recovered, active = active, critical = critical, casesPerOneMillion = casesPerOneMillion, deathsPerOneMillion = deathsPerOneMillion, totalTests=totalTests, testsPerOneMillion = testsPerOneMillion  )
    
if __name__ == '__main__':
    app.run(debug=True)







#run the app: FLASK_APP=api.py flask run    
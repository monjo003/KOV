from flask import Flask, render_template
import requests
import json


app = Flask(__name__)
app.config["DEBUG"] = True

 
with open("credentials.json", "r") as f:
    my_dict = json.load(f)
    map_api_key = my_dict["credentials"]["MAPS_API"]
# print(map_api_key)    

@app.route('/main', methods=['GET'])
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

    # print(map_api_key)

    return render_template('index.html', token= "YEAHHHHHHHHHHHH!!!!!!! LETSS GOOOOOO!!!!", map_api_key = map_api_key, country = country, cases = cases, todayCases = todayCases, deaths = deaths, todayDeaths = todayDeaths, recovered = recovered, active = active, critical = critical, casesPerOneMillion = casesPerOneMillion, deathsPerOneMillion = deathsPerOneMillion, totalTests=totalTests, testsPerOneMillion = testsPerOneMillion  )
    
if __name__ == '__main__':
    app.run(debug=True)







#run the app: FLASK_APP=api.py flask run    
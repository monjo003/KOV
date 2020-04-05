from flask import Flask, render_template
import requests

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    country = "ethiopia"
    url = 'https://api.covid19api.com/dayone/country/'+country+'/status/confirmed/live'
    
    r = requests.get(url.format(country)).json()
    #currentNo = []
    #currentNo.append( r[-1:])
    latest = r[-1]
    CaseNo = latest["Cases"]
    #print(latest)
    #print(type(latest))
    print(CaseNo)
    
   
    # for i in r :
    #     for key, value in i.items():
    #        print(key, value)
    return render_template('index.html', CaseNo = CaseNo)
    
if __name__ == '__main__':
    app.run(debug=True)







#run the app: FLASK_APP=api.py flask run    
from flask import Flask, render_template
import requests

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    url = 'https://api.covid19api.com/dayone/country/ethiopia/status/confirmed/live'
    country = 'ethiopia'
    r = requests.get(url.format(country)).json()
    currentNo = []
    currentNo.append( r[-1:])
    latest = r[-1]
  #  print(latest)
   # print(type(latest))
    print(latest["Cases"])

   
    # for i in r :
    #     for key, value in i.items():
    #        print(key, value)
  

  




    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)
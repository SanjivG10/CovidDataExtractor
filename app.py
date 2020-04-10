from flask  import Flask, render_template
from  scrapper import countDict
from preprocessData import get_processed_dict,getExploredDataCountryWise
from flask_pymongo import PyMongo
import time
from scrapper import getDataCountryWise


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://sanjiv:pass123@facebookreactions-iwesq.mongodb.net/covid19"
mongo = PyMongo(app)


countryData = get_processed_dict()
column_names = countDict.values()


@app.template_filter('ctime')
def timectime(s):
    return time.ctime(int(s))


@app.route('/')
def home():
    return render_template('index.html',column_names = column_names ,data = countryData)

# @app.route('/postDataFromHere')
# def postDataFromHere():
#     current_time_we_have = int(time.time())
#     data = {}
#     values = getDataCountryWise()
#     data[str(current_time_we_have)] = values
#     mongo.db.covid19.insert_one(data)
#     return 'success'

@app.route('/explore')
def explore():
    #let me process the data and do something like this! 
    allData = mongo.db.covid19.find({})
    timeEvents, values = getExploredDataCountryWise(allData,'USA','total cases')
    return render_template('savedData.html',labels = timeEvents, data = values)

@app.route('/details/<country_name>')
def details(country_name):
    return render_template('details.html',country_name=country_name)

if __name__=="__main__":
    app.run(debug=True)
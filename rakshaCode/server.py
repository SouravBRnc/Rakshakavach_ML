from flask import Flask, render_template, request
import datetime
from flask_restful import Resource, reqparse
from flask_restful import Api
from flask import Blueprint

from apixu.client import ApixuClient

api_key = '#API_KEY#'
client = ApixuClient(api_key)
import MainPrediction

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

class Unity(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('weather')
        parser.add_argument('junction')
        parser.add_argument('control')
        parser.add_argument('location')
        args = parser.parse_args()
        print(args)
        timeNow = datetime.datetime.now().hour
        if (timeNow >= 0 and timeNow < 3):
            time = 7
        if (timeNow >= 3 and timeNow < 6):
            time = 8
        if (timeNow >= 6 and timeNow < 9):
            time = 1
        if (timeNow >= 9 and timeNow < 12):
            time = 2
        if (timeNow >= 12 and timeNow < 15):
            time = 3
        if (timeNow >= 15 and timeNow < 18):
            time = 4
        if (timeNow >= 18 and timeNow < 21):
            time = 5
        if (timeNow >= 21):
            time = 6

        predictionArray = []

        predictionArray.append([int(args['weather']), int(args['junction']), int(args['control']), time, int(args['location'])])

        y_pred = MainPrediction.prediction(predictionArray)
        print(y_pred)
        return {'probability':y_pred[0]}


api.add_resource(Unity, '/unity', endpoint='unity')

CSVurl = "/home/sourav/Music/ACCIDENT_Data.xlsx"

pointsUrl = "/home/sourav/Music/data.txt"

data_blr = {

    'mathikere': [{'coord': [13.028138, 77.570283], 'tc':3, 'jun': 1, 'loc': 7},
                  {'coord': [13.048042, 77.521700], 'tc':1, 'jun': 3, 'loc': 4},
                  {'coord': [13.018440, 77.543503], 'tc':5, 'jun': 2, 'loc': 3}],

    'yeshwanthpur': [{'coord': [13.019577, 77.558089], 'tc':2, 'jun': 1, 'loc': 5},
                     {'coord': [13.012921, 77.554135], 'tc':5, 'jun': 4, 'loc': 6},
                     {'coord': [13.048865, 77.550126], 'tc':2, 'jun': 3, 'loc':7},
                     {'coord': [13.057337, 77.593428], 'tc':1, 'jun': 4, 'loc':5},
                     {'coord': [13.014612, 77.572763], 'tc':2, 'jun': 1, 'loc':1},
                     {'coord': [13.059550, 77.506896], 'tc':1, 'jun': 2, 'loc':4},
                     {'coord': [13.011426, 77.550803], 'tc':5, 'jun': 1, 'loc':3},
                     {'coord': [13.013590, 77.554089], 'tc':2, 'jun': 6, 'loc':2},
                     {'coord': [13.026413, 77.514629], 'tc':1, 'jun': 3, 'loc':6},
                     {'coord': [13.012012, 77.535673], 'tc':1, 'jun': 5, 'loc':4},
                     {'coord': [13.015759, 77.554027], 'tc':1, 'jun': 3, 'loc':9}],

    'whitefield':[{'coord' : [12.968522, 77.755968] , 'tc':5, 'jun':2 ,'loc':3},
                  {'coord' : [12.983483, 77.768292] , 'tc':1, 'jun':4 ,'loc':9},
                  {'coord' : [12.982323, 77.758110] , 'tc':5, 'jun':1 ,'loc':8},
                  {'coord' : [12.979119, 77.802371] , 'tc':1, 'jun':2 ,'loc':2},
                  {'coord' : [12.979786, 77.694749] , 'tc':2, 'jun':3 ,'loc':6},
                  {'coord' : [12.988045, 77.732634] , 'tc':1, 'jun':6 ,'loc':5},
                  {'coord' : [12.956093, 77.711389] , 'tc':5, 'jun':1 ,'loc':7},
                  {'coord' : [12.969141, 77.742709] , 'tc':1, 'jun':1 ,'loc':4}],
'electronic city'  : [{'coord' : [12.894159, 77.657019] , 'tc':1 , 'jun':3  ,'loc':8},
                      {'coord' : [12.875767, 77.671323] , 'tc':2 , 'jun':1  ,'loc':3},
                      {'coord' : [12.903891, 77.703276] , 'tc':5 , 'jun':4  ,'loc':5},
                      {'coord' : [12.917163, 77.644814] , 'tc':1 , 'jun':3  ,'loc':1},
                      {'coord' : [12.839050, 77.658972] , 'tc':1 , 'jun':1  ,'loc':6},
                      {'coord' : [12.907312, 77.600468] , 'tc':2 , 'jun': 2 ,'loc':3},
                      {'coord' : [12.906189, 77.595017] , 'tc':2 , 'jun':3  ,'loc':6},
                      {'coord' : [12.846628, 77.671795] , 'tc':1 , 'jun':4  ,'loc':9}],

'majestic'  : [{'coord' : [12.975666, 77.564636] , 'tc':1  , 'jun'   :2 ,'loc' :1 },
               {'coord' : [12.974749, 77.570611] ,   'tc'  :5  , 'jun'   :4 ,'loc' :9 },
               {'coord' : [12.975143, 77.576157] ,   'tc'  :2  , 'jun'   :6 ,'loc' :4},
               {'coord' : [12.979537, 77.581868] ,   'tc'  :1  , 'jun'   :1 ,'loc' :4},
               {'coord' : [12.988410, 77.572121] ,   'tc'  : 5 , 'jun'   :1 ,'loc' :7},
               {'coord' : [12.973121, 77.580984] ,   'tc'  :2  , 'jun'   :3 ,'loc' :4}],

'indiranagar'  : [{'coord' : [12.978313, 77.640730] ,   'tc'  :1  , 'jun'   :3 ,'loc' : 9},
                  {'coord' : [12.974983, 77.625395] ,   'tc'  :5  , 'jun'   :1 ,'loc' :3},
                  {'coord' : [12.980094, 77.637082] ,   'tc'  :1  , 'jun'   :3 ,'loc' :5},
                  {'coord' : [12.975984, 77.637002] ,   'tc'  :1  , 'jun'   :3 ,'loc' : 1},
                  {'coord' : [12.978055, 77.636683] ,   'tc'  :1  , 'jun'   :3 ,'loc' :6},
                  {'coord' : [12.970953, 77.647322] ,   'tc'  :1  , 'jun'   :3 ,'loc' : 6}]
}

data_tmk = {
    'tumkur'  : [{'coord' : [13.337708, 77.117857] , 'tc' :1 , 'jun' :5  ,'loc':7},
                 {'coord' : [13.349254, 77.102529] , 'tc' :5 , 'jun' :1  ,'loc':3},
                 {'coord' : [13.346351, 77.124955] , 'tc' :2 ,  'jun'  :3  ,'loc':5},
                 {'coord' : [13.332278, 77.126751] , 'tc' :5 , 'jun' :1  ,'loc':6},
                 {'coord' : [13.316050, 77.091019] , 'tc' :1 , 'jun' :6  ,'loc':1},
                 {'coord' : [13.329884, 77.115832] , 'tc' :5 , 'jun' :2  ,'loc':8},
                 {'coord' : [13.329934, 77.125781] , 'tc' :5 , 'jun' :1  ,'loc': 1},
                 {'coord' : [13.338294, 77.101256] , 'tc' :1 , 'jun' :1  ,'loc': 9}]
}

app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api')

@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method=="GET":
        return render_template("index.html")
    if request.method=="POST":
        city = request.form["cityname"]
        area = request.form['area']
        if(city=="bangalore"):
            if(area == "ypr"):
                newData = data_blr['yeshwanthpur']
            if(area == "mtkr"):
                newData = data_blr['mathikere']
            if (area == "ecity"):
                newData = data_blr['electronic city']
            if (area == "white"):
                newData = data_blr['whitefield']
            if (area == "majestic"):
                newData = data_blr['majestic']
            if (area == "indiranagar"):
                newData = data_blr['indiranagar']

        if(city=="tumkur"):
            newData= data_tmk['tumkur']

        current = client.current(q=city)

        temp = current['current']['temp_c']
        wind = current['current']['wind_kph']
        cond = current['current']['condition']['text']

        light_rain = ['Patchy rain possible','Patchy light drizzle','Patchy light rain','Light rain','Moderate rain at times','Moderate rain','Light rain shower','Patchy light rain with thunder']
        heav_rain = ['Thundery outbreaks possible','Heavy rain at times','Moderate or heavy rain shower','Moderate or heavy rain with thunder']

        if temp>15.0 and temp<30.0 and cond=="Sunny" or cond=="Clear":
            weather_val = 1
        elif temp>30.0 and cond=="Sunny" or cond=="Clear":
            weather_val = 8
        elif temp < 15.0 and cond == "Sunny" or cond == "Clear":
            weather_val = 9
        elif cond=="Mist" or cond=="Fog":
            weather_val = 2
        elif cond=="Cloudy" or cond=="Partly cloudy" or cond=="Overcast":
            weather_val = 3
        elif cond in light_rain:
            weather_val = 4
        elif cond in heav_rain:
            weather_val = 5
        else:
            weather_val = 7

        timeNow = datetime.datetime.now().hour
        if(timeNow>=0 and timeNow<3):
            time = 7
        if (timeNow >= 3 and timeNow < 6):
            time = 8
        if (timeNow >= 6 and timeNow < 9):
            time = 1
        if (timeNow >= 9 and timeNow < 12):
            time = 2
        if (timeNow >= 12 and timeNow < 15):
            time = 3
        if (timeNow >= 15 and timeNow < 18):
            time = 4
        if (timeNow >= 18 and timeNow < 21):
            time = 5
        if (timeNow >= 21):
            time = 6

        predictionArray = []

        for x in newData:
            predictionArray.append([weather_val,x['jun'],x['tc'],time,x['loc']])

        print(predictionArray)

        y_pred = MainPrediction.prediction(predictionArray)

        print(y_pred)

        toBeSent = []
        i=0

        for x in newData:
            toBeSent.append([x['coord'],y_pred[i]])
            i+=1

        return render_template("map.html",msg = toBeSent)


if __name__ == "__main__":
    app.run(port=5000, debug=True)

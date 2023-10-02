from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load your trained model
pipe = pickle.load(open('pipe1.pkl', 'rb'))
# pipe = pickle.load(open('pipe71.pkl', 'rb')) #(its for 71 cities)


# Define lists for teams and cities (you can remove the ones you don't need)
teams = ['Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa', 'England', 'Afghanistan', 'Pakistan', 'Sri Lanka', 'Netherlands']


## Use this cities for pipe71.pkl

# cities = [
#     'Colombo', 'London', 'Mirpur', 'Sydney', 'Centurion', 'Melbourne', 'Abu Dhabi', 'Rangiri', 'Adelaide', 'Johannesburg',
#     'Birmingham', 'Dubai', 'Perth', 'Auckland', 'Karachi', 'Lahore', 'Hamilton', 'Brisbane', 'Cardiff', 'Wellington',
#     'Manchester', 'Pallekele', 'Cape Town', 'Durban', 'Southampton', 'Sharjah', 'Nottingham', 'Chandigarh', 'Hambantota',
#     'Port Elizabeth', 'Christchurch', 'Leeds', 'Napier', 'Chester-le-Street', 'Dhaka', 'Hobart', 'Mumbai', 'Bloemfontein',
#     'Chattogram', 'Mount Maunganui', 'Nagpur', 'Rawalpindi', 'Dunedin', 'Delhi', 'Chittagong', 'Hyderabad', 'Pune', 'Paarl',
#     'Rajkot', 'Fatullah', 'Dambulla', 'Kolkata', 'Kandy', 'Jaipur', 'Bristol', 'Nelson', 'Indore', 'Ahmedabad', 'Harare',
#     'Ranchi', 'Visakhapatnam', 'Kimberley', 'Canberra', 'Kanpur', 'Potchefstroom', 'Chennai', 'Cuttack', 'Cairns', 'Trinidad',
#     'Bangalore', 'Amstelveen', 'Grenada', 'East London', 'Guwahati'
# ]


cities = [
    'Colombo', 'London', 'Mirpur', 'Sydney', 'Centurion', 'Melbourne', 'Abu Dhabi', 'Rangiri', 'Adelaide', 'Johannesburg',
    'Birmingham', 'Dubai', 'Perth', 'Auckland', 'Karachi', 'Lahore', 'Hamilton', 'Brisbane', 'Cardiff', 'Wellington',
    'Manchester', 'Pallekele', 'Cape Town', 'Durban', 'Southampton', 'Sharjah', 'Nottingham', 'Chandigarh', 'Hambantota',
    'Port Elizabeth', 'Christchurch', 'Leeds', 'Napier', 'Chester-le-Street', 'Dhaka', 'Hobart', 'Mumbai', 'Bloemfontein',
    'Chattogram', 'Mount Maunganui', 'Nagpur'
]





@app.route('/', methods=['GET', 'POST'])
def predict_score():
    if request.method == 'POST':
        batting_team = request.form['batting_team']
        Bowling_team = request.form['Bowling_team']
        city = request.form['city']
        current_score = float(request.form['current_score'])
        overs = float(request.form['overs'])
        wickets = int(request.form['wickets'])
        last_five = float(request.form['last_five'])

        balls_left = 300 - (overs * 6)
        wickets_left = 10 - wickets
        crr = current_score / overs

        input_df = pd.DataFrame({
            'batting_team': [batting_team], 'Bowling_team': [Bowling_team], 'city': [city],
            'current_score': [current_score], 'balls_left': [balls_left],
            'wickets_left': [wickets], 'crr': [crr], 'last_five': [last_five]
        })

        result = pipe.predict(input_df)
        predicted_score = int(result[0])

        return render_template('result.html', predicted_score=predicted_score)

    return render_template('index.html', teams=teams, cities=cities)

if __name__ == '__main__':
    app.run(debug=True)

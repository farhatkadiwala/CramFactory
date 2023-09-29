from flask import Flask, render_template, request
import backend

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/choose_option.html')
def choose_option():
	return render_template('choose_option.html')

@app.route('/recommendations_form.html')
def recommendations():
	return render_template('recommendations_form.html')

@app.route('/studyplan_form1.html')
def studyPlan():
	return render_template('studyplan_form1.html')

@app.route('/results.html', methods =["GET", "POST"])
def getResults():
    if request.method == "POST":
        name = request.form.get("name")
        subjects = request.form.get("subject")
        topics = request.form.get("topics")
        results = backend.provideLearningResources(subjects)
        print(name, results, subjects)  
        return render_template("results.html", results=results, name=name)

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(debug=True)

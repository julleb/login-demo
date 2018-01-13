from flask import Flask, redirect, url_for, session, request, render_template, send_file
from UserService import UserService

app = Flask(__name__)
app.debug=True
app.secret_key = "jahdkajhdkahkdh";
userservice = UserService();

@app.route('/')
def index():
	return render_template("index.html");

@app.route('/login', methods=["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("loginform.html");
	else:
		username = request.form["username"];
		password = request.form["password"];
		try:
			userservice.get_user(username, password);
		except Exception as e:
			return str(e);
		session["username"] = username;
		return index();

@app.route('/signup', methods=["GET", "POST"])
def signup():
	if request.method == "GET":
		return render_template("signup.html");
	else:
		username = request.form["username"];
		password = request.form["password"];
		try:
			userservice.create_user(username, password);
			return "username: " + username +" created! Go to login";
		except Exception as e:
			return str(e);
		
@app.route("/logout", methods=["GET", "POST"])
def logout():
	session.clear();
	return index();

@app.route('/user/<username>')
def user(username):
	return "user " + str(username);

@app.route("/test")
def test():
	userservice.create_user("hej", "pass");
	return "test"


#run the app plz
if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port=5050)

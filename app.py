from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "this_isasecret_"
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.init_app(app)

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True,nullable=False)
    password = db.Column(db.String(100), nullable=False)

db.init_app(app)
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# Initialize vote counts
votes = {"yes": 0, "no": 0}

@app.route('/')
def home():
 return render_template("home.html")


@app.route('/vote', methods=['POST'])
def update_votes():
    # Get the user's vote
    vote = request.form.get('vote')
    if vote in votes:
        votes[vote] += 1
    return jsonify(votes)  # Send the updated vote counts as JSON

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        hashed_password = generate_password_hash(request.form.get("password"), method="pbkdf2:sha256", salt_length=8)
        user = Users(username=request.form.get("username"), password=hashed_password)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("sign_up.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = Users.query.filter_by(
            username=request.form.get("username")).first()

        if user and check_password_hash(user.password, request.form.get("password")):
            login_user(user)
            return redirect(url_for("home"))
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)

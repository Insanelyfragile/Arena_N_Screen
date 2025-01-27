from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initialize vote counts
votes = {"yes": 0, "no": 0}


@app.route('/')
def poll():
    # Render the main poll page
    query = request.args.get('q', "")  # Optional query parameter
    return render_template("mainpage.html", query=query)


@app.route('/vote', methods=['POST'])
def update_votes():
    # Get the user's vote
    vote = request.form.get('vote')
    if vote in votes:
        votes[vote] += 1
    return jsonify(votes)  # Send the updated vote counts as JSON


if __name__ == '__main__':
    app.run(debug=True)

b=0
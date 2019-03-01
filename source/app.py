from flask import Flask, render_template, abort
import json

# Start the app
app = Flask(__name__)

# Load users from file (imagine this is a database connection)
users = json.loads(open('data/users.json').read())


# Website root, showing an overview of all users
@app.route('/')
def index():
    return render_template('index.html', users=enumerate(users))


@app.route('/<int:id>')
def user(id):
    # User not found
    if id < 0 or len(users) <= id:
        abort(404)

    return render_template('user.html', user=users[id])


if __name__ == "__main__":
    app.run()

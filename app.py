from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os

# init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init DB
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    date_of_birth = db.Column(db.String)
    years_of_experience = db.Column(db.Integer)

    def __init__(self, username, date_of_birth, years_of_experience):
        self.username = username
        self.date_of_birth = date_of_birth
        self.years_of_experience = years_of_experience


ma = Marshmallow(app)


class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ['id', 'username', 'date_of_birth',
                  'years_of_experience']


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route('/users', methods=['POST'])
def create_user():
    print(request.json, 'requser')
    username = request.json['username']
    date_of_birth = request.json['date_of_birth']
    years_of_experience = request.json['years_of_experience']

    new_user = User(username, date_of_birth, years_of_experience)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)


@app.route('/users', methods=['GET'])
def get_users():

    all_users = User.query.all()
    result = users_schema.dump(all_users)

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

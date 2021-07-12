import os
from flask import Flask, json, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import date
from flask_cors import CORS
from sqlalchemy.orm import relationship

# init app
app = Flask(__name__)
CORS(app)
ma = Marshmallow(app)

# UPLOAD_FOLDER = '/Users/essamabuissa/Desktop/Development/Python/hr-backend/resumes'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


basedir = os.path.abspath(os.path.dirname(__file__))

#======================================== DATABASE INIT ==============================================#

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
#======================================== DATABASE INIT ==============================================#

#======================================== MODELS ==============================================#


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    date_of_birth = db.Column(db.String)
    years_of_experience = db.Column(db.Integer)
    role = db.Column(db.String)
    created_at = db.Column(db.String, server_default=db.func.now())
    department = db.Column(db.String)
    # file = relationship("File", backref=db.backref("user", uselist=False))

    def __init__(self, username, date_of_birth, years_of_experience, role, created_at, department):
        self.username = username
        self.date_of_birth = date_of_birth
        self.years_of_experience = years_of_experience
        self.role = role
        self.created_at = created_at
        self.department = department
        # self.file = file


class File(db.Model):
    __tablename__ = 'file'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    type = db.Column(db.String(8))
    filename = db.column_property(name + '.' + type)
    path = db.column_property(
        '/Users/essamabuissa/Desktop/Development/Python/hr-backend/resumes' + filename.expression)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


#======================================== MODELS ==============================================#


#======================================== SCHEMAS ==============================================#

class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ['id', 'username', 'date_of_birth',
                  'years_of_experience', 'role', 'created_at', 'file', 'department']


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class FileSchema(ma.Schema):
    class Meta:
        model = File
        fields = ['id', 'name', 'type']


file_schema = FileSchema()

#======================================== SCHEMAS ==============================================#


#======================================== VIEWS ==============================================#


@app.route('/users', methods=['POST'])
def create_user():

    if(request.headers.__contains__('Token')):
        role = request.json['role'] = 'admin'
    else:
        role = request.json['role'] = 'candidate'

    username = request.json['username']
    date_of_birth = request.json['date_of_birth']
    years_of_experience = request.json['years_of_experience']
    created_at = request.json['created_at']
    department = request.json['department']

    new_user = User(username, date_of_birth,
                    years_of_experience, role, created_at, department)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)


@app.route('/users', methods=['GET'])
def get_users():
    if(request.headers.__contains__('Token')):
        all_users = User.query.all()
        result = users_schema.dump(all_users)
        return jsonify(result)
    else:
        return jsonify({'error': 'UNAUTHORIZED'}), 401


@app.route('/users/<id>', methods=['GET'])
def get_singleUser(id):
    user = User.query.get(id)
    if(request.headers.__contains__('Token')):
        if user:
            return user_schema.jsonify(user)
        else:
            return jsonify({'error': 'user not found'}), 404
    else:
        return jsonify({'error': 'UNAUTHORIZED'}), 401
#======================================== VIEWS ==============================================#


if __name__ == '__main__':
    print('run')
    app.run(debug=True)

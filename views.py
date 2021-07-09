# from models import User, db
# from flask import request, jsonify
# from app import app
# from schemas import user_schema


# @app.route('/users', methods=['POST'])
# def create_user():
#     username = request.json['username']
#     date_of_birth = request.json['date_of_birth']
#     years_of_experience = request.json['years_of_experience']
#     department = request.json['department']

#     new_user = User(username, date_of_birth, years_of_experience, department)
#     db.session.add(new_user)
#     db.session.commit()
#     return user_schema.jsonify(new_user)

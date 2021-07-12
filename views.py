# from run import User, UserSchema, db
# from app import app
# from flask import request, jsonify
# print('views')
# user_schema = UserSchema()
# users_schema = UserSchema()


# @app.route('/users', methods=['POST'])
# def create_user():
#     print(request.headers, 'headersssss')

#     if(request.headers.__contains__('Token')):
#         role = request.json['role'] = 'admin'
#     else:
#         role = request.json['role'] = 'candidate'

#     username = request.json['username']
#     date_of_birth = request.json['date_of_birth']
#     years_of_experience = request.json['years_of_experience']
#     created_at = request.json['created_at']

#     new_user = User(username, date_of_birth,
#                     years_of_experience, role, created_at)
#     db.session.add(new_user)
#     db.session.commit()
#     return user_schema.jsonify(new_user)


# @ app.route('/users', methods=['GET'])
# def get_users():
#     if(request.headers.__contains__('Token')):
#         all_users = User.query.all()
#         result = users_schema.dump(all_users)
#         return jsonify(result)
#     else:
#         return jsonify({'error': 'UNAUTHORIZED'}), 401


# @ app.route('/users/<id>', methods=['GET'])
# def get_singleUser(id):
#     user = User.query.get(id)
#     if user:
#         return user_schema.jsonify(user)
#     else:
#         return jsonify({'error': 'user not found'}), 404

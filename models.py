# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String)
#     date_of_birth = db.Column(db.String)
#     years_of_experience = db.Column(db.Integer)
#     role = db.Column(db.String)
#     created_at = db.Column(db.String, server_default=db.func.now())
#     department = db.Column(db.String)
#     # file = relationship("File", backref=db.backref("user", uselist=False))

#     def __init__(self, username, date_of_birth, years_of_experience, role, created_at, department):
#         self.username = username
#         self.date_of_birth = date_of_birth
#         self.years_of_experience = years_of_experience
#         self.role = role
#         self.created_at = created_at
#         self.department = department
#         # self.file = file


# class File(db.Model):
#     __tablename__ = 'file'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))
#     type = db.Column(db.String(8))
#     filename = db.column_property(name + '.' + type)
#     path = db.column_property(
#         '/Users/essamabuissa/Desktop/Development/Python/hr-backend/resumes' + filename.expression)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

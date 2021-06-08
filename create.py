from run import db, User

username = "Admin"
password = "admin123"
level = "Admin"
db.session.add(User(username,password,level))
db.session.commit()
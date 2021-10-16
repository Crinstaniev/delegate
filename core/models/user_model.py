from . import db, ma


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    user_name = db.Column(db.String(100))
    user_email = db.Column(db.String(100))
    user_sign_up_date = db.Column(db.DateTime)
    user_signature = db.Column(db.LargeBinary)

    psychology_test_result = db.relationship('PsychologyTestResult', backref='user', lazy=True)
    records = db.relationship('Record', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.user_name}>'


class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_name', 'user_email', 'user_sign_up_date', 'user_signature')


user_schema = UserSchema()
users_schema = UserSchema(many=True)

from . import db, ma


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    sign_up_date = db.Column(db.DateTime)
    signature = db.Column(db.Text)  # binary string
    password = db.Column(db.String(100))
    treatment = db.Column(db.Integer)
    rationality = db.Column(db.Boolean)

    psychology_test_result = db.relationship('PsychologyTestResult', backref='user', lazy=True)
    records = db.relationship('Record', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.user_name}>'


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'sign_up_date', 'treatment', 'rationality')


user_schema = UserSchema()
users_schema = UserSchema(many=True)

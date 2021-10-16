from . import db, ma


class PsychologyTestResult(db.Model):
    __tablename__ = 'psychology_test_result'

    id = db.Column(db.Integer, primary_key=True)

    question_id = db.Column(db.Integer)
    result = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class PsychologyTestResultSchema(ma.Schema):
    class Meta:
        fields = ('id', 'question_id', 'result', 'user_id')


psychology_test_result_schema = PsychologyTestResultSchema()
psychology_test_results_schema = PsychologyTestResultSchema(many=True)

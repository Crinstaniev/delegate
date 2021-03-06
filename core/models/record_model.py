from . import db, ma


class Record(db.Model):
    __tablename__ = 'record'

    id = db.Column(db.Integer, primary_key=True)

    time = db.Column(db.DateTime)
    cash = db.Column(db.Float)
    eth_holding = db.Column(db.Float)
    vta = db.Column(db.Float)
    roi_1 = db.Column(db.Float)
    roi_2 = db.Column(db.Float)
    roi_3 = db.Column(db.Float)
    decision_phase = db.Column(db.Integer)
    decision_maker = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Record {self.user_id} - {self.id}>'


class RecordSchema(ma.Schema):
    class Meta:
        fields = ('id', 'time', 'cash',
                  'eth_holding', 'vta', 'roi_1', 'roi_2', 'roi_3',
                  'decision_phase', 'decision_maker',
                  'user_id')


record_schema = RecordSchema()
records_schema = RecordSchema(many=True)

from . import db, ma


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    cash = db.Column(db.Float)
    eth_holding = db.Column(db.Float)
    vta = db.Column(db.Float)
    roi = db.Column(db.Float)
    decision_phase = db.Column(db.Integer)
    decision_maker = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Record {self.user_id} - {self.id}>'


class RecordSchema(ma.Schema):
    class Meta:
        fields = ('id', 'datetime', 'cash',
                  'eth_holding', 'vta', 'roi',
                  'decision_phase', 'decision_maker')


record_schema = RecordSchema()
records_schema = RecordSchema(many=True)

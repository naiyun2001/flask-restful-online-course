from restdemo import db


class Base(db.Model):

    __abstract__ = True     # 表抽象 class, 非正式的 DB Model

    def as_dict(self):
        # 轉 dict
        # column name(key): datd(val)
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

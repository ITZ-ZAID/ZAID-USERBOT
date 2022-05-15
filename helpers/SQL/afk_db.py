from sqlalchemy import Column, String, Boolean, UnicodeText

from helpers.SQL import BASE, SESSION
Owner = 0


class AFK(BASE):
    __tablename__ = "afk"
    user_id = Column(String(14), primary_key=True)
    is_afk = Column(Boolean, default=False)
    reason = Column(UnicodeText, default=False)

    def __init__(self, user_id, is_afk, reason):
        self.user_id = str(user_id)
        self.is_afk = is_afk
        self.reason = reason

    def __repr__(self):
        return "<AFK {}>".format(self.user_id)


AFK.__table__.create(checkfirst=True)

MY_AFK = {}


def set_afk(afk, reason):
    global MY_AFK
    afk_db = SESSION.query(AFK).get(str(Owner))
    if afk_db:
        SESSION.delete(afk_db)
    afk_db = AFK(Owner, afk, reason)
    SESSION.add(afk_db)
    SESSION.commit()
    MY_AFK[Owner] = {"afk": afk, "reason": reason}


def get_afk():
    return MY_AFK.get(Owner)


def __load_afk():
    global MY_AFK
    try:
        MY_AFK = {}
        qall = SESSION.query(AFK).all()
        for x in qall:
            MY_AFK[int(x.user_id)] = {"afk": x.is_afk, "reason": x.reason}
    finally:
        SESSION.close()


__load_afk()

try:
    from helpers.SQL import BASE, SESSION
except ImportError:
    raise AttributeError
from sqlalchemy import Column, String, UnicodeText
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.functions import user
from sqlalchemy.sql.sqltypes import Integer

warns=3 #max number of warning for a user

class User(BASE):
    __tablename__ = "permitted"
    user_id = Column(Integer, primary_key=True, nullable=False)
    warning = Column(Integer, primary_key=True, default=0)

    def __init__(self, variable):
        self.user_id = variable

    def __init__(self , userid , warning):
        self.user_id=userid
        self.warning=warning

User.__table__.create(checkfirst=True)

def givepermit(userid): # to give a permit to the user just pass the user id (can be a new user or old user with already warns), it would be updated in the db connected and warning would go to -1 i.e it is permitted
    if SESSION.query(User).filter(User.user_id == userid).one_or_none():
        SESSION.query(User).filter(User.user_id == userid).update({
            User.warning: -1
        })
    else:
        adduser=User(userid,-1)
        SESSION.add(adduser)
        SESSION.commit()

def checkpermit(userid): # if warning is -1(permitted) then returns true , if warning is warns(blocked) then returns false
    if SESSION.query(User).filter(User.user_id == userid).one_or_none():
        return SESSION.query(User).filter(User.user_id == userid).one_or_none().warning == -1
    else:
        if SESSION.query(User).filter(User.user_id == userid).one_or_none():
            return not (SESSION.query(User).filter(User.user_id == userid).one_or_none().warning == warns)

def blockuser(userid): # blocks a user by changing it's warning to warns(max warns)
    if SESSION.query(User).filter(User.user_id == userid).one_or_none():
        SESSION.query(User).filter(User.user_id == userid).update({
            User.warning: warns
        })
    else:
        adduser=User(userid,warns)
        SESSION.add(adduser)
        SESSION.commit()

def getwarns(userid): # to get warns of a specific user if it exists in db
    if SESSION.query(User).filter(User.user_id == userid).one_or_none():
        return SESSION.query(User).filter(User.user_id == userid).one_or_none().warning
    else:
        return "USER DON'T EXISTS"

def addwarns(userid): # updates the warning by 1 each time it is called , or gives a warn to the user if already not present
    if SESSION.query(User).filter(User.user_id == userid).one_or_none():
        SESSION.query(User).filter(User.user_id == userid).update({
            User.warning: User.warning+1
        })
    else:
        adduser=User(userid,1)
        SESSION.add(adduser)
        SESSION.commit()    


def allallowed():
    query = SESSION.query(User).filter(User.warning == -1)
    alloweduser=[]
    for row in query:
        alloweduser.append(row.user_id)
    return alloweduser

def allblocked():
    query = SESSION.query(User).filter(User.warning == warns)
    blockeduser=[]
    for row in query:
        blockeduser.append(row.user_id)
    return blockeduser

def inwarns():
    query = SESSION.query(User).filter(User.warning > -1 and User.warning<3)
    inwarns=[]
    for row in query:
        inwarns.append(row.user_id)
    return inwarns

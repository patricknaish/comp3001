"""
Session Datastore object
"""

import json
import time

from google.appengine.ext import db

class Session(db.Model):
    "Class representing a session in the book trading system"

    sessionID = db.StringProperty()
    data = db.StringProperty()
    expires = db.IntegerProperty()

    @staticmethod
    def write_session(sessionID, sessionData):
        sessionData = json.dumps(sessionData)
        if Session.get_session(sessionID) != None:
            session = Session.get_by_key_name(sessionID)
        else:
            session = Session(key_name = sessionID,
                              sessionID = sessionID,
                              data = sessionData,
                              expires = long(time.time() + 3600))
        session.put()

    @staticmethod
    def get_session(sessionID):
        session = Session.get_by_key_name(sessionID)
        if not session: return None
        return json.loads(session.data)

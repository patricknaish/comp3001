"""
Module containing methods for manipulating messages
"""

from google.appengine.ext import db
from lib import User

class Message(db.Model):
    """
    Defines the user schema
    """
    fromUser = db.ReferenceProperty(User, 
                                    required=True, 
                                    collection_name = 'messages')
    toUser = db.ReferenceProperty(User, 
                                  required=True, 
                                  collection_name = 'messages')
    sent = db.DateTimeProperty(auto_now_add=True)
    subject = db.StringProperty()
    body = db.TextProperty()

    @staticmethod
    def create_message(from_user_email,
                       to_user_email,
                       message_subject,
                       message_body):
        """
        Add a new message to the datastore
        """
        from_user_ref = User.get_by_key_name(from_user_email)
        to_user_ref = User.get_by_key_name(to_user_email)
        new_message = Message(fromUser=from_user_ref,
                              toUser=to_user_ref,
                              subject=message_subject,
                              body=message_body)
        new_message.put()
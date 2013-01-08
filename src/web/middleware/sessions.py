"""
Some Django Middleware that uses signed cookies
"""
import os
import time
import hashlib
import Cookie
import random

import logging

import lib

SESSION_KEY = "2af6da2818aede3c589c5508030f2e6d2fd2c279"

class SessionMiddleware(object):
    def process_request(self, request):
        self.request = request
        self.request.session = Session()

    def process_response(self, request, response):
        if hasattr(request, "session"):
            request.session.save()
            cookie = Cookie.SimpleCookie()
            cookie[request.session.get_cookie_name()] = request.session.get_cookie_data()
            cookie[request.session.get_cookie_name()]["path"] = "/"
            response.cookies = cookie
        return response

class Session(object):
    def __init__(self):
        self.SessionStore = dict()
        self._loadByCookie()

    def __setitem__(self, item, val):
        self.SessionStore[item] = val

    def __getitem__(self, item):
        return self.SessionStore[item]

    def __delitem__(self, item):
        del self.SessionStore[item]

    def get(self, item, default = None):
        if item in self.SessionStore.keys():
            return self.SessionStore[item]
        else:
            return default

    def keys(self):
        return self.SessionStore.keys()

    def items(self):
        return self.SessionStore.items()

    def setdefault(self):
        self.clear()

    def clear(self):
        self.SessionStore.clear()

    def flush(self):
        pass

    def save(self):
        lib.SESSION.write_session(self.SID, self.SessionStore)

    def _new_sid(self):
        return hashlib.md5(SESSION_KEY + repr(time.time()) + str(random.random())).hexdigest()

    def check_cookie(self):
        cookie = os.environ.get("HTTP_COOKIE", "")
        self.cookie = Cookie.SimpleCookie()
        self.cookie.load(cookie)
        if not "TTSID" in self.cookie.keys():
            self.SID = self._new_sid()

    def get_cookie_name(self):
        return "TTSID"

    def get_cookie_data(self):
        return self.SID

    def _loadByCookie(self):
        cookie = os.environ.get("HTTP_COOKIE", "")
        self.cookie = Cookie.SimpleCookie()
        self.cookie.load(cookie)
        if "TTSID" in self.cookie.keys():
            self.SID = self.cookie["TTSID"].value
            logging.info(self.SID)
            session = lib.SESSION.get_session(self.SID)
            if session != None:
                self.SessionStore = session
        else:
            self.SID = self._new_sid()

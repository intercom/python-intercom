# -*- coding: utf-8 -*-

import inspect


class BaseHandler(type):

    def __getattr__(cls, name):  # noqa
        # ignore underscore attrs
        if name[0] == "_":
            return

        import time
        a = time.time()
        # get the class heirarchy
        klasses = inspect.getmro(cls)
        b = time.time()
        # find a class that can handle this attr
        for klass in klasses:
            if hasattr(klass, 'handles_attr') and klass.handles_attr(name):
                c = time.time()
                d = b - a
                e = c - b
                print("GETMRO %s HANDLE %s" % (d, e))
                return klass._get(cls, name)

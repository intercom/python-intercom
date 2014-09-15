import numbers


class FlatStore(dict):

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __setitem__(self, key, value):
        if not (
            isinstance(value, numbers.Real) or
            isinstance(value, basestring)
        ):
            raise ValueError(
                "custom data only allows string and real number values")
        if not isinstance(key, basestring):
            raise ValueError("custom data only allows string keys")
        super(FlatStore, self).__setitem__(key, value)

    def update(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                raise TypeError("update expected at most 1 arguments, "
                                "got %d" % len(args))
            other = dict(args[0])
            for key in other:
                self[key] = other[key]
        for key in kwargs:
            self[key] = kwargs[key]

    def setdefault(self, key, value=None):
        if key not in self:
            self[key] = value
        return self[key]

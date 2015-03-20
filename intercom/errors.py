# -*- coding: utf-8 -*-


class ArgumentError(ValueError):
    pass


class HttpError(Exception):
    pass


class IntercomError(Exception):
    pass


class ResourceNotFound(IntercomError):
    pass


class AuthenticationError(IntercomError):
    pass


class ServerError(IntercomError):
    pass


class BadGatewayError(IntercomError):
    pass


class ServiceUnavailableError(IntercomError):
    pass

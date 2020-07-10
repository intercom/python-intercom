# -*- coding: utf-8 -*-


class IntercomError(Exception):

    def __init__(self, message=None, context=None):
        super(IntercomError, self).__init__(message)
        self.message = message
        self.context = context


class ArgumentError(ValueError, IntercomError):
    pass


class HttpError(IntercomError):
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


class BadRequestError(IntercomError):
    pass


class RateLimitExceeded(IntercomError):
    pass


class ResourceNotRestorable(IntercomError):
    pass


class MultipleMatchingUsersError(IntercomError):
    pass


class UnexpectedError(IntercomError):
    pass


class TokenUnauthorizedError(IntercomError):
    pass


class TokenNotFoundError(IntercomError):
    pass


error_codes = {
    'unauthorized': AuthenticationError,
    'forbidden': AuthenticationError,
    'bad_request': BadRequestError,
    'action_forbidden': BadRequestError,
    'missing_parameter': BadRequestError,
    'parameter_invalid': BadRequestError,
    'parameter_not_found': BadRequestError,
    'client_error': BadRequestError,
    'type_mismatch': BadRequestError,
    'not_found': ResourceNotFound,
    'company_not_found': ResourceNotFound,
    'admin_not_found': ResourceNotFound,
    'not_restorable': ResourceNotRestorable,
    'rate_limit_exceeded': RateLimitExceeded,
    'service_unavailable': ServiceUnavailableError,
    'server_error': ServiceUnavailableError,
    'conflict': MultipleMatchingUsersError,
    'unique_user_constraint': MultipleMatchingUsersError,
    'token_unauthorized': TokenUnauthorizedError,
    'token_not_found': TokenNotFoundError,
    'token_revoked': TokenNotFoundError,
    'token_blocked': TokenNotFoundError,
    'token_expired': TokenNotFoundError
}

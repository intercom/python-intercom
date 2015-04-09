# -*- coding: utf-8 -*-

import json
import os

from mock import Mock

DIRPATH = os.path.dirname(__file__)
FIXTURES = os.path.join(DIRPATH, 'fixtures')


def create_response(status, fixture=None):
    def request(*args, **kwargs):
        response = Mock()
        response.status_code = status
        if fixture:
            fixture_path = os.path.join(FIXTURES, fixture)
            response.content = open(fixture_path).read()
        return response
    return request


def local_response(**params):
    def _call(*args, **kwargs):
        response = Mock()
        reply = {}
        for name, value in list(kwargs.items()):
            reply[name] = value
        for name, value in list(params.items()):
            reply[name] = value
        response.content = json.dumps(reply)
        response.status_code = 200
        return response
    return _call


def mock_response(content, status_code=200, encoding='utf-8', headers=None):
    if headers is None:
        headers = {
            'x-ratelimit-limit': 500,
            'x-ratelimit-remaining': 500,
            'x-ratelimit-reset': 1427932858
        }
    return Mock(
        content=content, status_code=status_code, encoding=encoding, headers=headers)


def get_user(email="bob@example.com", name="Joe Schmoe"):
    return {
        "type": "user",
        "id": "aaaaaaaaaaaaaaaaaaaaaaaa",
        "user_id": 'id-from-customers-app',
        "email": email,
        "name": name,
        "avatar": {
            "type": "avatar",
            "image_url": "https://graph.facebook.com/1/picture?width=24&height=24"
        },
        "app_id": "the-app-id",
        "created_at": 1323422442,
        "custom_attributes": {"a": "b", "b": 2},
        "companies": {
            "type": "company.list",
            "companies": [
                {
                    "type": "company",
                    "company_id": "123",
                    "id": "bbbbbbbbbbbbbbbbbbbbbbbb",
                    "app_id": "the-app-id",
                    "name": "Company 1",
                    "remote_created_at": 1390936440,
                    "created_at": 1401970114,
                    "updated_at": 1401970114,
                    "last_request_at": 1401970113,
                    "monthly_spend": 0,
                    "session_count": 0,
                    "user_count": 1,
                    "tag_ids": [],
                    "custom_attributes": {
                        "category": "Tech"
                    }
                }
            ]
        },
        "session_count": 123,
        "unsubscribed_from_emails": True,
        "last_request_at": 1401970113,
        "created_at": 1401970114,
        "remote_created_at": 1393613864,
        "updated_at": 1401970114,
        "user_agent_data": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "social_profiles": {
            "type": "social_profile.list",
            "social_profiles": [
                {
                    "type": "social_profile",
                    "name": "twitter",
                    "url": "http://twitter.com/abc",
                    "username": "abc",
                    "id": None
                },
                {
                    "type": "social_profile",
                    "name": "twitter",
                    "username": "abc2",
                    "url": "http://twitter.com/abc2",
                    "id": None
                },
                {
                    "type": "social_profile",
                    "name": "facebook",
                    "url": "http://facebook.com/abc",
                    "username": "abc",
                    "id": "1234242"
                },
                {
                    "type": "social_profile",
                    "name": "quora",
                    "url": "http://facebook.com/abc",
                    "username": "abc",
                    "id": "1234242"
                }
            ]
        },
        "location_data": {
            "type": "location_data",
            "city_name": 'Dublin',
            "continent_code": 'EU',
            "country_name": 'Ireland',
            "latitude": '90',
            "longitude": '10',
            "postal_code": 'IE',
            "region_name": 'Europe',
            "timezone": '+1000',
            "country_code": "IRL"
        }
    }


def page_of_users(include_next_link=False):
    page = {
        "type": "user.list",
        "pages": {
            "type": "pages",
            "page": 1,
            "next": None,
            "per_page": 50,
            "total_pages": 7
        },
        "users": [
            get_user("user1@example.com"),
            get_user("user2@example.com"),
            get_user("user3@example.com")],
        "total_count": 314
    }
    if include_next_link:
        page["pages"]["next"] = "https://api.intercom.io/users?per_page=50&page=2"
    return page

test_tag = {
    "id": "4f73428b5e4dfc000b000112",
    "name": "Test Tag",
    "segment": False,
    "tagged_user_count": 2
}

test_subscription = {
    "type": "notification_subscription",
    "id": "nsub_123456789",
    "created_at": 1410368642,
    "updated_at": 1410368642,
    "service_type": "web",
    "app_id": "3qmk5gyg",
    "url": "http://example.com",
    "self": "https://api.intercom.io/subscriptions/nsub_123456789",
    "topics": ["user.created", "conversation.user.replied", "conversation.admin.replied"],
    "active": True,
    "metadata": {},
    "hub_secret": None,
    "mode": "point",
    "links": {
        "sent": "https://api.intercom.io/subscriptions/nsub_123456789/sent",
        "retry": "https://api.intercom.io/subscriptions/nsub_123456789/retry",
        "errors": "https://api.intercom.io/subscriptions/nsub_123456789/errors"
    },
    "notes": []
}

test_user_notification = {
    "type": "notification_event",
    "id": "notif_123456-56465-546546",
    "topic": "user.created",
    "app_id": "aaaaaa",
    "data": {
        "type": "notification_event_data",
        "item": {
            "type": "user",
            "id": "aaaaaaaaaaaaaaaaaaaaaaaa",
            "user_id": None,
            "email": "joe@example.com",
            "name": "Joe Schmoe",
            "avatar": {
                "type": "avatar",
                "image_url": None
            },
            "app_id": "aaaaa",
            "companies": {
                "type": "company.list",
                "companies": []
            },
            "location_data": {
            },
            "last_request_at": None,
            "created_at": "1401970114",
            "remote_created_at": None,
            "updated_at": "1401970114",
            "session_count": 0,
            "social_profiles": {
                "type": "social_profile.list",
                "social_profiles": []
            },
            "unsubscribed_from_emails": False,
            "user_agent_data": None,
            "tags": {
                "type": "tag.list",
                "tags": []
            },
            "segments": {
                "type": "segment.list",
                "segments": []
            },
            "custom_attributes": {
            }
        }
    },
    "delivery_status": None,
    "delivery_attempts": 1,
    "delivered_at": 0,
    "first_sent_at": 1410188629,
    "created_at": 1410188628,
    "links": {},
    "self": None
}

test_conversation_notification = {
    "type": "notification_event",
    "id": "notif_123456-56465-546546",
    "topic": "conversation.user.created",
    "app_id": "aaaaa",
    "data": {
        "type": "notification_event_data",
        "item": {
            "type": "conversation",
            "id": "123456789",
            "created_at": "1410335293",
            "updated_at": "1410335293",
            "user": {
                "type": "user",
                "id": "540f1de7112d3d1d51001637",
                "name": "Kill Bill",
                "email": "bill@bill.bill"
            },
            "assignee": {
                "type": "nobody_admin",
                "id": None
            },
            "conversation_message": {
                "type": "conversation_message",
                "id": "321546",
                "subject": "",
                "body": "<p>An important message</p>",
                "author": {
                    "type": "user",
                    "id": "aaaaaaaaaaaaaaaaaaaaaa",
                    "name": "Kill Bill",
                    "email": "bill@bill.bill"
                },
                "attachments": []
            },
            "conversation_parts": {
                "type": "conversation_part.list",
                "conversation_parts": []
            },
            "open": None,
            "read": True,
            "links": {
                "conversation_web": "https://app.intercom.io/a/apps/aaaaaa/inbox/all/conversations/123456789"
            }
        }
    },
    "delivery_status": None,
    "delivery_attempts": 1,
    "delivered_at": 0,
    "first_sent_at": 1410335293,
    "created_at": 1410335293,
    "links": {},
    "self": "http://example.com/resource/url/"
}

# coding=utf-8
#
# Copyright 2014 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from describe import expect
import intercom
import mock
import time
from datetime import datetime


class DescribeIntercom:

    # def it_has_a_version_number(self):
    #     expect(intercom).to.have_attr('__version__')

    class DescribeExpectingArguments:

        def before_each(self, context):
            logfile = open('log.txt', 'w')
            logfile.write('%s\n' % (context))
            logfile.close()
            context['intercom'] = intercom.Intercom
            self.intercom = context['intercom']
            self.intercom.app_id = 'abc123'
            self.intercom.app_api_key = 'super-secret-key'

        def it_raises_argumenterror_if_no_app_id_or_app_api_key_specified(self):
            self.intercom.app_id = None
            self.intercom.app_api_key = None
            with expect.to_raise_error(intercom.ArgumentError):
                self.intercom._target_base_url

        def it_returns_the_app_id_and_app_api_key_previously_set(self):
            expect(self.intercom.app_id) == 'abc123'
            expect(self.intercom.app_api_key) == 'super-secret-key'

        def it_defaults_to_https_to_api_intercom_io(self):
            expect(self.intercom._target_base_url) == \
                'https://abc123:super-secret-key@api.intercom.io'

        class DescribeOverridingProtocolHostname:
            def before_each(self, context):
                self.intercom = context['intercom']
                self.protocol = self.intercom.protocol
                self.hostname = self.intercom.hostname
                self.intercom.endpoints = None

            def after_each(self, context):
                self.intercom.protocol = self.protocol
                self.intercom.hostname = self.hostname
                self.intercom.endpoints = ["https://api.intercom.io"]

            def it_allows_overriding_of_the_endpoint_and_protocol(self):
                self.intercom.protocol = "http"
                self.intercom.hostname = "localhost:3000"
                expect(
                    self.intercom._target_base_url,
                    "http://abc123:super-secret-key@localhost:3000")

            def it_prefers_endpoints(self):
                self.intercom.endpoint = "https://localhost:7654"
                expect(self.intercom._target_base_url) == "https://abc123:super-secret-key@localhost:7654"

                # turn off the shuffle
                with mock.patch("random.shuffle") as mock_shuffle:
                    mock_shuffle.return_value = ["http://example.com", "https://localhost:7654"]
                    self.intercom.endpoints = ["http://example.com", "https://localhost:7654"]
                    expect(self.intercom._target_base_url) == \
                        'http://abc123:super-secret-key@example.com'

            def it_has_endpoints(self):
                expect(self.intercom.endpoints) == ["https://api.intercom.io"]
                self.intercom.endpoints = ["http://example.com","https://localhost:7654"]
                expect(self.intercom.endpoints) == ["http://example.com","https://localhost:7654"]

            def it_should_randomize_endpoints_if_last_checked_endpoint_is_gt_5_minutes_ago(self):
                now = time.mktime(datetime.utcnow().timetuple())
                self.intercom._config._endpoint_randomized_at = now
                self.intercom.endpoints = ["http://alternative"]
                self.intercom.current_endpoint = "http://start"

                self.intercom._config.endpoint_randomized_at = now - 120
                expect(self.intercom.current_endpoint) == "http://start"
                self.intercom._config.endpoint_randomized_at = now - 360
                expect(self.intercom.current_endpoint) == "http://alternative"


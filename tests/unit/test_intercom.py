
import intercom
import mock
import time
from datetime import datetime
from intercom import Intercom
from nose.tools import eq_
from nose.tools import ok_
from nose.tools import raises


def test_version():
    ok_(hasattr(intercom, '__version__'))


@raises(intercom.ArgumentError)
def test_no_app_config():
    Intercom.app_id = None
    Intercom.app_api_key = None
    Intercom._target_base_url


def test_app_config():
    Intercom.app_id = 'abc123'
    Intercom.app_api_key = 'super-secret-key'
    eq_('abc123', Intercom.app_id)
    eq_('super-secret-key', Intercom.app_api_key)


def test_https_base_url():
    Intercom.app_id = 'abc123'
    Intercom.app_api_key = 'super-secret-key'
    print "INTERCOM PROTOCOL 2", Intercom._protocol
    print "INTERCOM PROTOCOL 2", Intercom._hostname
    eq_(
        'https://abc123:super-secret-key@api.intercom.io',
        Intercom._target_base_url
    )


def test_default_endpoints():
    eq_(['https://api.intercom.io'], Intercom._endpoints)


class TestEndpoints(object):

    def setUp(self):
        self._protocol = Intercom._protocol
        self._hostname = Intercom._hostname
        Intercom.app_id = 'abc123'
        Intercom.app_api_key = 'super-secret-key'

    def tearDown(self):
        Intercom._protocol = self._protocol
        Intercom._hostname = self._hostname

    def test_overide_protocol_host(self):
        Intercom._protocol = 'http'
        Intercom._hostname = 'localhost:3000'

        eq_(['http://localhost:3000'], Intercom._endpoints)
        eq_(
            'http://abc123:super-secret-key@localhost:3000',
            Intercom._target_base_url
        )

    def test_prefers_endpoint(self):
        Intercom._endpoint = 'https://localhost:7654'
        eq_(
            'https://abc123:super-secret-key@localhost:7654',
            Intercom._target_base_url
        )
        # turn off the shuffle
        with mock.patch("random.shuffle") as mock_shuffle:
            mock_shuffle.return_value = ["http://example.com", "https://localhost:7654"]
            Intercom._endpoints = ["http://example.com", "https://localhost:7654"]
            eq_(
                'http://abc123:super-secret-key@example.com',
                Intercom._target_base_url
            )

    def test_has_endpoints(self):
        eq_(["https://api.intercom.io"], Intercom._endpoints)
        Intercom._endpoints = ["http://example.com", "https://localhost:7654"]
        eq_(["http://example.com", "https://localhost:7654"], Intercom._endpoints)


    def test_randomize_endpoints(self):
        now = time.mktime(datetime.utcnow().timetuple())
        Intercom._current_endpoint = "http://start"
        Intercom._endpoints = ["http://alternative"]
        print "ERA 1", Intercom._config.endpoint_randomized_at
        Intercom._config.endpoint_randomized_at = now - 120
        print "ERA 2", Intercom._config.endpoint_randomized_at
        eq_("http://start", Intercom._current_endpoint)
        print "ERA 3", Intercom._config.endpoint_randomized_at
        Intercom._config.endpoint_randomized_at = now - 360
        eq_("http://alternative", Intercom._current_endpoint)


      # it "should randomize endpoints if last checked endpoint is > 5 minutes ago" do
      #   Intercom.instance_variable_set(:@current_endpoint, "http://start")
      #   Intercom.instance_variable_set(:@endpoints, ["http://alternative"])
      #   Intercom.instance_variable_set(:@endpoint_randomized_at, Time.now - 120)
      #   Intercom.current_endpoint.must_equal "http://start"
      #   Intercom.instance_variable_set(:@endpoint_randomized_at, Time.now - 360)
      #   Intercom.current_endpoint.must_equal "http://alternative"
      #   Intercom.instance_variable_get(:@endpoint_randomized_at).to_i.must_be_close_to Time.now.to_i
      # end


    # def test_override
    #       it "allows overriding of the endpoint and protocol" do
    #         Intercom.protocol = "http"
    #         Intercom.hostname = "localhost:3000"
    #         Intercom.target_base_url.must_equal "http://abc123:super-secret-key@localhost:3000"
    #       end

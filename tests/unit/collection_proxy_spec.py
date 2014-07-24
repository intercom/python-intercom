import httpretty
import json
import re
from describe import expect
from intercom.admin import Admin
from intercom.collection_proxy import CollectionProxy

get = httpretty.GET
r = re.compile


class DescribeIntercomCollectionProxy:

    @httpretty.activate
    def it_stops_iterating_if_no_next_link(self):
        body = json.dumps({})
        httpretty.register_uri(get, r(r"/users"), body=body)
        all = Admin.all()
        expect(all).to.be_instance_of(CollectionProxy)


# require "spec_helper"

# describe Intercom::CollectionProxy do

#   it "stops iterating if no next link" do
#     Intercom.expects(:get).with("/users", {}).returns(page_of_users(include_next_link:false))
#     emails = []
#     Intercom::User.all.each { |user| emails << user.email }
#     emails.must_equal %W(user1@example.com user2@example.com user3@example.com)
#   end

#   it "keeps iterating if next link" do
#     Intercom.expects(:get).with("/users", {}).returns(page_of_users(include_next_link:true))
#     Intercom.expects(:get).with('https://api.intercom.io/users?per_page=50&page=2', {}).returns(page_of_users(include_next_link:false))
#     emails = []
#     Intercom::User.all.each { |user| emails << user.email }
#   end

#   it "supports indexed array access" do
#     Intercom.expects(:get).with("/users", {}).returns(page_of_users(include_next_link:false))
#     Intercom::User.all[0].email.must_equal 'user1@example.com'
#   end

#   it "supports map" do
#     Intercom.expects(:get).with("/users", {}).returns(page_of_users(include_next_link:false))
#     emails = Intercom::User.all.map { |user| user.email }
#     emails.must_equal %W(user1@example.com user2@example.com user3@example.com)
#   end

#   it "supports querying" do
#     Intercom.expects(:get).with("/users", {:tag_name => 'Taggart J'}).returns(page_of_users(include_next_link:false))
#     Intercom::User.find_all(:tag_name => 'Taggart J').map(&:email).must_equal %W(user1@example.com user2@example.com user3@example.com)
#   end
# end

# Shared Types

```python
from intercom.types import (
    Admin,
    ArticleContent,
    ArticleTranslatedContent,
    Company,
    Contact,
    Conversation,
    GroupContent,
    GroupTranslatedContent,
    Message,
    MultipleFilterSearchRequest,
    Note,
    PaginatedResponse,
    SearchRequest,
    SubscriptionTypeList,
    Tag,
    TagList,
    Ticket,
    TicketTypeAttribute,
)
```

# Me

Types:

```python
from intercom.types import AdminWithApp
```

Methods:

- <code title="get /me">client.me.<a href="./src/intercom/resources/me.py">retrieve</a>() -> <a href="./src/intercom/types/admin_with_app.py">Optional</a></code>

# Admins

Types:

```python
from intercom.types import AdminList
```

Methods:

- <code title="get /admins/{id}">client.admins.<a href="./src/intercom/resources/admins/admins.py">retrieve</a>(id) -> <a href="./src/intercom/types/shared/admin.py">Optional</a></code>
- <code title="get /admins">client.admins.<a href="./src/intercom/resources/admins/admins.py">list</a>() -> <a href="./src/intercom/types/admin_list.py">AdminList</a></code>
- <code title="put /admins/{id}/away">client.admins.<a href="./src/intercom/resources/admins/admins.py">set_away</a>(id, \*\*<a href="src/intercom/types/admin_set_away_params.py">params</a>) -> <a href="./src/intercom/types/shared/admin.py">Optional</a></code>

## ActivityLogs

Types:

```python
from intercom.types.admins import ActivityLogList
```

Methods:

- <code title="get /admins/activity_logs">client.admins.activity_logs.<a href="./src/intercom/resources/admins/activity_logs.py">list</a>(\*\*<a href="src/intercom/types/admins/activity_log_list_params.py">params</a>) -> <a href="./src/intercom/types/admins/activity_log_list.py">ActivityLogList</a></code>

# Articles

Types:

```python
from intercom.types import Article, ArticleList, ArticleSearchResponse, DeletedArticleObject
```

Methods:

- <code title="post /articles">client.articles.<a href="./src/intercom/resources/articles.py">create</a>(\*\*<a href="src/intercom/types/article_create_params.py">params</a>) -> <a href="./src/intercom/types/article.py">Article</a></code>
- <code title="get /articles/{id}">client.articles.<a href="./src/intercom/resources/articles.py">retrieve</a>(id) -> <a href="./src/intercom/types/article.py">Article</a></code>
- <code title="put /articles/{id}">client.articles.<a href="./src/intercom/resources/articles.py">update</a>(id, \*\*<a href="src/intercom/types/article_update_params.py">params</a>) -> <a href="./src/intercom/types/article.py">Article</a></code>
- <code title="get /articles">client.articles.<a href="./src/intercom/resources/articles.py">list</a>() -> <a href="./src/intercom/types/article_list.py">ArticleList</a></code>
- <code title="delete /articles/{id}">client.articles.<a href="./src/intercom/resources/articles.py">remove</a>(id) -> <a href="./src/intercom/types/deleted_article_object.py">DeletedArticleObject</a></code>
- <code title="get /articles/search">client.articles.<a href="./src/intercom/resources/articles.py">search</a>(\*\*<a href="src/intercom/types/article_search_params.py">params</a>) -> <a href="./src/intercom/types/article_search_response.py">ArticleSearchResponse</a></code>

# HelpCenter

## Collections

Types:

```python
from intercom.types.help_center import Collection, CollectionList, DeletedCollection
```

Methods:

- <code title="post /help_center/collections">client.help_center.collections.<a href="./src/intercom/resources/help_center/collections.py">create</a>(\*\*<a href="src/intercom/types/help_center/collection_create_params.py">params</a>) -> <a href="./src/intercom/types/help_center/collection.py">Collection</a></code>
- <code title="get /help_center/collections/{id}">client.help_center.collections.<a href="./src/intercom/resources/help_center/collections.py">retrieve</a>(id) -> <a href="./src/intercom/types/help_center/collection.py">Collection</a></code>
- <code title="put /help_center/collections/{id}">client.help_center.collections.<a href="./src/intercom/resources/help_center/collections.py">update</a>(id, \*\*<a href="src/intercom/types/help_center/collection_update_params.py">params</a>) -> <a href="./src/intercom/types/help_center/collection.py">Collection</a></code>
- <code title="get /help_center/collections">client.help_center.collections.<a href="./src/intercom/resources/help_center/collections.py">list</a>() -> <a href="./src/intercom/types/help_center/collection_list.py">CollectionList</a></code>
- <code title="delete /help_center/collections/{id}">client.help_center.collections.<a href="./src/intercom/resources/help_center/collections.py">delete</a>(id) -> <a href="./src/intercom/types/help_center/deleted_collection.py">DeletedCollection</a></code>

## HelpCenters

Types:

```python
from intercom.types.help_center import HelpCenter, HelpCenterList
```

Methods:

- <code title="get /help_center/help_centers/{id}">client.help_center.help_centers.<a href="./src/intercom/resources/help_center/help_centers.py">retrieve</a>(id) -> <a href="./src/intercom/types/help_center/help_center.py">HelpCenter</a></code>
- <code title="get /help_center/help_centers">client.help_center.help_centers.<a href="./src/intercom/resources/help_center/help_centers.py">list</a>() -> <a href="./src/intercom/types/help_center/help_center_list.py">HelpCenterList</a></code>

# Companies

Types:

```python
from intercom.types import CompanyList, CompanyScroll, DeletedCompanyObject
```

Methods:

- <code title="post /companies">client.companies.<a href="./src/intercom/resources/companies/companies.py">create</a>(\*\*<a href="src/intercom/types/company_create_params.py">params</a>) -> <a href="./src/intercom/types/shared/company.py">Company</a></code>
- <code title="get /companies/{id}">client.companies.<a href="./src/intercom/resources/companies/companies.py">retrieve</a>(id) -> <a href="./src/intercom/types/shared/company.py">Company</a></code>
- <code title="put /companies/{id}">client.companies.<a href="./src/intercom/resources/companies/companies.py">update</a>(id) -> <a href="./src/intercom/types/shared/company.py">Company</a></code>
- <code title="post /companies/list">client.companies.<a href="./src/intercom/resources/companies/companies.py">list</a>(\*\*<a href="src/intercom/types/company_list_params.py">params</a>) -> <a href="./src/intercom/types/company_list.py">CompanyList</a></code>
- <code title="delete /companies/{id}">client.companies.<a href="./src/intercom/resources/companies/companies.py">delete</a>(id) -> <a href="./src/intercom/types/deleted_company_object.py">DeletedCompanyObject</a></code>
- <code title="get /companies">client.companies.<a href="./src/intercom/resources/companies/companies.py">retrieve_list</a>(\*\*<a href="src/intercom/types/company_retrieve_list_params.py">params</a>) -> <a href="./src/intercom/types/company_list.py">CompanyList</a></code>
- <code title="get /companies/scroll">client.companies.<a href="./src/intercom/resources/companies/companies.py">scroll</a>(\*\*<a href="src/intercom/types/company_scroll_params.py">params</a>) -> <a href="./src/intercom/types/company_scroll.py">Optional</a></code>

## Contacts

Types:

```python
from intercom.types.companies import CompanyAttachedContacts
```

Methods:

- <code title="get /companies/{id}/contacts">client.companies.contacts.<a href="./src/intercom/resources/companies/contacts.py">list</a>(id) -> <a href="./src/intercom/types/companies/company_attached_contacts.py">CompanyAttachedContacts</a></code>

## Segments

Types:

```python
from intercom.types.companies import CompanyAttachedSegments
```

Methods:

- <code title="get /companies/{id}/segments">client.companies.segments.<a href="./src/intercom/resources/companies/segments.py">list</a>(id) -> <a href="./src/intercom/types/companies/company_attached_segments.py">CompanyAttachedSegments</a></code>

# Contacts

Types:

```python
from intercom.types import ContactArchived, ContactDeleted, ContactList, ContactUnarchived
```

Methods:

- <code title="post /contacts">client.contacts.<a href="./src/intercom/resources/contacts/contacts.py">create</a>(\*\*<a href="src/intercom/types/contact_create_params.py">params</a>) -> <a href="./src/intercom/types/shared/contact.py">Contact</a></code>
- <code title="get /contacts/{id}">client.contacts.<a href="./src/intercom/resources/contacts/contacts.py">retrieve</a>(id) -> <a href="./src/intercom/types/shared/contact.py">Contact</a></code>
- <code title="put /contacts/{id}">client.contacts.<a href="./src/intercom/resources/contacts/contacts.py">update</a>(id, \*\*<a href="src/intercom/types/contact_update_params.py">params</a>) -> <a href="./src/intercom/types/shared/contact.py">Contact</a></code>
- <code title="get /contacts">client.contacts.<a href="./src/intercom/resources/contacts/contacts.py">list</a>() -> <a href="./src/intercom/types/contact_list.py">ContactList</a></code>
- <code title="delete /contacts/{id}">client.contacts.<a href="./src/intercom/resources/contacts/contacts.py">delete</a>(id) -> <a href="./src/intercom/types/contact_deleted.py">ContactDeleted</a></code>
- <code title="post /contacts/{id}/archive">client.contacts.<a href="./src/intercom/resources/contacts/contacts.py">archive</a>(id) -> <a href="./src/intercom/types/contact_archived.py">ContactArchived</a></code>
- <code title="post /contacts/merge">client.contacts.<a href="./src/intercom/resources/contacts/contacts.py">merge</a>(\*\*<a href="src/intercom/types/contact_merge_params.py">params</a>) -> <a href="./src/intercom/types/shared/contact.py">Contact</a></code>
- <code title="post /contacts/search">client.contacts.<a href="./src/intercom/resources/contacts/contacts.py">search</a>(\*\*<a href="src/intercom/types/contact_search_params.py">params</a>) -> <a href="./src/intercom/types/contact_list.py">ContactList</a></code>
- <code title="post /contacts/{id}/unarchive">client.contacts.<a href="./src/intercom/resources/contacts/contacts.py">unarchive</a>(id) -> <a href="./src/intercom/types/contact_unarchived.py">ContactUnarchived</a></code>

## Companies

Types:

```python
from intercom.types.contacts import ContactAttachedCompanies
```

Methods:

- <code title="delete /contacts/{contact_id}/companies/{id}">client.contacts.companies.<a href="./src/intercom/resources/contacts/companies.py">delete</a>(id, \*, contact_id) -> <a href="./src/intercom/types/shared/company.py">Company</a></code>

## Notes

Types:

```python
from intercom.types.contacts import NoteList
```

Methods:

- <code title="post /contacts/{id}/notes">client.contacts.notes.<a href="./src/intercom/resources/contacts/notes.py">create</a>(id, \*\*<a href="src/intercom/types/contacts/note_create_params.py">params</a>) -> <a href="./src/intercom/types/shared/note.py">Note</a></code>
- <code title="get /contacts/{id}/notes">client.contacts.notes.<a href="./src/intercom/resources/contacts/notes.py">list</a>(id) -> <a href="./src/intercom/types/contacts/note_list.py">NoteList</a></code>

## Segments

Types:

```python
from intercom.types.contacts import ContactSegments
```

Methods:

- <code title="get /contacts/{contact_id}/segments">client.contacts.segments.<a href="./src/intercom/resources/contacts/segments.py">list</a>(contact_id) -> <a href="./src/intercom/types/contacts/contact_segments.py">ContactSegments</a></code>

## Subscriptions

Types:

```python
from intercom.types.contacts import SubscriptionType
```

Methods:

- <code title="post /contacts/{contact_id}/subscriptions">client.contacts.subscriptions.<a href="./src/intercom/resources/contacts/subscriptions.py">create</a>(contact_id, \*\*<a href="src/intercom/types/contacts/subscription_create_params.py">params</a>) -> <a href="./src/intercom/types/contacts/subscription_type.py">SubscriptionType</a></code>
- <code title="get /contacts/{contact_id}/subscriptions">client.contacts.subscriptions.<a href="./src/intercom/resources/contacts/subscriptions.py">list</a>(contact_id) -> <a href="./src/intercom/types/shared/subscription_type_list.py">SubscriptionTypeList</a></code>
- <code title="delete /contacts/{contact_id}/subscriptions/{id}">client.contacts.subscriptions.<a href="./src/intercom/resources/contacts/subscriptions.py">delete</a>(id, \*, contact_id) -> <a href="./src/intercom/types/contacts/subscription_type.py">SubscriptionType</a></code>

## Tags

Methods:

- <code title="post /contacts/{contact_id}/tags">client.contacts.tags.<a href="./src/intercom/resources/contacts/tags.py">create</a>(contact_id, \*\*<a href="src/intercom/types/contacts/tag_create_params.py">params</a>) -> <a href="./src/intercom/types/shared/tag.py">Tag</a></code>
- <code title="get /contacts/{contact_id}/tags">client.contacts.tags.<a href="./src/intercom/resources/contacts/tags.py">list</a>(contact_id) -> <a href="./src/intercom/types/shared/tag_list.py">TagList</a></code>
- <code title="delete /contacts/{contact_id}/tags/{id}">client.contacts.tags.<a href="./src/intercom/resources/contacts/tags.py">delete</a>(id, \*, contact_id) -> <a href="./src/intercom/types/shared/tag.py">Tag</a></code>

# Conversations

Types:

```python
from intercom.types import ConversationList
```

Methods:

- <code title="post /conversations">client.conversations.<a href="./src/intercom/resources/conversations/conversations.py">create</a>(\*\*<a href="src/intercom/types/conversation_create_params.py">params</a>) -> <a href="./src/intercom/types/shared/message.py">Message</a></code>
- <code title="get /conversations/{id}">client.conversations.<a href="./src/intercom/resources/conversations/conversations.py">retrieve</a>(id, \*\*<a href="src/intercom/types/conversation_retrieve_params.py">params</a>) -> <a href="./src/intercom/types/shared/conversation.py">Conversation</a></code>
- <code title="put /conversations/{id}">client.conversations.<a href="./src/intercom/resources/conversations/conversations.py">update</a>(id, \*\*<a href="src/intercom/types/conversation_update_params.py">params</a>) -> <a href="./src/intercom/types/shared/conversation.py">Conversation</a></code>
- <code title="get /conversations">client.conversations.<a href="./src/intercom/resources/conversations/conversations.py">list</a>(\*\*<a href="src/intercom/types/conversation_list_params.py">params</a>) -> <a href="./src/intercom/types/shared/paginated_response.py">PaginatedResponse</a></code>
- <code title="post /conversations/{id}/convert">client.conversations.<a href="./src/intercom/resources/conversations/conversations.py">convert</a>(id, \*\*<a href="src/intercom/types/conversation_convert_params.py">params</a>) -> <a href="./src/intercom/types/shared/ticket.py">Optional</a></code>
- <code title="post /conversations/redact">client.conversations.<a href="./src/intercom/resources/conversations/conversations.py">redact</a>(\*\*<a href="src/intercom/types/conversation_redact_params.py">params</a>) -> <a href="./src/intercom/types/shared/conversation.py">Conversation</a></code>
- <code title="post /conversations/search">client.conversations.<a href="./src/intercom/resources/conversations/conversations.py">search</a>(\*\*<a href="src/intercom/types/conversation_search_params.py">params</a>) -> <a href="./src/intercom/types/conversation_list.py">ConversationList</a></code>

## Tags

Methods:

- <code title="post /conversations/{conversation_id}/tags">client.conversations.tags.<a href="./src/intercom/resources/conversations/tags.py">create</a>(conversation_id, \*\*<a href="src/intercom/types/conversations/tag_create_params.py">params</a>) -> <a href="./src/intercom/types/shared/tag.py">Tag</a></code>
- <code title="delete /conversations/{conversation_id}/tags/{id}">client.conversations.tags.<a href="./src/intercom/resources/conversations/tags.py">delete</a>(id, \*, conversation_id, \*\*<a href="src/intercom/types/conversations/tag_delete_params.py">params</a>) -> <a href="./src/intercom/types/shared/tag.py">Tag</a></code>

## Reply

Methods:

- <code title="post /conversations/{id}/reply">client.conversations.reply.<a href="./src/intercom/resources/conversations/reply.py">create</a>(id, \*\*<a href="src/intercom/types/conversations/reply_create_params.py">params</a>) -> <a href="./src/intercom/types/shared/conversation.py">Conversation</a></code>

## Parts

Methods:

- <code title="post /conversations/{id}/parts">client.conversations.parts.<a href="./src/intercom/resources/conversations/parts.py">create</a>(id, \*\*<a href="src/intercom/types/conversations/part_create_params.py">params</a>) -> <a href="./src/intercom/types/shared/conversation.py">Conversation</a></code>

## RunAssignmentRules

Methods:

- <code title="post /conversations/{id}/run_assignment_rules">client.conversations.run_assignment_rules.<a href="./src/intercom/resources/conversations/run_assignment_rules.py">create</a>(id) -> <a href="./src/intercom/types/shared/conversation.py">Conversation</a></code>

## Customers

Methods:

- <code title="post /conversations/{id}/customers">client.conversations.customers.<a href="./src/intercom/resources/conversations/customers.py">create</a>(id, \*\*<a href="src/intercom/types/conversations/customer_create_params.py">params</a>) -> <a href="./src/intercom/types/shared/conversation.py">Conversation</a></code>
- <code title="delete /conversations/{conversation_id}/customers/{contact_id}">client.conversations.customers.<a href="./src/intercom/resources/conversations/customers.py">delete</a>(contact_id, \*, conversation_id, \*\*<a href="src/intercom/types/conversations/customer_delete_params.py">params</a>) -> <a href="./src/intercom/types/shared/conversation.py">Conversation</a></code>

# DataAttributes

Types:

```python
from intercom.types import DataAttribute, DataAttributeList
```

Methods:

- <code title="post /data_attributes">client.data_attributes.<a href="./src/intercom/resources/data_attributes.py">create</a>(\*\*<a href="src/intercom/types/data_attribute_create_params.py">params</a>) -> <a href="./src/intercom/types/data_attribute.py">DataAttribute</a></code>
- <code title="put /data_attributes/{id}">client.data_attributes.<a href="./src/intercom/resources/data_attributes.py">update</a>(id, \*\*<a href="src/intercom/types/data_attribute_update_params.py">params</a>) -> <a href="./src/intercom/types/data_attribute.py">DataAttribute</a></code>
- <code title="get /data_attributes">client.data_attributes.<a href="./src/intercom/resources/data_attributes.py">list</a>(\*\*<a href="src/intercom/types/data_attribute_list_params.py">params</a>) -> <a href="./src/intercom/types/data_attribute_list.py">DataAttributeList</a></code>

# DataEvents

Types:

```python
from intercom.types import DataEventSummary
```

Methods:

- <code title="post /events">client.data_events.<a href="./src/intercom/resources/data_events.py">create</a>(\*\*<a href="src/intercom/types/data_event_create_params.py">params</a>) -> None</code>
- <code title="get /events">client.data_events.<a href="./src/intercom/resources/data_events.py">list</a>(\*\*<a href="src/intercom/types/data_event_list_params.py">params</a>) -> <a href="./src/intercom/types/data_event_summary.py">DataEventSummary</a></code>
- <code title="post /events/summaries">client.data_events.<a href="./src/intercom/resources/data_events.py">summaries</a>(\*\*<a href="src/intercom/types/data_event_summaries_params.py">params</a>) -> None</code>

# DataExports

Types:

```python
from intercom.types import DataExport
```

Methods:

- <code title="post /export/content/data">client.data_exports.<a href="./src/intercom/resources/data_exports.py">content_data</a>(\*\*<a href="src/intercom/types/data_export_content_data_params.py">params</a>) -> <a href="./src/intercom/types/data_export.py">DataExport</a></code>

# Export

Methods:

- <code title="post /export/cancel/{job_identifier}">client.export.<a href="./src/intercom/resources/export/export.py">cancel</a>(job_identifier) -> <a href="./src/intercom/types/data_export.py">DataExport</a></code>

## Content

### Data

Methods:

- <code title="get /export/content/data/{job_identifier}">client.export.content.data.<a href="./src/intercom/resources/export/content/data.py">retrieve</a>(job_identifier) -> <a href="./src/intercom/types/data_export.py">DataExport</a></code>

# Download

## Content

### Data

Methods:

- <code title="get /download/content/data/{job_identifier}">client.download.content.data.<a href="./src/intercom/resources/download/content/data.py">retrieve</a>(job_identifier) -> None</code>

# Messages

Methods:

- <code title="post /messages">client.messages.<a href="./src/intercom/resources/messages.py">create</a>(\*\*<a href="src/intercom/types/message_create_params.py">params</a>) -> <a href="./src/intercom/types/shared/message.py">Message</a></code>

# News

## NewsItems

Types:

```python
from intercom.types.news import NewsItem, NewsItemDeleteResponse
```

Methods:

- <code title="post /news/news_items">client.news.news_items.<a href="./src/intercom/resources/news/news_items.py">create</a>(\*\*<a href="src/intercom/types/news/news_item_create_params.py">params</a>) -> <a href="./src/intercom/types/news/news_item.py">NewsItem</a></code>
- <code title="get /news/news_items/{id}">client.news.news_items.<a href="./src/intercom/resources/news/news_items.py">retrieve</a>(id) -> <a href="./src/intercom/types/news/news_item.py">NewsItem</a></code>
- <code title="put /news/news_items/{id}">client.news.news_items.<a href="./src/intercom/resources/news/news_items.py">update</a>(id, \*\*<a href="src/intercom/types/news/news_item_update_params.py">params</a>) -> <a href="./src/intercom/types/news/news_item.py">NewsItem</a></code>
- <code title="get /news/news_items">client.news.news_items.<a href="./src/intercom/resources/news/news_items.py">list</a>() -> <a href="./src/intercom/types/shared/paginated_response.py">PaginatedResponse</a></code>
- <code title="delete /news/news_items/{id}">client.news.news_items.<a href="./src/intercom/resources/news/news_items.py">delete</a>(id) -> <a href="./src/intercom/types/news/news_item_delete_response.py">NewsItemDeleteResponse</a></code>

## Newsfeeds

Types:

```python
from intercom.types.news import Newsfeed
```

Methods:

- <code title="get /news/newsfeeds/{id}">client.news.newsfeeds.<a href="./src/intercom/resources/news/newsfeeds/newsfeeds.py">retrieve</a>(id) -> <a href="./src/intercom/types/news/newsfeed.py">Newsfeed</a></code>
- <code title="get /news/newsfeeds">client.news.newsfeeds.<a href="./src/intercom/resources/news/newsfeeds/newsfeeds.py">list</a>() -> <a href="./src/intercom/types/shared/paginated_response.py">PaginatedResponse</a></code>

### Items

Methods:

- <code title="get /news/newsfeeds/{id}/items">client.news.newsfeeds.items.<a href="./src/intercom/resources/news/newsfeeds/items.py">list</a>(id) -> <a href="./src/intercom/types/shared/paginated_response.py">PaginatedResponse</a></code>

# Notes

Methods:

- <code title="get /notes/{id}">client.notes.<a href="./src/intercom/resources/notes.py">retrieve</a>(id) -> <a href="./src/intercom/types/shared/note.py">Note</a></code>

# Segments

Types:

```python
from intercom.types import Segment, SegmentList
```

Methods:

- <code title="get /segments/{id}">client.segments.<a href="./src/intercom/resources/segments.py">retrieve</a>(id) -> <a href="./src/intercom/types/segment.py">Segment</a></code>
- <code title="get /segments">client.segments.<a href="./src/intercom/resources/segments.py">list</a>(\*\*<a href="src/intercom/types/segment_list_params.py">params</a>) -> <a href="./src/intercom/types/segment_list.py">SegmentList</a></code>

# SubscriptionTypes

Methods:

- <code title="get /subscription_types">client.subscription_types.<a href="./src/intercom/resources/subscription_types.py">list</a>() -> <a href="./src/intercom/types/shared/subscription_type_list.py">SubscriptionTypeList</a></code>

# PhoneCallRedirects

Types:

```python
from intercom.types import PhoneSwitch
```

Methods:

- <code title="post /phone_call_redirects">client.phone_call_redirects.<a href="./src/intercom/resources/phone_call_redirects.py">create</a>(\*\*<a href="src/intercom/types/phone_call_redirect_create_params.py">params</a>) -> <a href="./src/intercom/types/phone_switch.py">Optional</a></code>

# Tags

Methods:

- <code title="get /tags/{id}">client.tags.<a href="./src/intercom/resources/tags.py">retrieve</a>(id) -> <a href="./src/intercom/types/shared/tag.py">Tag</a></code>
- <code title="get /tags">client.tags.<a href="./src/intercom/resources/tags.py">list</a>() -> <a href="./src/intercom/types/shared/tag_list.py">TagList</a></code>
- <code title="delete /tags/{id}">client.tags.<a href="./src/intercom/resources/tags.py">delete</a>(id) -> None</code>
- <code title="post /tags">client.tags.<a href="./src/intercom/resources/tags.py">create_or_update</a>(\*\*<a href="src/intercom/types/tag_create_or_update_params.py">params</a>) -> <a href="./src/intercom/types/shared/tag.py">Tag</a></code>

# Teams

Types:

```python
from intercom.types import Team, TeamList
```

Methods:

- <code title="get /teams/{id}">client.teams.<a href="./src/intercom/resources/teams.py">retrieve</a>(id) -> <a href="./src/intercom/types/team.py">Team</a></code>
- <code title="get /teams">client.teams.<a href="./src/intercom/resources/teams.py">list</a>() -> <a href="./src/intercom/types/team_list.py">TeamList</a></code>

# TicketTypes

Types:

```python
from intercom.types import TicketType, TicketTypeList
```

Methods:

- <code title="post /ticket_types">client.ticket_types.<a href="./src/intercom/resources/ticket_types/ticket_types.py">create</a>(\*\*<a href="src/intercom/types/ticket_type_create_params.py">params</a>) -> <a href="./src/intercom/types/ticket_type.py">Optional</a></code>
- <code title="get /ticket_types/{id}">client.ticket_types.<a href="./src/intercom/resources/ticket_types/ticket_types.py">retrieve</a>(id) -> <a href="./src/intercom/types/ticket_type.py">Optional</a></code>
- <code title="put /ticket_types/{id}">client.ticket_types.<a href="./src/intercom/resources/ticket_types/ticket_types.py">update</a>(id, \*\*<a href="src/intercom/types/ticket_type_update_params.py">params</a>) -> <a href="./src/intercom/types/ticket_type.py">Optional</a></code>
- <code title="get /ticket_types">client.ticket_types.<a href="./src/intercom/resources/ticket_types/ticket_types.py">list</a>() -> <a href="./src/intercom/types/ticket_type_list.py">TicketTypeList</a></code>

## Attributes

Methods:

- <code title="post /ticket_types/{ticket_type_id}/attributes">client.ticket_types.attributes.<a href="./src/intercom/resources/ticket_types/attributes.py">create</a>(ticket_type_id, \*\*<a href="src/intercom/types/ticket_types/attribute_create_params.py">params</a>) -> <a href="./src/intercom/types/shared/ticket_type_attribute.py">Optional</a></code>
- <code title="put /ticket_types/{ticket_type_id}/attributes/{id}">client.ticket_types.attributes.<a href="./src/intercom/resources/ticket_types/attributes.py">update</a>(id, \*, ticket_type_id, \*\*<a href="src/intercom/types/ticket_types/attribute_update_params.py">params</a>) -> <a href="./src/intercom/types/shared/ticket_type_attribute.py">Optional</a></code>

# Tickets

Types:

```python
from intercom.types import TicketList, TicketReply
```

Methods:

- <code title="post /tickets">client.tickets.<a href="./src/intercom/resources/tickets/tickets.py">create</a>(\*\*<a href="src/intercom/types/ticket_create_params.py">params</a>) -> <a href="./src/intercom/types/shared/ticket.py">Optional</a></code>
- <code title="post /tickets/{id}/reply">client.tickets.<a href="./src/intercom/resources/tickets/tickets.py">reply</a>(id, \*\*<a href="src/intercom/types/ticket_reply_params.py">params</a>) -> <a href="./src/intercom/types/ticket_reply.py">TicketReply</a></code>
- <code title="get /tickets/{id}">client.tickets.<a href="./src/intercom/resources/tickets/tickets.py">retrieve_by_id</a>(id) -> <a href="./src/intercom/types/shared/ticket.py">Optional</a></code>
- <code title="post /tickets/search">client.tickets.<a href="./src/intercom/resources/tickets/tickets.py">search</a>(\*\*<a href="src/intercom/types/ticket_search_params.py">params</a>) -> <a href="./src/intercom/types/ticket_list.py">TicketList</a></code>
- <code title="put /tickets/{id}">client.tickets.<a href="./src/intercom/resources/tickets/tickets.py">update_by_id</a>(id, \*\*<a href="src/intercom/types/ticket_update_by_id_params.py">params</a>) -> <a href="./src/intercom/types/shared/ticket.py">Optional</a></code>

## Tags

Methods:

- <code title="post /tickets/{ticket_id}/tags">client.tickets.tags.<a href="./src/intercom/resources/tickets/tags.py">create</a>(ticket_id, \*\*<a href="src/intercom/types/tickets/tag_create_params.py">params</a>) -> <a href="./src/intercom/types/shared/tag.py">Tag</a></code>
- <code title="delete /tickets/{ticket_id}/tags/{id}">client.tickets.tags.<a href="./src/intercom/resources/tickets/tags.py">remove</a>(id, \*, ticket_id, \*\*<a href="src/intercom/types/tickets/tag_remove_params.py">params</a>) -> <a href="./src/intercom/types/shared/tag.py">Tag</a></code>

# Visitors

Types:

```python
from intercom.types import Visitor, VisitorDeletedObject
```

Methods:

- <code title="get /visitors">client.visitors.<a href="./src/intercom/resources/visitors.py">retrieve</a>(\*\*<a href="src/intercom/types/visitor_retrieve_params.py">params</a>) -> <a href="./src/intercom/types/visitor.py">Optional</a></code>
- <code title="put /visitors">client.visitors.<a href="./src/intercom/resources/visitors.py">update</a>(\*\*<a href="src/intercom/types/visitor_update_params.py">params</a>) -> <a href="./src/intercom/types/visitor.py">Optional</a></code>
- <code title="post /visitors/convert">client.visitors.<a href="./src/intercom/resources/visitors.py">convert</a>(\*\*<a href="src/intercom/types/visitor_convert_params.py">params</a>) -> <a href="./src/intercom/types/shared/contact.py">Contact</a></code>

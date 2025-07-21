# Reference
## Admins
<details><summary><code>client.admins.<a href="src/intercom/admins/client.py">identify</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


You can view the currently authorised admin along with the embedded app object (a "workspace" in legacy terminology).

> 🚧 Single Sign On
>
> If you are building a custom "Log in with Intercom" flow for your site, and you call the `/me` endpoint to identify the logged-in user, you should not accept any sign-ins from users with unverified email addresses as it poses a potential impersonation security risk.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.admins.identify()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admins.<a href="src/intercom/admins/client.py">away</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can set an Admin as away for the Inbox.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.admins.away(
    admin_id="admin_id",
    away_mode_enabled=True,
    away_mode_reassign=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**admin_id:** `str` — The unique identifier of a given admin
    
</dd>
</dl>

<dl>
<dd>

**away_mode_enabled:** `bool` — Set to "true" to change the status of the admin to away.
    
</dd>
</dl>

<dl>
<dd>

**away_mode_reassign:** `bool` — Set to "true" to assign any new conversation replies to your default inbox.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admins.<a href="src/intercom/admins/client.py">list_all_activity_logs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can get a log of activities by all admins in an app.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.admins.list_all_activity_logs(
    created_at_after="1677253093",
    created_at_before="1677861493",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**created_at_after:** `str` — The start date that you request data for. It must be formatted as a UNIX timestamp.
    
</dd>
</dl>

<dl>
<dd>

**created_at_before:** `typing.Optional[str]` — The end date that you request data for. It must be formatted as a UNIX timestamp.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admins.<a href="src/intercom/admins/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of admins for a given workspace.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.admins.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.admins.<a href="src/intercom/admins/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can retrieve the details of a single admin.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.admins.find(
    admin_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**admin_id:** `str` — The unique identifier of a given admin
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Articles
<details><summary><code>client.articles.<a href="src/intercom/articles/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all articles by making a GET request to `https://api.intercom.io/articles`.

> 📘 How are the articles sorted and ordered?
>
> Articles will be returned in descending order on the `updated_at` attribute. This means if you need to iterate through results then we'll show the most recently updated articles first.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
response = client.articles.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page of results to fetch. Defaults to first page
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — How many results to display per page. Defaults to 15
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.articles.<a href="src/intercom/articles/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a new article by making a POST request to `https://api.intercom.io/articles`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.articles.create(
    title="Thanks for everything",
    description="Description of the Article",
    body="Body of the Article",
    author_id=1295,
    state="published",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**title:** `str` — The title of the article.For multilingual articles, this will be the title of the default language's content.
    
</dd>
</dl>

<dl>
<dd>

**author_id:** `int` — The id of the author of the article. For multilingual articles, this will be the id of the author of the default language's content. Must be a teammate on the help center's workspace.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the article. For multilingual articles, this will be the description of the default language's content.
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[str]` — The content of the article. For multilingual articles, this will be the body of the default language's content.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[CreateArticleRequestState]` — Whether the article will be `published` or will be a `draft`. Defaults to draft. For multilingual articles, this will be the state of the default language's content.
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[int]` — The id of the article's parent collection or section. An article without this field stands alone.
    
</dd>
</dl>

<dl>
<dd>

**parent_type:** `typing.Optional[CreateArticleRequestParentType]` — The type of parent, which can either be a `collection` or `section`.
    
</dd>
</dl>

<dl>
<dd>

**translated_content:** `typing.Optional[ArticleTranslatedContentParams]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.articles.<a href="src/intercom/articles/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single article by making a GET request to `https://api.intercom.io/articles/<id>`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.articles.find(
    article_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**article_id:** `str` — The unique identifier for the article which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.articles.<a href="src/intercom/articles/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can update the details of a single article by making a PUT request to `https://api.intercom.io/articles/<id>`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.articles.update(
    article_id="123",
    title="Christmas is here!",
    body="<p>New gifts in store for the jolly season</p>",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**article_id:** `str` — The unique identifier for the article which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title of the article.For multilingual articles, this will be the title of the default language's content.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the article. For multilingual articles, this will be the description of the default language's content.
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[str]` — The content of the article. For multilingual articles, this will be the body of the default language's content.
    
</dd>
</dl>

<dl>
<dd>

**author_id:** `typing.Optional[int]` — The id of the author of the article. For multilingual articles, this will be the id of the author of the default language's content. Must be a teammate on the help center's workspace.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[UpdateArticleRequestBodyState]` — Whether the article will be `published` or will be a `draft`. Defaults to draft. For multilingual articles, this will be the state of the default language's content.
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` — The id of the article's parent collection or section. An article without this field stands alone.
    
</dd>
</dl>

<dl>
<dd>

**parent_type:** `typing.Optional[UpdateArticleRequestBodyParentType]` — The type of parent, which can either be a `collection` or `section`.
    
</dd>
</dl>

<dl>
<dd>

**translated_content:** `typing.Optional[ArticleTranslatedContentParams]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.articles.<a href="src/intercom/articles/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can delete a single article by making a DELETE request to `https://api.intercom.io/articles/<id>`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.articles.delete(
    article_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**article_id:** `str` — The unique identifier for the article which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.articles.<a href="src/intercom/articles/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can search for articles by making a GET request to `https://api.intercom.io/articles/search`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.articles.search(
    phrase="Getting started",
    state="published",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**phrase:** `typing.Optional[str]` — The phrase within your articles to search for.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` — The state of the Articles returned. One of `published`, `draft` or `all`.
    
</dd>
</dl>

<dl>
<dd>

**help_center_id:** `typing.Optional[int]` — The ID of the Help Center to search in.
    
</dd>
</dl>

<dl>
<dd>

**highlight:** `typing.Optional[bool]` — Return a highlighted version of the matching content within your articles. Refer to the response schema for more details.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## HelpCenters
<details><summary><code>client.help_centers.<a href="src/intercom/help_centers/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single Help Center by making a GET request to `https://api.intercom.io/help_center/help_center/<id>`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.help_centers.find(
    help_center_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**help_center_id:** `str` — The unique identifier for the Help Center which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.help_centers.<a href="src/intercom/help_centers/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can list all Help Centers by making a GET request to `https://api.intercom.io/help_center/help_centers`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
response = client.help_centers.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page of results to fetch. Defaults to first page
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — How many results to display per page. Defaults to 15
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Companies
<details><summary><code>client.companies.<a href="src/intercom/companies/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a single company by passing in `company_id` or `name`.

  `https://api.intercom.io/companies?name={name}`

  `https://api.intercom.io/companies?company_id={company_id}`

You can fetch all companies and filter by `segment_id` or `tag_id` as a query parameter.

  `https://api.intercom.io/companies?tag_id={tag_id}`

  `https://api.intercom.io/companies?segment_id={segment_id}`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.companies.retrieve(
    name="my company",
    company_id="12345",
    tag_id="678910",
    segment_id="98765",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` — The `name` of the company to filter by.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` — The `company_id` of the company to filter by.
    
</dd>
</dl>

<dl>
<dd>

**tag_id:** `typing.Optional[str]` — The `tag_id` of the company to filter by.
    
</dd>
</dl>

<dl>
<dd>

**segment_id:** `typing.Optional[str]` — The `segment_id` of the company to filter by.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page of results to fetch. Defaults to first page
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — How many results to display per page. Defaults to 15
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/intercom/companies/client.py">create_or_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create or update a company.

Companies will be only visible in Intercom when there is at least one associated user.

Companies are looked up via `company_id` in a `POST` request, if not found via `company_id`, the new company will be created, if found, that company will be updated.

{% admonition type="warning" name="Using `company_id`" %}
  You can set a unique `company_id` value when creating a company. However, it is not possible to update `company_id`. Be sure to set a unique value once upon creation of the company.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.companies.create_or_update()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the Company
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` — The company id you have defined for the company. Can't be updated
    
</dd>
</dl>

<dl>
<dd>

**plan:** `typing.Optional[str]` — The name of the plan you have associated with the company.
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — The number of employees in this company.
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` — The URL for this company's website. Please note that the value specified here is not validated. Accepts any string.
    
</dd>
</dl>

<dl>
<dd>

**industry:** `typing.Optional[str]` — The industry that this company operates in.
    
</dd>
</dl>

<dl>
<dd>

**custom_attributes:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — A hash of key/value pairs containing any other data about the company you want Intercom to store.
    
</dd>
</dl>

<dl>
<dd>

**remote_created_at:** `typing.Optional[int]` — The time the company was created by you.
    
</dd>
</dl>

<dl>
<dd>

**monthly_spend:** `typing.Optional[int]` — How much revenue the company generates for your business. Note that this will truncate floats. i.e. it only allow for whole integers, 155.98 will be truncated to 155. Note that this has an upper limit of 2**31-1 or 2147483647..
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/intercom/companies/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a single company.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.companies.find(
    company_id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` — The unique identifier for the company which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/intercom/companies/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can update a single company using the Intercom provisioned `id`.

{% admonition type="warning" name="Using `company_id`" %}
  When updating a company it is not possible to update `company_id`. This can only be set once upon creation of the company.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.companies.update(
    company_id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` — The unique identifier for the company which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/intercom/companies/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can delete a single company.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.companies.delete(
    company_id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` — The unique identifier for the company which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/intercom/companies/client.py">list_attached_contacts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all contacts that belong to a company.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.companies.list_attached_contacts(
    company_id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` — The unique identifier for the company which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page of results to fetch. Defaults to first page
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — How many results to return per page. Defaults to 15
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/intercom/companies/client.py">list_attached_segments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all segments that belong to a company.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.companies.list_attached_segments(
    company_id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `str` — The unique identifier for the company which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/intercom/companies/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can list companies. The company list is sorted by the `last_request_at` field and by default is ordered descending, most recently requested first.

Note that the API does not include companies who have no associated users in list responses.

When using the Companies endpoint and the pages object to iterate through the returned companies, there is a limit of 10,000 Companies that can be returned. If you need to list or iterate on more than 10,000 Companies, please use the [Scroll API](https://developers.intercom.com/reference#iterating-over-all-companies).
{% admonition type="warning" name="Pagination" %}
  You can use pagination to limit the number of results returned. The default is `20` results per page.
  See the [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#pagination-for-list-apis) for more details on how to use the `starting_after` param.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
response = client.companies.list(
    order="desc",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page of results to fetch. Defaults to first page
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — How many results to return per page. Defaults to 15
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — `asc` or `desc`. Return the companies in ascending or descending order. Defaults to desc
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/intercom/companies/client.py">scroll</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

      The `list all companies` functionality does not work well for huge datasets, and can result in errors and performance problems when paging deeply. The Scroll API provides an efficient mechanism for iterating over all companies in a dataset.

- Each app can only have 1 scroll open at a time. You'll get an error message if you try to have more than one open per app.
- If the scroll isn't used for 1 minute, it expires and calls with that scroll param will fail
- If the end of the scroll is reached, "companies" will be empty and the scroll parameter will expire

{% admonition type="info" name="Scroll Parameter" %}
  You can get the first page of companies by simply sending a GET request to the scroll endpoint.
  For subsequent requests you will need to use the scroll parameter from the response.
{% /admonition %}
{% admonition type="danger" name="Scroll network timeouts" %}
  Since scroll is often used on large datasets network errors such as timeouts can be encountered. When this occurs you will see a HTTP 500 error with the following message:
  "Request failed due to an internal network error. Please restart the scroll operation."
  If this happens, you will need to restart your scroll query: It is not possible to continue from a specific point when using scroll.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
response = client.companies.scroll()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scroll_param:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/intercom/companies/client.py">attach_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can attach a company to a single contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.companies.attach_contact(
    contact_id="contact_id",
    company_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — The unique identifier for the contact which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — The unique identifier for the company which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/intercom/companies/client.py">detach_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can detach a company from a single contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.companies.detach_contact(
    contact_id="58a430d35458202d41b1e65b",
    company_id="58a430d35458202d41b1e65b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — The unique identifier for the contact which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — The unique identifier for the company which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Contacts
<details><summary><code>client.contacts.<a href="src/intercom/contacts/client.py">list_attached_companies</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of companies that are associated to a contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
response = client.contacts.list_attached_companies(
    contact_id="63a07ddf05a32042dffac965",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — The unique identifier for the contact which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page of results to fetch. Defaults to first page
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — How many results to display per page. Defaults to 15
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/intercom/contacts/client.py">list_attached_segments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of segments that are associated to a contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.contacts.list_attached_segments(
    contact_id="63a07ddf05a32042dffac965",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — The unique identifier for the contact which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/intercom/contacts/client.py">list_attached_subscriptions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of subscription types that are attached to a contact. These can be subscriptions that a user has 'opted-in' to or has 'opted-out' from, depending on the subscription type.
This will return a list of Subscription Type objects that the contact is associated with.

The data property will show a combined list of:

  1.Opt-out subscription types that the user has opted-out from.
  2.Opt-in subscription types that the user has opted-in to receiving.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.contacts.list_attached_subscriptions(
    contact_id="63a07ddf05a32042dffac965",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — The unique identifier for the contact which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/intercom/contacts/client.py">attach_subscription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can add a specific subscription to a contact. In Intercom, we have two different subscription types based on user consent - opt-out and opt-in:

  1.Attaching a contact to an opt-out subscription type will opt that user out from receiving messages related to that subscription type.

  2.Attaching a contact to an opt-in subscription type will opt that user in to receiving messages related to that subscription type.

This will return a subscription type model for the subscription type that was added to the contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.contacts.attach_subscription(
    contact_id="63a07ddf05a32042dffac965",
    subscription_id="invalid_id",
    consent_type="opt_in",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — The unique identifier for the contact which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `str` — The unique identifier for the subscription which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**consent_type:** `str` — The consent_type of a subscription, opt_out or opt_in.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/intercom/contacts/client.py">detach_subscription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can remove a specific subscription from a contact. This will return a subscription type model for the subscription type that was removed from the contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.contacts.detach_subscription(
    contact_id="63a07ddf05a32042dffac965",
    subscription_id="37846",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — The unique identifier for the contact which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `str` — The unique identifier for the subscription type which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/intercom/contacts/client.py">list_attached_tags</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all tags that are attached to a specific contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.contacts.list_attached_tags(
    contact_id="63a07ddf05a32042dffac965",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — The unique identifier for the contact which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/intercom/contacts/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.contacts.find(
    contact_id="63a07ddf05a32042dffac965",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/intercom/contacts/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can update an existing contact (ie. user or lead).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.contacts.update(
    contact_id="63a07ddf05a32042dffac965",
    email="joebloggs@intercom.io",
    name="joe bloggs",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — id
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[str]` — The role of the contact.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[str]` — A unique identifier for the contact which is given to Intercom
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — The contacts email
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — The contacts phone
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The contacts name
    
</dd>
</dl>

<dl>
<dd>

**avatar:** `typing.Optional[str]` — An image URL containing the avatar of a contact
    
</dd>
</dl>

<dl>
<dd>

**signed_up_at:** `typing.Optional[int]` — The time specified for when a contact signed up
    
</dd>
</dl>

<dl>
<dd>

**last_seen_at:** `typing.Optional[int]` — The time when the contact was last seen (either where the Intercom Messenger was installed or when specified manually)
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[int]` — The id of an admin that has been assigned account ownership of the contact
    
</dd>
</dl>

<dl>
<dd>

**unsubscribed_from_emails:** `typing.Optional[bool]` — Whether the contact is unsubscribed from emails
    
</dd>
</dl>

<dl>
<dd>

**custom_attributes:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The custom attributes which are set for the contact
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/intercom/contacts/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can delete a single contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.contacts.delete(
    contact_id="contact_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/intercom/contacts/client.py">merge_lead_in_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can merge a contact with a `role` of `lead` into a contact with a `role` of `user`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.contacts.merge_lead_in_user(
    lead_id="667d60ac8a68186f43bafdbb",
    contact_id="667d60ac8a68186f43bafdbc",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**lead_id:** `str` — The unique identifier for the contact to merge away from. Must be a lead.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `str` — The unique identifier for the contact to merge into. Must be a user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/intercom/contacts/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can search for multiple contacts by the value of their attributes in order to fetch exactly who you want.

To search for contacts, you need to send a `POST` request to `https://api.intercom.io/contacts/search`.

This will accept a query object in the body which will define your filters in order to search for contacts.

{% admonition type="warning" name="Optimizing search queries" %}
  Search queries can be complex, so optimizing them can help the performance of your search.
  Use the `AND` and `OR` operators to combine multiple filters to get the exact results you need and utilize
  pagination to limit the number of results returned. The default is `50` results per page.
  See the [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#example-search-conversations-request) for more details on how to use the `starting_after` param.
{% /admonition %}
### Contact Creation Delay

If a contact has recently been created, there is a possibility that it will not yet be available when searching. This means that it may not appear in the response. This delay can take a few minutes. If you need to be instantly notified it is recommended to use webhooks and iterate to see if they match your search filters.

### Nesting & Limitations

You can nest these filters in order to get even more granular insights that pinpoint exactly what you need. Example: (1 OR 2) AND (3 OR 4).
There are some limitations to the amount of multiple's there can be:
* There's a limit of max 2 nested filters
* There's a limit of max 15 filters for each AND or OR group

### Searching for Timestamp Fields

All timestamp fields (created_at, updated_at etc.) are indexed as Dates for Contact Search queries; Datetime queries are not currently supported. This means you can only query for timestamp fields by day - not hour, minute or second.
For example, if you search for all Contacts with a created_at value greater (>) than 1577869200 (the UNIX timestamp for January 1st, 2020 9:00 AM), that will be interpreted as 1577836800 (January 1st, 2020 12:00 AM). The search results will then include Contacts created from January 2nd, 2020 12:00 AM onwards.
If you'd like to get contacts created on January 1st, 2020 you should search with a created_at value equal (=) to 1577836800 (January 1st, 2020 12:00 AM).
This behaviour applies only to timestamps used in search queries. The search results will still contain the full UNIX timestamp and be sorted accordingly.

### Accepted Fields

Most key listed as part of the Contacts Model are searchable, whether writeable or not. The value you search for has to match the accepted type, otherwise the query will fail (ie. as `created_at` accepts a date, the `value` cannot be a string such as `"foorbar"`).

| Field                              | Type                           |
| ---------------------------------- | ------------------------------ |
| id                                 | String                         |
| role                               | String<br>Accepts user or lead |
| name                               | String                         |
| avatar                             | String                         |
| owner_id                           | Integer                        |
| email                              | String                         |
| email_domain                       | String                         |
| phone                              | String                         |
| external_id                        | String                         |
| created_at                         | Date (UNIX Timestamp)          |
| signed_up_at                       | Date (UNIX Timestamp)          |
| updated_at                         | Date (UNIX Timestamp)          |
| last_seen_at                       | Date (UNIX Timestamp)          |
| last_contacted_at                  | Date (UNIX Timestamp)          |
| last_replied_at                    | Date (UNIX Timestamp)          |
| last_email_opened_at               | Date (UNIX Timestamp)          |
| last_email_clicked_at              | Date (UNIX Timestamp)          |
| language_override                  | String                         |
| browser                            | String                         |
| browser_language                   | String                         |
| os                                 | String                         |
| location.country                   | String                         |
| location.region                    | String                         |
| location.city                      | String                         |
| unsubscribed_from_emails           | Boolean                        |
| marked_email_as_spam               | Boolean                        |
| has_hard_bounced                   | Boolean                        |
| ios_last_seen_at                   | Date (UNIX Timestamp)          |
| ios_app_version                    | String                         |
| ios_device                         | String                         |
| ios_app_device                     | String                         |
| ios_os_version                     | String                         |
| ios_app_name                       | String                         |
| ios_sdk_version                    | String                         |
| android_last_seen_at               | Date (UNIX Timestamp)          |
| android_app_version                | String                         |
| android_device                     | String                         |
| android_app_name                   | String                         |
| andoid_sdk_version                 | String                         |
| segment_id                         | String                         |
| tag_id                             | String                         |
| custom_attributes.{attribute_name} | String                         |

### Accepted Operators

{% admonition type="warning" name="Searching based on `created_at`" %}
  You cannot use the `<=` or `>=` operators to search by `created_at`.
{% /admonition %}

The table below shows the operators you can use to define how you want to search for the value.  The operator should be put in as a string (`"="`). The operator has to be compatible with the field's type (eg. you cannot search with `>` for a given string value as it's only compatible for integer's and dates).

| Operator | Valid Types                      | Description                                                      |
| :------- | :------------------------------- | :--------------------------------------------------------------- |
| =        | All                              | Equals                                                           |
| !=       | All                              | Doesn't Equal                                                    |
| IN       | All                              | In<br>Shortcut for `OR` queries<br>Values must be in Array       |
| NIN      | All                              | Not In<br>Shortcut for `OR !` queries<br>Values must be in Array |
| >        | Integer<br>Date (UNIX Timestamp) | Greater than                                                     |
| <       | Integer<br>Date (UNIX Timestamp) | Lower than                                                       |
| ~        | String                           | Contains                                                         |
| !~       | String                           | Doesn't Contain                                                  |
| ^        | String                           | Starts With                                                      |
| $        | String                           | Ends With                                                        |
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
response = client.contacts.search(
    query={
        "operator": "AND",
        "value": [
            {"field": "created_at", "operator": ">", "value": "1306054154"}
        ],
    },
    pagination={"per_page": 5},
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `SearchRequestQueryParams` 
    
</dd>
</dl>

<dl>
<dd>

**pagination:** `typing.Optional[StartingAfterPagingParams]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/intercom/contacts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all contacts (ie. users or leads) in your workspace.
{% admonition type="warning" name="Pagination" %}
  You can use pagination to limit the number of results returned. The default is `50` results per page.
  See the [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#pagination-for-list-apis) for more details on how to use the `starting_after` param.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
response = client.contacts.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page of results to fetch. Defaults to first page
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — How many results to display per page. Defaults to 15
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — String used to get the next page of conversations.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/intercom/contacts/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a new contact (ie. user or lead).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.contacts.create(
    request={"email": "joebloggs@intercom.io"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateContactRequestParams` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/intercom/contacts/client.py">archive</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can archive a single contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.contacts.archive(
    contact_id="63a07ddf05a32042dffac965",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contacts.<a href="src/intercom/contacts/client.py">unarchive</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can unarchive a single contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.contacts.unarchive(
    contact_id="63a07ddf05a32042dffac965",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Notes
<details><summary><code>client.notes.<a href="src/intercom/notes/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of notes that are associated to a contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
response = client.notes.list(
    contact_id="contact_id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — The unique identifier of a contact.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page of results to fetch. Defaults to first page
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — How many results to display per page. Defaults to 15
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notes.<a href="src/intercom/notes/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can add a note to a single contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.notes.create(
    contact_id="123",
    body="Hello",
    admin_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — The unique identifier of a given contact.
    
</dd>
</dl>

<dl>
<dd>

**body:** `str` — The text of the note.
    
</dd>
</dl>

<dl>
<dd>

**admin_id:** `typing.Optional[str]` — The unique identifier of a given admin.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notes.<a href="src/intercom/notes/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single note.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.notes.find(
    note_id="1",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**note_id:** `str` — The unique identifier of a given note
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tags
<details><summary><code>client.tags.<a href="src/intercom/tags/client.py">tag_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can tag a specific contact. This will return a tag object for the tag that was added to the contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.tags.tag_contact(
    contact_id="63a07ddf05a32042dffac965",
    tag_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — The unique identifier for the contact which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**tag_id:** `str` — The unique identifier for the tag which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/intercom/tags/client.py">untag_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can remove tag from a specific contact. This will return a tag object for the tag that was removed from the contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.tags.untag_contact(
    contact_id="63a07ddf05a32042dffac965",
    tag_id="7522907",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — The unique identifier for the contact which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**tag_id:** `str` — The unique identifier for the tag which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/intercom/tags/client.py">tag_conversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can tag a specific conversation. This will return a tag object for the tag that was added to the conversation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.tags.tag_conversation(
    conversation_id="64619700005694",
    tag_id="7522907",
    admin_id="780",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — conversation_id
    
</dd>
</dl>

<dl>
<dd>

**tag_id:** `str` — The unique identifier for the tag which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**admin_id:** `str` — The unique identifier for the admin which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/intercom/tags/client.py">untag_conversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can remove tag from a specific conversation. This will return a tag object for the tag that was removed from the conversation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.tags.untag_conversation(
    conversation_id="64619700005694",
    tag_id="7522907",
    admin_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — conversation_id
    
</dd>
</dl>

<dl>
<dd>

**tag_id:** `str` — id
    
</dd>
</dl>

<dl>
<dd>

**admin_id:** `str` — The unique identifier for the admin which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/intercom/tags/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all tags for a given workspace.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.tags.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/intercom/tags/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can use this endpoint to perform the following operations:

  **1. Create a new tag:** You can create a new tag by passing in the tag name as specified in "Create or Update Tag Request Payload" described below.

  **2. Update an existing tag:** You can update an existing tag by passing the id of the tag as specified in "Create or Update Tag Request Payload" described below.

  **3. Tag Companies:** You can tag single company or a list of companies. You can tag a company by passing in the tag name and the company details as specified in "Tag Company Request Payload" described below. Also, if the tag doesn't exist then a new one will be created automatically.

  **4. Untag Companies:** You can untag a single company or a list of companies. You can untag a company by passing in the tag id and the company details as specified in "Untag Company Request Payload" described below.

  **5. Tag Multiple Users:** You can tag a list of users. You can tag the users by passing in the tag name and the user details as specified in "Tag Users Request Payload" described below.

Each operation will return a tag object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.tags.create(
    request={"name": "test", "users": [{"id": "123"}]},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `TagsCreateRequestBodyParams` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/intercom/tags/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of tags that are on the workspace by their id.
This will return a tag object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.tags.find(
    tag_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tag_id:** `str` — The unique identifier of a given tag
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/intercom/tags/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can delete the details of tags that are on the workspace by passing in the id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.tags.delete(
    tag_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tag_id:** `str` — The unique identifier of a given tag
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/intercom/tags/client.py">tag_ticket</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can tag a specific ticket. This will return a tag object for the tag that was added to the ticket.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.tags.tag_ticket(
    ticket_id="64619700005694",
    tag_id="7522907",
    admin_id="780",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ticket_id:** `str` — ticket_id
    
</dd>
</dl>

<dl>
<dd>

**tag_id:** `str` — The unique identifier for the tag which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**admin_id:** `str` — The unique identifier for the admin which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/intercom/tags/client.py">untag_ticket</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can remove tag from a specific ticket. This will return a tag object for the tag that was removed from the ticket.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.tags.untag_ticket(
    ticket_id="64619700005694",
    tag_id="7522907",
    admin_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ticket_id:** `str` — ticket_id
    
</dd>
</dl>

<dl>
<dd>

**tag_id:** `str` — The unique identifier for the tag which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**admin_id:** `str` — The unique identifier for the admin which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Conversations
<details><summary><code>client.conversations.<a href="src/intercom/conversations/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all conversations.

You can optionally request the result page size and the cursor to start after to fetch the result.
{% admonition type="warning" name="Pagination" %}
  You can use pagination to limit the number of results returned. The default is `20` results per page.
  See the [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#pagination-for-list-apis) for more details on how to use the `starting_after` param.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
response = client.conversations.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — How many results per page
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — String used to get the next page of conversations.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/intercom/conversations/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a conversation that has been initiated by a contact (ie. user or lead).
The conversation can be an in-app message only.

{% admonition type="info" name="Sending for visitors" %}
You can also send a message from a visitor by specifying their `user_id` or `id` value in the `from` field, along with a `type` field value of `contact`.
This visitor will be automatically converted to a contact with a lead role once the conversation is created.
{% /admonition %}

This will return the Message model that has been created.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.conversations.create(
    from_={"type": "user", "id": "123_doesnt_exist"},
    body="Hello there",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_:** `CreateConversationRequestFromParams` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `str` — The content of the message. HTML is not supported.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[int]` — The time the conversation was created as a UTC Unix timestamp. If not provided, the current time will be used. This field is only recommneded for migrating past conversations from another source into Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/intercom/conversations/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


You can fetch the details of a single conversation.

This will return a single Conversation model with all its conversation parts.

{% admonition type="warning" name="Hard limit of 500 parts" %}
The maximum number of conversation parts that can be returned via the API is 500. If you have more than that we will return the 500 most recent conversation parts.
{% /admonition %}

For AI agent conversation metadata, please note that you need to have the agent enabled in your workspace, which is a [paid feature](https://www.intercom.com/help/en/articles/8205718-fin-resolutions#h_97f8c2e671).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.conversations.find(
    conversation_id="123",
    display_as="plaintext",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The id of the conversation to target
    
</dd>
</dl>

<dl>
<dd>

**display_as:** `typing.Optional[str]` — Set to plaintext to retrieve conversation messages in plain text.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/intercom/conversations/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


You can update an existing conversation.

{% admonition type="info" name="Replying and other actions" %}
If you want to reply to a coveration or take an action such as assign, unassign, open, close or snooze, take a look at the reply and manage endpoints.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.conversations.update(
    conversation_id="123",
    display_as="plaintext",
    read=True,
    custom_attributes={"issue_type": "Billing", "priority": "High"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The id of the conversation to target
    
</dd>
</dl>

<dl>
<dd>

**display_as:** `typing.Optional[str]` — Set to plaintext to retrieve conversation messages in plain text.
    
</dd>
</dl>

<dl>
<dd>

**read:** `typing.Optional[bool]` — Mark a conversation as read within Intercom.
    
</dd>
</dl>

<dl>
<dd>

**custom_attributes:** `typing.Optional[CustomAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/intercom/conversations/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can search for multiple conversations by the value of their attributes in order to fetch exactly which ones you want.

To search for conversations, you need to send a `POST` request to `https://api.intercom.io/conversations/search`.

This will accept a query object in the body which will define your filters in order to search for conversations.
{% admonition type="warning" name="Optimizing search queries" %}
  Search queries can be complex, so optimizing them can help the performance of your search.
  Use the `AND` and `OR` operators to combine multiple filters to get the exact results you need and utilize
  pagination to limit the number of results returned. The default is `20` results per page and maximum is `150`.
  See the [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#example-search-conversations-request) for more details on how to use the `starting_after` param.
{% /admonition %}

### Nesting & Limitations

You can nest these filters in order to get even more granular insights that pinpoint exactly what you need. Example: (1 OR 2) AND (3 OR 4).
There are some limitations to the amount of multiple's there can be:
- There's a limit of max 2 nested filters
- There's a limit of max 15 filters for each AND or OR group

### Accepted Fields

Most keys listed as part of the The conversation model is searchable, whether writeable or not. The value you search for has to match the accepted type, otherwise the query will fail (ie. as `created_at` accepts a date, the `value` cannot be a string such as `"foorbar"`).
The `source.body` field is unique as the search will not be performed against the entire value, but instead against every element of the value separately. For example, when searching for a conversation with a `"I need support"` body - the query should contain a `=` operator with the value `"support"` for such conversation to be returned. A query with a `=` operator and a `"need support"` value will not yield a result.

| Field                                     | Type                                                                                                                                                   |
| :---------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                                        | String                                                                                                                                                 |
| created_at                                | Date (UNIX timestamp)                                                                                                                                  |
| updated_at                                | Date (UNIX timestamp)                                                                                                                                  |
| source.type                               | String<br>Accepted fields are `conversation`, `email`, `facebook`, `instagram`, `phone_call`, `phone_switch`, `push`, `sms`, `twitter` and `whatsapp`. |
| source.id                                 | String                                                                                                                                                 |
| source.delivered_as                       | String                                                                                                                                                 |
| source.subject                            | String                                                                                                                                                 |
| source.body                               | String                                                                                                                                                 |
| source.author.id                          | String                                                                                                                                                 |
| source.author.type                        | String                                                                                                                                                 |
| source.author.name                        | String                                                                                                                                                 |
| source.author.email                       | String                                                                                                                                                 |
| source.url                                | String                                                                                                                                                 |
| contact_ids                               | String                                                                                                                                                 |
| teammate_ids                              | String                                                                                                                                                 |
| admin_assignee_id                         | String                                                                                                                                                 |
| team_assignee_id                          | String                                                                                                                                                 |
| channel_initiated                         | String                                                                                                                                                 |
| open                                      | Boolean                                                                                                                                                |
| read                                      | Boolean                                                                                                                                                |
| state                                     | String                                                                                                                                                 |
| waiting_since                             | Date (UNIX timestamp)                                                                                                                                  |
| snoozed_until                             | Date (UNIX timestamp)                                                                                                                                  |
| tag_ids                                   | String                                                                                                                                                 |
| priority                                  | String                                                                                                                                                 |
| statistics.time_to_assignment             | Integer                                                                                                                                                |
| statistics.time_to_admin_reply            | Integer                                                                                                                                                |
| statistics.time_to_first_close            | Integer                                                                                                                                                |
| statistics.time_to_last_close             | Integer                                                                                                                                                |
| statistics.median_time_to_reply           | Integer                                                                                                                                                |
| statistics.first_contact_reply_at         | Date (UNIX timestamp)                                                                                                                                  |
| statistics.first_assignment_at            | Date (UNIX timestamp)                                                                                                                                  |
| statistics.first_admin_reply_at           | Date (UNIX timestamp)                                                                                                                                  |
| statistics.first_close_at                 | Date (UNIX timestamp)                                                                                                                                  |
| statistics.last_assignment_at             | Date (UNIX timestamp)                                                                                                                                  |
| statistics.last_assignment_admin_reply_at | Date (UNIX timestamp)                                                                                                                                  |
| statistics.last_contact_reply_at          | Date (UNIX timestamp)                                                                                                                                  |
| statistics.last_admin_reply_at            | Date (UNIX timestamp)                                                                                                                                  |
| statistics.last_close_at                  | Date (UNIX timestamp)                                                                                                                                  |
| statistics.last_closed_by_id              | String                                                                                                                                                 |
| statistics.count_reopens                  | Integer                                                                                                                                                |
| statistics.count_assignments              | Integer                                                                                                                                                |
| statistics.count_conversation_parts       | Integer                                                                                                                                                |
| conversation_rating.requested_at          | Date (UNIX timestamp)                                                                                                                                  |
| conversation_rating.replied_at            | Date (UNIX timestamp)                                                                                                                                  |
| conversation_rating.score                 | Integer                                                                                                                                                |
| conversation_rating.remark                | String                                                                                                                                                 |
| conversation_rating.contact_id            | String                                                                                                                                                 |
| conversation_rating.admin_d               | String                                                                                                                                                 |
| ai_agent_participated                     | Boolean                                                                                                                                                |
| ai_agent.resolution_state                 | String                                                                                                                                                 |
| ai_agent.last_answer_type                 | String                                                                                                                                                 |
| ai_agent.rating                           | Integer                                                                                                                                                |
| ai_agent.rating_remark                    | String                                                                                                                                                 |
| ai_agent.source_type                      | String                                                                                                                                                 |
| ai_agent.source_title                     | String                                                                                                                                                 |

### Accepted Operators

The table below shows the operators you can use to define how you want to search for the value.  The operator should be put in as a string (`"="`). The operator has to be compatible with the field's type  (eg. you cannot search with `>` for a given string value as it's only compatible for integer's and dates).

| Operator | Valid Types                    | Description                                                  |
| :------- | :----------------------------- | :----------------------------------------------------------- |
| =        | All                            | Equals                                                       |
| !=       | All                            | Doesn't Equal                                                |
| IN       | All                            | In  Shortcut for `OR` queries  Values most be in Array       |
| NIN      | All                            | Not In  Shortcut for `OR !` queries  Values must be in Array |
| >        | Integer  Date (UNIX Timestamp) | Greater (or equal) than                                      |
| <       | Integer  Date (UNIX Timestamp) | Lower (or equal) than                                        |
| ~        | String                         | Contains                                                     |
| !~       | String                         | Doesn't Contain                                              |
| ^        | String                         | Starts With                                                  |
| $        | String                         | Ends With                                                    |
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
response = client.conversations.search(
    query={
        "operator": "AND",
        "value": [
            {"field": "created_at", "operator": ">", "value": "1306054154"}
        ],
    },
    pagination={"per_page": 5},
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `SearchRequestQueryParams` 
    
</dd>
</dl>

<dl>
<dd>

**pagination:** `typing.Optional[StartingAfterPagingParams]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/intercom/conversations/client.py">reply</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can reply to a conversation with a message from an admin or on behalf of a contact, or with a note for admins.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.conversations.reply(
    conversation_id='123 or "last"',
    request={
        "message_type": "comment",
        "type": "user",
        "body": "Thanks again :)",
        "intercom_user_id": "667d60f18a68186f43bafdf4",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The Intercom provisioned identifier for the conversation or the string "last" to reply to the last part of the conversation
    
</dd>
</dl>

<dl>
<dd>

**request:** `ReplyConversationRequestParams` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/intercom/conversations/client.py">manage</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

For managing conversations you can:
- Close a conversation
- Snooze a conversation to reopen on a future date
- Open a conversation which is `snoozed` or `closed`
- Assign a conversation to an admin and/or team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.conversations.manage(
    conversation_id="123",
    request={"type": "admin", "admin_id": "12345", "message_type": "close"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The identifier for the conversation as given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ConversationsManageRequestBodyParams` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/intercom/conversations/client.py">run_assignment_rules</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

{% admonition type="danger" name="Deprecation of Run Assignment Rules" %}
Run assignment rules is now deprecated in version 2.12 and future versions and will be permanently removed on December 31, 2026. After this date, any requests made to this endpoint will fail.
{% /admonition %}
You can let a conversation be automatically assigned following assignment rules.
{% admonition type="warning" name="When using workflows" %}
It is not possible to use this endpoint with Workflows.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.conversations.run_assignment_rules(
    conversation_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The identifier for the conversation as given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/intercom/conversations/client.py">attach_contact_as_admin</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can add participants who are contacts to a conversation, on behalf of either another contact or an admin.

{% admonition type="warning" name="Contacts without an email" %}
If you add a contact via the email parameter and there is no user/lead found on that workspace with he given email, then we will create a new contact with `role` set to `lead`.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.conversations.attach_contact_as_admin(
    conversation_id="123",
    admin_id="12345",
    customer={"intercom_user_id": "667d61188a68186f43bafe0e"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The identifier for the conversation as given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**admin_id:** `typing.Optional[str]` — The `id` of the admin who is adding the new participant.
    
</dd>
</dl>

<dl>
<dd>

**customer:** `typing.Optional[AttachContactToConversationRequestCustomerParams]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/intercom/conversations/client.py">detach_contact_as_admin</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can add participants who are contacts to a conversation, on behalf of either another contact or an admin.

{% admonition type="warning" name="Contacts without an email" %}
If you add a contact via the email parameter and there is no user/lead found on that workspace with he given email, then we will create a new contact with `role` set to `lead`.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.conversations.detach_contact_as_admin(
    conversation_id="123",
    contact_id="123",
    admin_id="5017690",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The identifier for the conversation as given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `str` — The identifier for the contact as given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**admin_id:** `str` — The `id` of the admin who is performing the action.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/intercom/conversations/client.py">redact_conversation_part</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can redact a conversation part or the source message of a conversation (as seen in the source object).

{% admonition type="info" name="Redacting parts and messages" %}
If you are redacting a conversation part, it must have a `body`. If you are redacting a source message, it must have been created by a contact. We will return a `conversation_part_not_redactable` error if these criteria are not met.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.conversations.redact_conversation_part(
    request={
        "conversation_id": "really_123_doesnt_exist",
        "conversation_part_id": "really_123_doesnt_exist",
        "type": "conversation_part",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `RedactConversationRequestParams` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/intercom/conversations/client.py">convert_to_ticket</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can convert a conversation to a ticket.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.conversations.convert_to_ticket(
    conversation_id="123",
    ticket_type_id="80",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The id of the conversation to target
    
</dd>
</dl>

<dl>
<dd>

**ticket_type_id:** `str` — The ID of the type of ticket you want to convert the conversation to
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[TicketRequestCustomAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Data Attributes
<details><summary><code>client.data_attributes.<a href="src/intercom/data_attributes/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all data attributes belonging to a workspace for contacts, companies or conversations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.data_attributes.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model:** `typing.Optional[DataAttributesListRequestModel]` — Specify the data attribute model to return.
    
</dd>
</dl>

<dl>
<dd>

**include_archived:** `typing.Optional[bool]` — Include archived attributes in the list. By default we return only non archived data attributes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_attributes.<a href="src/intercom/data_attributes/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a data attributes for a `contact` or a `company`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.data_attributes.create(
    name="My Data Attribute",
    model="contact",
    data_type="string",
    description="Just a plain old ring",
    options=["options"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the data attribute.
    
</dd>
</dl>

<dl>
<dd>

**model:** `CreateDataAttributeRequestModel` — The model that the data attribute belongs to.
    
</dd>
</dl>

<dl>
<dd>

**data_type:** `CreateDataAttributeRequestDataType` — The type of data stored for this attribute.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The readable description you see in the UI for the attribute.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[typing.Sequence[str]]` — To create list attributes. Provide a set of hashes with `value` as the key of the options you want to make. `data_type` must be `string`.
    
</dd>
</dl>

<dl>
<dd>

**messenger_writable:** `typing.Optional[bool]` — Can this attribute be updated by the Messenger
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_attributes.<a href="src/intercom/data_attributes/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


You can update a data attribute.

> 🚧 Updating the data type is not possible
>
> It is currently a dangerous action to execute changing a data attribute's type via the API. You will need to update the type via the UI instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.data_attributes.update(
    data_attribute_id="1",
    archived=True,
    description="Trying to archieve",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data_attribute_id:** `str` — The data attribute id
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` — Whether the attribute is to be archived or not.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The readable description you see in the UI for the attribute.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[typing.Sequence[UpdateDataAttributeRequestOptionsItemParams]]` — To create list attributes. Provide a set of hashes with `value` as the key of the options you want to make. `data_type` must be `string`.
    
</dd>
</dl>

<dl>
<dd>

**messenger_writable:** `typing.Optional[bool]` — Can this attribute be updated by the Messenger
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Events
<details><summary><code>client.events.<a href="src/intercom/events/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


> 🚧
>
> Please note that you can only 'list' events that are less than 90 days old. Event counts and summaries will still include your events older than 90 days but you cannot 'list' these events individually if they are older than 90 days

The events belonging to a customer can be listed by sending a GET request to `https://api.intercom.io/events` with a user or lead identifier along with a `type` parameter. The identifier parameter can be one of `user_id`, `email` or `intercom_user_id`. The `type` parameter value must be `user`.

- `https://api.intercom.io/events?type=user&user_id={user_id}`
- `https://api.intercom.io/events?type=user&email={email}`
- `https://api.intercom.io/events?type=user&intercom_user_id={id}` (this call can be used to list leads)

The `email` parameter value should be [url encoded](http://en.wikipedia.org/wiki/Percent-encoding) when sending.

You can optionally define the result page size as well with the `per_page` parameter.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.events.list(
    type="type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `str` — The value must be user
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — user_id query parameter
    
</dd>
</dl>

<dl>
<dd>

**intercom_user_id:** `typing.Optional[str]` — intercom_user_id query parameter
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — email query parameter
    
</dd>
</dl>

<dl>
<dd>

**summary:** `typing.Optional[bool]` — summary flag
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — How many results to display per page. Defaults to 15
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/intercom/events/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


You will need an Access Token that has write permissions to send Events. Once you have a key you can submit events via POST to the Events resource, which is located at https://api.intercom.io/events, or you can send events using one of the client libraries. When working with the HTTP API directly a client should send the event with a `Content-Type` of `application/json`.

When using the JavaScript API, [adding the code to your app](http://docs.intercom.io/configuring-Intercom/tracking-user-events-in-your-app) makes the Events API available. Once added, you can submit an event using the `trackEvent` method. This will associate the event with the Lead or currently logged-in user or logged-out visitor/lead and send it to Intercom. The final parameter is a map that can be used to send optional metadata about the event.

With the Ruby client you pass a hash describing the event to `Intercom::Event.create`, or call the `track_user` method directly on the current user object (e.g. `user.track_event`).

**NB: For the JSON object types, please note that we do not currently support nested JSON structure.**

| Type            | Description                                                                                                                                                                                                     | Example                                                                           |
| :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| String          | The value is a JSON String                                                                                                                                                                                      | `"source":"desktop"`                                                              |
| Number          | The value is a JSON Number                                                                                                                                                                                      | `"load": 3.67`                                                                    |
| Date            | The key ends with the String `_date` and the value is a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time), assumed to be in the [UTC](http://en.wikipedia.org/wiki/Coordinated_Universal_Time) timezone. | `"contact_date": 1392036272`                                                      |
| Link            | The value is a HTTP or HTTPS URI.                                                                                                                                                                               | `"article": "https://example.org/ab1de.html"`                                     |
| Rich Link       | The value is a JSON object that contains `url` and `value` keys.                                                                                                                                                | `"article": {"url": "https://example.org/ab1de.html", "value":"the dude abides"}` |
| Monetary Amount | The value is a JSON object that contains `amount` and `currency` keys. The `amount` key is a positive integer representing the amount in cents. The price in the example to the right denotes €349.99.          | `"price": {"amount": 34999, "currency": "eur"}`                                   |

**Lead Events**

When submitting events for Leads, you will need to specify the Lead's `id`.

**Metadata behaviour**

- We currently limit the number of tracked metadata keys to 10 per event. Once the quota is reached, we ignore any further keys we receive. The first 10 metadata keys are determined by the order in which they are sent in with the event.
- It is not possible to change the metadata keys once the event has been sent. A new event will need to be created with the new keys and you can archive the old one.
- There might be up to 24 hrs delay when you send a new metadata for an existing event.

**Event de-duplication**

The API may detect and ignore duplicate events. Each event is uniquely identified as a combination of the following data - the Workspace identifier, the Contact external identifier, the Data Event name and the Data Event created time. As a result, it is **strongly recommended** to send a second granularity Unix timestamp in the `created_at` field.

Duplicated events are responded to using the normal `202 Accepted` code - an error is not thrown, however repeat requests will be counted against any rate limit that is in place.

### HTTP API Responses

- Successful responses to submitted events return `202 Accepted` with an empty body.
- Unauthorised access will be rejected with a `401 Unauthorized` or `403 Forbidden` response code.
- Events sent about users that cannot be found will return a `404 Not Found`.
- Event lists containing duplicate events will have those duplicates ignored.
- Server errors will return a `500` response code and may contain an error message in the body.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.events.create(
    request={
        "id": "8a88a590-e1c3-41e2-a502-e0649dbf721c",
        "event_name": "invited-friend",
        "created_at": 1671028894,
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateDataEventRequestParams` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/intercom/events/client.py">summaries</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create event summaries for a user. Event summaries are used to track the number of times an event has occurred, the first time it occurred and the last time it occurred.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.events.summaries()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Your identifier for the user.
    
</dd>
</dl>

<dl>
<dd>

**event_summaries:** `typing.Optional[CreateDataEventSummariesRequestEventSummariesParams]` — A list of event summaries for the user. Each event summary should contain the event name, the time the event occurred, and the number of times the event occurred. The event name should be a past tense 'verb-noun' combination, to improve readability, for example `updated-plan`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Data Export
<details><summary><code>client.data_export.<a href="src/intercom/data_export/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

To create your export job, you need to send a `POST` request to the export endpoint `https://api.intercom.io/export/content/data`.

The only parameters you need to provide are the range of dates that you want exported.

>🚧 Limit of one active job
>
> You can only have one active job per workspace. You will receive a HTTP status code of 429 with the message Exceeded rate limit of 1 pending message data export jobs if you attempt to create a second concurrent job.

>❗️ Updated_at not included
>
> It should be noted that the timeframe only includes messages sent during the time period and not messages that were only updated during this period. For example, if a message was updated yesterday but sent two days ago, you would need to set the created_at_after date before the message was sent to include that in your retrieval job.

>📘 Date ranges are inclusive
>
> Requesting data for 2018-06-01 until 2018-06-30 will get all data for those days including those specified - e.g. 2018-06-01 00:00:00 until 2018-06-30 23:59:99.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.data_export.create(
    created_at_after=1719474967,
    created_at_before=1719492967,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**created_at_after:** `int` — The start date that you request data for. It must be formatted as a unix timestamp.
    
</dd>
</dl>

<dl>
<dd>

**created_at_before:** `int` — The end date that you request data for. It must be formatted as a unix timestamp.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_export.<a href="src/intercom/data_export/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can view the status of your job by sending a `GET` request to the URL
`https://api.intercom.io/export/content/data/{job_identifier}` - the `{job_identifier}` is the value returned in the response when you first created the export job. More on it can be seen in the Export Job Model.

> 🚧 Jobs expire after two days
> All jobs that have completed processing (and are thus available to download from the provided URL) will have an expiry limit of two days from when the export ob completed. After this, the data will no longer be available.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.data_export.find(
    job_identifier="job_identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_identifier:** `str` — job_identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_export.<a href="src/intercom/data_export/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can cancel your job
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.data_export.cancel(
    job_identifier="job_identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_identifier:** `str` — job_identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_export.<a href="src/intercom/data_export/client.py">download</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

When a job has a status of complete, and thus a filled download_url, you can download your data by hitting that provided URL, formatted like so: https://api.intercom.io/download/content/data/xyz1234.

Your exported message data will be streamed continuously back down to you in a gzipped CSV format.

> 📘 Octet header required
>
> You will have to specify the header Accept: `application/octet-stream` when hitting this endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.data_export.download(
    job_identifier="job_identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_identifier:** `str` — job_identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Messages
<details><summary><code>client.messages.<a href="src/intercom/messages/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a message that has been initiated by an admin. The conversation can be either an in-app message or an email.

> 🚧 Sending for visitors
>
> There can be a short delay between when a contact is created and when a contact becomes available to be messaged through the API. A 404 Not Found error will be returned in this case.

This will return the Message model that has been created.

> 🚧 Retrieving Associated Conversations
>
> As this is a message, there will be no conversation present until the contact responds. Once they do, you will have to search for a contact's conversations with the id of the message.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.messages.create(
    request={
        "subject": "Thanks for everything",
        "body": "Hello there",
        "template": "plain",
        "from_": {"type": "admin", "id": 394051},
        "to": {"type": "user", "id": "536e564f316c83104c000020"},
        "message_type": "email",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateMessageRequestParams` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Segments
<details><summary><code>client.segments.<a href="src/intercom/segments/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all segments.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.segments.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — It includes the count of contacts that belong to each segment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.segments.<a href="src/intercom/segments/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single segment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.segments.find(
    segment_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**segment_id:** `str` — The unique identified of a given segment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Subscription Types
<details><summary><code>client.subscription_types.<a href="src/intercom/subscription_types/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can list all subscription types. A list of subscription type objects will be returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.subscription_types.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PhoneCallRedirects
<details><summary><code>client.phone_call_redirects.<a href="src/intercom/phone_call_redirects/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can use the API to deflect phone calls to the Intercom Messenger.
Calling this endpoint will send an SMS with a link to the Messenger to the phone number specified.

If custom attributes are specified, they will be added to the user or lead's custom data attributes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.phone_call_redirects.create(
    phone="+40241100100",
    custom_attributes={"issue_type": "Billing", "priority": "High"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**phone:** `str` — Phone number in E.164 format, that will receive the SMS to continue the conversation in the Messenger.
    
</dd>
</dl>

<dl>
<dd>

**custom_attributes:** `typing.Optional[CustomAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Teams
<details><summary><code>client.teams.<a href="src/intercom/teams/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This will return a list of team objects for the App.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.teams.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/intercom/teams/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single team, containing an array of admins that belong to this team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.teams.find(
    team_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `str` — The unique identifier of a given team.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Ticket Types
<details><summary><code>client.ticket_types.<a href="src/intercom/ticket_types/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can get a list of all ticket types for a workspace.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.ticket_types.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ticket_types.<a href="src/intercom/ticket_types/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a new ticket type.
> 📘 Creating ticket types.
>
> Every ticket type will be created with two default attributes: _default_title_ and _default_description_.
> For the `icon` propery, use an emoji from [Twemoji Cheatsheet](https://twemoji-cheatsheet.vercel.app/)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.ticket_types.create(
    name="Customer Issue",
    description="Customer Report Template",
    category="Customer",
    icon="🎟️",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the ticket type.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the ticket type.
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[CreateTicketTypeRequestCategory]` — Category of the Ticket Type.
    
</dd>
</dl>

<dl>
<dd>

**icon:** `typing.Optional[str]` — The icon of the ticket type.
    
</dd>
</dl>

<dl>
<dd>

**is_internal:** `typing.Optional[bool]` — Whether the tickets associated with this ticket type are intended for internal use only or will be shared with customers. This is currently a limited attribute.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ticket_types.<a href="src/intercom/ticket_types/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single ticket type.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.ticket_types.get(
    ticket_type_id="ticket_type_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ticket_type_id:** `str` — The unique identifier for the ticket type which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ticket_types.<a href="src/intercom/ticket_types/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


You can update a ticket type.

> 📘 Updating a ticket type.
>
> For the `icon` propery, use an emoji from [Twemoji Cheatsheet](https://twemoji-cheatsheet.vercel.app/)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.ticket_types.update(
    ticket_type_id="ticket_type_id",
    name="Bug Report 2",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ticket_type_id:** `str` — The unique identifier for the ticket type which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the ticket type.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the ticket type.
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[UpdateTicketTypeRequestBodyCategory]` — Category of the Ticket Type.
    
</dd>
</dl>

<dl>
<dd>

**icon:** `typing.Optional[str]` — The icon of the ticket type.
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` — The archived status of the ticket type.
    
</dd>
</dl>

<dl>
<dd>

**is_internal:** `typing.Optional[bool]` — Whether the tickets associated with this ticket type are intended for internal use only or will be shared with customers. This is currently a limited attribute.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tickets
<details><summary><code>client.tickets.<a href="src/intercom/tickets/client.py">reply</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can reply to a ticket with a message from an admin or on behalf of a contact, or with a note for admins.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.tickets.reply(
    ticket_id="123",
    request={
        "message_type": "comment",
        "type": "user",
        "body": "Thanks again :)",
        "intercom_user_id": "667d619d8a68186f43bafe82",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ticket_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `TicketsReplyRequestBodyParams` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tickets.<a href="src/intercom/tickets/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a new ticket.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.tickets.create(
    ticket_type_id="1234",
    contacts=[{"id": "667d61b78a68186f43bafe8d"}],
    ticket_attributes={
        "_default_title_": "example",
        "_default_description_": "there is a problem",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ticket_type_id:** `str` — The ID of the type of ticket you want to create
    
</dd>
</dl>

<dl>
<dd>

**contacts:** `typing.Sequence[CreateTicketRequestContactsItemParams]` — The list of contacts (users or leads) affected by this ticket. Currently only one is allowed
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` — The ID of the company that the ticket is associated with. The ID that you set upon company creation.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[int]` — The time the ticket was created. If not provided, the current time will be used.
    
</dd>
</dl>

<dl>
<dd>

**ticket_attributes:** `typing.Optional[TicketRequestCustomAttributes]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tickets.<a href="src/intercom/tickets/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single ticket.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.tickets.get(
    ticket_id="ticket_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ticket_id:** `str` — The unique identifier for the ticket which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tickets.<a href="src/intercom/tickets/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can update a ticket.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.tickets.update(
    ticket_id="ticket_id",
    ticket_attributes={
        "_default_title_": "example",
        "_default_description_": "there is a problem",
    },
    state="in_progress",
    assignment={"admin_id": "991267899", "assignee_id": "456"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ticket_id:** `str` — The unique identifier for the ticket which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**ticket_attributes:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The attributes set on the ticket.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[UpdateTicketRequestState]` — The state of the ticket.
    
</dd>
</dl>

<dl>
<dd>

**open:** `typing.Optional[bool]` — Specify if a ticket is open. Set to false to close a ticket. Closing a ticket will also unsnooze it.
    
</dd>
</dl>

<dl>
<dd>

**is_shared:** `typing.Optional[bool]` — Specify whether the ticket is visible to users.
    
</dd>
</dl>

<dl>
<dd>

**snoozed_until:** `typing.Optional[int]` — The time you want the ticket to reopen.
    
</dd>
</dl>

<dl>
<dd>

**assignment:** `typing.Optional[UpdateTicketRequestAssignmentParams]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tickets.<a href="src/intercom/tickets/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can search for multiple tickets by the value of their attributes in order to fetch exactly which ones you want.

To search for tickets, you send a `POST` request to `https://api.intercom.io/tickets/search`.

This will accept a query object in the body which will define your filters.
{% admonition type="warning" name="Optimizing search queries" %}
  Search queries can be complex, so optimizing them can help the performance of your search.
  Use the `AND` and `OR` operators to combine multiple filters to get the exact results you need and utilize
  pagination to limit the number of results returned. The default is `20` results per page.
  See the [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#example-search-conversations-request) for more details on how to use the `starting_after` param.
{% /admonition %}

### Nesting & Limitations

You can nest these filters in order to get even more granular insights that pinpoint exactly what you need. Example: (1 OR 2) AND (3 OR 4).
There are some limitations to the amount of multiples there can be:
- There's a limit of max 2 nested filters
- There's a limit of max 15 filters for each AND or OR group

### Accepted Fields

Most keys listed as part of the Ticket model are searchable, whether writeable or not. The value you search for has to match the accepted type, otherwise the query will fail (ie. as `created_at` accepts a date, the `value` cannot be a string such as `"foobar"`).

| Field                                     | Type                                                                                     |
| :---------------------------------------- | :--------------------------------------------------------------------------------------- |
| id                                        | String                                                                                   |
| created_at                                | Date (UNIX timestamp)                                                                    |
| updated_at                                | Date (UNIX timestamp)                                                                    |
| _default_title_                           | String                                                                                   |
| _default_description_                     | String                                                                                   |
| category                                  | String                                                                                   |
| ticket_type_id                            | String                                                                                   |
| contact_ids                               | String                                                                                   |
| teammate_ids                              | String                                                                                   |
| admin_assignee_id                         | String                                                                                   |
| team_assignee_id                          | String                                                                                   |
| open                                      | Boolean                                                                                  |
| state                                     | String                                                                                   |
| snoozed_until                             | Date (UNIX timestamp)                                                                    |
| ticket_attribute.{id}                     | String or Boolean or Date (UNIX timestamp) or Float or Integer                           |

### Accepted Operators

{% admonition type="info" name="Searching based on `created_at`" %}
  You may use the `<=` or `>=` operators to search by `created_at`.
{% /admonition %}

The table below shows the operators you can use to define how you want to search for the value.  The operator should be put in as a string (`"="`). The operator has to be compatible with the field's type  (eg. you cannot search with `>` for a given string value as it's only compatible for integer's and dates).

| Operator | Valid Types                    | Description                                                  |
| :------- | :----------------------------- | :----------------------------------------------------------- |
| =        | All                            | Equals                                                       |
| !=       | All                            | Doesn't Equal                                                |
| IN       | All                            | In  Shortcut for `OR` queries  Values most be in Array       |
| NIN      | All                            | Not In  Shortcut for `OR !` queries  Values must be in Array |
| >        | Integer  Date (UNIX Timestamp) | Greater (or equal) than                                      |
| <       | Integer  Date (UNIX Timestamp) | Lower (or equal) than                                        |
| ~        | String                         | Contains                                                     |
| !~       | String                         | Doesn't Contain                                              |
| ^        | String                         | Starts With                                                  |
| $        | String                         | Ends With                                                    |
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
response = client.tickets.search(
    query={
        "operator": "AND",
        "value": [
            {"field": "created_at", "operator": ">", "value": "1306054154"}
        ],
    },
    pagination={"per_page": 5},
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `SearchRequestQueryParams` 
    
</dd>
</dl>

<dl>
<dd>

**pagination:** `typing.Optional[StartingAfterPagingParams]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Visitors
<details><summary><code>client.visitors.<a href="src/intercom/visitors/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single visitor.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.visitors.find(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The user_id of the Visitor you want to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.visitors.<a href="src/intercom/visitors/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sending a PUT request to `/visitors` will result in an update of an existing Visitor.

**Option 1.** You can update a visitor by passing in the `user_id` of the visitor in the Request body.

**Option 2.** You can update a visitor by passing in the `id` of the visitor in the Request body.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.visitors.update(
    request={"user_id": "fail", "name": "Christian Fail"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `UpdateVisitorRequestParams` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.visitors.<a href="src/intercom/visitors/client.py">merge_to_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can merge a Visitor to a Contact of role type `lead` or `user`.

> 📘 What happens upon a visitor being converted?
>
> If the User exists, then the Visitor will be merged into it, the Visitor deleted and the User returned. If the User does not exist, the Visitor will be converted to a User, with the User identifiers replacing it's Visitor identifiers.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.visitors.merge_to_contact(
    type="user",
    user={"id": "8a88a590-e1c3-41e2-a502-e0649dbf721c", "email": "foo@bar.com"},
    visitor={"user_id": "3ecf64d0-9ed1-4e9f-88e1-da7d6e6782f3"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `str` — Represents the role of the Contact model. Accepts `lead` or `user`.
    
</dd>
</dl>

<dl>
<dd>

**user:** `ConvertVisitorRequestUserParams` — The unique identifiers retained after converting or merging.
    
</dd>
</dl>

<dl>
<dd>

**visitor:** `ConvertVisitorRequestVisitorParams` — The unique identifiers to convert a single Visitor.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## HelpCenters Collections
<details><summary><code>client.help_centers.collections.<a href="src/intercom/help_centers/collections/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all collections by making a GET request to `https://api.intercom.io/help_center/collections`.

Collections will be returned in descending order on the `updated_at` attribute. This means if you need to iterate through results then we'll show the most recently updated collections first.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
response = client.help_centers.collections.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page of results to fetch. Defaults to first page
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — How many results to display per page. Defaults to 15
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.help_centers.collections.<a href="src/intercom/help_centers/collections/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a new collection by making a POST request to `https://api.intercom.io/help_center/collections.`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.help_centers.collections.create(
    name="collection 51",
    description="Missing required parameter",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the collection. For multilingual collections, this will be the name of the default language's content.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the collection. For multilingual collections, this will be the description of the default language's content.
    
</dd>
</dl>

<dl>
<dd>

**translated_content:** `typing.Optional[GroupTranslatedContentParams]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` — The id of the parent collection. If `null` then it will be created as the first level collection.
    
</dd>
</dl>

<dl>
<dd>

**help_center_id:** `typing.Optional[int]` — The id of the help center where the collection will be created. If `null` then it will be created in the default help center.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.help_centers.collections.<a href="src/intercom/help_centers/collections/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single collection by making a GET request to `https://api.intercom.io/help_center/collections/<id>`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.help_centers.collections.find(
    collection_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — The unique identifier for the collection which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.help_centers.collections.<a href="src/intercom/help_centers/collections/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can update the details of a single collection by making a PUT request to `https://api.intercom.io/collections/<id>`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.help_centers.collections.update(
    collection_id="123",
    name="Update collection name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — The unique identifier for the collection which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the collection. For multilingual collections, this will be the name of the default language's content.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the collection. For multilingual collections, this will be the description of the default language's content.
    
</dd>
</dl>

<dl>
<dd>

**translated_content:** `typing.Optional[GroupTranslatedContentParams]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` — The id of the parent collection. If `null` then it will be updated as the first level collection.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.help_centers.collections.<a href="src/intercom/help_centers/collections/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can delete a single collection by making a DELETE request to `https://api.intercom.io/collections/<id>`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.help_centers.collections.delete(
    collection_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `str` — The unique identifier for the collection which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## News Items
<details><summary><code>client.news.items.<a href="src/intercom/news/items/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all news items
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.news.items.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.news.items.<a href="src/intercom/news/items/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a news item
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.news.items.create(
    title="Halloween is here!",
    body="<p>New costumes in store for this spooky season</p>",
    sender_id=991267734,
    state="live",
    deliver_silently=True,
    labels=["Product", "Update", "New"],
    reactions=["😆", "😅"],
    newsfeed_assignments=[{"newsfeed_id": 53, "published_at": 1664638214}],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**title:** `str` — The title of the news item.
    
</dd>
</dl>

<dl>
<dd>

**sender_id:** `int` — The id of the sender of the news item. Must be a teammate on the workspace.
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[str]` — The news item body, which may contain HTML.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[NewsItemRequestState]` — News items will not be visible to your users in the assigned newsfeeds until they are set live.
    
</dd>
</dl>

<dl>
<dd>

**deliver_silently:** `typing.Optional[bool]` — When set to `true`, the news item will appear in the messenger newsfeed without showing a notification badge.
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Sequence[str]]` — Label names displayed to users to categorize the news item.
    
</dd>
</dl>

<dl>
<dd>

**reactions:** `typing.Optional[typing.Sequence[typing.Optional[str]]]` — Ordered list of emoji reactions to the news item. When empty, reactions are disabled.
    
</dd>
</dl>

<dl>
<dd>

**newsfeed_assignments:** `typing.Optional[typing.Sequence[NewsfeedAssignmentParams]]` — A list of newsfeed_assignments to assign to the specified newsfeed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.news.items.<a href="src/intercom/news/items/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single news item.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.news.items.find(
    news_item_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**news_item_id:** `str` — The unique identifier for the news item which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.news.items.<a href="src/intercom/news/items/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.news.items.update(
    news_item_id="123",
    title="Christmas is here!",
    body="<p>New gifts in store for the jolly season</p>",
    sender_id=991267748,
    reactions=["😝", "😂"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**news_item_id:** `str` — The unique identifier for the news item which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` — The title of the news item.
    
</dd>
</dl>

<dl>
<dd>

**sender_id:** `int` — The id of the sender of the news item. Must be a teammate on the workspace.
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[str]` — The news item body, which may contain HTML.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[NewsItemRequestState]` — News items will not be visible to your users in the assigned newsfeeds until they are set live.
    
</dd>
</dl>

<dl>
<dd>

**deliver_silently:** `typing.Optional[bool]` — When set to `true`, the news item will appear in the messenger newsfeed without showing a notification badge.
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Sequence[str]]` — Label names displayed to users to categorize the news item.
    
</dd>
</dl>

<dl>
<dd>

**reactions:** `typing.Optional[typing.Sequence[typing.Optional[str]]]` — Ordered list of emoji reactions to the news item. When empty, reactions are disabled.
    
</dd>
</dl>

<dl>
<dd>

**newsfeed_assignments:** `typing.Optional[typing.Sequence[NewsfeedAssignmentParams]]` — A list of newsfeed_assignments to assign to the specified newsfeed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.news.items.<a href="src/intercom/news/items/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can delete a single news item.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.news.items.delete(
    news_item_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**news_item_id:** `str` — The unique identifier for the news item which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## News Feeds
<details><summary><code>client.news.feeds.<a href="src/intercom/news/feeds/client.py">list_items</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all news items that are live on a given newsfeed
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.news.feeds.list_items(
    newsfeed_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**newsfeed_id:** `str` — The unique identifier for the news feed item which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.news.feeds.<a href="src/intercom/news/feeds/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all newsfeeds
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.news.feeds.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.news.feeds.<a href="src/intercom/news/feeds/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single newsfeed
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.news.feeds.find(
    newsfeed_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**newsfeed_id:** `str` — The unique identifier for the news feed item which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TicketTypes Attributes
<details><summary><code>client.ticket_types.attributes.<a href="src/intercom/ticket_types/attributes/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a new attribute for a ticket type.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.ticket_types.attributes.create(
    ticket_type_id="ticket_type_id",
    name="Attribute Title",
    description="Attribute Description",
    data_type="string",
    required_to_create=False,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ticket_type_id:** `str` — The unique identifier for the ticket type which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the ticket type attribute
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — The description of the attribute presented to the teammate or contact
    
</dd>
</dl>

<dl>
<dd>

**data_type:** `CreateTicketTypeAttributeRequestDataType` — The data type of the attribute
    
</dd>
</dl>

<dl>
<dd>

**required_to_create:** `typing.Optional[bool]` — Whether the attribute is required to be filled in when teammates are creating the ticket in Inbox.
    
</dd>
</dl>

<dl>
<dd>

**required_to_create_for_contacts:** `typing.Optional[bool]` — Whether the attribute is required to be filled in when contacts are creating the ticket in Messenger.
    
</dd>
</dl>

<dl>
<dd>

**visible_on_create:** `typing.Optional[bool]` — Whether the attribute is visible to teammates when creating a ticket in Inbox.
    
</dd>
</dl>

<dl>
<dd>

**visible_to_contacts:** `typing.Optional[bool]` — Whether the attribute is visible to contacts when creating a ticket in Messenger.
    
</dd>
</dl>

<dl>
<dd>

**multiline:** `typing.Optional[bool]` — Whether the attribute allows multiple lines of text (only applicable to string attributes)
    
</dd>
</dl>

<dl>
<dd>

**list_items:** `typing.Optional[str]` — A comma delimited list of items for the attribute value (only applicable to list attributes)
    
</dd>
</dl>

<dl>
<dd>

**allow_multiple_values:** `typing.Optional[bool]` — Whether the attribute allows multiple files to be attached to it (only applicable to file attributes)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ticket_types.attributes.<a href="src/intercom/ticket_types/attributes/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can update an existing attribute for a ticket type.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.ticket_types.attributes.update(
    ticket_type_id="ticket_type_id",
    attribute_id="attribute_id",
    description="New Attribute Description",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ticket_type_id:** `str` — The unique identifier for the ticket type which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**attribute_id:** `str` — The unique identifier for the ticket type attribute which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the ticket type attribute
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the attribute presented to the teammate or contact
    
</dd>
</dl>

<dl>
<dd>

**required_to_create:** `typing.Optional[bool]` — Whether the attribute is required to be filled in when teammates are creating the ticket in Inbox.
    
</dd>
</dl>

<dl>
<dd>

**required_to_create_for_contacts:** `typing.Optional[bool]` — Whether the attribute is required to be filled in when contacts are creating the ticket in Messenger.
    
</dd>
</dl>

<dl>
<dd>

**visible_on_create:** `typing.Optional[bool]` — Whether the attribute is visible to teammates when creating a ticket in Inbox.
    
</dd>
</dl>

<dl>
<dd>

**visible_to_contacts:** `typing.Optional[bool]` — Whether the attribute is visible to contacts when creating a ticket in Messenger.
    
</dd>
</dl>

<dl>
<dd>

**multiline:** `typing.Optional[bool]` — Whether the attribute allows multiple lines of text (only applicable to string attributes)
    
</dd>
</dl>

<dl>
<dd>

**list_items:** `typing.Optional[str]` — A comma delimited list of items for the attribute value (only applicable to list attributes)
    
</dd>
</dl>

<dl>
<dd>

**allow_multiple_values:** `typing.Optional[bool]` — Whether the attribute allows multiple files to be attached to it (only applicable to file attributes)
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` — Whether the attribute should be archived and not shown during creation of the ticket (it will still be present on previously created tickets)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Admins
<details><summary><code>client.unstable.admins.<a href="src/intercom/unstable/admins/client.py">identify_admin</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


You can view the currently authorised admin along with the embedded app object (a "workspace" in legacy terminology).

> 🚧 Single Sign On
>
> If you are building a custom "Log in with Intercom" flow for your site, and you call the `/me` endpoint to identify the logged-in user, you should not accept any sign-ins from users with unverified email addresses as it poses a potential impersonation security risk.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.admins.identify_admin()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.admins.<a href="src/intercom/unstable/admins/client.py">set_away_admin</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can set an Admin as away for the Inbox.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.admins.set_away_admin(
    id=1,
    away_mode_enabled=True,
    away_mode_reassign=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — The unique identifier of a given admin
    
</dd>
</dl>

<dl>
<dd>

**away_mode_enabled:** `bool` — Set to "true" to change the status of the admin to away.
    
</dd>
</dl>

<dl>
<dd>

**away_mode_reassign:** `bool` — Set to "true" to assign any new conversation replies to your default inbox.
    
</dd>
</dl>

<dl>
<dd>

**away_status_reason_id:** `typing.Optional[int]` — The unique identifier of the away status reason
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.admins.<a href="src/intercom/unstable/admins/client.py">list_activity_logs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can get a log of activities by all admins in an app.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.admins.list_activity_logs(
    created_at_after="1677253093",
    created_at_before="1677861493",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**created_at_after:** `str` — The start date that you request data for. It must be formatted as a UNIX timestamp.
    
</dd>
</dl>

<dl>
<dd>

**created_at_before:** `typing.Optional[str]` — The end date that you request data for. It must be formatted as a UNIX timestamp.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.admins.<a href="src/intercom/unstable/admins/client.py">list_admins</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of admins for a given workspace.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.admins.list_admins()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.admins.<a href="src/intercom/unstable/admins/client.py">retrieve_admin</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can retrieve the details of a single admin.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.admins.retrieve_admin(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — The unique identifier of a given admin
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AI Content
<details><summary><code>client.unstable.ai_content.<a href="src/intercom/unstable/ai_content/client.py">list_content_import_sources</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can retrieve a list of all content import sources for a workspace.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.ai_content.list_content_import_sources()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.ai_content.<a href="src/intercom/unstable/ai_content/client.py">create_content_import_source</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a new content import source by sending a POST request to this endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.ai_content.create_content_import_source(
    url="https://www.example.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url:** `str` — The URL of the content import source.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[CreateContentImportSourceRequestStatus]` — The status of the content import source.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.ai_content.<a href="src/intercom/unstable/ai_content/client.py">get_content_import_source</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.ai_content.get_content_import_source(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the content import source which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.ai_content.<a href="src/intercom/unstable/ai_content/client.py">update_content_import_source</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can update an existing content import source.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.ai_content.update_content_import_source(
    id="id",
    sync_behavior="api",
    url="https://www.example.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the content import source which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**sync_behavior:** `UpdateContentImportSourceRequestSyncBehavior` — If you intend to create or update External Pages via the API, this should be set to `api`. You can not change the value to or from api.
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — The URL of the content import source. This may only be different from the existing value if the sync behavior is API.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[UpdateContentImportSourceRequestStatus]` — The status of the content import source.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.ai_content.<a href="src/intercom/unstable/ai_content/client.py">delete_content_import_source</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can delete a content import source by making a DELETE request this endpoint. This will also delete all external pages that were imported from this source.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.ai_content.delete_content_import_source(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the content import source which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.ai_content.<a href="src/intercom/unstable/ai_content/client.py">list_external_pages</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can retrieve a list of all external pages for a workspace.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.ai_content.list_external_pages()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.ai_content.<a href="src/intercom/unstable/ai_content/client.py">create_external_page</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a new external page by sending a POST request to this endpoint. If an external page already exists with the specified source_id and external_id, it will be updated instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.ai_content.create_external_page(
    title="Test",
    html="<html><body><h1>Test</h1></body></html>",
    url="https://www.example.com",
    source_id=44,
    external_id="abc1234",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**title:** `str` — The title of the external page.
    
</dd>
</dl>

<dl>
<dd>

**html:** `str` — The body of the external page in HTML.
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `int` — The unique identifier for the source of the external page which was given by Intercom. Every external page must be associated with a Content Import Source which represents the place it comes from and from which it inherits a default audience (configured in the UI). For a new source, make a POST request to the Content Import Source endpoint and an ID for the source will be returned in the response.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `str` — The identifier for the external page which was given by the source. Must be unique for the source.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — The URL of the external page. This will be used by Fin to link end users to the page it based its answer on. When a URL is not present, Fin will not reference the source.
    
</dd>
</dl>

<dl>
<dd>

**ai_agent_availability:** `typing.Optional[bool]` — Whether the external page should be used to answer questions by AI Agent. Will not default when updating an existing external page.
    
</dd>
</dl>

<dl>
<dd>

**ai_copilot_availability:** `typing.Optional[bool]` — Whether the external page should be used to answer questions by AI Copilot. Will not default when updating an existing external page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.ai_content.<a href="src/intercom/unstable/ai_content/client.py">get_external_page</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can retrieve an external page.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.ai_content.get_external_page(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the external page which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.ai_content.<a href="src/intercom/unstable/ai_content/client.py">update_external_page</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can update an existing external page (if it was created via the API).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.ai_content.update_external_page(
    id="id",
    title="Test",
    html="<html><body><h1>Test</h1></body></html>",
    url="https://www.example.com",
    source_id=47,
    external_id="5678",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the external page which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` — The title of the external page.
    
</dd>
</dl>

<dl>
<dd>

**html:** `str` — The body of the external page in HTML.
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — The URL of the external page. This will be used by Fin to link end users to the page it based its answer on.
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `int` — The unique identifier for the source of the external page which was given by Intercom. Every external page must be associated with a Content Import Source which represents the place it comes from and from which it inherits a default audience (configured in the UI). For a new source, make a POST request to the Content Import Source endpoint and an ID for the source will be returned in the response.
    
</dd>
</dl>

<dl>
<dd>

**fin_availability:** `typing.Optional[bool]` — Whether the external page should be used to answer questions by Fin.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[str]` — The identifier for the external page which was given by the source. Must be unique for the source.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.ai_content.<a href="src/intercom/unstable/ai_content/client.py">delete_external_page</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sending a DELETE request for an external page will remove it from the content library UI and from being used for AI answers.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.ai_content.delete_external_page(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the external page which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Articles
<details><summary><code>client.unstable.articles.<a href="src/intercom/unstable/articles/client.py">list_articles</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all articles by making a GET request to `https://api.intercom.io/articles`.

> 📘 How are the articles sorted and ordered?
>
> Articles will be returned in descending order on the `updated_at` attribute. This means if you need to iterate through results then we'll show the most recently updated articles first.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.articles.list_articles()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.articles.<a href="src/intercom/unstable/articles/client.py">create_article</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a new article by making a POST request to `https://api.intercom.io/articles`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.articles.create_article(
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.articles.<a href="src/intercom/unstable/articles/client.py">retrieve_article</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single article by making a GET request to `https://api.intercom.io/articles/<id>`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.articles.retrieve_article(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — The unique identifier for the article which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.articles.<a href="src/intercom/unstable/articles/client.py">delete_article</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can delete a single article by making a DELETE request to `https://api.intercom.io/articles/<id>`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.articles.delete_article(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — The unique identifier for the article which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.articles.<a href="src/intercom/unstable/articles/client.py">search_articles</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can search for articles by making a GET request to `https://api.intercom.io/articles/search`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.articles.search_articles(
    phrase="Getting started",
    state="published",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**phrase:** `typing.Optional[str]` — The phrase within your articles to search for.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` — The state of the Articles returned. One of `published`, `draft` or `all`.
    
</dd>
</dl>

<dl>
<dd>

**help_center_id:** `typing.Optional[int]` — The ID of the Help Center to search in.
    
</dd>
</dl>

<dl>
<dd>

**highlight:** `typing.Optional[bool]` — Return a highlighted version of the matching content within your articles. Refer to the response schema for more details.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Away Status Reasons
<details><summary><code>client.unstable.away_status_reasons.<a href="src/intercom/unstable/away_status_reasons/client.py">list_away_status_reasons</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all away status reasons configured for the workspace, including deleted ones.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.away_status_reasons.list_away_status_reasons()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Unstable Export
<details><summary><code>client.unstable.export.<a href="src/intercom/unstable/export/client.py">enqueue_a_new_reporting_data_export_job</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.export.enqueue_a_new_reporting_data_export_job(
    dataset_id="conversation",
    attribute_ids=[
        "conversation.id",
        "conversation.first_user_conversation_part_created_at",
    ],
    start_time=1717490000,
    end_time=1717510000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**dataset_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**attribute_ids:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.export.<a href="src/intercom/unstable/export/client.py">list_available_datasets_and_attributes</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.export.list_available_datasets_and_attributes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Help Center
<details><summary><code>client.unstable.help_center.<a href="src/intercom/unstable/help_center/client.py">list_all_collections</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all collections by making a GET request to `https://api.intercom.io/help_center/collections`.

Collections will be returned in descending order on the `updated_at` attribute. This means if you need to iterate through results then we'll show the most recently updated collections first.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.help_center.list_all_collections()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.help_center.<a href="src/intercom/unstable/help_center/client.py">create_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a new collection by making a POST request to `https://api.intercom.io/help_center/collections.`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.help_center.create_collection(
    name="collection 51",
    description="Missing required parameter",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the collection. For multilingual collections, this will be the name of the default language's content.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the collection. For multilingual collections, this will be the description of the default language's content.
    
</dd>
</dl>

<dl>
<dd>

**translated_content:** `typing.Optional[GroupTranslatedContentParams]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` — The id of the parent collection. If `null` then it will be created as the first level collection.
    
</dd>
</dl>

<dl>
<dd>

**help_center_id:** `typing.Optional[int]` — The id of the help center where the collection will be created. If `null` then it will be created in the default help center.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.help_center.<a href="src/intercom/unstable/help_center/client.py">retrieve_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single collection by making a GET request to `https://api.intercom.io/help_center/collections/<id>`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.help_center.retrieve_collection(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — The unique identifier for the collection which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.help_center.<a href="src/intercom/unstable/help_center/client.py">update_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can update the details of a single collection by making a PUT request to `https://api.intercom.io/collections/<id>`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.help_center.update_collection(
    id=1,
    name="Update collection name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — The unique identifier for the collection which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the collection. For multilingual collections, this will be the name of the default language's content.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the collection. For multilingual collections, this will be the description of the default language's content.
    
</dd>
</dl>

<dl>
<dd>

**translated_content:** `typing.Optional[GroupTranslatedContentParams]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` — The id of the parent collection. If `null` then it will be updated as the first level collection.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.help_center.<a href="src/intercom/unstable/help_center/client.py">delete_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can delete a single collection by making a DELETE request to `https://api.intercom.io/collections/<id>`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.help_center.delete_collection(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — The unique identifier for the collection which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.help_center.<a href="src/intercom/unstable/help_center/client.py">retrieve_help_center</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single Help Center by making a GET request to `https://api.intercom.io/help_center/help_center/<id>`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.help_center.retrieve_help_center(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — The unique identifier for the collection which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.help_center.<a href="src/intercom/unstable/help_center/client.py">list_help_centers</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can list all Help Centers by making a GET request to `https://api.intercom.io/help_center/help_centers`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.help_center.list_help_centers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Companies
<details><summary><code>client.unstable.companies.<a href="src/intercom/unstable/companies/client.py">retrieve_company</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a single company by passing in `company_id` or `name`.

  `https://api.intercom.io/companies?name={name}`

  `https://api.intercom.io/companies?company_id={company_id}`

You can fetch all companies and filter by `segment_id` or `tag_id` as a query parameter.

  `https://api.intercom.io/companies?tag_id={tag_id}`

  `https://api.intercom.io/companies?segment_id={segment_id}`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.companies.retrieve_company(
    name="my company",
    company_id="12345",
    tag_id="678910",
    segment_id="98765",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` — The `name` of the company to filter by.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` — The `company_id` of the company to filter by.
    
</dd>
</dl>

<dl>
<dd>

**tag_id:** `typing.Optional[str]` — The `tag_id` of the company to filter by.
    
</dd>
</dl>

<dl>
<dd>

**segment_id:** `typing.Optional[str]` — The `segment_id` of the company to filter by.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page of results to fetch. Defaults to first page
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — How many results to display per page. Defaults to 15
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.companies.<a href="src/intercom/unstable/companies/client.py">create_or_update_company</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create or update a company.

Companies will be only visible in Intercom when there is at least one associated user.

Companies are looked up via `company_id` in a `POST` request, if not found via `company_id`, the new company will be created, if found, that company will be updated.

{% admonition type="warning" name="Using `company_id`" %}
  You can set a unique `company_id` value when creating a company. However, it is not possible to update `company_id`. Be sure to set a unique value once upon creation of the company.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.companies.create_or_update_company(
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.companies.<a href="src/intercom/unstable/companies/client.py">retrieve_a_company_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a single company.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.companies.retrieve_a_company_by_id(
    id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the company which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.companies.<a href="src/intercom/unstable/companies/client.py">update_company</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can update a single company using the Intercom provisioned `id`.

{% admonition type="warning" name="Using `company_id`" %}
  When updating a company it is not possible to update `company_id`. This can only be set once upon creation of the company.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.companies.update_company(
    id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the company which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.companies.<a href="src/intercom/unstable/companies/client.py">delete_company</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can delete a single company.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.companies.delete_company(
    id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the company which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.companies.<a href="src/intercom/unstable/companies/client.py">list_attached_contacts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all contacts that belong to a company.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.companies.list_attached_contacts(
    id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the company which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.companies.<a href="src/intercom/unstable/companies/client.py">list_attached_segments_for_companies</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all segments that belong to a company.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.companies.list_attached_segments_for_companies(
    id="5f4d3c1c-7b1b-4d7d-a97e-6095715c6632",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the company which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.companies.<a href="src/intercom/unstable/companies/client.py">list_all_companies</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can list companies. The company list is sorted by the `last_request_at` field and by default is ordered descending, most recently requested first.

Note that the API does not include companies who have no associated users in list responses.

When using the Companies endpoint and the pages object to iterate through the returned companies, there is a limit of 10,000 Companies that can be returned. If you need to list or iterate on more than 10,000 Companies, please use the [Scroll API](https://developers.intercom.com/reference#iterating-over-all-companies).
{% admonition type="warning" name="Pagination" %}
  You can use pagination to limit the number of results returned. The default is `20` results per page.
  See the [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#pagination-for-list-apis) for more details on how to use the `starting_after` param.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.companies.list_all_companies(
    order="desc",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — The page of results to fetch. Defaults to first page
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — How many results to return per page. Defaults to 15
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — `asc` or `desc`. Return the companies in ascending or descending order. Defaults to desc
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.companies.<a href="src/intercom/unstable/companies/client.py">scroll_over_all_companies</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

      The `list all companies` functionality does not work well for huge datasets, and can result in errors and performance problems when paging deeply. The Scroll API provides an efficient mechanism for iterating over all companies in a dataset.

- Each app can only have 1 scroll open at a time. You'll get an error message if you try to have more than one open per app.
- If the scroll isn't used for 1 minute, it expires and calls with that scroll param will fail
- If the end of the scroll is reached, "companies" will be empty and the scroll parameter will expire

{% admonition type="info" name="Scroll Parameter" %}
  You can get the first page of companies by simply sending a GET request to the scroll endpoint.
  For subsequent requests you will need to use the scroll parameter from the response.
{% /admonition %}
{% admonition type="danger" name="Scroll network timeouts" %}
  Since scroll is often used on large datasets network errors such as timeouts can be encountered. When this occurs you will see a HTTP 500 error with the following message:
  "Request failed due to an internal network error. Please restart the scroll operation."
  If this happens, you will need to restart your scroll query: It is not possible to continue from a specific point when using scroll.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.companies.scroll_over_all_companies()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scroll_param:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.companies.<a href="src/intercom/unstable/companies/client.py">attach_contact_to_a_company</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can attach a company to a single contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.companies.attach_contact_to_a_company(
    id="id",
    company_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the contact which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — The unique identifier for the company which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.companies.<a href="src/intercom/unstable/companies/client.py">detach_contact_from_a_company</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can detach a company from a single contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.companies.detach_contact_from_a_company(
    contact_id="58a430d35458202d41b1e65b",
    id="58a430d35458202d41b1e65b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — The unique identifier for the contact which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The unique identifier for the company which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Contacts
<details><summary><code>client.unstable.contacts.<a href="src/intercom/unstable/contacts/client.py">list_companies_for_a_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of companies that are associated to a contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.contacts.list_companies_for_a_contact(
    id="63a07ddf05a32042dffac965",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the contact which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.contacts.<a href="src/intercom/unstable/contacts/client.py">list_segments_for_a_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of segments that are associated to a contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.contacts.list_segments_for_a_contact(
    contact_id="63a07ddf05a32042dffac965",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — The unique identifier for the contact which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.contacts.<a href="src/intercom/unstable/contacts/client.py">list_subscriptions_for_a_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of subscription types that are attached to a contact. These can be subscriptions that a user has 'opted-in' to or has 'opted-out' from, depending on the subscription type.
This will return a list of Subscription Type objects that the contact is associated with.

The data property will show a combined list of:

  1.Opt-out subscription types that the user has opted-out from.
  2.Opt-in subscription types that the user has opted-in to receiving.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.contacts.list_subscriptions_for_a_contact(
    contact_id="63a07ddf05a32042dffac965",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — The unique identifier for the contact which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.contacts.<a href="src/intercom/unstable/contacts/client.py">list_tags_for_a_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all tags that are attached to a specific contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.contacts.list_tags_for_a_contact(
    contact_id="63a07ddf05a32042dffac965",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — The unique identifier for the contact which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.contacts.<a href="src/intercom/unstable/contacts/client.py">show_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.contacts.show_contact(
    id="63a07ddf05a32042dffac965",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.contacts.<a href="src/intercom/unstable/contacts/client.py">update_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can update an existing contact (ie. user or lead).

{% admonition type="info" %}
  This endpoint handles both **contact updates** and **custom object associations**.

  See _`update a contact with an association to a custom object instance`_ in the request/response examples to see the custom object association format.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.contacts.update_contact(
    id="63a07ddf05a32042dffac965",
    custom_attributes={"order": ["21"]},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — id
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[str]` — The role of the contact.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[str]` — A unique identifier for the contact which is given to Intercom
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — The contacts email
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — The contacts phone
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The contacts name
    
</dd>
</dl>

<dl>
<dd>

**avatar:** `typing.Optional[str]` — An image URL containing the avatar of a contact
    
</dd>
</dl>

<dl>
<dd>

**signed_up_at:** `typing.Optional[int]` — The time specified for when a contact signed up
    
</dd>
</dl>

<dl>
<dd>

**last_seen_at:** `typing.Optional[int]` — The time when the contact was last seen (either where the Intercom Messenger was installed or when specified manually)
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[int]` — The id of an admin that has been assigned account ownership of the contact
    
</dd>
</dl>

<dl>
<dd>

**unsubscribed_from_emails:** `typing.Optional[bool]` — Whether the contact is unsubscribed from emails
    
</dd>
</dl>

<dl>
<dd>

**custom_attributes:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The custom attributes which are set for the contact
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.contacts.<a href="src/intercom/unstable/contacts/client.py">delete_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can delete a single contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.contacts.delete_contact(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.contacts.<a href="src/intercom/unstable/contacts/client.py">merge_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can merge a contact with a `role` of `lead` into a contact with a `role` of `user`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.contacts.merge_contact(
    from_="6762f0d51bb69f9f2193bb7f",
    into="6762f0d51bb69f9f2193bb80",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_:** `typing.Optional[str]` — The unique identifier for the contact to merge away from. Must be a lead.
    
</dd>
</dl>

<dl>
<dd>

**into:** `typing.Optional[str]` — The unique identifier for the contact to merge into. Must be a user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.contacts.<a href="src/intercom/unstable/contacts/client.py">search_contacts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can search for multiple contacts by the value of their attributes in order to fetch exactly who you want.

To search for contacts, you need to send a `POST` request to `https://api.intercom.io/contacts/search`.

This will accept a query object in the body which will define your filters in order to search for contacts.

{% admonition type="warning" name="Optimizing search queries" %}
  Search queries can be complex, so optimizing them can help the performance of your search.
  Use the `AND` and `OR` operators to combine multiple filters to get the exact results you need and utilize
  pagination to limit the number of results returned. The default is `50` results per page.
  See the [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#example-search-conversations-request) for more details on how to use the `starting_after` param.
{% /admonition %}
### Contact Creation Delay

If a contact has recently been created, there is a possibility that it will not yet be available when searching. This means that it may not appear in the response. This delay can take a few minutes. If you need to be instantly notified it is recommended to use webhooks and iterate to see if they match your search filters.

### Nesting & Limitations

You can nest these filters in order to get even more granular insights that pinpoint exactly what you need. Example: (1 OR 2) AND (3 OR 4).
There are some limitations to the amount of multiple's there can be:
* There's a limit of max 2 nested filters
* There's a limit of max 15 filters for each AND or OR group

### Searching for Timestamp Fields

All timestamp fields (created_at, updated_at etc.) are indexed as Dates for Contact Search queries; Datetime queries are not currently supported. This means you can only query for timestamp fields by day - not hour, minute or second.
For example, if you search for all Contacts with a created_at value greater (>) than 1577869200 (the UNIX timestamp for January 1st, 2020 9:00 AM), that will be interpreted as 1577836800 (January 1st, 2020 12:00 AM). The search results will then include Contacts created from January 2nd, 2020 12:00 AM onwards.
If you'd like to get contacts created on January 1st, 2020 you should search with a created_at value equal (=) to 1577836800 (January 1st, 2020 12:00 AM).
This behaviour applies only to timestamps used in search queries. The search results will still contain the full UNIX timestamp and be sorted accordingly.

### Accepted Fields

Most key listed as part of the Contacts Model are searchable, whether writeable or not. The value you search for has to match the accepted type, otherwise the query will fail (ie. as `created_at` accepts a date, the `value` cannot be a string such as `"foorbar"`).

| Field                              | Type                           |
| ---------------------------------- | ------------------------------ |
| id                                 | String                         |
| role                               | String<br>Accepts user or lead |
| name                               | String                         |
| avatar                             | String                         |
| owner_id                           | Integer                        |
| email                              | String                         |
| email_domain                       | String                         |
| phone                              | String                         |
| formatted_phone                    | String                         |
| external_id                        | String                         |
| created_at                         | Date (UNIX Timestamp)          |
| signed_up_at                       | Date (UNIX Timestamp)          |
| updated_at                         | Date (UNIX Timestamp)          |
| last_seen_at                       | Date (UNIX Timestamp)          |
| last_contacted_at                  | Date (UNIX Timestamp)          |
| last_replied_at                    | Date (UNIX Timestamp)          |
| last_email_opened_at               | Date (UNIX Timestamp)          |
| last_email_clicked_at              | Date (UNIX Timestamp)          |
| language_override                  | String                         |
| browser                            | String                         |
| browser_language                   | String                         |
| os                                 | String                         |
| location.country                   | String                         |
| location.region                    | String                         |
| location.city                      | String                         |
| unsubscribed_from_emails           | Boolean                        |
| marked_email_as_spam               | Boolean                        |
| has_hard_bounced                   | Boolean                        |
| ios_last_seen_at                   | Date (UNIX Timestamp)          |
| ios_app_version                    | String                         |
| ios_device                         | String                         |
| ios_app_device                     | String                         |
| ios_os_version                     | String                         |
| ios_app_name                       | String                         |
| ios_sdk_version                    | String                         |
| android_last_seen_at               | Date (UNIX Timestamp)          |
| android_app_version                | String                         |
| android_device                     | String                         |
| android_app_name                   | String                         |
| andoid_sdk_version                 | String                         |
| segment_id                         | String                         |
| tag_id                             | String                         |
| custom_attributes.{attribute_name} | String                         |

### Accepted Operators

{% admonition type="warning" name="Searching based on `created_at`" %}
  You cannot use the `<=` or `>=` operators to search by `created_at`.
{% /admonition %}

The table below shows the operators you can use to define how you want to search for the value.  The operator should be put in as a string (`"="`). The operator has to be compatible with the field's type (eg. you cannot search with `>` for a given string value as it's only compatible for integer's and dates).

| Operator | Valid Types                      | Description                                                      |
| :------- | :------------------------------- | :--------------------------------------------------------------- |
| =        | All                              | Equals                                                           |
| !=       | All                              | Doesn't Equal                                                    |
| IN       | All                              | In<br>Shortcut for `OR` queries<br>Values must be in Array       |
| NIN      | All                              | Not In<br>Shortcut for `OR !` queries<br>Values must be in Array |
| >        | Integer<br>Date (UNIX Timestamp) | Greater than                                                     |
| <       | Integer<br>Date (UNIX Timestamp) | Lower than                                                       |
| ~        | String                           | Contains                                                         |
| !~       | String                           | Doesn't Contain                                                  |
| ^        | String                           | Starts With                                                      |
| $        | String                           | Ends With                                                        |
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.contacts.search_contacts(
    query={
        "operator": "AND",
        "value": [
            {"field": "created_at", "operator": ">", "value": "1306054154"}
        ],
    },
    pagination={"per_page": 5},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `SearchRequestQueryParams` 
    
</dd>
</dl>

<dl>
<dd>

**pagination:** `typing.Optional[StartingAfterPagingParams]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.contacts.<a href="src/intercom/unstable/contacts/client.py">list_contacts</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all contacts (ie. users or leads) in your workspace.
{% admonition type="warning" name="Pagination" %}
  You can use pagination to limit the number of results returned. The default is `50` results per page.
  See the [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#pagination-for-list-apis) for more details on how to use the `starting_after` param.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.contacts.list_contacts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.contacts.<a href="src/intercom/unstable/contacts/client.py">create_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a new contact (ie. user or lead).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.contacts.create_contact(
    request={"email": "joebloggs@intercom.io"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateContactRequestTwo` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.contacts.<a href="src/intercom/unstable/contacts/client.py">show_contact_by_external_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single contact by external ID. Note that this endpoint only supports users and not leads.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.contacts.show_contact_by_external_id(
    external_id="cdd29344-5e0c-4ef0-ac56-f9ba2979bc27",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**external_id:** `str` — The external ID of the user that you want to retrieve
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.contacts.<a href="src/intercom/unstable/contacts/client.py">archive_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can archive a single contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.contacts.archive_contact(
    id="63a07ddf05a32042dffac965",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.contacts.<a href="src/intercom/unstable/contacts/client.py">unarchive_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can unarchive a single contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.contacts.unarchive_contact(
    id="63a07ddf05a32042dffac965",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.contacts.<a href="src/intercom/unstable/contacts/client.py">block_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Block a single contact.<br>**Note:** conversations of the contact will also be archived during the process.<br>More details in [FAQ How do I block Inbox spam?](https://www.intercom.com/help/en/articles/8838656-inbox-faqs)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.contacts.block_contact(
    id="63a07ddf05a32042dffac965",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Notes
<details><summary><code>client.unstable.notes.<a href="src/intercom/unstable/notes/client.py">list_notes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of notes that are associated to a contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.notes.list_notes(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — The unique identifier of a contact.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.notes.<a href="src/intercom/unstable/notes/client.py">create_note</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can add a note to a single contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.notes.create_note(
    id=1,
    body="Hello",
    contact_id="123",
    admin_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — The unique identifier of a given contact.
    
</dd>
</dl>

<dl>
<dd>

**body:** `str` — The text of the note.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` — The unique identifier of a given contact.
    
</dd>
</dl>

<dl>
<dd>

**admin_id:** `typing.Optional[str]` — The unique identifier of a given admin.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.notes.<a href="src/intercom/unstable/notes/client.py">retrieve_note</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single note.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.notes.retrieve_note(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — The unique identifier of a given note
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Subscription Types
<details><summary><code>client.unstable.subscription_types.<a href="src/intercom/unstable/subscription_types/client.py">attach_subscription_type_to_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can add a specific subscription to a contact. In Intercom, we have two different subscription types based on user consent - opt-out and opt-in:

  1.Attaching a contact to an opt-out subscription type will opt that user out from receiving messages related to that subscription type.

  2.Attaching a contact to an opt-in subscription type will opt that user in to receiving messages related to that subscription type.

This will return a subscription type model for the subscription type that was added to the contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.subscription_types.attach_subscription_type_to_contact(
    contact_id="63a07ddf05a32042dffac965",
    id="invalid_id",
    consent_type="opt_in",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — The unique identifier for the contact which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The unique identifier for the subscription which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**consent_type:** `str` — The consent_type of a subscription, opt_out or opt_in.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.subscription_types.<a href="src/intercom/unstable/subscription_types/client.py">detach_subscription_type_to_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can remove a specific subscription from a contact. This will return a subscription type model for the subscription type that was removed from the contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.subscription_types.detach_subscription_type_to_contact(
    contact_id="63a07ddf05a32042dffac965",
    id="37846",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — The unique identifier for the contact which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The unique identifier for the subscription type which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.subscription_types.<a href="src/intercom/unstable/subscription_types/client.py">list_subscription_types</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can list all subscription types. A list of subscription type objects will be returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.subscription_types.list_subscription_types()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tags
<details><summary><code>client.unstable.tags.<a href="src/intercom/unstable/tags/client.py">attach_tag_to_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can tag a specific contact. This will return a tag object for the tag that was added to the contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.tags.attach_tag_to_contact(
    contact_id="63a07ddf05a32042dffac965",
    id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — The unique identifier for the contact which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The unique identifier for the tag which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.tags.<a href="src/intercom/unstable/tags/client.py">detach_tag_from_contact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can remove tag from a specific contact. This will return a tag object for the tag that was removed from the contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.tags.detach_tag_from_contact(
    contact_id="63a07ddf05a32042dffac965",
    id="7522907",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` — The unique identifier for the contact which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The unique identifier for the tag which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.tags.<a href="src/intercom/unstable/tags/client.py">attach_tag_to_conversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can tag a specific conversation. This will return a tag object for the tag that was added to the conversation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.tags.attach_tag_to_conversation(
    conversation_id="64619700005694",
    id="7522907",
    admin_id="780",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — conversation_id
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The unique identifier for the tag which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**admin_id:** `str` — The unique identifier for the admin which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.tags.<a href="src/intercom/unstable/tags/client.py">detach_tag_from_conversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can remove tag from a specific conversation. This will return a tag object for the tag that was removed from the conversation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.tags.detach_tag_from_conversation(
    conversation_id="64619700005694",
    id="7522907",
    admin_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — conversation_id
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — id
    
</dd>
</dl>

<dl>
<dd>

**admin_id:** `str` — The unique identifier for the admin which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.tags.<a href="src/intercom/unstable/tags/client.py">list_tags</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all tags for a given workspace.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.tags.list_tags()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.tags.<a href="src/intercom/unstable/tags/client.py">create_tag</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can use this endpoint to perform the following operations:

  **1. Create a new tag:** You can create a new tag by passing in the tag name as specified in "Create or Update Tag Request Payload" described below.

  **2. Update an existing tag:** You can update an existing tag by passing the id of the tag as specified in "Create or Update Tag Request Payload" described below.

  **3. Tag Companies:** You can tag single company or a list of companies. You can tag a company by passing in the tag name and the company details as specified in "Tag Company Request Payload" described below. Also, if the tag doesn't exist then a new one will be created automatically.

  **4. Untag Companies:** You can untag a single company or a list of companies. You can untag a company by passing in the tag id and the company details as specified in "Untag Company Request Payload" described below.

  **5. Tag Multiple Users:** You can tag a list of users. You can tag the users by passing in the tag name and the user details as specified in "Tag Users Request Payload" described below.

Each operation will return a tag object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.tags.create_tag(
    request={"name": "test", "users": [{"id": "123"}]},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateTagRequestBodyParams` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.tags.<a href="src/intercom/unstable/tags/client.py">find_tag</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of tags that are on the workspace by their id.
This will return a tag object.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.tags.find_tag(
    id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier of a given tag
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.tags.<a href="src/intercom/unstable/tags/client.py">delete_tag</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can delete the details of tags that are on the workspace by passing in the id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.tags.delete_tag(
    id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier of a given tag
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.tags.<a href="src/intercom/unstable/tags/client.py">attach_tag_to_ticket</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can tag a specific ticket. This will return a tag object for the tag that was added to the ticket.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.tags.attach_tag_to_ticket(
    ticket_id="64619700005694",
    id="7522907",
    admin_id="780",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ticket_id:** `str` — ticket_id
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The unique identifier for the tag which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**admin_id:** `str` — The unique identifier for the admin which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.tags.<a href="src/intercom/unstable/tags/client.py">detach_tag_from_ticket</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can remove tag from a specific ticket. This will return a tag object for the tag that was removed from the ticket.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.tags.detach_tag_from_ticket(
    ticket_id="64619700005694",
    id="7522907",
    admin_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ticket_id:** `str` — ticket_id
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The unique identifier for the tag which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**admin_id:** `str` — The unique identifier for the admin which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Conversations
<details><summary><code>client.unstable.conversations.<a href="src/intercom/unstable/conversations/client.py">list_conversations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all conversations.

You can optionally request the result page size and the cursor to start after to fetch the result.
{% admonition type="warning" name="Pagination" %}
  You can use pagination to limit the number of results returned. The default is `20` results per page.
  See the [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#pagination-for-list-apis) for more details on how to use the `starting_after` param.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.conversations.list_conversations()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — How many results per page
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — String used to get the next page of conversations.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.conversations.<a href="src/intercom/unstable/conversations/client.py">create_conversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a conversation that has been initiated by a contact (ie. user or lead).
The conversation can be an in-app message only.

{% admonition type="info" name="Sending for visitors" %}
You can also send a message from a visitor by specifying their `user_id` or `id` value in the `from` field, along with a `type` field value of `contact`.
This visitor will be automatically converted to a contact with a lead role once the conversation is created.
{% /admonition %}

This will return the Message model that has been created.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.conversations.create_conversation(
    from_={"type": "user", "id": "123_doesnt_exist"},
    body="Hello there",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**from_:** `CreateConversationRequestFromParams` 
    
</dd>
</dl>

<dl>
<dd>

**body:** `str` — The content of the message. HTML is not supported.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[int]` — The time the conversation was created as a UTC Unix timestamp. If not provided, the current time will be used. This field is only recommneded for migrating past conversations from another source into Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.conversations.<a href="src/intercom/unstable/conversations/client.py">retrieve_conversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


You can fetch the details of a single conversation.

This will return a single Conversation model with all its conversation parts.

{% admonition type="warning" name="Hard limit of 500 parts" %}
The maximum number of conversation parts that can be returned via the API is 500. If you have more than that we will return the 500 most recent conversation parts.
{% /admonition %}

For AI agent conversation metadata, please note that you need to have the agent enabled in your workspace, which is a [paid feature](https://www.intercom.com/help/en/articles/8205718-fin-resolutions#h_97f8c2e671).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.conversations.retrieve_conversation(
    id=1,
    display_as="plaintext",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — The id of the conversation to target
    
</dd>
</dl>

<dl>
<dd>

**display_as:** `typing.Optional[str]` — Set to plaintext to retrieve conversation messages in plain text.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.conversations.<a href="src/intercom/unstable/conversations/client.py">update_conversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


You can update an existing conversation.

{% admonition type="info" name="Replying and other actions" %}
If you want to reply to a coveration or take an action such as assign, unassign, open, close or snooze, take a look at the reply and manage endpoints.
{% /admonition %}

{% admonition type="info" %}
  This endpoint handles both **conversation updates** and **custom object associations**.

  See _`update a conversation with an association to a custom object instance`_ in the request/response examples to see the custom object association format.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.conversations.update_conversation(
    id=1,
    display_as="plaintext",
    read=True,
    title="new conversation title",
    custom_attributes={"issue_type": "Billing", "priority": "High"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — The id of the conversation to target
    
</dd>
</dl>

<dl>
<dd>

**display_as:** `typing.Optional[str]` — Set to plaintext to retrieve conversation messages in plain text.
    
</dd>
</dl>

<dl>
<dd>

**read:** `typing.Optional[bool]` — Mark a conversation as read within Intercom.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title given to the conversation
    
</dd>
</dl>

<dl>
<dd>

**custom_attributes:** `typing.Optional[CustomAttributesParams]` 
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` — The ID of the company that the conversation is associated with. The unique identifier for the company which is given by Intercom. Set to nil to remove company.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.conversations.<a href="src/intercom/unstable/conversations/client.py">delete_conversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can delete a single conversation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.conversations.delete_conversation(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.conversations.<a href="src/intercom/unstable/conversations/client.py">search_conversations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can search for multiple conversations by the value of their attributes in order to fetch exactly which ones you want.

To search for conversations, you need to send a `POST` request to `https://api.intercom.io/conversations/search`.

This will accept a query object in the body which will define your filters in order to search for conversations.
{% admonition type="warning" name="Optimizing search queries" %}
  Search queries can be complex, so optimizing them can help the performance of your search.
  Use the `AND` and `OR` operators to combine multiple filters to get the exact results you need and utilize
  pagination to limit the number of results returned. The default is `20` results per page and maximum is `150`.
  See the [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#example-search-conversations-request) for more details on how to use the `starting_after` param.
{% /admonition %}

### Nesting & Limitations

You can nest these filters in order to get even more granular insights that pinpoint exactly what you need. Example: (1 OR 2) AND (3 OR 4).
There are some limitations to the amount of multiple's there can be:
- There's a limit of max 2 nested filters
- There's a limit of max 15 filters for each AND or OR group

### Accepted Fields

Most keys listed in the conversation model are searchable, whether writeable or not. The value you search for has to match the accepted type, otherwise the query will fail (ie. as `created_at` accepts a date, the `value` cannot be a string such as `"foorbar"`).
The `source.body` field is unique as the search will not be performed against the entire value, but instead against every element of the value separately. For example, when searching for a conversation with a `"I need support"` body - the query should contain a `=` operator with the value `"support"` for such conversation to be returned. A query with a `=` operator and a `"need support"` value will not yield a result.

| Field                                     | Type                                                                                                                                                   |
| :---------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                                        | String                                                                                                                                                 |
| created_at                                | Date (UNIX timestamp)                                                                                                                                  |
| updated_at                                | Date (UNIX timestamp)                                                                                                                                  |
| source.type                               | String<br>Accepted fields are `conversation`, `email`, `facebook`, `instagram`, `phone_call`, `phone_switch`, `push`, `sms`, `twitter` and `whatsapp`. |
| source.id                                 | String                                                                                                                                                 |
| source.delivered_as                       | String                                                                                                                                                 |
| source.subject                            | String                                                                                                                                                 |
| source.body                               | String                                                                                                                                                 |
| source.author.id                          | String                                                                                                                                                 |
| source.author.type                        | String                                                                                                                                                 |
| source.author.name                        | String                                                                                                                                                 |
| source.author.email                       | String                                                                                                                                                 |
| source.url                                | String                                                                                                                                                 |
| contact_ids                               | String                                                                                                                                                 |
| teammate_ids                              | String                                                                                                                                                 |
| admin_assignee_id                         | String                                                                                                                                                 |
| team_assignee_id                          | String                                                                                                                                                 |
| channel_initiated                         | String                                                                                                                                                 |
| open                                      | Boolean                                                                                                                                                |
| read                                      | Boolean                                                                                                                                                |
| state                                     | String                                                                                                                                                 |
| waiting_since                             | Date (UNIX timestamp)                                                                                                                                  |
| snoozed_until                             | Date (UNIX timestamp)                                                                                                                                  |
| tag_ids                                   | String                                                                                                                                                 |
| priority                                  | String                                                                                                                                                 |
| statistics.time_to_assignment             | Integer                                                                                                                                                |
| statistics.time_to_admin_reply            | Integer                                                                                                                                                |
| statistics.time_to_first_close            | Integer                                                                                                                                                |
| statistics.time_to_last_close             | Integer                                                                                                                                                |
| statistics.median_time_to_reply           | Integer                                                                                                                                                |
| statistics.first_contact_reply_at         | Date (UNIX timestamp)                                                                                                                                  |
| statistics.first_assignment_at            | Date (UNIX timestamp)                                                                                                                                  |
| statistics.first_admin_reply_at           | Date (UNIX timestamp)                                                                                                                                  |
| statistics.first_close_at                 | Date (UNIX timestamp)                                                                                                                                  |
| statistics.last_assignment_at             | Date (UNIX timestamp)                                                                                                                                  |
| statistics.last_assignment_admin_reply_at | Date (UNIX timestamp)                                                                                                                                  |
| statistics.last_contact_reply_at          | Date (UNIX timestamp)                                                                                                                                  |
| statistics.last_admin_reply_at            | Date (UNIX timestamp)                                                                                                                                  |
| statistics.last_close_at                  | Date (UNIX timestamp)                                                                                                                                  |
| statistics.last_closed_by_id              | String                                                                                                                                                 |
| statistics.count_reopens                  | Integer                                                                                                                                                |
| statistics.count_assignments              | Integer                                                                                                                                                |
| statistics.count_conversation_parts       | Integer                                                                                                                                                |
| conversation_rating.requested_at          | Date (UNIX timestamp)                                                                                                                                  |
| conversation_rating.replied_at            | Date (UNIX timestamp)                                                                                                                                  |
| conversation_rating.score                 | Integer                                                                                                                                                |
| conversation_rating.remark                | String                                                                                                                                                 |
| conversation_rating.contact_id            | String                                                                                                                                                 |
| conversation_rating.admin_d               | String                                                                                                                                                 |
| ai_agent_participated                     | Boolean                                                                                                                                                |
| ai_agent.resolution_state                 | String                                                                                                                                                 |
| ai_agent.last_answer_type                 | String                                                                                                                                                 |
| ai_agent.rating                           | Integer                                                                                                                                                |
| ai_agent.rating_remark                    | String                                                                                                                                                 |
| ai_agent.source_type                      | String                                                                                                                                                 |
| ai_agent.source_title                     | String                                                                                                                                                 |

### Accepted Operators

The table below shows the operators you can use to define how you want to search for the value.  The operator should be put in as a string (`"="`). The operator has to be compatible with the field's type  (eg. you cannot search with `>` for a given string value as it's only compatible for integer's and dates).

| Operator | Valid Types                    | Description                                                  |
| :------- | :----------------------------- | :----------------------------------------------------------- |
| =        | All                            | Equals                                                       |
| !=       | All                            | Doesn't Equal                                                |
| IN       | All                            | In  Shortcut for `OR` queries  Values most be in Array       |
| NIN      | All                            | Not In  Shortcut for `OR !` queries  Values must be in Array |
| >        | Integer  Date (UNIX Timestamp) | Greater (or equal) than                                      |
| <       | Integer  Date (UNIX Timestamp) | Lower (or equal) than                                        |
| ~        | String                         | Contains                                                     |
| !~       | String                         | Doesn't Contain                                              |
| ^        | String                         | Starts With                                                  |
| $        | String                         | Ends With                                                    |
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.conversations.search_conversations(
    query={
        "operator": "AND",
        "value": [
            {"field": "created_at", "operator": ">", "value": "1306054154"}
        ],
    },
    pagination={"per_page": 5},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `SearchRequestQueryParams` 
    
</dd>
</dl>

<dl>
<dd>

**pagination:** `typing.Optional[StartingAfterPagingParams]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.conversations.<a href="src/intercom/unstable/conversations/client.py">reply_conversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can reply to a conversation with a message from an admin or on behalf of a contact, or with a note for admins.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.conversations.reply_conversation(
    id='123 or "last"',
    request={
        "message_type": "comment",
        "type": "user",
        "body": "Thanks again :)",
        "intercom_user_id": "6762f1661bb69f9f2193bbbf",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The Intercom provisioned identifier for the conversation or the string "last" to reply to the last part of the conversation
    
</dd>
</dl>

<dl>
<dd>

**request:** `ReplyConversationRequestBodyParams` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.conversations.<a href="src/intercom/unstable/conversations/client.py">manage_conversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

For managing conversations you can:
- Close a conversation
- Snooze a conversation to reopen on a future date
- Open a conversation which is `snoozed` or `closed`
- Assign a conversation to an admin and/or team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.conversations.manage_conversation(
    id="123",
    request={"type": "admin", "admin_id": "12345", "message_type": "close"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The identifier for the conversation as given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request:** `ManageConversationRequestBodyParams` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.conversations.<a href="src/intercom/unstable/conversations/client.py">attach_contact_to_conversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can add participants who are contacts to a conversation, on behalf of either another contact or an admin.

{% admonition type="warning" name="Contacts without an email" %}
If you add a contact via the email parameter and there is no user/lead found on that workspace with he given email, then we will create a new contact with `role` set to `lead`.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.conversations.attach_contact_to_conversation(
    id="123",
    admin_id="12345",
    customer={"intercom_user_id": "6762f19e1bb69f9f2193bbd5"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The identifier for the conversation as given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**admin_id:** `typing.Optional[str]` — The `id` of the admin who is adding the new participant.
    
</dd>
</dl>

<dl>
<dd>

**customer:** `typing.Optional[AttachContactToConversationRequestCustomerParams]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.conversations.<a href="src/intercom/unstable/conversations/client.py">detach_contact_from_conversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can add participants who are contacts to a conversation, on behalf of either another contact or an admin.

{% admonition type="warning" name="Contacts without an email" %}
If you add a contact via the email parameter and there is no user/lead found on that workspace with he given email, then we will create a new contact with `role` set to `lead`.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.conversations.detach_contact_from_conversation(
    conversation_id="123",
    contact_id="123",
    admin_id="5017690",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The identifier for the conversation as given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `str` — The identifier for the contact as given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**admin_id:** `str` — The `id` of the admin who is performing the action.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.conversations.<a href="src/intercom/unstable/conversations/client.py">redact_conversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can redact a conversation part or the source message of a conversation (as seen in the source object).

{% admonition type="info" name="Redacting parts and messages" %}
If you are redacting a conversation part, it must have a `body`. If you are redacting a source message, it must have been created by a contact. We will return a `conversation_part_not_redactable` error if these criteria are not met.
{% /admonition %}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.conversations.redact_conversation(
    request={
        "conversation_id": "really_123_doesnt_exist",
        "conversation_part_id": "really_123_doesnt_exist",
        "type": "conversation_part",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `RedactConversationRequestParams` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.conversations.<a href="src/intercom/unstable/conversations/client.py">convert_conversation_to_ticket</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can convert a conversation to a ticket.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.conversations.convert_conversation_to_ticket(
    id=1,
    ticket_type_id="54",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — The id of the conversation to target
    
</dd>
</dl>

<dl>
<dd>

**ticket_type_id:** `str` — The ID of the type of ticket you want to convert the conversation to
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[TicketRequestCustomAttributesParams]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Unstable CustomChannelEvents
<details><summary><code>client.unstable.custom_channel_events.<a href="src/intercom/unstable/custom_channel_events/client.py">notify_new_conversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Notifies Intercom that a new conversation was created in your custom channel/platform. This triggers conversation creation and workflow automations within Intercom for your custom channel integration.
> **Note:** This endpoint is currently under managed availability. Please reach out to your accounts team to discuss access and tailored, hands-on support.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.custom_channel_events.notify_new_conversation(
    event_id="evt_12345",
    external_conversation_id="conv_67890",
    contact={
        "type": "user",
        "external_id": "user_001",
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event_id:** `str` — Unique identifier for the event.
    
</dd>
</dl>

<dl>
<dd>

**external_conversation_id:** `str` — Identifier for the conversation in your application.
    
</dd>
</dl>

<dl>
<dd>

**contact:** `CustomChannelContactParams` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.custom_channel_events.<a href="src/intercom/unstable/custom_channel_events/client.py">notify_new_message</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Notifies Intercom that a new message was sent in a conversation on your custom channel/platform. This allows Intercom to process the message and trigger any relevant workflow automations.
> **Note:** This endpoint is currently under managed availability. Please reach out to your accounts team to discuss access and tailored, hands-on support.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.custom_channel_events.notify_new_message(
    event_id="evt_54321",
    external_conversation_id="conv_98765",
    contact={
        "type": "user",
        "external_id": "user_002",
        "name": "John Smith",
        "email": "john.smith@example.com",
    },
    body="Hello, I need help with my order.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**body:** `str` — The message content sent by the user.
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `str` — Unique identifier for the event.
    
</dd>
</dl>

<dl>
<dd>

**external_conversation_id:** `str` — Identifier for the conversation in your application.
    
</dd>
</dl>

<dl>
<dd>

**contact:** `CustomChannelContactParams` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.custom_channel_events.<a href="src/intercom/unstable/custom_channel_events/client.py">notify_quick_reply_selected</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Notifies Intercom that a user selected a quick reply option in your custom channel/platform. This allows Intercom to process the response and trigger any relevant workflow automations.
> **Note:** This endpoint is currently under managed availability. Please reach out to your accounts team to discuss access and tailored, hands-on support.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.custom_channel_events.notify_quick_reply_selected(
    event_id="evt_67890",
    external_conversation_id="conv_13579",
    contact={
        "type": "user",
        "external_id": "user_003",
        "name": "Alice Example",
        "email": "alice@example.com",
    },
    quick_reply_option_id="1234",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**quick_reply_option_id:** `str` — Id of the selected quick reply option.
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `str` — Unique identifier for the event.
    
</dd>
</dl>

<dl>
<dd>

**external_conversation_id:** `str` — Identifier for the conversation in your application.
    
</dd>
</dl>

<dl>
<dd>

**contact:** `CustomChannelContactParams` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.custom_channel_events.<a href="src/intercom/unstable/custom_channel_events/client.py">notify_attribute_collected</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Notifies Intercom that a user provided a response to an attribute collector in your custom channel/platform. This allows Intercom to process the attribute and trigger any relevant workflow automations.
> **Note:** This endpoint is currently under managed availability. Please reach out to your accounts team to discuss access and tailored, hands-on support.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.custom_channel_events.notify_attribute_collected(
    event_id="evt_24680",
    external_conversation_id="conv_11223",
    contact={
        "type": "user",
        "external_id": "user_004",
        "name": "Bob Example",
        "email": "bob@example.com",
    },
    attribute={"id": "shipping_address", "value": "123 Main St, Springfield"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**attribute:** `CustomChannelAttributeParams` 
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `str` — Unique identifier for the event.
    
</dd>
</dl>

<dl>
<dd>

**external_conversation_id:** `str` — Identifier for the conversation in your application.
    
</dd>
</dl>

<dl>
<dd>

**contact:** `CustomChannelContactParams` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Custom Object Instances
<details><summary><code>client.unstable.custom_object_instances.<a href="src/intercom/unstable/custom_object_instances/client.py">get_custom_object_instances_by_external_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch a Custom Object Instance by external_id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.custom_object_instances.get_custom_object_instances_by_external_id(
    custom_object_type_identifier="Order",
    external_id="external_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_object_type_identifier:** `str` — The unique identifier of the custom object type that defines the structure of the custom object instance.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.custom_object_instances.<a href="src/intercom/unstable/custom_object_instances/client.py">create_custom_object_instances</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update a custom object instance
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.custom_object_instances.create_custom_object_instances(
    custom_object_type_identifier="Order",
    external_id="123",
    external_created_at=1392036272,
    external_updated_at=1392036272,
    custom_attributes={
        "order_number": "ORDER-12345",
        "total_amount": "custom_attributes",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_object_type_identifier:** `str` — The unique identifier of the custom object type that defines the structure of the custom object instance.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[str]` — A unique identifier for the Custom Object instance in the external system it originated from.
    
</dd>
</dl>

<dl>
<dd>

**external_created_at:** `typing.Optional[int]` — The time when the Custom Object instance was created in the external system it originated from.
    
</dd>
</dl>

<dl>
<dd>

**external_updated_at:** `typing.Optional[int]` — The time when the Custom Object instance was last updated in the external system it originated from.
    
</dd>
</dl>

<dl>
<dd>

**custom_attributes:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — The custom attributes which are set for the Custom Object instance.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.custom_object_instances.<a href="src/intercom/unstable/custom_object_instances/client.py">delete_custom_object_instances_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a single Custom Object instance by external_id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.custom_object_instances.delete_custom_object_instances_by_id(
    custom_object_type_identifier="Order",
    external_id="external_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_object_type_identifier:** `str` — The unique identifier of the custom object type that defines the structure of the custom object instance.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.custom_object_instances.<a href="src/intercom/unstable/custom_object_instances/client.py">get_custom_object_instances_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch a Custom Object Instance by id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.custom_object_instances.get_custom_object_instances_by_id(
    custom_object_type_identifier="Order",
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_object_type_identifier:** `str` — The unique identifier of the custom object type that defines the structure of the custom object instance.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The id or external_id of the custom object instance
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.custom_object_instances.<a href="src/intercom/unstable/custom_object_instances/client.py">delete_custom_object_instances_by_external_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a single Custom Object instance using the Intercom defined id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.custom_object_instances.delete_custom_object_instances_by_external_id(
    custom_object_type_identifier="Order",
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_object_type_identifier:** `str` — The unique identifier of the custom object type that defines the structure of the custom object instance.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The Intercom defined id of the custom object instance
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Data Attributes
<details><summary><code>client.unstable.data_attributes.<a href="src/intercom/unstable/data_attributes/client.py">lis_data_attributes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all data attributes belonging to a workspace for contacts, companies or conversations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.data_attributes.lis_data_attributes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model:** `typing.Optional[LisDataAttributesRequestModel]` — Specify the data attribute model to return.
    
</dd>
</dl>

<dl>
<dd>

**include_archived:** `typing.Optional[bool]` — Include archived attributes in the list. By default we return only non archived data attributes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.data_attributes.<a href="src/intercom/unstable/data_attributes/client.py">create_data_attribute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a data attributes for a `contact` or a `company`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.data_attributes.create_data_attribute(
    name="My Data Attribute",
    model="contact",
    data_type="string",
    description="Just a plain old ring",
    options=["options"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the data attribute.
    
</dd>
</dl>

<dl>
<dd>

**model:** `CreateDataAttributeRequestModel` — The model that the data attribute belongs to.
    
</dd>
</dl>

<dl>
<dd>

**data_type:** `CreateDataAttributeRequestDataType` — The type of data stored for this attribute.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The readable description you see in the UI for the attribute.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[typing.Sequence[str]]` — To create list attributes. Provide a set of hashes with `value` as the key of the options you want to make. `data_type` must be `string`.
    
</dd>
</dl>

<dl>
<dd>

**messenger_writable:** `typing.Optional[bool]` — Can this attribute be updated by the Messenger
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.data_attributes.<a href="src/intercom/unstable/data_attributes/client.py">update_data_attribute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


You can update a data attribute.

> 🚧 Updating the data type is not possible
>
> It is currently a dangerous action to execute changing a data attribute's type via the API. You will need to update the type via the UI instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.data_attributes.update_data_attribute(
    id=1,
    archived=True,
    description="Trying to archieve",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — The data attribute id
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` — Whether the attribute is to be archived or not.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The readable description you see in the UI for the attribute.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[typing.Sequence[str]]` — To create list attributes. Provide a set of hashes with `value` as the key of the options you want to make. `data_type` must be `string`.
    
</dd>
</dl>

<dl>
<dd>

**messenger_writable:** `typing.Optional[bool]` — Can this attribute be updated by the Messenger
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Data Events
<details><summary><code>client.unstable.data_events.<a href="src/intercom/unstable/data_events/client.py">lis_data_events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


> 🚧
>
> Please note that you can only 'list' events that are less than 90 days old. Event counts and summaries will still include your events older than 90 days but you cannot 'list' these events individually if they are older than 90 days

The events belonging to a customer can be listed by sending a GET request to `https://api.intercom.io/events` with a user or lead identifier along with a `type` parameter. The identifier parameter can be one of `user_id`, `email` or `intercom_user_id`. The `type` parameter value must be `user`.

- `https://api.intercom.io/events?type=user&user_id={user_id}`
- `https://api.intercom.io/events?type=user&email={email}`
- `https://api.intercom.io/events?type=user&intercom_user_id={id}` (this call can be used to list leads)

The `email` parameter value should be [url encoded](http://en.wikipedia.org/wiki/Percent-encoding) when sending.

You can optionally define the result page size as well with the `per_page` parameter.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.data_events.lis_data_events(
    filter={"user_id": "user_id"},
    type="type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter:** `LisDataEventsRequestFilterParams` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The value must be user
    
</dd>
</dl>

<dl>
<dd>

**summary:** `typing.Optional[bool]` — summary flag
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.data_events.<a href="src/intercom/unstable/data_events/client.py">create_data_event</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


You will need an Access Token that has write permissions to send Events. Once you have a key you can submit events via POST to the Events resource, which is located at https://api.intercom.io/events, or you can send events using one of the client libraries. When working with the HTTP API directly a client should send the event with a `Content-Type` of `application/json`.

When using the JavaScript API, [adding the code to your app](http://docs.intercom.io/configuring-Intercom/tracking-user-events-in-your-app) makes the Events API available. Once added, you can submit an event using the `trackEvent` method. This will associate the event with the Lead or currently logged-in user or logged-out visitor/lead and send it to Intercom. The final parameter is a map that can be used to send optional metadata about the event.

With the Ruby client you pass a hash describing the event to `Intercom::Event.create`, or call the `track_user` method directly on the current user object (e.g. `user.track_event`).

**NB: For the JSON object types, please note that we do not currently support nested JSON structure.**

| Type            | Description                                                                                                                                                                                                     | Example                                                                           |
| :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| String          | The value is a JSON String                                                                                                                                                                                      | `"source":"desktop"`                                                              |
| Number          | The value is a JSON Number                                                                                                                                                                                      | `"load": 3.67`                                                                    |
| Date            | The key ends with the String `_date` and the value is a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time), assumed to be in the [UTC](http://en.wikipedia.org/wiki/Coordinated_Universal_Time) timezone. | `"contact_date": 1392036272`                                                      |
| Link            | The value is a HTTP or HTTPS URI.                                                                                                                                                                               | `"article": "https://example.org/ab1de.html"`                                     |
| Rich Link       | The value is a JSON object that contains `url` and `value` keys.                                                                                                                                                | `"article": {"url": "https://example.org/ab1de.html", "value":"the dude abides"}` |
| Monetary Amount | The value is a JSON object that contains `amount` and `currency` keys. The `amount` key is a positive integer representing the amount in cents. The price in the example to the right denotes €349.99.          | `"price": {"amount": 34999, "currency": "eur"}`                                   |

**Lead Events**

When submitting events for Leads, you will need to specify the Lead's `id`.

**Metadata behaviour**

- We currently limit the number of tracked metadata keys to 10 per event. Once the quota is reached, we ignore any further keys we receive. The first 10 metadata keys are determined by the order in which they are sent in with the event.
- It is not possible to change the metadata keys once the event has been sent. A new event will need to be created with the new keys and you can archive the old one.
- There might be up to 24 hrs delay when you send a new metadata for an existing event.

**Event de-duplication**

The API may detect and ignore duplicate events. Each event is uniquely identified as a combination of the following data - the Workspace identifier, the Contact external identifier, the Data Event name and the Data Event created time. As a result, it is **strongly recommended** to send a second granularity Unix timestamp in the `created_at` field.

Duplicated events are responded to using the normal `202 Accepted` code - an error is not thrown, however repeat requests will be counted against any rate limit that is in place.

### HTTP API Responses

- Successful responses to submitted events return `202 Accepted` with an empty body.
- Unauthorised access will be rejected with a `401 Unauthorized` or `403 Forbidden` response code.
- Events sent about users that cannot be found will return a `404 Not Found`.
- Event lists containing duplicate events will have those duplicates ignored.
- Server errors will return a `500` response code and may contain an error message in the body.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.data_events.create_data_event(
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateDataEventRequestTwo` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.data_events.<a href="src/intercom/unstable/data_events/client.py">data_event_summaries</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create event summaries for a user. Event summaries are used to track the number of times an event has occurred, the first time it occurred and the last time it occurred.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.data_events.data_event_summaries()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — Your identifier for the user.
    
</dd>
</dl>

<dl>
<dd>

**event_summaries:** `typing.Optional[CreateDataEventSummariesRequestEventSummariesParams]` — A list of event summaries for the user. Each event summary should contain the event name, the time the event occurred, and the number of times the event occurred. The event name should be a past tense 'verb-noun' combination, to improve readability, for example `updated-plan`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Data Export
<details><summary><code>client.unstable.data_export.<a href="src/intercom/unstable/data_export/client.py">create_data_export</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

To create your export job, you need to send a `POST` request to the export endpoint `https://api.intercom.io/export/content/data`.

The only parameters you need to provide are the range of dates that you want exported.

>🚧 Limit of one active job
>
> You can only have one active job per workspace. You will receive a HTTP status code of 429 with the message Exceeded rate limit of 1 pending message data export jobs if you attempt to create a second concurrent job.

>❗️ Updated_at not included
>
> It should be noted that the timeframe only includes messages sent during the time period and not messages that were only updated during this period. For example, if a message was updated yesterday but sent two days ago, you would need to set the created_at_after date before the message was sent to include that in your retrieval job.

>📘 Date ranges are inclusive
>
> Requesting data for 2018-06-01 until 2018-06-30 will get all data for those days including those specified - e.g. 2018-06-01 00:00:00 until 2018-06-30 23:59:99.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.data_export.create_data_export(
    created_at_after=1734519776,
    created_at_before=1734537776,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**created_at_after:** `int` — The start date that you request data for. It must be formatted as a unix timestamp.
    
</dd>
</dl>

<dl>
<dd>

**created_at_before:** `int` — The end date that you request data for. It must be formatted as a unix timestamp.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.data_export.<a href="src/intercom/unstable/data_export/client.py">get_data_export</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can view the status of your job by sending a `GET` request to the URL
`https://api.intercom.io/export/content/data/{job_identifier}` - the `{job_identifier}` is the value returned in the response when you first created the export job. More on it can be seen in the Export Job Model.

> 🚧 Jobs expire after two days
> All jobs that have completed processing (and are thus available to download from the provided URL) will have an expiry limit of two days from when the export ob completed. After this, the data will no longer be available.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.data_export.get_data_export(
    job_identifier="job_identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_identifier:** `str` — job_identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.data_export.<a href="src/intercom/unstable/data_export/client.py">cancel_data_export</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can cancel your job
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.data_export.cancel_data_export(
    job_identifier="job_identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_identifier:** `str` — job_identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.data_export.<a href="src/intercom/unstable/data_export/client.py">download_data_export</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

When a job has a status of complete, and thus a filled download_url, you can download your data by hitting that provided URL, formatted like so: https://api.intercom.io/download/content/data/xyz1234.

Your exported message data will be streamed continuously back down to you in a gzipped CSV format.

> 📘 Octet header required
>
> You will have to specify the header Accept: `application/octet-stream` when hitting this endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.data_export.download_data_export(
    job_identifier="job_identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_identifier:** `str` — job_identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Jobs
<details><summary><code>client.unstable.jobs.<a href="src/intercom/unstable/jobs/client.py">status</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the status of job execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.jobs.status(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the job which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Messages
<details><summary><code>client.unstable.messages.<a href="src/intercom/unstable/messages/client.py">create_message</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a message that has been initiated by an admin. The conversation can be either an in-app message, an email, sms or whatsapp.

> 🚧 Sending for visitors
>
> There can be a short delay between when a contact is created and when a contact becomes available to be messaged through the API. A 404 Not Found error will be returned in this case.

This will return the Message model that has been created.

> 🚧 Retrieving Associated Conversations
>
> As this is a message, there will be no conversation present until the contact responds. Once they do, you will have to search for a contact's conversations with the id of the message.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.messages.create_message(
    request={
        "from": {"type": "admin", "id": "991267821"},
        "to": {"type": "user", "id": "6762f23b1bb69f9f2193bc1d"},
        "message_type": "sms",
        "body": "heyy https://picsum.photos/200/300",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateMessageRequestThree` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.messages.<a href="src/intercom/unstable/messages/client.py">get_whats_app_message_status</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves statuses of messages sent from the Outbound module. Currently, this API only supports WhatsApp messages.


This endpoint returns paginated status events for WhatsApp messages sent via the Outbound module, providing
information about delivery state and related message details.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.messages.get_whats_app_message_status(
    ruleset_id="ruleset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ruleset_id:** `str` — The unique identifier for the set of messages to check status for
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page (default 50, max 100)
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — Cursor for pagination, used to fetch the next page of results
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## News
<details><summary><code>client.unstable.news.<a href="src/intercom/unstable/news/client.py">list_news_items</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all news items
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.news.list_news_items()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.news.<a href="src/intercom/unstable/news/client.py">create_news_item</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a news item
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.news.create_news_item(
    title="Halloween is here!",
    body="<p>New costumes in store for this spooky season</p>",
    sender_id=991267834,
    state="live",
    deliver_silently=True,
    labels=["Product", "Update", "New"],
    reactions=["😆", "😅"],
    newsfeed_assignments=[{"newsfeed_id": 53, "published_at": 1664638214}],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**title:** `str` — The title of the news item.
    
</dd>
</dl>

<dl>
<dd>

**sender_id:** `int` — The id of the sender of the news item. Must be a teammate on the workspace.
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[str]` — The news item body, which may contain HTML.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[NewsItemRequestState]` — News items will not be visible to your users in the assigned newsfeeds until they are set live.
    
</dd>
</dl>

<dl>
<dd>

**deliver_silently:** `typing.Optional[bool]` — When set to `true`, the news item will appear in the messenger newsfeed without showing a notification badge.
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Sequence[str]]` — Label names displayed to users to categorize the news item.
    
</dd>
</dl>

<dl>
<dd>

**reactions:** `typing.Optional[typing.Sequence[typing.Optional[str]]]` — Ordered list of emoji reactions to the news item. When empty, reactions are disabled.
    
</dd>
</dl>

<dl>
<dd>

**newsfeed_assignments:** `typing.Optional[typing.Sequence[NewsfeedAssignmentParams]]` — A list of newsfeed_assignments to assign to the specified newsfeed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.news.<a href="src/intercom/unstable/news/client.py">retrieve_news_item</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single news item.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.news.retrieve_news_item(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — The unique identifier for the news item which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.news.<a href="src/intercom/unstable/news/client.py">update_news_item</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.news.update_news_item(
    id=1,
    title="Christmas is here!",
    body="<p>New gifts in store for the jolly season</p>",
    sender_id=991267848,
    reactions=["😝", "😂"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — The unique identifier for the news item which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` — The title of the news item.
    
</dd>
</dl>

<dl>
<dd>

**sender_id:** `int` — The id of the sender of the news item. Must be a teammate on the workspace.
    
</dd>
</dl>

<dl>
<dd>

**body:** `typing.Optional[str]` — The news item body, which may contain HTML.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[NewsItemRequestState]` — News items will not be visible to your users in the assigned newsfeeds until they are set live.
    
</dd>
</dl>

<dl>
<dd>

**deliver_silently:** `typing.Optional[bool]` — When set to `true`, the news item will appear in the messenger newsfeed without showing a notification badge.
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Sequence[str]]` — Label names displayed to users to categorize the news item.
    
</dd>
</dl>

<dl>
<dd>

**reactions:** `typing.Optional[typing.Sequence[typing.Optional[str]]]` — Ordered list of emoji reactions to the news item. When empty, reactions are disabled.
    
</dd>
</dl>

<dl>
<dd>

**newsfeed_assignments:** `typing.Optional[typing.Sequence[NewsfeedAssignmentParams]]` — A list of newsfeed_assignments to assign to the specified newsfeed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.news.<a href="src/intercom/unstable/news/client.py">delete_news_item</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can delete a single news item.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.news.delete_news_item(
    id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` — The unique identifier for the news item which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.news.<a href="src/intercom/unstable/news/client.py">list_live_newsfeed_items</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all news items that are live on a given newsfeed
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.news.list_live_newsfeed_items(
    id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the news feed item which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.news.<a href="src/intercom/unstable/news/client.py">list_newsfeeds</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all newsfeeds
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.news.list_newsfeeds()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.news.<a href="src/intercom/unstable/news/client.py">retrieve_newsfeed</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single newsfeed
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.news.retrieve_newsfeed(
    id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the news feed item which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Segments
<details><summary><code>client.unstable.segments.<a href="src/intercom/unstable/segments/client.py">list_segments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch a list of all segments.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.segments.list_segments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**include_count:** `typing.Optional[bool]` — It includes the count of contacts that belong to each segment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.segments.<a href="src/intercom/unstable/segments/client.py">retrieve_segment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single segment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.segments.retrieve_segment(
    id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identified of a given segment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Switch
<details><summary><code>client.unstable.switch.<a href="src/intercom/unstable/switch/client.py">create_phone_switch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can use the API to deflect phone calls to the Intercom Messenger.
Calling this endpoint will send an SMS with a link to the Messenger to the phone number specified.

If custom attributes are specified, they will be added to the user or lead's custom data attributes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.switch.create_phone_switch(
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Teams
<details><summary><code>client.unstable.teams.<a href="src/intercom/unstable/teams/client.py">list_teams</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This will return a list of team objects for the App.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.teams.list_teams()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.teams.<a href="src/intercom/unstable/teams/client.py">retrieve_team</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single team, containing an array of admins that belong to this team.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.teams.retrieve_team(
    id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier of a given team.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Ticket States
<details><summary><code>client.unstable.ticket_states.<a href="src/intercom/unstable/ticket_states/client.py">list_ticket_states</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can get a list of all ticket states for a workspace.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.ticket_states.list_ticket_states()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Ticket Type Attributes
<details><summary><code>client.unstable.ticket_type_attributes.<a href="src/intercom/unstable/ticket_type_attributes/client.py">create_ticket_type_attribute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a new attribute for a ticket type.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.ticket_type_attributes.create_ticket_type_attribute(
    ticket_type_id="ticket_type_id",
    name="Attribute Title",
    description="Attribute Description",
    data_type="string",
    required_to_create=False,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ticket_type_id:** `str` — The unique identifier for the ticket type which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the ticket type attribute
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — The description of the attribute presented to the teammate or contact
    
</dd>
</dl>

<dl>
<dd>

**data_type:** `CreateTicketTypeAttributeRequestDataType` — The data type of the attribute
    
</dd>
</dl>

<dl>
<dd>

**required_to_create:** `typing.Optional[bool]` — Whether the attribute is required to be filled in when teammates are creating the ticket in Inbox.
    
</dd>
</dl>

<dl>
<dd>

**required_to_create_for_contacts:** `typing.Optional[bool]` — Whether the attribute is required to be filled in when contacts are creating the ticket in Messenger.
    
</dd>
</dl>

<dl>
<dd>

**visible_on_create:** `typing.Optional[bool]` — Whether the attribute is visible to teammates when creating a ticket in Inbox.
    
</dd>
</dl>

<dl>
<dd>

**visible_to_contacts:** `typing.Optional[bool]` — Whether the attribute is visible to contacts when creating a ticket in Messenger.
    
</dd>
</dl>

<dl>
<dd>

**multiline:** `typing.Optional[bool]` — Whether the attribute allows multiple lines of text (only applicable to string attributes)
    
</dd>
</dl>

<dl>
<dd>

**list_items:** `typing.Optional[str]` — A comma delimited list of items for the attribute value (only applicable to list attributes)
    
</dd>
</dl>

<dl>
<dd>

**allow_multiple_values:** `typing.Optional[bool]` — Whether the attribute allows multiple files to be attached to it (only applicable to file attributes)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.ticket_type_attributes.<a href="src/intercom/unstable/ticket_type_attributes/client.py">update_ticket_type_attribute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can update an existing attribute for a ticket type.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.ticket_type_attributes.update_ticket_type_attribute(
    ticket_type_id="ticket_type_id",
    id="id",
    description="New Attribute Description",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ticket_type_id:** `str` — The unique identifier for the ticket type which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The unique identifier for the ticket type attribute which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the ticket type attribute
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the attribute presented to the teammate or contact
    
</dd>
</dl>

<dl>
<dd>

**required_to_create:** `typing.Optional[bool]` — Whether the attribute is required to be filled in when teammates are creating the ticket in Inbox.
    
</dd>
</dl>

<dl>
<dd>

**required_to_create_for_contacts:** `typing.Optional[bool]` — Whether the attribute is required to be filled in when contacts are creating the ticket in Messenger.
    
</dd>
</dl>

<dl>
<dd>

**visible_on_create:** `typing.Optional[bool]` — Whether the attribute is visible to teammates when creating a ticket in Inbox.
    
</dd>
</dl>

<dl>
<dd>

**visible_to_contacts:** `typing.Optional[bool]` — Whether the attribute is visible to contacts when creating a ticket in Messenger.
    
</dd>
</dl>

<dl>
<dd>

**multiline:** `typing.Optional[bool]` — Whether the attribute allows multiple lines of text (only applicable to string attributes)
    
</dd>
</dl>

<dl>
<dd>

**list_items:** `typing.Optional[str]` — A comma delimited list of items for the attribute value (only applicable to list attributes)
    
</dd>
</dl>

<dl>
<dd>

**allow_multiple_values:** `typing.Optional[bool]` — Whether the attribute allows multiple files to be attached to it (only applicable to file attributes)
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` — Whether the attribute should be archived and not shown during creation of the ticket (it will still be present on previously created tickets)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Ticket Types
<details><summary><code>client.unstable.ticket_types.<a href="src/intercom/unstable/ticket_types/client.py">list_ticket_types</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can get a list of all ticket types for a workspace.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.ticket_types.list_ticket_types()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.ticket_types.<a href="src/intercom/unstable/ticket_types/client.py">create_ticket_type</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can create a new ticket type.
> 📘 Creating ticket types.
>
> Every ticket type will be created with two default attributes: _default_title_ and _default_description_.
> For the `icon` propery, use an emoji from [Twemoji Cheatsheet](https://twemoji-cheatsheet.vercel.app/)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.ticket_types.create_ticket_type(
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.ticket_types.<a href="src/intercom/unstable/ticket_types/client.py">get_ticket_type</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single ticket type.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.ticket_types.get_ticket_type(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the ticket type which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tickets
<details><summary><code>client.unstable.tickets.<a href="src/intercom/unstable/tickets/client.py">reply_ticket</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can reply to a ticket with a message from an admin or on behalf of a contact, or with a note for admins.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.tickets.reply_ticket(
    id="123",
    request={
        "message_type": "comment",
        "type": "user",
        "body": "Thanks again :)",
        "intercom_user_id": "6762f2a41bb69f9f2193bc4c",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ReplyTicketRequestBodyParams` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.tickets.<a href="src/intercom/unstable/tickets/client.py">enqueue_create_ticket</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enqueues ticket creation for asynchronous processing, returning if the job was enqueued successfully to be processed. We attempt to perform a best-effort validation on inputs before tasks are enqueued. If the given parameters are incorrect, we won't enqueue the job.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.tickets.enqueue_create_ticket(
    ticket_type_id="1234",
    contacts=[{"id": "6762f2d81bb69f9f2193bc54"}],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ticket_type_id:** `str` — The ID of the type of ticket you want to create
    
</dd>
</dl>

<dl>
<dd>

**contacts:** `typing.Sequence[CreateTicketRequestContactsItemParams]` — The list of contacts (users or leads) affected by this ticket. Currently only one is allowed
    
</dd>
</dl>

<dl>
<dd>

**skip_notifications:** `typing.Optional[bool]` — Option to disable notifications when a Ticket is created.
    
</dd>
</dl>

<dl>
<dd>

**conversation_to_link_id:** `typing.Optional[str]` 

The ID of the conversation you want to link to the ticket. Here are the valid ways of linking two tickets:
 - conversation | back-office ticket
 - customer tickets | non-shared back-office ticket
 - conversation | tracker ticket
 - customer ticket | tracker ticket
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` — The ID of the company that the ticket is associated with. The unique identifier for the company which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[int]` — The time the ticket was created. If not provided, the current time will be used.
    
</dd>
</dl>

<dl>
<dd>

**assignment:** `typing.Optional[CreateTicketRequestAssignmentParams]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.tickets.<a href="src/intercom/unstable/tickets/client.py">get_ticket</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single ticket.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.tickets.get_ticket(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the ticket which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.tickets.<a href="src/intercom/unstable/tickets/client.py">update_ticket</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can update a ticket.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.tickets.update_ticket(
    id="id",
    ticket_state_id="123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the ticket which is given by Intercom
    
</dd>
</dl>

<dl>
<dd>

**ticket_attributes:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The attributes set on the ticket.
    
</dd>
</dl>

<dl>
<dd>

**ticket_state_id:** `typing.Optional[str]` — The ID of the ticket state associated with the ticket type.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` — The ID of the company that the ticket is associated with. The unique identifier for the company which is given by Intercom. Set to nil to remove company.
    
</dd>
</dl>

<dl>
<dd>

**open:** `typing.Optional[bool]` — Specify if a ticket is open. Set to false to close a ticket. Closing a ticket will also unsnooze it.
    
</dd>
</dl>

<dl>
<dd>

**is_shared:** `typing.Optional[bool]` — Specify whether the ticket is visible to users.
    
</dd>
</dl>

<dl>
<dd>

**snoozed_until:** `typing.Optional[int]` — The time you want the ticket to reopen.
    
</dd>
</dl>

<dl>
<dd>

**admin_id:** `typing.Optional[int]` — The ID of the admin performing ticket update. Needed for workflows execution and attributing actions to specific admins.
    
</dd>
</dl>

<dl>
<dd>

**assignee_id:** `typing.Optional[str]` — The ID of the admin or team to which the ticket is assigned. Set this 0 to unassign it.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.tickets.<a href="src/intercom/unstable/tickets/client.py">delete_ticket</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can delete a ticket using the Intercom provided ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.tickets.delete_ticket(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The unique identifier for the ticket which is given by Intercom.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.tickets.<a href="src/intercom/unstable/tickets/client.py">search_tickets</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can search for multiple tickets by the value of their attributes in order to fetch exactly which ones you want.

To search for tickets, you send a `POST` request to `https://api.intercom.io/tickets/search`.

This will accept a query object in the body which will define your filters.
{% admonition type="warning" name="Optimizing search queries" %}
  Search queries can be complex, so optimizing them can help the performance of your search.
  Use the `AND` and `OR` operators to combine multiple filters to get the exact results you need and utilize
  pagination to limit the number of results returned. The default is `20` results per page.
  See the [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#example-search-conversations-request) for more details on how to use the `starting_after` param.
{% /admonition %}

### Nesting & Limitations

You can nest these filters in order to get even more granular insights that pinpoint exactly what you need. Example: (1 OR 2) AND (3 OR 4).
There are some limitations to the amount of multiples there can be:
- There's a limit of max 2 nested filters
- There's a limit of max 15 filters for each AND or OR group

### Accepted Fields

Most keys listed as part of the Ticket model are searchable, whether writeable or not. The value you search for has to match the accepted type, otherwise the query will fail (ie. as `created_at` accepts a date, the `value` cannot be a string such as `"foobar"`).
The `source.body` field is unique as the search will not be performed against the entire value, but instead against every element of the value separately. For example, when searching for a conversation with a `"I need support"` body - the query should contain a `=` operator with the value `"support"` for such conversation to be returned. A query with a `=` operator and a `"need support"` value will not yield a result.

| Field                                     | Type                                                                                     |
| :---------------------------------------- | :--------------------------------------------------------------------------------------- |
| id                                        | String                                                                                   |
| created_at                                | Date (UNIX timestamp)                                                                    |
| updated_at                                | Date (UNIX timestamp)                                                                    |
| _default_title_                           | String                                                                                   |
| _default_description_                     | String                                                                                   |
| category                                  | String                                                                                   |
| ticket_type_id                            | String                                                                                   |
| contact_ids                               | String                                                                                   |
| teammate_ids                              | String                                                                                   |
| admin_assignee_id                         | String                                                                                   |
| team_assignee_id                          | String                                                                                   |
| open                                      | Boolean                                                                                  |
| state                                     | String                                                                                   |
| snoozed_until                             | Date (UNIX timestamp)                                                                    |
| ticket_attribute.{id}                     | String or Boolean or Date (UNIX timestamp) or Float or Integer                           |

{% admonition type="info" name="Searching by Category" %}
When searching for tickets by the **`category`** field, specific terms must be used instead of the category names:
* For **Customer** category tickets, use the term `request`.
* For **Back-office** category tickets, use the term `task`.
* For **Tracker** category tickets, use the term `tracker`.
{% /admonition %}

### Accepted Operators

{% admonition type="info" name="Searching based on `created_at`" %}
  You may use the `<=` or `>=` operators to search by `created_at`.
{% /admonition %}

The table below shows the operators you can use to define how you want to search for the value.  The operator should be put in as a string (`"="`). The operator has to be compatible with the field's type  (eg. you cannot search with `>` for a given string value as it's only compatible for integer's and dates).

| Operator | Valid Types                    | Description                                                  |
| :------- | :----------------------------- | :----------------------------------------------------------- |
| =        | All                            | Equals                                                       |
| !=       | All                            | Doesn't Equal                                                |
| IN       | All                            | In  Shortcut for `OR` queries  Values most be in Array       |
| NIN      | All                            | Not In  Shortcut for `OR !` queries  Values must be in Array |
| >        | Integer  Date (UNIX Timestamp) | Greater (or equal) than                                      |
| <       | Integer  Date (UNIX Timestamp) | Lower (or equal) than                                        |
| ~        | String                         | Contains                                                     |
| !~       | String                         | Doesn't Contain                                              |
| ^        | String                         | Starts With                                                  |
| $        | String                         | Ends With                                                    |
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.tickets.search_tickets(
    query={
        "operator": "AND",
        "value": [
            {"field": "created_at", "operator": ">", "value": "1306054154"}
        ],
    },
    pagination={"per_page": 5},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `SearchRequestQueryParams` 
    
</dd>
</dl>

<dl>
<dd>

**pagination:** `typing.Optional[StartingAfterPagingParams]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Visitors
<details><summary><code>client.unstable.visitors.<a href="src/intercom/unstable/visitors/client.py">retrieve_visitor_with_user_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can fetch the details of a single visitor.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.visitors.retrieve_visitor_with_user_id(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The user_id of the Visitor you want to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.visitors.<a href="src/intercom/unstable/visitors/client.py">update_visitor</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sending a PUT request to `/visitors` will result in an update of an existing Visitor.

**Option 1.** You can update a visitor by passing in the `user_id` of the visitor in the Request body.

**Option 2.** You can update a visitor by passing in the `id` of the visitor in the Request body.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.visitors.update_visitor(
    request={"user_id": "fail", "name": "Christian Fail"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `UpdateVisitorRequestOne` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.unstable.visitors.<a href="src/intercom/unstable/visitors/client.py">convert_visitor</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can merge a Visitor to a Contact of role type `lead` or `user`.

> 📘 What happens upon a visitor being converted?
>
> If the User exists, then the Visitor will be merged into it, the Visitor deleted and the User returned. If the User does not exist, the Visitor will be converted to a User, with the User identifiers replacing it's Visitor identifiers.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from intercom import Intercom

client = Intercom(
    token="YOUR_TOKEN",
)
client.unstable.visitors.convert_visitor(
    type="user",
    user={"email": "foo@bar.com"},
    visitor={"user_id": "3ecf64d0-9ed1-4e9f-88e1-da7d6e6782f3"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `str` — Represents the role of the Contact model. Accepts `lead` or `user`.
    
</dd>
</dl>

<dl>
<dd>

**user:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**visitor:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>


# ValidateLogin

Types:

```python
from blink.types import CredentialsEmailPassword, ValidateLoginValidateResponse
```

Methods:

- <code title="post /validate_login">client.validate_login.<a href="./src/blink/resources/validate_login.py">validate</a>(\*\*<a href="src/blink/types/validate_login_validate_params.py">params</a>) -> <a href="./src/blink/types/validate_login_validate_response.py">ValidateLoginValidateResponse</a></code>

# AccessToken

Types:

```python
from blink.types import AccessTokenCreateResponse
```

Methods:

- <code title="post /access_token">client.access_token.<a href="./src/blink/resources/access_token.py">create</a>(\*\*<a href="src/blink/types/access_token_create_params.py">params</a>) -> <a href="./src/blink/types/access_token_create_response.py">AccessTokenCreateResponse</a></code>

# Users

Types:

```python
from blink.types import UserListResponse
```

Methods:

- <code title="get /users">client.users.<a href="./src/blink/resources/users.py">list</a>() -> <a href="./src/blink/types/user_list_response.py">UserListResponse</a></code>

# Links

Types:

```python
from blink.types import (
    LinkCreateResponse,
    LinkRetrieveResponse,
    LinkUpdateResponse,
    LinkListResponse,
    LinkGetByAliasResponse,
    LinkGetClickedResponse,
    LinkGetRawClicksResponse,
    LinkValidateResponse,
)
```

Methods:

- <code title="post /{domain_id}/links">client.links.<a href="./src/blink/resources/links/links.py">create</a>(domain_id, \*\*<a href="src/blink/types/link_create_params.py">params</a>) -> <a href="./src/blink/types/link_create_response.py">LinkCreateResponse</a></code>
- <code title="get /{domain_id}/links/{link_id}">client.links.<a href="./src/blink/resources/links/links.py">retrieve</a>(link_id, \*, domain_id) -> <a href="./src/blink/types/link_retrieve_response.py">LinkRetrieveResponse</a></code>
- <code title="patch /{domain_id}/links/{link_id}">client.links.<a href="./src/blink/resources/links/links.py">update</a>(link_id, \*, domain_id, \*\*<a href="src/blink/types/link_update_params.py">params</a>) -> <a href="./src/blink/types/link_update_response.py">LinkUpdateResponse</a></code>
- <code title="get /{domain_id}/links">client.links.<a href="./src/blink/resources/links/links.py">list</a>(domain_id, \*\*<a href="src/blink/types/link_list_params.py">params</a>) -> <a href="./src/blink/types/link_list_response.py">LinkListResponse</a></code>
- <code title="get /{domain_id}/links/exists?alias={alias}">client.links.<a href="./src/blink/resources/links/links.py">get_by_alias</a>(path_alias, \*, domain_id, \*\*<a href="src/blink/types/link_get_by_alias_params.py">params</a>) -> <a href="./src/blink/types/link_get_by_alias_response.py">LinkGetByAliasResponse</a></code>
- <code title="get /{domain_id}/links/clicked?tag={tag}">client.links.<a href="./src/blink/resources/links/links.py">get_clicked</a>(path_tag, \*, domain_id, \*\*<a href="src/blink/types/link_get_clicked_params.py">params</a>) -> <a href="./src/blink/types/link_get_clicked_response.py">LinkGetClickedResponse</a></code>
- <code title="get /{domain_id}/links/{link_id}/qr">client.links.<a href="./src/blink/resources/links/links.py">get_qr</a>(link_id, \*, domain_id, \*\*<a href="src/blink/types/link_get_qr_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /{domain_id}/links/{link_id}/rawclicks">client.links.<a href="./src/blink/resources/links/links.py">get_raw_clicks</a>(link_id, \*, domain_id) -> <a href="./src/blink/types/link_get_raw_clicks_response.py">LinkGetRawClicksResponse</a></code>
- <code title="post /links/validate">client.links.<a href="./src/blink/resources/links/links.py">validate</a>(\*\*<a href="src/blink/types/link_validate_params.py">params</a>) -> <a href="./src/blink/types/link_validate_response.py">LinkValidateResponse</a></code>

## Clicks

Types:

```python
from blink.types.links import (
    ClickGetByCityResponse,
    ClickGetByCountryResponse,
    ClickGetByDeviceResponse,
    ClickGetByReferrerResponse,
    ClickGetByRegionResponse,
    ClickGetDailyResponse,
    ClickGetHourlyResponse,
    ClickGetTotalResponse,
)
```

Methods:

- <code title="get /{domain_id}/links/{link_id}/clicks/city">client.links.clicks.<a href="./src/blink/resources/links/clicks.py">get_by_city</a>(link_id, \*, domain_id, \*\*<a href="src/blink/types/links/click_get_by_city_params.py">params</a>) -> <a href="./src/blink/types/links/click_get_by_city_response.py">ClickGetByCityResponse</a></code>
- <code title="get /{domain_id}/links/{link_id}/clicks/country">client.links.clicks.<a href="./src/blink/resources/links/clicks.py">get_by_country</a>(link_id, \*, domain_id, \*\*<a href="src/blink/types/links/click_get_by_country_params.py">params</a>) -> <a href="./src/blink/types/links/click_get_by_country_response.py">ClickGetByCountryResponse</a></code>
- <code title="get /{domain_id}/links/{link_id}/clicks/device">client.links.clicks.<a href="./src/blink/resources/links/clicks.py">get_by_device</a>(link_id, \*, domain_id, \*\*<a href="src/blink/types/links/click_get_by_device_params.py">params</a>) -> <a href="./src/blink/types/links/click_get_by_device_response.py">ClickGetByDeviceResponse</a></code>
- <code title="get /{domain_id}/links/{link_id}/clicks/referrer">client.links.clicks.<a href="./src/blink/resources/links/clicks.py">get_by_referrer</a>(link_id, \*, domain_id, \*\*<a href="src/blink/types/links/click_get_by_referrer_params.py">params</a>) -> <a href="./src/blink/types/links/click_get_by_referrer_response.py">ClickGetByReferrerResponse</a></code>
- <code title="get /{domain_id}/links/{link_id}/clicks/region">client.links.clicks.<a href="./src/blink/resources/links/clicks.py">get_by_region</a>(link_id, \*, domain_id, \*\*<a href="src/blink/types/links/click_get_by_region_params.py">params</a>) -> <a href="./src/blink/types/links/click_get_by_region_response.py">ClickGetByRegionResponse</a></code>
- <code title="get /{domain_id}/links/{link_id}/clicks/daily">client.links.clicks.<a href="./src/blink/resources/links/clicks.py">get_daily</a>(link_id, \*, domain_id, \*\*<a href="src/blink/types/links/click_get_daily_params.py">params</a>) -> <a href="./src/blink/types/links/click_get_daily_response.py">ClickGetDailyResponse</a></code>
- <code title="get /{domain_id}/links/{link_id}/clicks/hourly">client.links.clicks.<a href="./src/blink/resources/links/clicks.py">get_hourly</a>(link_id, \*, domain_id, \*\*<a href="src/blink/types/links/click_get_hourly_params.py">params</a>) -> <a href="./src/blink/types/links/click_get_hourly_response.py">ClickGetHourlyResponse</a></code>
- <code title="get /{domain_id}/links/{link_id}/clicks">client.links.clicks.<a href="./src/blink/resources/links/clicks.py">get_total</a>(link_id, \*, domain_id, \*\*<a href="src/blink/types/links/click_get_total_params.py">params</a>) -> <a href="./src/blink/types/links/click_get_total_response.py">ClickGetTotalResponse</a></code>

# Clicks

Types:

```python
from blink.types import (
    ClickCityCountsResponse,
    ClickCountryCountsResponse,
    ClickDailyCountsResponse,
    ClickDeviceCountsResponse,
    ClickReferrerCountsResponse,
    ClickRegionCountsResponse,
)
```

Methods:

- <code title="get /{domain_id}/clicks/city">client.clicks.<a href="./src/blink/resources/clicks.py">city_counts</a>(domain_id, \*\*<a href="src/blink/types/click_city_counts_params.py">params</a>) -> <a href="./src/blink/types/click_city_counts_response.py">ClickCityCountsResponse</a></code>
- <code title="get /{domain_id}/clicks/country">client.clicks.<a href="./src/blink/resources/clicks.py">country_counts</a>(domain_id, \*\*<a href="src/blink/types/click_country_counts_params.py">params</a>) -> <a href="./src/blink/types/click_country_counts_response.py">ClickCountryCountsResponse</a></code>
- <code title="get /{domain_id}/clicks/daily">client.clicks.<a href="./src/blink/resources/clicks.py">daily_counts</a>(domain_id, \*\*<a href="src/blink/types/click_daily_counts_params.py">params</a>) -> <a href="./src/blink/types/click_daily_counts_response.py">ClickDailyCountsResponse</a></code>
- <code title="get /{domain_id}/clicks/device">client.clicks.<a href="./src/blink/resources/clicks.py">device_counts</a>(domain_id, \*\*<a href="src/blink/types/click_device_counts_params.py">params</a>) -> <a href="./src/blink/types/click_device_counts_response.py">ClickDeviceCountsResponse</a></code>
- <code title="get /{domain_id}/clicks/referrer">client.clicks.<a href="./src/blink/resources/clicks.py">referrer_counts</a>(domain_id, \*\*<a href="src/blink/types/click_referrer_counts_params.py">params</a>) -> <a href="./src/blink/types/click_referrer_counts_response.py">ClickReferrerCountsResponse</a></code>
- <code title="get /{domain_id}/clicks/region">client.clicks.<a href="./src/blink/resources/clicks.py">region_counts</a>(domain_id, \*\*<a href="src/blink/types/click_region_counts_params.py">params</a>) -> <a href="./src/blink/types/click_region_counts_response.py">ClickRegionCountsResponse</a></code>

# Tags

Types:

```python
from blink.types import TagCreateResponse, TagListResponse
```

Methods:

- <code title="post /tags">client.tags.<a href="./src/blink/resources/tags.py">create</a>(\*\*<a href="src/blink/types/tag_create_params.py">params</a>) -> <a href="./src/blink/types/tag_create_response.py">TagCreateResponse</a></code>
- <code title="get /tags">client.tags.<a href="./src/blink/resources/tags.py">list</a>(\*\*<a href="src/blink/types/tag_list_params.py">params</a>) -> <a href="./src/blink/types/tag_list_response.py">TagListResponse</a></code>

# Domains

Types:

```python
from blink.types import Domain, DomainDeleteResponse
```

Methods:

- <code title="post /domains">client.domains.<a href="./src/blink/resources/domains.py">create</a>(\*\*<a href="src/blink/types/domain_create_params.py">params</a>) -> <a href="./src/blink/types/domain.py">Domain</a></code>
- <code title="get /domains/{domain_id}">client.domains.<a href="./src/blink/resources/domains.py">retrieve</a>(domain_id) -> <a href="./src/blink/types/domain.py">Domain</a></code>
- <code title="patch /domains/{domain_id}">client.domains.<a href="./src/blink/resources/domains.py">update</a>(domain_id, \*\*<a href="src/blink/types/domain_update_params.py">params</a>) -> <a href="./src/blink/types/domain.py">Domain</a></code>
- <code title="get /domains">client.domains.<a href="./src/blink/resources/domains.py">list</a>(\*\*<a href="src/blink/types/domain_list_params.py">params</a>) -> <a href="./src/blink/types/domain.py">Domain</a></code>
- <code title="delete /domains/{domain_id}">client.domains.<a href="./src/blink/resources/domains.py">delete</a>(domain_id) -> <a href="./src/blink/types/domain_delete_response.py">DomainDeleteResponse</a></code>

# DomainsDomainName

Methods:

- <code title="get /domains?domain_name={domain_name}">client.domains_domain_name.<a href="./src/blink/resources/domains_domain_name.py">list</a>(path_domain_name, \*\*<a href="src/blink/types/domains_domain_name_list_params.py">params</a>) -> <a href="./src/blink/types/domain.py">Domain</a></code>

# UtmTemplates

Types:

```python
from blink.types import UtmTemplateListResponse
```

Methods:

- <code title="get /utm_templates">client.utm_templates.<a href="./src/blink/resources/utm_templates.py">list</a>(\*\*<a href="src/blink/types/utm_template_list_params.py">params</a>) -> <a href="./src/blink/types/utm_template_list_response.py">UtmTemplateListResponse</a></code>

# Groups

Types:

```python
from blink.types import GroupListResponse
```

Methods:

- <code title="get /groups">client.groups.<a href="./src/blink/resources/groups.py">list</a>(\*\*<a href="src/blink/types/group_list_params.py">params</a>) -> <a href="./src/blink/types/group_list_response.py">GroupListResponse</a></code>

# ErrorCodes

Types:

```python
from blink.types import ErrorCodeListResponse
```

Methods:

- <code title="get /error_codes">client.error_codes.<a href="./src/blink/resources/error_codes.py">list</a>() -> <a href="./src/blink/types/error_code_list_response.py">ErrorCodeListResponse</a></code>

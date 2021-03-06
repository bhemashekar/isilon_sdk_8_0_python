# isi_sdk.ProtocolsHdfsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_proxyusers_name_member**](ProtocolsHdfsApi.md#create_proxyusers_name_member) | **POST** /platform/1/protocols/hdfs/proxyusers/{Name}/members | 
[**delete_proxyusers_name_member**](ProtocolsHdfsApi.md#delete_proxyusers_name_member) | **DELETE** /platform/1/protocols/hdfs/proxyusers/{Name}/members/{ProxyusersNameMemberId} | 
[**list_proxyusers_name_members**](ProtocolsHdfsApi.md#list_proxyusers_name_members) | **GET** /platform/1/protocols/hdfs/proxyusers/{Name}/members | 
[**update_proxyusers_name_member**](ProtocolsHdfsApi.md#update_proxyusers_name_member) | **PUT** /platform/1/protocols/hdfs/proxyusers/{Name}/members/{ProxyusersNameMemberId} | 


# **create_proxyusers_name_member**
> CreateResponse create_proxyusers_name_member(proxyusers_name_member, name)



Add a member to the HDFS proxyuser.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ProtocolsHdfsApi()
proxyusers_name_member = isi_sdk.GroupMember() # GroupMember | 
name = 'name_example' # str | 

try: 
    api_response = api_instance.create_proxyusers_name_member(proxyusers_name_member, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtocolsHdfsApi->create_proxyusers_name_member: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proxyusers_name_member** | [**GroupMember**](GroupMember.md)|  | 
 **name** | **str**|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_proxyusers_name_member**
> delete_proxyusers_name_member(proxyusers_name_member_id, name)



Remove a member from the HDFS proxyuser.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ProtocolsHdfsApi()
proxyusers_name_member_id = 'proxyusers_name_member_id_example' # str | Remove a member from the HDFS proxyuser.
name = 'name_example' # str | 

try: 
    api_instance.delete_proxyusers_name_member(proxyusers_name_member_id, name)
except ApiException as e:
    print "Exception when calling ProtocolsHdfsApi->delete_proxyusers_name_member: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proxyusers_name_member_id** | **str**| Remove a member from the HDFS proxyuser. | 
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_proxyusers_name_members**
> GroupMembers list_proxyusers_name_members(name)



List all the members of the HDFS proxyuser.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ProtocolsHdfsApi()
name = 'name_example' # str | 

try: 
    api_response = api_instance.list_proxyusers_name_members(name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProtocolsHdfsApi->list_proxyusers_name_members: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**GroupMembers**](GroupMembers.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_proxyusers_name_member**
> update_proxyusers_name_member(proxyusers_name_member, proxyusers_name_member_id, name)



Create a new HDFS proxyuser.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ProtocolsHdfsApi()
proxyusers_name_member = isi_sdk.Empty() # Empty | 
proxyusers_name_member_id = 'proxyusers_name_member_id_example' # str | Create a new HDFS proxyuser.
name = 'name_example' # str | 

try: 
    api_instance.update_proxyusers_name_member(proxyusers_name_member, proxyusers_name_member_id, name)
except ApiException as e:
    print "Exception when calling ProtocolsHdfsApi->update_proxyusers_name_member: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proxyusers_name_member** | [**Empty**](Empty.md)|  | 
 **proxyusers_name_member_id** | **str**| Create a new HDFS proxyuser. | 
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


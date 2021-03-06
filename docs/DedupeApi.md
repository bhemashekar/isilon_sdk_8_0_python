# isi_sdk.DedupeApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dedupe_dedupe_summary**](DedupeApi.md#get_dedupe_dedupe_summary) | **GET** /platform/1/dedupe/dedupe-summary | 
[**get_dedupe_report**](DedupeApi.md#get_dedupe_report) | **GET** /platform/1/dedupe/reports/{DedupeReportId} | 
[**get_dedupe_reports**](DedupeApi.md#get_dedupe_reports) | **GET** /platform/1/dedupe/reports | 
[**get_dedupe_settings**](DedupeApi.md#get_dedupe_settings) | **GET** /platform/1/dedupe/settings | 
[**update_dedupe_settings**](DedupeApi.md#update_dedupe_settings) | **PUT** /platform/1/dedupe/settings | 


# **get_dedupe_dedupe_summary**
> DedupeDedupeSummary get_dedupe_dedupe_summary()



Return summary information about dedupe.

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
api_instance = isi_sdk.DedupeApi()

try: 
    api_response = api_instance.get_dedupe_dedupe_summary()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DedupeApi->get_dedupe_dedupe_summary: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DedupeDedupeSummary**](DedupeDedupeSummary.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dedupe_report**
> DedupeReports get_dedupe_report(dedupe_report_id, scope=scope)



Retrieve a report for a single dedupe job.

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
api_instance = isi_sdk.DedupeApi()
dedupe_report_id = 'dedupe_report_id_example' # str | Retrieve a report for a single dedupe job.
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)

try: 
    api_response = api_instance.get_dedupe_report(dedupe_report_id, scope=scope)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DedupeApi->get_dedupe_report: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dedupe_report_id** | **str**| Retrieve a report for a single dedupe job. | 
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 

### Return type

[**DedupeReports**](DedupeReports.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dedupe_reports**
> DedupeReportsExtended get_dedupe_reports(sort=sort, begin=begin, end=end, job_id=job_id, resume=resume, job_type=job_type, limit=limit, dir=dir)



List dedupe reports.

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
api_instance = isi_sdk.DedupeApi()
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
begin = 56 # int | Restrict the query to reports at or after the given time, in seconds since the Epoch. (optional)
end = 56 # int | Restrict the query to reports at or before the given time, in seconds since the Epoch. (optional)
job_id = 56 # int | Restrict the query to the given job ID. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
job_type = 'job_type_example' # str | Restrict the query to the given job type. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try: 
    api_response = api_instance.get_dedupe_reports(sort=sort, begin=begin, end=end, job_id=job_id, resume=resume, job_type=job_type, limit=limit, dir=dir)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DedupeApi->get_dedupe_reports: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **begin** | **int**| Restrict the query to reports at or after the given time, in seconds since the Epoch. | [optional] 
 **end** | **int**| Restrict the query to reports at or before the given time, in seconds since the Epoch. | [optional] 
 **job_id** | **int**| Restrict the query to the given job ID. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **job_type** | **str**| Restrict the query to the given job type. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**DedupeReportsExtended**](DedupeReportsExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dedupe_settings**
> DedupeSettings get_dedupe_settings()



Retrieve the dedupe settings.

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
api_instance = isi_sdk.DedupeApi()

try: 
    api_response = api_instance.get_dedupe_settings()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DedupeApi->get_dedupe_settings: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DedupeSettings**](DedupeSettings.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dedupe_settings**
> update_dedupe_settings(dedupe_settings)



Modify the dedupe settings. All input fields are optional, but one or more must be supplied.

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
api_instance = isi_sdk.DedupeApi()
dedupe_settings = isi_sdk.DedupeSettingsExtended() # DedupeSettingsExtended | 

try: 
    api_instance.update_dedupe_settings(dedupe_settings)
except ApiException as e:
    print "Exception when calling DedupeApi->update_dedupe_settings: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dedupe_settings** | [**DedupeSettingsExtended**](DedupeSettingsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


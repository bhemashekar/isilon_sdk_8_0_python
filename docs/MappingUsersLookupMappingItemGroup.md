# MappingUsersLookupMappingItemGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dn** | **str** | Specifies the distinguished name for the user. | 
**dns_domain** | **str** | Specifies the DNS domain. | 
**domain** | **str** | Specifies the domain that the object is part of. | 
**email** | **str** | Specifies an email address. | [optional] 
**enabled** | **bool** | If true, the authenticated user is enabled. | [optional] 
**expired** | **bool** | If true, the authenticated auth user is expired. | [optional] 
**expiry** | **int** | Specifies the Epoch time at which the authenticated user will expire. | [optional] 
**gecos** | **str** | Specifies the GECOS value, which is usually the full name. | [optional] 
**generated_gid** | **bool** | If true, indicates that the GID was generated. | [optional] 
**generated_uid** | **bool** | If true, indicates that the UID was generated. | [optional] 
**generated_upn** | **bool** | If true, indicates that the UPN was generated. | [optional] 
**gid** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**home_directory** | **str** | Specifies the home directory for the user. | [optional] 
**id** | **str** | Specifies the user or group ID. | 
**locked** | **bool** | If true, the account is locked out. | [optional] 
**max_password_age** | **int** | Specifies the maximum time in seconds allowed before the password expires. | [optional] 
**member_of** | [**list[GroupMember]**](GroupMember.md) |  | 
**name** | **str** | Specifies a user or group name. | 
**on_disk_group_identity** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**on_disk_user_identity** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**password_expired** | **bool** | If true, the password has expired. | [optional] 
**password_expires** | **bool** | If true, the password is allowed to expire. | [optional] 
**password_expiry** | **int** | Specifies the time in Epoch seconds the password will expire. | [optional] 
**password_last_set** | **int** | Specifies the last time the password was set. | [optional] 
**primary_group_sid** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**prompt_password_change** | **bool** | If true, prompts the user to change their password on next login. | [optional] 
**provider** | **str** | Specifies the authentication provider that the object belongs to. | 
**sam_account_name** | **str** | Specifies a user or group name. | 
**shell** | **str** | Specifies the path to the shell for the user. | [optional] 
**sid** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | 
**type** | **str** | Specifies the object type. | 
**uid** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**upn** | **str** | Specifies the user principal name. | [optional] 
**user_can_change_password** | **bool** | If true, the user password can be changed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1

from __future__ import absolute_import

from .addresses import Addresses
from .api_key import ApiKey
from .api_key_search_request import ApiKeySearchRequest
from .api_key_user import ApiKeyUser
from .api_keys import ApiKeys
from .auth_token import AuthToken
from .auth_token_search_request import AuthTokenSearchRequest
from .auth_token_user import AuthTokenUser
from .auth_tokens import AuthTokens
from .authentication_factor_setting import AuthenticationFactorSetting
from .authentication_factor_settings import AuthenticationFactorSettings
from .authentication_factor_settings_bypass_code_settings import AuthenticationFactorSettingsBypassCodeSettings
from .authentication_factor_settings_client_app_settings import AuthenticationFactorSettingsClientAppSettings
from .authentication_factor_settings_compliance_policy import AuthenticationFactorSettingsCompliancePolicy
from .authentication_factor_settings_duo_security_settings import AuthenticationFactorSettingsDuoSecuritySettings
from .authentication_factor_settings_email_settings import AuthenticationFactorSettingsEmailSettings
from .authentication_factor_settings_endpoint_restrictions import AuthenticationFactorSettingsEndpointRestrictions
from .authentication_factor_settings_identity_store_settings import AuthenticationFactorSettingsIdentityStoreSettings
from .authentication_factor_settings_notification_settings import AuthenticationFactorSettingsNotificationSettings
from .authentication_factor_settings_search_request import AuthenticationFactorSettingsSearchRequest
from .authentication_factor_settings_third_party_factor import AuthenticationFactorSettingsThirdPartyFactor
from .authentication_factor_settings_totp_settings import AuthenticationFactorSettingsTotpSettings
from .authentication_factors_remover import AuthenticationFactorsRemover
from .authentication_factors_remover_user import AuthenticationFactorsRemoverUser
from .customer_secret_key import CustomerSecretKey
from .customer_secret_key_search_request import CustomerSecretKeySearchRequest
from .customer_secret_key_user import CustomerSecretKeyUser
from .customer_secret_keys import CustomerSecretKeys
from .defined_tags import DefinedTags
from .dynamic_resource_group import DynamicResourceGroup
from .dynamic_resource_group_dynamic_group_app_roles import DynamicResourceGroupDynamicGroupAppRoles
from .dynamic_resource_group_grants import DynamicResourceGroupGrants
from .dynamic_resource_group_search_request import DynamicResourceGroupSearchRequest
from .dynamic_resource_groups import DynamicResourceGroups
from .extension_adaptive_user import ExtensionAdaptiveUser
from .extension_capabilities_user import ExtensionCapabilitiesUser
from .extension_db_credentials_user import ExtensionDbCredentialsUser
from .extension_db_user_user import ExtensionDbUserUser
from .extension_dbcs_group import ExtensionDbcsGroup
from .extension_dynamic_group import ExtensionDynamicGroup
from .extension_enterprise20_user import ExtensionEnterprise20User
from .extension_fido_authentication_factor_settings import ExtensionFidoAuthenticationFactorSettings
from .extension_group_group import ExtensionGroupGroup
from .extension_kerberos_user_user import ExtensionKerberosUserUser
from .extension_me_user import ExtensionMeUser
from .extension_messages_error import ExtensionMessagesError
from .extension_mfa_user import ExtensionMfaUser
from .extension_oci_tags import ExtensionOCITags
from .extension_password_state_user import ExtensionPasswordStateUser
from .extension_passwordless_user import ExtensionPasswordlessUser
from .extension_posix_group import ExtensionPosixGroup
from .extension_posix_user import ExtensionPosixUser
from .extension_requestable_group import ExtensionRequestableGroup
from .extension_security_questions_user import ExtensionSecurityQuestionsUser
from .extension_self_change_user import ExtensionSelfChangeUser
from .extension_self_registration_user import ExtensionSelfRegistrationUser
from .extension_sff_user import ExtensionSffUser
from .extension_social_account_user import ExtensionSocialAccountUser
from .extension_social_identity_provider import ExtensionSocialIdentityProvider
from .extension_terms_of_use_user import ExtensionTermsOfUseUser
from .extension_third_party_authentication_factor_settings import ExtensionThirdPartyAuthenticationFactorSettings
from .extension_user_credentials_user import ExtensionUserCredentialsUser
from .extension_user_state_user import ExtensionUserStateUser
from .extension_user_user import ExtensionUserUser
from .extension_x509_identity_provider import ExtensionX509IdentityProvider
from .freeform_tags import FreeformTags
from .group import Group
from .group_ext_app_roles import GroupExtAppRoles
from .group_ext_domain_level_schema_names import GroupExtDomainLevelSchemaNames
from .group_ext_grants import GroupExtGrants
from .group_ext_instance_level_schema_names import GroupExtInstanceLevelSchemaNames
from .group_ext_owners import GroupExtOwners
from .group_ext_password_policy import GroupExtPasswordPolicy
from .group_ext_synced_from_app import GroupExtSyncedFromApp
from .group_members import GroupMembers
from .group_search_request import GroupSearchRequest
from .groups import Groups
from .idcs_created_by import IdcsCreatedBy
from .idcs_last_modified_by import IdcsLastModifiedBy
from .identity_provider import IdentityProvider
from .identity_provider_correlation_policy import IdentityProviderCorrelationPolicy
from .identity_provider_jit_user_prov_assigned_groups import IdentityProviderJitUserProvAssignedGroups
from .identity_provider_jit_user_prov_attributes import IdentityProviderJitUserProvAttributes
from .identity_provider_jit_user_prov_group_mappings import IdentityProviderJitUserProvGroupMappings
from .identity_provider_search_request import IdentityProviderSearchRequest
from .identity_providers import IdentityProviders
from .kmsi_setting import KmsiSetting
from .kmsi_settings import KmsiSettings
from .kmsi_settings_search_request import KmsiSettingsSearchRequest
from .me import Me
from .me_emails import MeEmails
from .me_entitlements import MeEntitlements
from .me_groups import MeGroups
from .me_ims import MeIms
from .me_name import MeName
from .me_password_changer import MePasswordChanger
from .me_phone_numbers import MePhoneNumbers
from .me_photos import MePhotos
from .me_roles import MeRoles
from .me_x509_certificates import MeX509Certificates
from .meta import Meta
from .my_api_key import MyApiKey
from .my_api_key_user import MyApiKeyUser
from .my_api_keys import MyApiKeys
from .my_auth_token import MyAuthToken
from .my_auth_token_user import MyAuthTokenUser
from .my_auth_tokens import MyAuthTokens
from .my_authentication_factor_initiator import MyAuthenticationFactorInitiator
from .my_authentication_factor_initiator_additional_attributes import MyAuthenticationFactorInitiatorAdditionalAttributes
from .my_authentication_factor_initiator_third_party_factor import MyAuthenticationFactorInitiatorThirdPartyFactor
from .my_authentication_factor_validator import MyAuthenticationFactorValidator
from .my_authentication_factor_validator_additional_attributes import MyAuthenticationFactorValidatorAdditionalAttributes
from .my_authentication_factor_validator_security_questions import MyAuthenticationFactorValidatorSecurityQuestions
from .my_authentication_factor_validator_third_party_factor import MyAuthenticationFactorValidatorThirdPartyFactor
from .my_authentication_factors_remover import MyAuthenticationFactorsRemover
from .my_authentication_factors_remover_user import MyAuthenticationFactorsRemoverUser
from .my_customer_secret_key import MyCustomerSecretKey
from .my_customer_secret_key_user import MyCustomerSecretKeyUser
from .my_customer_secret_keys import MyCustomerSecretKeys
from .my_device import MyDevice
from .my_device_additional_attributes import MyDeviceAdditionalAttributes
from .my_device_authentication_factors import MyDeviceAuthenticationFactors
from .my_device_non_compliances import MyDeviceNonCompliances
from .my_device_push_notification_target import MyDevicePushNotificationTarget
from .my_device_third_party_factor import MyDeviceThirdPartyFactor
from .my_device_user import MyDeviceUser
from .my_devices import MyDevices
from .my_group import MyGroup
from .my_group_members import MyGroupMembers
from .my_group_search_request import MyGroupSearchRequest
from .my_groups import MyGroups
from .my_o_auth2_client_credential import MyOAuth2ClientCredential
from .my_o_auth2_client_credential_scopes import MyOAuth2ClientCredentialScopes
from .my_o_auth2_client_credential_user import MyOAuth2ClientCredentialUser
from .my_o_auth2_client_credentials import MyOAuth2ClientCredentials
from .my_smtp_credential import MySmtpCredential
from .my_smtp_credential_user import MySmtpCredentialUser
from .my_smtp_credentials import MySmtpCredentials
from .my_support_account import MySupportAccount
from .my_support_account_user import MySupportAccountUser
from .my_support_accounts import MySupportAccounts
from .my_trusted_user_agent import MyTrustedUserAgent
from .my_trusted_user_agent_trusted_factors import MyTrustedUserAgentTrustedFactors
from .my_trusted_user_agent_user import MyTrustedUserAgentUser
from .my_trusted_user_agents import MyTrustedUserAgents
from .my_user_db_credential import MyUserDbCredential
from .my_user_db_credentials import MyUserDbCredentials
from .my_user_db_credentials_user import MyUserDbCredentialsUser
from .o_auth2_client_credential import OAuth2ClientCredential
from .o_auth2_client_credential_scopes import OAuth2ClientCredentialScopes
from .o_auth2_client_credential_search_request import OAuth2ClientCredentialSearchRequest
from .o_auth2_client_credential_user import OAuth2ClientCredentialUser
from .o_auth2_client_credentials import OAuth2ClientCredentials
from .operations import Operations
from .password_policies import PasswordPolicies
from .password_policy import PasswordPolicy
from .password_policy_configured_password_policy_rules import PasswordPolicyConfiguredPasswordPolicyRules
from .password_policy_groups import PasswordPolicyGroups
from .password_policy_search_request import PasswordPolicySearchRequest
from .patch_op import PatchOp
from .smtp_credential import SmtpCredential
from .smtp_credential_search_request import SmtpCredentialSearchRequest
from .smtp_credential_user import SmtpCredentialUser
from .smtp_credentials import SmtpCredentials
from .tags import Tags
from .user import User
from .user_capabilities_changer import UserCapabilitiesChanger
from .user_db_credential import UserDbCredential
from .user_db_credentials import UserDbCredentials
from .user_db_credentials_search_request import UserDbCredentialsSearchRequest
from .user_db_credentials_user import UserDbCredentialsUser
from .user_emails import UserEmails
from .user_entitlements import UserEntitlements
from .user_ext_accounts import UserExtAccounts
from .user_ext_api_keys import UserExtApiKeys
from .user_ext_app_roles import UserExtAppRoles
from .user_ext_applicable_authentication_target_app import UserExtApplicableAuthenticationTargetApp
from .user_ext_applicable_password_policy import UserExtApplicablePasswordPolicy
from .user_ext_auth_tokens import UserExtAuthTokens
from .user_ext_bypass_codes import UserExtBypassCodes
from .user_ext_customer_secret_keys import UserExtCustomerSecretKeys
from .user_ext_db_credentials import UserExtDbCredentials
from .user_ext_delegated_authentication_target_app import UserExtDelegatedAuthenticationTargetApp
from .user_ext_devices import UserExtDevices
from .user_ext_factor_identifier import UserExtFactorIdentifier
from .user_ext_grants import UserExtGrants
from .user_ext_idcs_app_roles_limited_to_groups import UserExtIdcsAppRolesLimitedToGroups
from .user_ext_locked import UserExtLocked
from .user_ext_manager import UserExtManager
from .user_ext_o_auth2_client_credentials import UserExtOAuth2ClientCredentials
from .user_ext_password_verifiers import UserExtPasswordVerifiers
from .user_ext_preferred_device import UserExtPreferredDevice
from .user_ext_realm_users import UserExtRealmUsers
from .user_ext_recovery_locked import UserExtRecoveryLocked
from .user_ext_risk_scores import UserExtRiskScores
from .user_ext_sec_questions import UserExtSecQuestions
from .user_ext_self_registration_profile import UserExtSelfRegistrationProfile
from .user_ext_smtp_credentials import UserExtSmtpCredentials
from .user_ext_social_accounts import UserExtSocialAccounts
from .user_ext_support_accounts import UserExtSupportAccounts
from .user_ext_synced_from_app import UserExtSyncedFromApp
from .user_ext_terms_of_use_consents import UserExtTermsOfUseConsents
from .user_ext_trusted_user_agents import UserExtTrustedUserAgents
from .user_ext_user_token import UserExtUserToken
from .user_groups import UserGroups
from .user_ims import UserIms
from .user_name import UserName
from .user_password_changer import UserPasswordChanger
from .user_password_resetter import UserPasswordResetter
from .user_password_resetter_user_token import UserPasswordResetterUserToken
from .user_phone_numbers import UserPhoneNumbers
from .user_photos import UserPhotos
from .user_roles import UserRoles
from .user_search_request import UserSearchRequest
from .user_status_changer import UserStatusChanger
from .user_x509_certificates import UserX509Certificates
from .users import Users

# Maps type names to classes for identity_domains services.
identity_domains_type_mapping = {
    "Addresses": Addresses,
    "ApiKey": ApiKey,
    "ApiKeySearchRequest": ApiKeySearchRequest,
    "ApiKeyUser": ApiKeyUser,
    "ApiKeys": ApiKeys,
    "AuthToken": AuthToken,
    "AuthTokenSearchRequest": AuthTokenSearchRequest,
    "AuthTokenUser": AuthTokenUser,
    "AuthTokens": AuthTokens,
    "AuthenticationFactorSetting": AuthenticationFactorSetting,
    "AuthenticationFactorSettings": AuthenticationFactorSettings,
    "AuthenticationFactorSettingsBypassCodeSettings": AuthenticationFactorSettingsBypassCodeSettings,
    "AuthenticationFactorSettingsClientAppSettings": AuthenticationFactorSettingsClientAppSettings,
    "AuthenticationFactorSettingsCompliancePolicy": AuthenticationFactorSettingsCompliancePolicy,
    "AuthenticationFactorSettingsDuoSecuritySettings": AuthenticationFactorSettingsDuoSecuritySettings,
    "AuthenticationFactorSettingsEmailSettings": AuthenticationFactorSettingsEmailSettings,
    "AuthenticationFactorSettingsEndpointRestrictions": AuthenticationFactorSettingsEndpointRestrictions,
    "AuthenticationFactorSettingsIdentityStoreSettings": AuthenticationFactorSettingsIdentityStoreSettings,
    "AuthenticationFactorSettingsNotificationSettings": AuthenticationFactorSettingsNotificationSettings,
    "AuthenticationFactorSettingsSearchRequest": AuthenticationFactorSettingsSearchRequest,
    "AuthenticationFactorSettingsThirdPartyFactor": AuthenticationFactorSettingsThirdPartyFactor,
    "AuthenticationFactorSettingsTotpSettings": AuthenticationFactorSettingsTotpSettings,
    "AuthenticationFactorsRemover": AuthenticationFactorsRemover,
    "AuthenticationFactorsRemoverUser": AuthenticationFactorsRemoverUser,
    "CustomerSecretKey": CustomerSecretKey,
    "CustomerSecretKeySearchRequest": CustomerSecretKeySearchRequest,
    "CustomerSecretKeyUser": CustomerSecretKeyUser,
    "CustomerSecretKeys": CustomerSecretKeys,
    "DefinedTags": DefinedTags,
    "DynamicResourceGroup": DynamicResourceGroup,
    "DynamicResourceGroupDynamicGroupAppRoles": DynamicResourceGroupDynamicGroupAppRoles,
    "DynamicResourceGroupGrants": DynamicResourceGroupGrants,
    "DynamicResourceGroupSearchRequest": DynamicResourceGroupSearchRequest,
    "DynamicResourceGroups": DynamicResourceGroups,
    "ExtensionAdaptiveUser": ExtensionAdaptiveUser,
    "ExtensionCapabilitiesUser": ExtensionCapabilitiesUser,
    "ExtensionDbCredentialsUser": ExtensionDbCredentialsUser,
    "ExtensionDbUserUser": ExtensionDbUserUser,
    "ExtensionDbcsGroup": ExtensionDbcsGroup,
    "ExtensionDynamicGroup": ExtensionDynamicGroup,
    "ExtensionEnterprise20User": ExtensionEnterprise20User,
    "ExtensionFidoAuthenticationFactorSettings": ExtensionFidoAuthenticationFactorSettings,
    "ExtensionGroupGroup": ExtensionGroupGroup,
    "ExtensionKerberosUserUser": ExtensionKerberosUserUser,
    "ExtensionMeUser": ExtensionMeUser,
    "ExtensionMessagesError": ExtensionMessagesError,
    "ExtensionMfaUser": ExtensionMfaUser,
    "ExtensionOCITags": ExtensionOCITags,
    "ExtensionPasswordStateUser": ExtensionPasswordStateUser,
    "ExtensionPasswordlessUser": ExtensionPasswordlessUser,
    "ExtensionPosixGroup": ExtensionPosixGroup,
    "ExtensionPosixUser": ExtensionPosixUser,
    "ExtensionRequestableGroup": ExtensionRequestableGroup,
    "ExtensionSecurityQuestionsUser": ExtensionSecurityQuestionsUser,
    "ExtensionSelfChangeUser": ExtensionSelfChangeUser,
    "ExtensionSelfRegistrationUser": ExtensionSelfRegistrationUser,
    "ExtensionSffUser": ExtensionSffUser,
    "ExtensionSocialAccountUser": ExtensionSocialAccountUser,
    "ExtensionSocialIdentityProvider": ExtensionSocialIdentityProvider,
    "ExtensionTermsOfUseUser": ExtensionTermsOfUseUser,
    "ExtensionThirdPartyAuthenticationFactorSettings": ExtensionThirdPartyAuthenticationFactorSettings,
    "ExtensionUserCredentialsUser": ExtensionUserCredentialsUser,
    "ExtensionUserStateUser": ExtensionUserStateUser,
    "ExtensionUserUser": ExtensionUserUser,
    "ExtensionX509IdentityProvider": ExtensionX509IdentityProvider,
    "FreeformTags": FreeformTags,
    "Group": Group,
    "GroupExtAppRoles": GroupExtAppRoles,
    "GroupExtDomainLevelSchemaNames": GroupExtDomainLevelSchemaNames,
    "GroupExtGrants": GroupExtGrants,
    "GroupExtInstanceLevelSchemaNames": GroupExtInstanceLevelSchemaNames,
    "GroupExtOwners": GroupExtOwners,
    "GroupExtPasswordPolicy": GroupExtPasswordPolicy,
    "GroupExtSyncedFromApp": GroupExtSyncedFromApp,
    "GroupMembers": GroupMembers,
    "GroupSearchRequest": GroupSearchRequest,
    "Groups": Groups,
    "IdcsCreatedBy": IdcsCreatedBy,
    "IdcsLastModifiedBy": IdcsLastModifiedBy,
    "IdentityProvider": IdentityProvider,
    "IdentityProviderCorrelationPolicy": IdentityProviderCorrelationPolicy,
    "IdentityProviderJitUserProvAssignedGroups": IdentityProviderJitUserProvAssignedGroups,
    "IdentityProviderJitUserProvAttributes": IdentityProviderJitUserProvAttributes,
    "IdentityProviderJitUserProvGroupMappings": IdentityProviderJitUserProvGroupMappings,
    "IdentityProviderSearchRequest": IdentityProviderSearchRequest,
    "IdentityProviders": IdentityProviders,
    "KmsiSetting": KmsiSetting,
    "KmsiSettings": KmsiSettings,
    "KmsiSettingsSearchRequest": KmsiSettingsSearchRequest,
    "Me": Me,
    "MeEmails": MeEmails,
    "MeEntitlements": MeEntitlements,
    "MeGroups": MeGroups,
    "MeIms": MeIms,
    "MeName": MeName,
    "MePasswordChanger": MePasswordChanger,
    "MePhoneNumbers": MePhoneNumbers,
    "MePhotos": MePhotos,
    "MeRoles": MeRoles,
    "MeX509Certificates": MeX509Certificates,
    "Meta": Meta,
    "MyApiKey": MyApiKey,
    "MyApiKeyUser": MyApiKeyUser,
    "MyApiKeys": MyApiKeys,
    "MyAuthToken": MyAuthToken,
    "MyAuthTokenUser": MyAuthTokenUser,
    "MyAuthTokens": MyAuthTokens,
    "MyAuthenticationFactorInitiator": MyAuthenticationFactorInitiator,
    "MyAuthenticationFactorInitiatorAdditionalAttributes": MyAuthenticationFactorInitiatorAdditionalAttributes,
    "MyAuthenticationFactorInitiatorThirdPartyFactor": MyAuthenticationFactorInitiatorThirdPartyFactor,
    "MyAuthenticationFactorValidator": MyAuthenticationFactorValidator,
    "MyAuthenticationFactorValidatorAdditionalAttributes": MyAuthenticationFactorValidatorAdditionalAttributes,
    "MyAuthenticationFactorValidatorSecurityQuestions": MyAuthenticationFactorValidatorSecurityQuestions,
    "MyAuthenticationFactorValidatorThirdPartyFactor": MyAuthenticationFactorValidatorThirdPartyFactor,
    "MyAuthenticationFactorsRemover": MyAuthenticationFactorsRemover,
    "MyAuthenticationFactorsRemoverUser": MyAuthenticationFactorsRemoverUser,
    "MyCustomerSecretKey": MyCustomerSecretKey,
    "MyCustomerSecretKeyUser": MyCustomerSecretKeyUser,
    "MyCustomerSecretKeys": MyCustomerSecretKeys,
    "MyDevice": MyDevice,
    "MyDeviceAdditionalAttributes": MyDeviceAdditionalAttributes,
    "MyDeviceAuthenticationFactors": MyDeviceAuthenticationFactors,
    "MyDeviceNonCompliances": MyDeviceNonCompliances,
    "MyDevicePushNotificationTarget": MyDevicePushNotificationTarget,
    "MyDeviceThirdPartyFactor": MyDeviceThirdPartyFactor,
    "MyDeviceUser": MyDeviceUser,
    "MyDevices": MyDevices,
    "MyGroup": MyGroup,
    "MyGroupMembers": MyGroupMembers,
    "MyGroupSearchRequest": MyGroupSearchRequest,
    "MyGroups": MyGroups,
    "MyOAuth2ClientCredential": MyOAuth2ClientCredential,
    "MyOAuth2ClientCredentialScopes": MyOAuth2ClientCredentialScopes,
    "MyOAuth2ClientCredentialUser": MyOAuth2ClientCredentialUser,
    "MyOAuth2ClientCredentials": MyOAuth2ClientCredentials,
    "MySmtpCredential": MySmtpCredential,
    "MySmtpCredentialUser": MySmtpCredentialUser,
    "MySmtpCredentials": MySmtpCredentials,
    "MySupportAccount": MySupportAccount,
    "MySupportAccountUser": MySupportAccountUser,
    "MySupportAccounts": MySupportAccounts,
    "MyTrustedUserAgent": MyTrustedUserAgent,
    "MyTrustedUserAgentTrustedFactors": MyTrustedUserAgentTrustedFactors,
    "MyTrustedUserAgentUser": MyTrustedUserAgentUser,
    "MyTrustedUserAgents": MyTrustedUserAgents,
    "MyUserDbCredential": MyUserDbCredential,
    "MyUserDbCredentials": MyUserDbCredentials,
    "MyUserDbCredentialsUser": MyUserDbCredentialsUser,
    "OAuth2ClientCredential": OAuth2ClientCredential,
    "OAuth2ClientCredentialScopes": OAuth2ClientCredentialScopes,
    "OAuth2ClientCredentialSearchRequest": OAuth2ClientCredentialSearchRequest,
    "OAuth2ClientCredentialUser": OAuth2ClientCredentialUser,
    "OAuth2ClientCredentials": OAuth2ClientCredentials,
    "Operations": Operations,
    "PasswordPolicies": PasswordPolicies,
    "PasswordPolicy": PasswordPolicy,
    "PasswordPolicyConfiguredPasswordPolicyRules": PasswordPolicyConfiguredPasswordPolicyRules,
    "PasswordPolicyGroups": PasswordPolicyGroups,
    "PasswordPolicySearchRequest": PasswordPolicySearchRequest,
    "PatchOp": PatchOp,
    "SmtpCredential": SmtpCredential,
    "SmtpCredentialSearchRequest": SmtpCredentialSearchRequest,
    "SmtpCredentialUser": SmtpCredentialUser,
    "SmtpCredentials": SmtpCredentials,
    "Tags": Tags,
    "User": User,
    "UserCapabilitiesChanger": UserCapabilitiesChanger,
    "UserDbCredential": UserDbCredential,
    "UserDbCredentials": UserDbCredentials,
    "UserDbCredentialsSearchRequest": UserDbCredentialsSearchRequest,
    "UserDbCredentialsUser": UserDbCredentialsUser,
    "UserEmails": UserEmails,
    "UserEntitlements": UserEntitlements,
    "UserExtAccounts": UserExtAccounts,
    "UserExtApiKeys": UserExtApiKeys,
    "UserExtAppRoles": UserExtAppRoles,
    "UserExtApplicableAuthenticationTargetApp": UserExtApplicableAuthenticationTargetApp,
    "UserExtApplicablePasswordPolicy": UserExtApplicablePasswordPolicy,
    "UserExtAuthTokens": UserExtAuthTokens,
    "UserExtBypassCodes": UserExtBypassCodes,
    "UserExtCustomerSecretKeys": UserExtCustomerSecretKeys,
    "UserExtDbCredentials": UserExtDbCredentials,
    "UserExtDelegatedAuthenticationTargetApp": UserExtDelegatedAuthenticationTargetApp,
    "UserExtDevices": UserExtDevices,
    "UserExtFactorIdentifier": UserExtFactorIdentifier,
    "UserExtGrants": UserExtGrants,
    "UserExtIdcsAppRolesLimitedToGroups": UserExtIdcsAppRolesLimitedToGroups,
    "UserExtLocked": UserExtLocked,
    "UserExtManager": UserExtManager,
    "UserExtOAuth2ClientCredentials": UserExtOAuth2ClientCredentials,
    "UserExtPasswordVerifiers": UserExtPasswordVerifiers,
    "UserExtPreferredDevice": UserExtPreferredDevice,
    "UserExtRealmUsers": UserExtRealmUsers,
    "UserExtRecoveryLocked": UserExtRecoveryLocked,
    "UserExtRiskScores": UserExtRiskScores,
    "UserExtSecQuestions": UserExtSecQuestions,
    "UserExtSelfRegistrationProfile": UserExtSelfRegistrationProfile,
    "UserExtSmtpCredentials": UserExtSmtpCredentials,
    "UserExtSocialAccounts": UserExtSocialAccounts,
    "UserExtSupportAccounts": UserExtSupportAccounts,
    "UserExtSyncedFromApp": UserExtSyncedFromApp,
    "UserExtTermsOfUseConsents": UserExtTermsOfUseConsents,
    "UserExtTrustedUserAgents": UserExtTrustedUserAgents,
    "UserExtUserToken": UserExtUserToken,
    "UserGroups": UserGroups,
    "UserIms": UserIms,
    "UserName": UserName,
    "UserPasswordChanger": UserPasswordChanger,
    "UserPasswordResetter": UserPasswordResetter,
    "UserPasswordResetterUserToken": UserPasswordResetterUserToken,
    "UserPhoneNumbers": UserPhoneNumbers,
    "UserPhotos": UserPhotos,
    "UserRoles": UserRoles,
    "UserSearchRequest": UserSearchRequest,
    "UserStatusChanger": UserStatusChanger,
    "UserX509Certificates": UserX509Certificates,
    "Users": Users
}

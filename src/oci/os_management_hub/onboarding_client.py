# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from oci._vendor import requests  # noqa: F401
from oci._vendor import six

from oci import retry, circuit_breaker  # noqa: F401
from oci.base_client import BaseClient
from oci.config import get_config_value_or_default, validate_config
from oci.signer import Signer
from oci.util import Sentinel, get_signer_from_authentication_type, AUTHENTICATION_TYPE_FIELD_NAME
from .models import os_management_hub_type_mapping
missing = Sentinel("Missing")


class OnboardingClient(object):
    """
    Use the OS Management Hub API to manage and monitor updates and patches for the operating system environments in your private data centers through a single management console. For more information, see [Overview of OS Management Hub](https://docs.cloud.oracle.com/iaas/osmh/doc/overview.htm).
    Use the table of contents and search tool to explore the  OS Management Hub API.
    """

    def __init__(self, config, **kwargs):
        """
        Creates a new service client

        :param dict config:
            Configuration keys and values as per `SDK and Tool Configuration <https://docs.cloud.oracle.com/Content/API/Concepts/sdkconfig.htm>`__.
            The :py:meth:`~oci.config.from_file` method can be used to load configuration from a file. Alternatively, a ``dict`` can be passed. You can validate_config
            the dict using :py:meth:`~oci.config.validate_config`

        :param str service_endpoint: (optional)
            The endpoint of the service to call using this client. For example ``https://iaas.us-ashburn-1.oraclecloud.com``. If this keyword argument is
            not provided then it will be derived using the region in the config parameter. You should only provide this keyword argument if you have an explicit
            need to specify a service endpoint.

        :param timeout: (optional)
            The connection and read timeouts for the client. The default values are connection timeout 10 seconds and read timeout 60 seconds. This keyword argument can be provided
            as a single float, in which case the value provided is used for both the read and connection timeouts, or as a tuple of two floats. If
            a tuple is provided then the first value is used as the connection timeout and the second value as the read timeout.
        :type timeout: float or tuple(float, float)

        :param signer: (optional)
            The signer to use when signing requests made by the service client. The default is to use a :py:class:`~oci.signer.Signer` based on the values
            provided in the config parameter.

            One use case for this parameter is for `Instance Principals authentication <https://docs.cloud.oracle.com/Content/Identity/Tasks/callingservicesfrominstances.htm>`__
            by passing an instance of :py:class:`~oci.auth.signers.InstancePrincipalsSecurityTokenSigner` as the value for this keyword argument
        :type signer: :py:class:`~oci.signer.AbstractBaseSigner`

        :param obj retry_strategy: (optional)
            A retry strategy to apply to all calls made by this service client (i.e. at the client level). There is no retry strategy applied by default.
            Retry strategies can also be applied at the operation level by passing a ``retry_strategy`` keyword argument as part of calling the operation.
            Any value provided at the operation level will override whatever is specified at the client level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

        :param obj circuit_breaker_strategy: (optional)
            A circuit breaker strategy to apply to all calls made by this service client (i.e. at the client level).
            This client uses :py:data:`~oci.circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY` as default if no circuit breaker strategy is provided.
            The specifics of circuit breaker strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/circuit_breakers.html>`__.

        :param function circuit_breaker_callback: (optional)
            Callback function to receive any exceptions triggerred by the circuit breaker.

        :param bool client_level_realm_specific_endpoint_template_enabled: (optional)
            A boolean flag to indicate whether or not this client should be created with realm specific endpoint template enabled or disable. By default, this will be set as None.

        :param allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this client should allow control characters in the response object. By default, the client will not
            allow control characters to be in the response object.
        """
        validate_config(config, signer=kwargs.get('signer'))
        if 'signer' in kwargs:
            signer = kwargs['signer']

        elif AUTHENTICATION_TYPE_FIELD_NAME in config:
            signer = get_signer_from_authentication_type(config)

        else:
            signer = Signer(
                tenancy=config["tenancy"],
                user=config["user"],
                fingerprint=config["fingerprint"],
                private_key_file_location=config.get("key_file"),
                pass_phrase=get_config_value_or_default(config, "pass_phrase"),
                private_key_content=config.get("key_content")
            )

        base_client_init_kwargs = {
            'regional_client': True,
            'service_endpoint': kwargs.get('service_endpoint'),
            'base_path': '/20220901',
            'service_endpoint_template': 'https://osmh.{region}.oci.{secondLevelDomain}',
            'service_endpoint_template_per_realm': {  },  # noqa: E201 E202
            'skip_deserialization': kwargs.get('skip_deserialization', False),
            'circuit_breaker_strategy': kwargs.get('circuit_breaker_strategy', circuit_breaker.GLOBAL_CIRCUIT_BREAKER_STRATEGY),
            'client_level_realm_specific_endpoint_template_enabled': kwargs.get('client_level_realm_specific_endpoint_template_enabled')
        }
        if 'timeout' in kwargs:
            base_client_init_kwargs['timeout'] = kwargs.get('timeout')
        if base_client_init_kwargs.get('circuit_breaker_strategy') is None:
            base_client_init_kwargs['circuit_breaker_strategy'] = circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY
        if 'allow_control_chars' in kwargs:
            base_client_init_kwargs['allow_control_chars'] = kwargs.get('allow_control_chars')
        self.base_client = BaseClient("onboarding", config, signer, os_management_hub_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self.circuit_breaker_callback = kwargs.get('circuit_breaker_callback')

    def create_profile(self, create_profile_details, **kwargs):
        """
        Creates a registration profile.
        A profile is a supplementary file for the OS Management Hub agentry
        that dictates the content for a managed instance at registration time.


        :param oci.os_management_hub.models.CreateProfileDetails create_profile_details: (required)
            Details for the new registration profile.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.os_management_hub.models.Profile`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/osmanagementhub/create_profile.py.html>`__ to see an example of how to use create_profile API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = []
        resource_path = "/profiles"
        method = "POST"
        operation_name = "create_profile"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_profile got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_profile_details,
                response_type="Profile",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_profile_details,
                response_type="Profile",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def delete_profile(self, profile_id, **kwargs):
        """
        Deletes a specified registration profile.


        :param str profile_id: (required)
            The OCID of the registration profile.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/osmanagementhub/delete_profile.py.html>`__ to see an example of how to use delete_profile API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['profileId']
        resource_path = "/profiles/{profileId}"
        method = "DELETE"
        operation_name = "delete_profile"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_profile got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "profileId": profile_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def get_profile(self, profile_id, **kwargs):
        """
        Gets information about the specified registration profile.


        :param str profile_id: (required)
            The OCID of the registration profile.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.os_management_hub.models.Profile`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/osmanagementhub/get_profile.py.html>`__ to see an example of how to use get_profile API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['profileId']
        resource_path = "/profiles/{profileId}"
        method = "GET"
        operation_name = "get_profile"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_profile got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "profileId": profile_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Profile",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Profile",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def list_profiles(self, **kwargs):
        """
        Lists registration profiles that match the specified compartment or profile OCID. Filter the list against a
        variety of criteria including but not limited to its name, status, vendor name, and architecture type.


        :param str compartment_id: (optional)
            The OCID of the compartment that contains the resources to list.

        :param list[str] display_name: (optional)
            A filter to return resources that match the given display names.

        :param str display_name_contains: (optional)
            A filter to return resources that may partially match the given display name.

        :param list[str] profile_type: (optional)
            A filter to return registration profiles that match the given profileType.

            Allowed values are: "SOFTWARESOURCE", "GROUP", "LIFECYCLE", "STATION"

        :param str profile_id: (optional)
            The OCID of the registration profile.

        :param str os_family: (optional)
            A filter to return only profiles that match the given osFamily.

            Allowed values are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7"

        :param str arch_type: (optional)
            A filter to return only profiles that match the given archType.

            Allowed values are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC"

        :param str vendor_name: (optional)
            A filter to return only profiles that match the given vendorName.

            Allowed values are: "ORACLE"

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            Example: `3`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str lifecycle_state: (optional)
            A filter to return only registration profile whose lifecycleState matches the given lifecycleState.

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"

        :param str sort_order: (optional)
            The sort order to use, either 'ASC' or 'DESC'.

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort by. Only one sort order may be provided.
            Default order for timeCreated is descending.
            Default order for displayName is ascending.

            Allowed values are: "timeCreated", "displayName"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.os_management_hub.models.ProfileCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/osmanagementhub/list_profiles.py.html>`__ to see an example of how to use list_profiles API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = []
        resource_path = "/profiles"
        method = "GET"
        operation_name = "list_profiles"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "display_name",
            "display_name_contains",
            "profile_type",
            "profile_id",
            "os_family",
            "arch_type",
            "vendor_name",
            "limit",
            "page",
            "lifecycle_state",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_profiles got unknown kwargs: {!r}".format(extra_kwargs))

        if 'profile_type' in kwargs:
            profile_type_allowed_values = ["SOFTWARESOURCE", "GROUP", "LIFECYCLE", "STATION"]
            for profile_type_item in kwargs['profile_type']:
                if profile_type_item not in profile_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `profile_type`, must be one of {0}".format(profile_type_allowed_values)
                    )

        if 'os_family' in kwargs:
            os_family_allowed_values = ["ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7"]
            if kwargs['os_family'] not in os_family_allowed_values:
                raise ValueError(
                    "Invalid value for `os_family`, must be one of {0}".format(os_family_allowed_values)
                )

        if 'arch_type' in kwargs:
            arch_type_allowed_values = ["X86_64", "AARCH64", "I686", "NOARCH", "SRC"]
            if kwargs['arch_type'] not in arch_type_allowed_values:
                raise ValueError(
                    "Invalid value for `arch_type`, must be one of {0}".format(arch_type_allowed_values)
                )

        if 'vendor_name' in kwargs:
            vendor_name_allowed_values = ["ORACLE"]
            if kwargs['vendor_name'] not in vendor_name_allowed_values:
                raise ValueError(
                    "Invalid value for `vendor_name`, must be one of {0}".format(vendor_name_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeCreated", "displayName"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "displayName": self.base_client.generate_collection_format_param(kwargs.get("display_name", missing), 'multi'),
            "displayNameContains": kwargs.get("display_name_contains", missing),
            "profileType": self.base_client.generate_collection_format_param(kwargs.get("profile_type", missing), 'multi'),
            "profileId": kwargs.get("profile_id", missing),
            "osFamily": kwargs.get("os_family", missing),
            "archType": kwargs.get("arch_type", missing),
            "vendorName": kwargs.get("vendor_name", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="ProfileCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="ProfileCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def update_profile(self, profile_id, update_profile_details, **kwargs):
        """
        Updates the specified profile's name, description, and tags.


        :param str profile_id: (required)
            The OCID of the registration profile.

        :param oci.os_management_hub.models.UpdateProfileDetails update_profile_details: (required)
            The information to be updated.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.os_management_hub.models.Profile`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/osmanagementhub/update_profile.py.html>`__ to see an example of how to use update_profile API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['profileId']
        resource_path = "/profiles/{profileId}"
        method = "PUT"
        operation_name = "update_profile"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_profile got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "profileId": profile_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_profile_details,
                response_type="Profile",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_profile_details,
                response_type="Profile",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

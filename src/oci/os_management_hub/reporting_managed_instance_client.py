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


class ReportingManagedInstanceClient(object):
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
        self.base_client = BaseClient("reporting_managed_instance", config, signer, os_management_hub_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self.circuit_breaker_callback = kwargs.get('circuit_breaker_callback')

    def get_managed_instance_analytic_content(self, **kwargs):
        """
        Returns a CSV format report of managed instances matching the given filters.


        :param str compartment_id: (optional)
            This compartmentId is used to list managed instances within a compartment.
            Or serve as an additional filter to restrict only managed instances with in certain compartment if other filter presents.

        :param str managed_instance_group_id: (optional)
            The OCID of the managed instance group for which to list resources.

        :param str lifecycle_environment_id: (optional)
            The OCID of the lifecycle environment.

        :param str lifecycle_stage_id: (optional)
            The OCID of the lifecycle stage for which to list resources.

        :param list[str] status: (optional)
            A filter to return only instances whose managed instance status matches the given status.

            Allowed values are: "NORMAL", "UNREACHABLE", "ERROR", "WARNING", "REGISTRATION_ERROR"

        :param list[str] display_name: (optional)
            A filter to return resources that match the given display names.

        :param str display_name_contains: (optional)
            A filter to return resources that may partially match the given display name.

        :param str instance_location: (optional)
            Filter instances by Location. Used when report target type is compartment or group.

            Allowed values are: "ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2"

        :param int security_updates_available_equals_to: (optional)
            A filter to return instances with number of available security updates equals to the number specified.

        :param int bug_updates_available_equals_to: (optional)
            A filter to return instances with number of available bug updates equals to the number specified.

        :param int security_updates_available_greater_than: (optional)
            A filter to return instances with number of available security updates greater than the number specified.

        :param int bug_updates_available_greater_than: (optional)
            A filter to return instances with number of available bug updates greater than the number specified.

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

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/osmanagementhub/get_managed_instance_analytic_content.py.html>`__ to see an example of how to use get_managed_instance_analytic_content API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = []
        resource_path = "/managedInstanceAnalytics/content"
        method = "GET"
        operation_name = "get_managed_instance_analytic_content"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "managed_instance_group_id",
            "lifecycle_environment_id",
            "lifecycle_stage_id",
            "status",
            "display_name",
            "display_name_contains",
            "instance_location",
            "security_updates_available_equals_to",
            "bug_updates_available_equals_to",
            "security_updates_available_greater_than",
            "bug_updates_available_greater_than",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_managed_instance_analytic_content got unknown kwargs: {!r}".format(extra_kwargs))

        if 'status' in kwargs:
            status_allowed_values = ["NORMAL", "UNREACHABLE", "ERROR", "WARNING", "REGISTRATION_ERROR"]
            for status_item in kwargs['status']:
                if status_item not in status_allowed_values:
                    raise ValueError(
                        "Invalid value for `status`, must be one of {0}".format(status_allowed_values)
                    )

        if 'instance_location' in kwargs:
            instance_location_allowed_values = ["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2"]
            if kwargs['instance_location'] not in instance_location_allowed_values:
                raise ValueError(
                    "Invalid value for `instance_location`, must be one of {0}".format(instance_location_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "managedInstanceGroupId": kwargs.get("managed_instance_group_id", missing),
            "lifecycleEnvironmentId": kwargs.get("lifecycle_environment_id", missing),
            "lifecycleStageId": kwargs.get("lifecycle_stage_id", missing),
            "status": self.base_client.generate_collection_format_param(kwargs.get("status", missing), 'multi'),
            "displayName": self.base_client.generate_collection_format_param(kwargs.get("display_name", missing), 'multi'),
            "displayNameContains": kwargs.get("display_name_contains", missing),
            "instanceLocation": kwargs.get("instance_location", missing),
            "securityUpdatesAvailableEqualsTo": kwargs.get("security_updates_available_equals_to", missing),
            "bugUpdatesAvailableEqualsTo": kwargs.get("bug_updates_available_equals_to", missing),
            "securityUpdatesAvailableGreaterThan": kwargs.get("security_updates_available_greater_than", missing),
            "bugUpdatesAvailableGreaterThan": kwargs.get("bug_updates_available_greater_than", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/x-yaml",
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
                response_type="stream",
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
                response_type="stream",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def get_managed_instance_content(self, managed_instance_id, **kwargs):
        """
        Returns a CSV format report of a single managed instance whose associated Erratas match the given filters.


        :param str managed_instance_id: (required)
            The OCID of the managed instance.

        :param list[str] advisory_name: (optional)
            The assigned erratum name. It's unique and not changeable.

            Example: `ELSA-2020-5804`

        :param str advisory_name_contains: (optional)
            A filter to return resources that may partially match the erratum advisory name given.

        :param list[str] advisory_type: (optional)
            A filter to return only errata that match the given advisory types.

            Allowed values are: "SECURITY", "BUGFIX", "ENHANCEMENT"

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

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/osmanagementhub/get_managed_instance_content.py.html>`__ to see an example of how to use get_managed_instance_content API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['managedInstanceId']
        resource_path = "/managedInstances/{managedInstanceId}/content"
        method = "GET"
        operation_name = "get_managed_instance_content"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "advisory_name",
            "advisory_name_contains",
            "advisory_type",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_managed_instance_content got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedInstanceId": managed_instance_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'advisory_type' in kwargs:
            advisory_type_allowed_values = ["SECURITY", "BUGFIX", "ENHANCEMENT"]
            for advisory_type_item in kwargs['advisory_type']:
                if advisory_type_item not in advisory_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `advisory_type`, must be one of {0}".format(advisory_type_allowed_values)
                    )

        query_params = {
            "advisoryName": self.base_client.generate_collection_format_param(kwargs.get("advisory_name", missing), 'multi'),
            "advisoryNameContains": kwargs.get("advisory_name_contains", missing),
            "advisoryType": self.base_client.generate_collection_format_param(kwargs.get("advisory_type", missing), 'multi')
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/x-yaml",
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
                query_params=query_params,
                header_params=header_params,
                response_type="stream",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="stream",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

    def summarize_managed_instance_analytics(self, metric_names, **kwargs):
        """
        Returns a list of user specified metrics for a collection of managed instances.


        :param oci.os_management_hub.models.list[str] metric_names: (required)
            A filter to return only metrics whose name matches the given metric names.

            Allowed values are: "TOTAL_INSTANCE_COUNT", "INSTANCE_WITH_AVAILABLE_SECURITY_UPDATES_COUNT", "INSTANCE_WITH_AVAILABLE_BUGFIX_UPDATES_COUNT", "NORMAL_INSTANCE_COUNT", "ERROR_INSTANCE_COUNT", "WARNING_INSTANCE_COUNT", "UNREACHABLE_INSTANCE_COUNT", "REGISTRATION_FAILED_INSTANCE_COUNT", "INSTANCE_SECURITY_UPDATES_COUNT", "INSTANCE_BUGFIX_UPDATES_COUNT"

        :param str compartment_id: (optional)
            This compartmentId is used to list managed instances within a compartment.
            Or serve as an additional filter to restrict only managed instances with in certain compartment if other filter presents.

        :param str managed_instance_group_id: (optional)
            The OCID of the managed instance group for which to list resources.

        :param str lifecycle_environment_id: (optional)
            The OCID of the lifecycle environment.

        :param str lifecycle_stage_id: (optional)
            The OCID of the lifecycle stage for which to list resources.

        :param list[str] status: (optional)
            A filter to return only instances whose managed instance status matches the given status.

            Allowed values are: "NORMAL", "UNREACHABLE", "ERROR", "WARNING", "REGISTRATION_ERROR"

        :param list[str] display_name: (optional)
            A filter to return resources that match the given display names.

        :param str display_name_contains: (optional)
            A filter to return resources that may partially match the given display name.

        :param str instance_location: (optional)
            Filter instances by Location. Used when report target type is compartment or group.

            Allowed values are: "ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2"

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

        :param str sort_by: (optional)
            The field to sort by. Only one sort order may be provided. Default order for name is ascending.

            Allowed values are: "name"

        :param str sort_order: (optional)
            The sort order to use, either 'ASC' or 'DESC'.

            Allowed values are: "ASC", "DESC"

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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.os_management_hub.models.ManagedInstanceAnalyticCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/osmanagementhub/summarize_managed_instance_analytics.py.html>`__ to see an example of how to use summarize_managed_instance_analytics API.
        """
        # Required path and query arguments. These are in camelCase to replace values in service endpoints.
        required_arguments = ['metricNames']
        resource_path = "/managedInstanceAnalytics"
        method = "GET"
        operation_name = "summarize_managed_instance_analytics"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "managed_instance_group_id",
            "lifecycle_environment_id",
            "lifecycle_stage_id",
            "status",
            "display_name",
            "display_name_contains",
            "instance_location",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_managed_instance_analytics got unknown kwargs: {!r}".format(extra_kwargs))

        metric_names_allowed_values = ["TOTAL_INSTANCE_COUNT", "INSTANCE_WITH_AVAILABLE_SECURITY_UPDATES_COUNT", "INSTANCE_WITH_AVAILABLE_BUGFIX_UPDATES_COUNT", "NORMAL_INSTANCE_COUNT", "ERROR_INSTANCE_COUNT", "WARNING_INSTANCE_COUNT", "UNREACHABLE_INSTANCE_COUNT", "REGISTRATION_FAILED_INSTANCE_COUNT", "INSTANCE_SECURITY_UPDATES_COUNT", "INSTANCE_BUGFIX_UPDATES_COUNT"]
        for metric_names_item in metric_names:
            if metric_names_item not in metric_names_allowed_values:
                raise ValueError(
                    "Invalid value for `metric_names`, must be one of {0}".format(metric_names_allowed_values)
                )

        if 'status' in kwargs:
            status_allowed_values = ["NORMAL", "UNREACHABLE", "ERROR", "WARNING", "REGISTRATION_ERROR"]
            for status_item in kwargs['status']:
                if status_item not in status_allowed_values:
                    raise ValueError(
                        "Invalid value for `status`, must be one of {0}".format(status_allowed_values)
                    )

        if 'instance_location' in kwargs:
            instance_location_allowed_values = ["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2"]
            if kwargs['instance_location'] not in instance_location_allowed_values:
                raise ValueError(
                    "Invalid value for `instance_location`, must be one of {0}".format(instance_location_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["name"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "metricNames": self.base_client.generate_collection_format_param(metric_names, 'multi'),
            "compartmentId": kwargs.get("compartment_id", missing),
            "managedInstanceGroupId": kwargs.get("managed_instance_group_id", missing),
            "lifecycleEnvironmentId": kwargs.get("lifecycle_environment_id", missing),
            "lifecycleStageId": kwargs.get("lifecycle_stage_id", missing),
            "status": self.base_client.generate_collection_format_param(kwargs.get("status", missing), 'multi'),
            "displayName": self.base_client.generate_collection_format_param(kwargs.get("display_name", missing), 'multi'),
            "displayNameContains": kwargs.get("display_name_contains", missing),
            "instanceLocation": kwargs.get("instance_location", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
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
                response_type="ManagedInstanceAnalyticCollection",
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
                response_type="ManagedInstanceAnalyticCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link,
                required_arguments=required_arguments)

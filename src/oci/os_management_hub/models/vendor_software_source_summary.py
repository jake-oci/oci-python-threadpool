# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .software_source_summary import SoftwareSourceSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VendorSoftwareSourceSummary(SoftwareSourceSummary):
    """
    A vendor software source summary summarizes a vendor software source.
    """

    #: A constant which can be used with the vendor_name property of a VendorSoftwareSourceSummary.
    #: This constant has a value of "ORACLE"
    VENDOR_NAME_ORACLE = "ORACLE"

    def __init__(self, **kwargs):
        """
        Initializes a new VendorSoftwareSourceSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.os_management_hub.models.VendorSoftwareSourceSummary.software_source_type` attribute
        of this class is ``VENDOR`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this VendorSoftwareSourceSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this VendorSoftwareSourceSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this VendorSoftwareSourceSummary.
        :type display_name: str

        :param repo_id:
            The value to assign to the repo_id property of this VendorSoftwareSourceSummary.
        :type repo_id: str

        :param url:
            The value to assign to the url property of this VendorSoftwareSourceSummary.
        :type url: str

        :param time_created:
            The value to assign to the time_created property of this VendorSoftwareSourceSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this VendorSoftwareSourceSummary.
        :type time_updated: datetime

        :param description:
            The value to assign to the description property of this VendorSoftwareSourceSummary.
        :type description: str

        :param software_source_type:
            The value to assign to the software_source_type property of this VendorSoftwareSourceSummary.
            Allowed values for this property are: "VENDOR", "CUSTOM", "VERSIONED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type software_source_type: str

        :param availability:
            The value to assign to the availability property of this VendorSoftwareSourceSummary.
            Allowed values for this property are: "AVAILABLE", "SELECTED", "RESTRICTED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type availability: str

        :param os_family:
            The value to assign to the os_family property of this VendorSoftwareSourceSummary.
            Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type os_family: str

        :param arch_type:
            The value to assign to the arch_type property of this VendorSoftwareSourceSummary.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type arch_type: str

        :param package_count:
            The value to assign to the package_count property of this VendorSoftwareSourceSummary.
        :type package_count: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VendorSoftwareSourceSummary.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this VendorSoftwareSourceSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this VendorSoftwareSourceSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this VendorSoftwareSourceSummary.
        :type system_tags: dict(str, dict(str, object))

        :param vendor_name:
            The value to assign to the vendor_name property of this VendorSoftwareSourceSummary.
            Allowed values for this property are: "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type vendor_name: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'repo_id': 'str',
            'url': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'description': 'str',
            'software_source_type': 'str',
            'availability': 'str',
            'os_family': 'str',
            'arch_type': 'str',
            'package_count': 'int',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'vendor_name': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'repo_id': 'repoId',
            'url': 'url',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'description': 'description',
            'software_source_type': 'softwareSourceType',
            'availability': 'availability',
            'os_family': 'osFamily',
            'arch_type': 'archType',
            'package_count': 'packageCount',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'vendor_name': 'vendorName'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._repo_id = None
        self._url = None
        self._time_created = None
        self._time_updated = None
        self._description = None
        self._software_source_type = None
        self._availability = None
        self._os_family = None
        self._arch_type = None
        self._package_count = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._vendor_name = None
        self._software_source_type = 'VENDOR'

    @property
    def vendor_name(self):
        """
        **[Required]** Gets the vendor_name of this VendorSoftwareSourceSummary.
        Name of the vendor providing the software source.

        Allowed values for this property are: "ORACLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The vendor_name of this VendorSoftwareSourceSummary.
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """
        Sets the vendor_name of this VendorSoftwareSourceSummary.
        Name of the vendor providing the software source.


        :param vendor_name: The vendor_name of this VendorSoftwareSourceSummary.
        :type: str
        """
        allowed_values = ["ORACLE"]
        if not value_allowed_none_or_none_sentinel(vendor_name, allowed_values):
            vendor_name = 'UNKNOWN_ENUM_VALUE'
        self._vendor_name = vendor_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

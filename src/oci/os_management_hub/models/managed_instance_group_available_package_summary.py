# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedInstanceGroupAvailablePackageSummary(object):
    """
    Summary information pertaining to an available package for a managed instance group.
    """

    #: A constant which can be used with the architecture property of a ManagedInstanceGroupAvailablePackageSummary.
    #: This constant has a value of "X86_64"
    ARCHITECTURE_X86_64 = "X86_64"

    #: A constant which can be used with the architecture property of a ManagedInstanceGroupAvailablePackageSummary.
    #: This constant has a value of "AARCH64"
    ARCHITECTURE_AARCH64 = "AARCH64"

    #: A constant which can be used with the architecture property of a ManagedInstanceGroupAvailablePackageSummary.
    #: This constant has a value of "I686"
    ARCHITECTURE_I686 = "I686"

    #: A constant which can be used with the architecture property of a ManagedInstanceGroupAvailablePackageSummary.
    #: This constant has a value of "NOARCH"
    ARCHITECTURE_NOARCH = "NOARCH"

    #: A constant which can be used with the architecture property of a ManagedInstanceGroupAvailablePackageSummary.
    #: This constant has a value of "SRC"
    ARCHITECTURE_SRC = "SRC"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedInstanceGroupAvailablePackageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this ManagedInstanceGroupAvailablePackageSummary.
        :type display_name: str

        :param name:
            The value to assign to the name property of this ManagedInstanceGroupAvailablePackageSummary.
        :type name: str

        :param type:
            The value to assign to the type property of this ManagedInstanceGroupAvailablePackageSummary.
        :type type: str

        :param version:
            The value to assign to the version property of this ManagedInstanceGroupAvailablePackageSummary.
        :type version: str

        :param architecture:
            The value to assign to the architecture property of this ManagedInstanceGroupAvailablePackageSummary.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type architecture: str

        :param software_sources:
            The value to assign to the software_sources property of this ManagedInstanceGroupAvailablePackageSummary.
        :type software_sources: list[oci.os_management_hub.models.SoftwareSourceDetails]

        :param is_latest:
            The value to assign to the is_latest property of this ManagedInstanceGroupAvailablePackageSummary.
        :type is_latest: bool

        """
        self.swagger_types = {
            'display_name': 'str',
            'name': 'str',
            'type': 'str',
            'version': 'str',
            'architecture': 'str',
            'software_sources': 'list[SoftwareSourceDetails]',
            'is_latest': 'bool'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'name': 'name',
            'type': 'type',
            'version': 'version',
            'architecture': 'architecture',
            'software_sources': 'softwareSources',
            'is_latest': 'isLatest'
        }

        self._display_name = None
        self._name = None
        self._type = None
        self._version = None
        self._architecture = None
        self._software_sources = None
        self._is_latest = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ManagedInstanceGroupAvailablePackageSummary.
        Package name.


        :return: The display_name of this ManagedInstanceGroupAvailablePackageSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ManagedInstanceGroupAvailablePackageSummary.
        Package name.


        :param display_name: The display_name of this ManagedInstanceGroupAvailablePackageSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ManagedInstanceGroupAvailablePackageSummary.
        Unique identifier for the package. NOTE - This is not an OCID.


        :return: The name of this ManagedInstanceGroupAvailablePackageSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ManagedInstanceGroupAvailablePackageSummary.
        Unique identifier for the package. NOTE - This is not an OCID.


        :param name: The name of this ManagedInstanceGroupAvailablePackageSummary.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ManagedInstanceGroupAvailablePackageSummary.
        Type of the package.


        :return: The type of this ManagedInstanceGroupAvailablePackageSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ManagedInstanceGroupAvailablePackageSummary.
        Type of the package.


        :param type: The type of this ManagedInstanceGroupAvailablePackageSummary.
        :type: str
        """
        self._type = type

    @property
    def version(self):
        """
        **[Required]** Gets the version of this ManagedInstanceGroupAvailablePackageSummary.
        Version of the installed package.


        :return: The version of this ManagedInstanceGroupAvailablePackageSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ManagedInstanceGroupAvailablePackageSummary.
        Version of the installed package.


        :param version: The version of this ManagedInstanceGroupAvailablePackageSummary.
        :type: str
        """
        self._version = version

    @property
    def architecture(self):
        """
        Gets the architecture of this ManagedInstanceGroupAvailablePackageSummary.
        The architecture for which this package was built.

        Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The architecture of this ManagedInstanceGroupAvailablePackageSummary.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this ManagedInstanceGroupAvailablePackageSummary.
        The architecture for which this package was built.


        :param architecture: The architecture of this ManagedInstanceGroupAvailablePackageSummary.
        :type: str
        """
        allowed_values = ["X86_64", "AARCH64", "I686", "NOARCH", "SRC"]
        if not value_allowed_none_or_none_sentinel(architecture, allowed_values):
            architecture = 'UNKNOWN_ENUM_VALUE'
        self._architecture = architecture

    @property
    def software_sources(self):
        """
        Gets the software_sources of this ManagedInstanceGroupAvailablePackageSummary.
        List of software sources that provide the software package.


        :return: The software_sources of this ManagedInstanceGroupAvailablePackageSummary.
        :rtype: list[oci.os_management_hub.models.SoftwareSourceDetails]
        """
        return self._software_sources

    @software_sources.setter
    def software_sources(self, software_sources):
        """
        Sets the software_sources of this ManagedInstanceGroupAvailablePackageSummary.
        List of software sources that provide the software package.


        :param software_sources: The software_sources of this ManagedInstanceGroupAvailablePackageSummary.
        :type: list[oci.os_management_hub.models.SoftwareSourceDetails]
        """
        self._software_sources = software_sources

    @property
    def is_latest(self):
        """
        Gets the is_latest of this ManagedInstanceGroupAvailablePackageSummary.
        Flag to return only latest package versions.


        :return: The is_latest of this ManagedInstanceGroupAvailablePackageSummary.
        :rtype: bool
        """
        return self._is_latest

    @is_latest.setter
    def is_latest(self, is_latest):
        """
        Sets the is_latest of this ManagedInstanceGroupAvailablePackageSummary.
        Flag to return only latest package versions.


        :param is_latest: The is_latest of this ManagedInstanceGroupAvailablePackageSummary.
        :type: bool
        """
        self._is_latest = is_latest

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

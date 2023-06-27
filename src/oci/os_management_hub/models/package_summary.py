# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PackageSummary(object):
    """
    A software package summary.
    """

    #: A constant which can be used with the architecture property of a PackageSummary.
    #: This constant has a value of "X86_64"
    ARCHITECTURE_X86_64 = "X86_64"

    #: A constant which can be used with the architecture property of a PackageSummary.
    #: This constant has a value of "AARCH64"
    ARCHITECTURE_AARCH64 = "AARCH64"

    #: A constant which can be used with the architecture property of a PackageSummary.
    #: This constant has a value of "I686"
    ARCHITECTURE_I686 = "I686"

    #: A constant which can be used with the architecture property of a PackageSummary.
    #: This constant has a value of "NOARCH"
    ARCHITECTURE_NOARCH = "NOARCH"

    #: A constant which can be used with the architecture property of a PackageSummary.
    #: This constant has a value of "SRC"
    ARCHITECTURE_SRC = "SRC"

    #: A constant which can be used with the package_classification property of a PackageSummary.
    #: This constant has a value of "INSTALLED"
    PACKAGE_CLASSIFICATION_INSTALLED = "INSTALLED"

    #: A constant which can be used with the package_classification property of a PackageSummary.
    #: This constant has a value of "AVAILABLE"
    PACKAGE_CLASSIFICATION_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the package_classification property of a PackageSummary.
    #: This constant has a value of "UPDATABLE"
    PACKAGE_CLASSIFICATION_UPDATABLE = "UPDATABLE"

    def __init__(self, **kwargs):
        """
        Initializes a new PackageSummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.os_management_hub.models.AvailablePackageSummary`
        * :class:`~oci.os_management_hub.models.InstalledPackageSummary`
        * :class:`~oci.os_management_hub.models.UpdatablePackageSummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this PackageSummary.
        :type display_name: str

        :param name:
            The value to assign to the name property of this PackageSummary.
        :type name: str

        :param type:
            The value to assign to the type property of this PackageSummary.
        :type type: str

        :param version:
            The value to assign to the version property of this PackageSummary.
        :type version: str

        :param architecture:
            The value to assign to the architecture property of this PackageSummary.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC"
        :type architecture: str

        :param software_sources:
            The value to assign to the software_sources property of this PackageSummary.
        :type software_sources: list[oci.os_management_hub.models.SoftwareSourceDetails]

        :param package_classification:
            The value to assign to the package_classification property of this PackageSummary.
            Allowed values for this property are: "INSTALLED", "AVAILABLE", "UPDATABLE"
        :type package_classification: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'name': 'str',
            'type': 'str',
            'version': 'str',
            'architecture': 'str',
            'software_sources': 'list[SoftwareSourceDetails]',
            'package_classification': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'name': 'name',
            'type': 'type',
            'version': 'version',
            'architecture': 'architecture',
            'software_sources': 'softwareSources',
            'package_classification': 'packageClassification'
        }

        self._display_name = None
        self._name = None
        self._type = None
        self._version = None
        self._architecture = None
        self._software_sources = None
        self._package_classification = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['packageClassification']

        if type == 'AVAILABLE':
            return 'AvailablePackageSummary'

        if type == 'INSTALLED':
            return 'InstalledPackageSummary'

        if type == 'UPDATABLE':
            return 'UpdatablePackageSummary'
        else:
            return 'PackageSummary'

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this PackageSummary.
        Package name.


        :return: The display_name of this PackageSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PackageSummary.
        Package name.


        :param display_name: The display_name of this PackageSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        **[Required]** Gets the name of this PackageSummary.
        Unique identifier for the package.


        :return: The name of this PackageSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PackageSummary.
        Unique identifier for the package.


        :param name: The name of this PackageSummary.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this PackageSummary.
        Type of the package.


        :return: The type of this PackageSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PackageSummary.
        Type of the package.


        :param type: The type of this PackageSummary.
        :type: str
        """
        self._type = type

    @property
    def version(self):
        """
        **[Required]** Gets the version of this PackageSummary.
        Version of the installed package.


        :return: The version of this PackageSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PackageSummary.
        Version of the installed package.


        :param version: The version of this PackageSummary.
        :type: str
        """
        self._version = version

    @property
    def architecture(self):
        """
        Gets the architecture of this PackageSummary.
        The architecture for which this package was built.

        Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC"


        :return: The architecture of this PackageSummary.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this PackageSummary.
        The architecture for which this package was built.


        :param architecture: The architecture of this PackageSummary.
        :type: str
        """
        allowed_values = ["X86_64", "AARCH64", "I686", "NOARCH", "SRC"]
        if not value_allowed_none_or_none_sentinel(architecture, allowed_values):
            raise ValueError(
                "Invalid value for `architecture`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._architecture = architecture

    @property
    def software_sources(self):
        """
        Gets the software_sources of this PackageSummary.
        list of software sources that provide the software package.


        :return: The software_sources of this PackageSummary.
        :rtype: list[oci.os_management_hub.models.SoftwareSourceDetails]
        """
        return self._software_sources

    @software_sources.setter
    def software_sources(self, software_sources):
        """
        Sets the software_sources of this PackageSummary.
        list of software sources that provide the software package.


        :param software_sources: The software_sources of this PackageSummary.
        :type: list[oci.os_management_hub.models.SoftwareSourceDetails]
        """
        self._software_sources = software_sources

    @property
    def package_classification(self):
        """
        **[Required]** Gets the package_classification of this PackageSummary.
        classifier for child instances of this object.

        Allowed values for this property are: "INSTALLED", "AVAILABLE", "UPDATABLE"


        :return: The package_classification of this PackageSummary.
        :rtype: str
        """
        return self._package_classification

    @package_classification.setter
    def package_classification(self, package_classification):
        """
        Sets the package_classification of this PackageSummary.
        classifier for child instances of this object.


        :param package_classification: The package_classification of this PackageSummary.
        :type: str
        """
        allowed_values = ["INSTALLED", "AVAILABLE", "UPDATABLE"]
        if not value_allowed_none_or_none_sentinel(package_classification, allowed_values):
            raise ValueError(
                "Invalid value for `package_classification`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._package_classification = package_classification

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

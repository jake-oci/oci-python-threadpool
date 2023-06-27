# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SoftwareSourceAvailability(object):
    """
    An object that contains a software source OCID and its availability.
    """

    #: A constant which can be used with the availability property of a SoftwareSourceAvailability.
    #: This constant has a value of "AVAILABLE"
    AVAILABILITY_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the availability property of a SoftwareSourceAvailability.
    #: This constant has a value of "SELECTED"
    AVAILABILITY_SELECTED = "SELECTED"

    #: A constant which can be used with the availability property of a SoftwareSourceAvailability.
    #: This constant has a value of "RESTRICTED"
    AVAILABILITY_RESTRICTED = "RESTRICTED"

    def __init__(self, **kwargs):
        """
        Initializes a new SoftwareSourceAvailability object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param software_source_id:
            The value to assign to the software_source_id property of this SoftwareSourceAvailability.
        :type software_source_id: str

        :param availability:
            The value to assign to the availability property of this SoftwareSourceAvailability.
            Allowed values for this property are: "AVAILABLE", "SELECTED", "RESTRICTED"
        :type availability: str

        """
        self.swagger_types = {
            'software_source_id': 'str',
            'availability': 'str'
        }

        self.attribute_map = {
            'software_source_id': 'softwareSourceId',
            'availability': 'availability'
        }

        self._software_source_id = None
        self._availability = None

    @property
    def software_source_id(self):
        """
        **[Required]** Gets the software_source_id of this SoftwareSourceAvailability.
        The OCID for a vendor software source.


        :return: The software_source_id of this SoftwareSourceAvailability.
        :rtype: str
        """
        return self._software_source_id

    @software_source_id.setter
    def software_source_id(self, software_source_id):
        """
        Sets the software_source_id of this SoftwareSourceAvailability.
        The OCID for a vendor software source.


        :param software_source_id: The software_source_id of this SoftwareSourceAvailability.
        :type: str
        """
        self._software_source_id = software_source_id

    @property
    def availability(self):
        """
        **[Required]** Gets the availability of this SoftwareSourceAvailability.
        Possible availabilities of a software source.

        Allowed values for this property are: "AVAILABLE", "SELECTED", "RESTRICTED"


        :return: The availability of this SoftwareSourceAvailability.
        :rtype: str
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """
        Sets the availability of this SoftwareSourceAvailability.
        Possible availabilities of a software source.


        :param availability: The availability of this SoftwareSourceAvailability.
        :type: str
        """
        allowed_values = ["AVAILABLE", "SELECTED", "RESTRICTED"]
        if not value_allowed_none_or_none_sentinel(availability, allowed_values):
            raise ValueError(
                "Invalid value for `availability`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._availability = availability

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

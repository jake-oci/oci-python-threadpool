# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SearchSoftwareSourceModulesDetails(object):
    """
    Contains a list of software sources to get the combined list of modules from all of those software sources.
    """

    #: A constant which can be used with the sort_order property of a SearchSoftwareSourceModulesDetails.
    #: This constant has a value of "ASC"
    SORT_ORDER_ASC = "ASC"

    #: A constant which can be used with the sort_order property of a SearchSoftwareSourceModulesDetails.
    #: This constant has a value of "DESC"
    SORT_ORDER_DESC = "DESC"

    #: A constant which can be used with the sort_by property of a SearchSoftwareSourceModulesDetails.
    #: This constant has a value of "NAME"
    SORT_BY_NAME = "NAME"

    def __init__(self, **kwargs):
        """
        Initializes a new SearchSoftwareSourceModulesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param software_source_ids:
            The value to assign to the software_source_ids property of this SearchSoftwareSourceModulesDetails.
        :type software_source_ids: list[str]

        :param sort_order:
            The value to assign to the sort_order property of this SearchSoftwareSourceModulesDetails.
            Allowed values for this property are: "ASC", "DESC"
        :type sort_order: str

        :param name:
            The value to assign to the name property of this SearchSoftwareSourceModulesDetails.
        :type name: str

        :param name_contains:
            The value to assign to the name_contains property of this SearchSoftwareSourceModulesDetails.
        :type name_contains: str

        :param sort_by:
            The value to assign to the sort_by property of this SearchSoftwareSourceModulesDetails.
            Allowed values for this property are: "NAME"
        :type sort_by: str

        """
        self.swagger_types = {
            'software_source_ids': 'list[str]',
            'sort_order': 'str',
            'name': 'str',
            'name_contains': 'str',
            'sort_by': 'str'
        }

        self.attribute_map = {
            'software_source_ids': 'softwareSourceIds',
            'sort_order': 'sortOrder',
            'name': 'name',
            'name_contains': 'nameContains',
            'sort_by': 'sortBy'
        }

        self._software_source_ids = None
        self._sort_order = None
        self._name = None
        self._name_contains = None
        self._sort_by = None

    @property
    def software_source_ids(self):
        """
        **[Required]** Gets the software_source_ids of this SearchSoftwareSourceModulesDetails.
        List of software source OCIDs.


        :return: The software_source_ids of this SearchSoftwareSourceModulesDetails.
        :rtype: list[str]
        """
        return self._software_source_ids

    @software_source_ids.setter
    def software_source_ids(self, software_source_ids):
        """
        Sets the software_source_ids of this SearchSoftwareSourceModulesDetails.
        List of software source OCIDs.


        :param software_source_ids: The software_source_ids of this SearchSoftwareSourceModulesDetails.
        :type: list[str]
        """
        self._software_source_ids = software_source_ids

    @property
    def sort_order(self):
        """
        Gets the sort_order of this SearchSoftwareSourceModulesDetails.
        The sort order.

        Allowed values for this property are: "ASC", "DESC"


        :return: The sort_order of this SearchSoftwareSourceModulesDetails.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """
        Sets the sort_order of this SearchSoftwareSourceModulesDetails.
        The sort order.


        :param sort_order: The sort_order of this SearchSoftwareSourceModulesDetails.
        :type: str
        """
        allowed_values = ["ASC", "DESC"]
        if not value_allowed_none_or_none_sentinel(sort_order, allowed_values):
            raise ValueError(
                "Invalid value for `sort_order`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._sort_order = sort_order

    @property
    def name(self):
        """
        Gets the name of this SearchSoftwareSourceModulesDetails.
        The name of a module.


        :return: The name of this SearchSoftwareSourceModulesDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SearchSoftwareSourceModulesDetails.
        The name of a module.


        :param name: The name of this SearchSoftwareSourceModulesDetails.
        :type: str
        """
        self._name = name

    @property
    def name_contains(self):
        """
        Gets the name_contains of this SearchSoftwareSourceModulesDetails.
        filters results, allowing only those with a name which contains the string.


        :return: The name_contains of this SearchSoftwareSourceModulesDetails.
        :rtype: str
        """
        return self._name_contains

    @name_contains.setter
    def name_contains(self, name_contains):
        """
        Sets the name_contains of this SearchSoftwareSourceModulesDetails.
        filters results, allowing only those with a name which contains the string.


        :param name_contains: The name_contains of this SearchSoftwareSourceModulesDetails.
        :type: str
        """
        self._name_contains = name_contains

    @property
    def sort_by(self):
        """
        Gets the sort_by of this SearchSoftwareSourceModulesDetails.
        The field to sort by.

        Allowed values for this property are: "NAME"


        :return: The sort_by of this SearchSoftwareSourceModulesDetails.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """
        Sets the sort_by of this SearchSoftwareSourceModulesDetails.
        The field to sort by.


        :param sort_by: The sort_by of this SearchSoftwareSourceModulesDetails.
        :type: str
        """
        allowed_values = ["NAME"]
        if not value_allowed_none_or_none_sentinel(sort_by, allowed_values):
            raise ValueError(
                "Invalid value for `sort_by`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._sort_by = sort_by

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

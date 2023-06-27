# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SearchSoftwareSourcePackageGroupsDetails(object):
    """
    Contains a list of software sources to get the list of associated package groups.
    """

    #: A constant which can be used with the sort_order property of a SearchSoftwareSourcePackageGroupsDetails.
    #: This constant has a value of "ASC"
    SORT_ORDER_ASC = "ASC"

    #: A constant which can be used with the sort_order property of a SearchSoftwareSourcePackageGroupsDetails.
    #: This constant has a value of "DESC"
    SORT_ORDER_DESC = "DESC"

    #: A constant which can be used with the sort_by property of a SearchSoftwareSourcePackageGroupsDetails.
    #: This constant has a value of "NAME"
    SORT_BY_NAME = "NAME"

    def __init__(self, **kwargs):
        """
        Initializes a new SearchSoftwareSourcePackageGroupsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param software_source_ids:
            The value to assign to the software_source_ids property of this SearchSoftwareSourcePackageGroupsDetails.
        :type software_source_ids: list[str]

        :param sort_order:
            The value to assign to the sort_order property of this SearchSoftwareSourcePackageGroupsDetails.
            Allowed values for this property are: "ASC", "DESC"
        :type sort_order: str

        :param sort_by:
            The value to assign to the sort_by property of this SearchSoftwareSourcePackageGroupsDetails.
            Allowed values for this property are: "NAME"
        :type sort_by: str

        :param name_contains:
            The value to assign to the name_contains property of this SearchSoftwareSourcePackageGroupsDetails.
        :type name_contains: str

        :param group_type:
            The value to assign to the group_type property of this SearchSoftwareSourcePackageGroupsDetails.
        :type group_type: str

        """
        self.swagger_types = {
            'software_source_ids': 'list[str]',
            'sort_order': 'str',
            'sort_by': 'str',
            'name_contains': 'str',
            'group_type': 'str'
        }

        self.attribute_map = {
            'software_source_ids': 'softwareSourceIds',
            'sort_order': 'sortOrder',
            'sort_by': 'sortBy',
            'name_contains': 'nameContains',
            'group_type': 'groupType'
        }

        self._software_source_ids = None
        self._sort_order = None
        self._sort_by = None
        self._name_contains = None
        self._group_type = None

    @property
    def software_source_ids(self):
        """
        **[Required]** Gets the software_source_ids of this SearchSoftwareSourcePackageGroupsDetails.
        List of software source OCIDs.


        :return: The software_source_ids of this SearchSoftwareSourcePackageGroupsDetails.
        :rtype: list[str]
        """
        return self._software_source_ids

    @software_source_ids.setter
    def software_source_ids(self, software_source_ids):
        """
        Sets the software_source_ids of this SearchSoftwareSourcePackageGroupsDetails.
        List of software source OCIDs.


        :param software_source_ids: The software_source_ids of this SearchSoftwareSourcePackageGroupsDetails.
        :type: list[str]
        """
        self._software_source_ids = software_source_ids

    @property
    def sort_order(self):
        """
        Gets the sort_order of this SearchSoftwareSourcePackageGroupsDetails.
        The sort order.

        Allowed values for this property are: "ASC", "DESC"


        :return: The sort_order of this SearchSoftwareSourcePackageGroupsDetails.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """
        Sets the sort_order of this SearchSoftwareSourcePackageGroupsDetails.
        The sort order.


        :param sort_order: The sort_order of this SearchSoftwareSourcePackageGroupsDetails.
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
    def sort_by(self):
        """
        Gets the sort_by of this SearchSoftwareSourcePackageGroupsDetails.
        The field to sort by.

        Allowed values for this property are: "NAME"


        :return: The sort_by of this SearchSoftwareSourcePackageGroupsDetails.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """
        Sets the sort_by of this SearchSoftwareSourcePackageGroupsDetails.
        The field to sort by.


        :param sort_by: The sort_by of this SearchSoftwareSourcePackageGroupsDetails.
        :type: str
        """
        allowed_values = ["NAME"]
        if not value_allowed_none_or_none_sentinel(sort_by, allowed_values):
            raise ValueError(
                "Invalid value for `sort_by`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._sort_by = sort_by

    @property
    def name_contains(self):
        """
        Gets the name_contains of this SearchSoftwareSourcePackageGroupsDetails.
        filters results, allowing only those with a Name which contains the string.


        :return: The name_contains of this SearchSoftwareSourcePackageGroupsDetails.
        :rtype: str
        """
        return self._name_contains

    @name_contains.setter
    def name_contains(self, name_contains):
        """
        Sets the name_contains of this SearchSoftwareSourcePackageGroupsDetails.
        filters results, allowing only those with a Name which contains the string.


        :param name_contains: The name_contains of this SearchSoftwareSourcePackageGroupsDetails.
        :type: str
        """
        self._name_contains = name_contains

    @property
    def group_type(self):
        """
        Gets the group_type of this SearchSoftwareSourcePackageGroupsDetails.
        Indicates if this is a group, category or environment.


        :return: The group_type of this SearchSoftwareSourcePackageGroupsDetails.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """
        Sets the group_type of this SearchSoftwareSourcePackageGroupsDetails.
        Indicates if this is a group, category or environment.


        :param group_type: The group_type of this SearchSoftwareSourcePackageGroupsDetails.
        :type: str
        """
        self._group_type = group_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

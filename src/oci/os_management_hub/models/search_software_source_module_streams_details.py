# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SearchSoftwareSourceModuleStreamsDetails(object):
    """
    Contains a list of software sources to get the combined list of module streams from all of those software sources.
    """

    #: A constant which can be used with the sort_order property of a SearchSoftwareSourceModuleStreamsDetails.
    #: This constant has a value of "ASC"
    SORT_ORDER_ASC = "ASC"

    #: A constant which can be used with the sort_order property of a SearchSoftwareSourceModuleStreamsDetails.
    #: This constant has a value of "DESC"
    SORT_ORDER_DESC = "DESC"

    #: A constant which can be used with the sort_by property of a SearchSoftwareSourceModuleStreamsDetails.
    #: This constant has a value of "MODULENAME"
    SORT_BY_MODULENAME = "MODULENAME"

    def __init__(self, **kwargs):
        """
        Initializes a new SearchSoftwareSourceModuleStreamsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param software_source_ids:
            The value to assign to the software_source_ids property of this SearchSoftwareSourceModuleStreamsDetails.
        :type software_source_ids: list[str]

        :param sort_order:
            The value to assign to the sort_order property of this SearchSoftwareSourceModuleStreamsDetails.
            Allowed values for this property are: "ASC", "DESC"
        :type sort_order: str

        :param module_name:
            The value to assign to the module_name property of this SearchSoftwareSourceModuleStreamsDetails.
        :type module_name: str

        :param sort_by:
            The value to assign to the sort_by property of this SearchSoftwareSourceModuleStreamsDetails.
            Allowed values for this property are: "MODULENAME"
        :type sort_by: str

        """
        self.swagger_types = {
            'software_source_ids': 'list[str]',
            'sort_order': 'str',
            'module_name': 'str',
            'sort_by': 'str'
        }

        self.attribute_map = {
            'software_source_ids': 'softwareSourceIds',
            'sort_order': 'sortOrder',
            'module_name': 'moduleName',
            'sort_by': 'sortBy'
        }

        self._software_source_ids = None
        self._sort_order = None
        self._module_name = None
        self._sort_by = None

    @property
    def software_source_ids(self):
        """
        **[Required]** Gets the software_source_ids of this SearchSoftwareSourceModuleStreamsDetails.
        List of software source OCIDs.


        :return: The software_source_ids of this SearchSoftwareSourceModuleStreamsDetails.
        :rtype: list[str]
        """
        return self._software_source_ids

    @software_source_ids.setter
    def software_source_ids(self, software_source_ids):
        """
        Sets the software_source_ids of this SearchSoftwareSourceModuleStreamsDetails.
        List of software source OCIDs.


        :param software_source_ids: The software_source_ids of this SearchSoftwareSourceModuleStreamsDetails.
        :type: list[str]
        """
        self._software_source_ids = software_source_ids

    @property
    def sort_order(self):
        """
        Gets the sort_order of this SearchSoftwareSourceModuleStreamsDetails.
        The sort order.

        Allowed values for this property are: "ASC", "DESC"


        :return: The sort_order of this SearchSoftwareSourceModuleStreamsDetails.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """
        Sets the sort_order of this SearchSoftwareSourceModuleStreamsDetails.
        The sort order.


        :param sort_order: The sort_order of this SearchSoftwareSourceModuleStreamsDetails.
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
    def module_name(self):
        """
        Gets the module_name of this SearchSoftwareSourceModuleStreamsDetails.
        The name of a module.


        :return: The module_name of this SearchSoftwareSourceModuleStreamsDetails.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """
        Sets the module_name of this SearchSoftwareSourceModuleStreamsDetails.
        The name of a module.


        :param module_name: The module_name of this SearchSoftwareSourceModuleStreamsDetails.
        :type: str
        """
        self._module_name = module_name

    @property
    def sort_by(self):
        """
        Gets the sort_by of this SearchSoftwareSourceModuleStreamsDetails.
        The field to sort by.

        Allowed values for this property are: "MODULENAME"


        :return: The sort_by of this SearchSoftwareSourceModuleStreamsDetails.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """
        Sets the sort_by of this SearchSoftwareSourceModuleStreamsDetails.
        The field to sort by.


        :param sort_by: The sort_by of this SearchSoftwareSourceModuleStreamsDetails.
        :type: str
        """
        allowed_values = ["MODULENAME"]
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

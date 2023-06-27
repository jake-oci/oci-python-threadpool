# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SynchronizeMirrorsDetails(object):
    """
    Details for syncing selected mirrors
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SynchronizeMirrorsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param software_source_list:
            The value to assign to the software_source_list property of this SynchronizeMirrorsDetails.
        :type software_source_list: list[str]

        """
        self.swagger_types = {
            'software_source_list': 'list[str]'
        }

        self.attribute_map = {
            'software_source_list': 'softwareSourceList'
        }

        self._software_source_list = None

    @property
    def software_source_list(self):
        """
        **[Required]** Gets the software_source_list of this SynchronizeMirrorsDetails.
        List of Software Source OCIDs to synchronize


        :return: The software_source_list of this SynchronizeMirrorsDetails.
        :rtype: list[str]
        """
        return self._software_source_list

    @software_source_list.setter
    def software_source_list(self, software_source_list):
        """
        Sets the software_source_list of this SynchronizeMirrorsDetails.
        List of Software Source OCIDs to synchronize


        :param software_source_list: The software_source_list of this SynchronizeMirrorsDetails.
        :type: list[str]
        """
        self._software_source_list = software_source_list

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

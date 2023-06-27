# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestManagementStationDetails(object):
    """
    Details about management station actions.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestManagementStationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param management_station_version:
            The value to assign to the management_station_version property of this WorkRequestManagementStationDetails.
        :type management_station_version: str

        :param config:
            The value to assign to the config property of this WorkRequestManagementStationDetails.
        :type config: str

        :param software_source_ids:
            The value to assign to the software_source_ids property of this WorkRequestManagementStationDetails.
        :type software_source_ids: list[str]

        """
        self.swagger_types = {
            'management_station_version': 'str',
            'config': 'str',
            'software_source_ids': 'list[str]'
        }

        self.attribute_map = {
            'management_station_version': 'managementStationVersion',
            'config': 'config',
            'software_source_ids': 'softwareSourceIds'
        }

        self._management_station_version = None
        self._config = None
        self._software_source_ids = None

    @property
    def management_station_version(self):
        """
        Gets the management_station_version of this WorkRequestManagementStationDetails.
        Target version to update the management station software.


        :return: The management_station_version of this WorkRequestManagementStationDetails.
        :rtype: str
        """
        return self._management_station_version

    @management_station_version.setter
    def management_station_version(self, management_station_version):
        """
        Sets the management_station_version of this WorkRequestManagementStationDetails.
        Target version to update the management station software.


        :param management_station_version: The management_station_version of this WorkRequestManagementStationDetails.
        :type: str
        """
        self._management_station_version = management_station_version

    @property
    def config(self):
        """
        Gets the config of this WorkRequestManagementStationDetails.
        Target config needed for set management station config.


        :return: The config of this WorkRequestManagementStationDetails.
        :rtype: str
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this WorkRequestManagementStationDetails.
        Target config needed for set management station config.


        :param config: The config of this WorkRequestManagementStationDetails.
        :type: str
        """
        self._config = config

    @property
    def software_source_ids(self):
        """
        Gets the software_source_ids of this WorkRequestManagementStationDetails.
        Optional list for mirrors to sync.


        :return: The software_source_ids of this WorkRequestManagementStationDetails.
        :rtype: list[str]
        """
        return self._software_source_ids

    @software_source_ids.setter
    def software_source_ids(self, software_source_ids):
        """
        Sets the software_source_ids of this WorkRequestManagementStationDetails.
        Optional list for mirrors to sync.


        :param software_source_ids: The software_source_ids of this WorkRequestManagementStationDetails.
        :type: list[str]
        """
        self._software_source_ids = software_source_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

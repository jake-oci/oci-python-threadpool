# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigureAutomaticCaptureFiltersDetails(object):
    """
    The details required to configure automatic capture filters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigureAutomaticCaptureFiltersDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param auto_capture_filters:
            The value to assign to the auto_capture_filters property of this ConfigureAutomaticCaptureFiltersDetails.
        :type auto_capture_filters: list[oci.database_management.models.AutomaticCaptureFilterDetails]

        :param credentials:
            The value to assign to the credentials property of this ConfigureAutomaticCaptureFiltersDetails.
        :type credentials: oci.database_management.models.ManagedDatabaseCredential

        """
        self.swagger_types = {
            'auto_capture_filters': 'list[AutomaticCaptureFilterDetails]',
            'credentials': 'ManagedDatabaseCredential'
        }

        self.attribute_map = {
            'auto_capture_filters': 'autoCaptureFilters',
            'credentials': 'credentials'
        }

        self._auto_capture_filters = None
        self._credentials = None

    @property
    def auto_capture_filters(self):
        """
        **[Required]** Gets the auto_capture_filters of this ConfigureAutomaticCaptureFiltersDetails.
        The filters used in automatic initial plan capture.


        :return: The auto_capture_filters of this ConfigureAutomaticCaptureFiltersDetails.
        :rtype: list[oci.database_management.models.AutomaticCaptureFilterDetails]
        """
        return self._auto_capture_filters

    @auto_capture_filters.setter
    def auto_capture_filters(self, auto_capture_filters):
        """
        Sets the auto_capture_filters of this ConfigureAutomaticCaptureFiltersDetails.
        The filters used in automatic initial plan capture.


        :param auto_capture_filters: The auto_capture_filters of this ConfigureAutomaticCaptureFiltersDetails.
        :type: list[oci.database_management.models.AutomaticCaptureFilterDetails]
        """
        self._auto_capture_filters = auto_capture_filters

    @property
    def credentials(self):
        """
        **[Required]** Gets the credentials of this ConfigureAutomaticCaptureFiltersDetails.

        :return: The credentials of this ConfigureAutomaticCaptureFiltersDetails.
        :rtype: oci.database_management.models.ManagedDatabaseCredential
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this ConfigureAutomaticCaptureFiltersDetails.

        :param credentials: The credentials of this ConfigureAutomaticCaptureFiltersDetails.
        :type: oci.database_management.models.ManagedDatabaseCredential
        """
        self._credentials = credentials

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

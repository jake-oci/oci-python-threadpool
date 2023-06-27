# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstallModuleStreamProfileOnManagedInstanceGroupDetails(object):
    """
    The work request details for the module stream profile operation on the managed instance group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstallModuleStreamProfileOnManagedInstanceGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param module_name:
            The value to assign to the module_name property of this InstallModuleStreamProfileOnManagedInstanceGroupDetails.
        :type module_name: str

        :param stream_name:
            The value to assign to the stream_name property of this InstallModuleStreamProfileOnManagedInstanceGroupDetails.
        :type stream_name: str

        :param profile_name:
            The value to assign to the profile_name property of this InstallModuleStreamProfileOnManagedInstanceGroupDetails.
        :type profile_name: str

        :param work_request_details:
            The value to assign to the work_request_details property of this InstallModuleStreamProfileOnManagedInstanceGroupDetails.
        :type work_request_details: oci.os_management_hub.models.WorkRequestDetails

        """
        self.swagger_types = {
            'module_name': 'str',
            'stream_name': 'str',
            'profile_name': 'str',
            'work_request_details': 'WorkRequestDetails'
        }

        self.attribute_map = {
            'module_name': 'moduleName',
            'stream_name': 'streamName',
            'profile_name': 'profileName',
            'work_request_details': 'workRequestDetails'
        }

        self._module_name = None
        self._stream_name = None
        self._profile_name = None
        self._work_request_details = None

    @property
    def module_name(self):
        """
        Gets the module_name of this InstallModuleStreamProfileOnManagedInstanceGroupDetails.
        The name of a module.


        :return: The module_name of this InstallModuleStreamProfileOnManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """
        Sets the module_name of this InstallModuleStreamProfileOnManagedInstanceGroupDetails.
        The name of a module.


        :param module_name: The module_name of this InstallModuleStreamProfileOnManagedInstanceGroupDetails.
        :type: str
        """
        self._module_name = module_name

    @property
    def stream_name(self):
        """
        Gets the stream_name of this InstallModuleStreamProfileOnManagedInstanceGroupDetails.
        The name of a stream of the specified module.


        :return: The stream_name of this InstallModuleStreamProfileOnManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """
        Sets the stream_name of this InstallModuleStreamProfileOnManagedInstanceGroupDetails.
        The name of a stream of the specified module.


        :param stream_name: The stream_name of this InstallModuleStreamProfileOnManagedInstanceGroupDetails.
        :type: str
        """
        self._stream_name = stream_name

    @property
    def profile_name(self):
        """
        Gets the profile_name of this InstallModuleStreamProfileOnManagedInstanceGroupDetails.
        The name of a profile of the specified module stream.


        :return: The profile_name of this InstallModuleStreamProfileOnManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """
        Sets the profile_name of this InstallModuleStreamProfileOnManagedInstanceGroupDetails.
        The name of a profile of the specified module stream.


        :param profile_name: The profile_name of this InstallModuleStreamProfileOnManagedInstanceGroupDetails.
        :type: str
        """
        self._profile_name = profile_name

    @property
    def work_request_details(self):
        """
        Gets the work_request_details of this InstallModuleStreamProfileOnManagedInstanceGroupDetails.

        :return: The work_request_details of this InstallModuleStreamProfileOnManagedInstanceGroupDetails.
        :rtype: oci.os_management_hub.models.WorkRequestDetails
        """
        return self._work_request_details

    @work_request_details.setter
    def work_request_details(self, work_request_details):
        """
        Sets the work_request_details of this InstallModuleStreamProfileOnManagedInstanceGroupDetails.

        :param work_request_details: The work_request_details of this InstallModuleStreamProfileOnManagedInstanceGroupDetails.
        :type: oci.os_management_hub.models.WorkRequestDetails
        """
        self._work_request_details = work_request_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

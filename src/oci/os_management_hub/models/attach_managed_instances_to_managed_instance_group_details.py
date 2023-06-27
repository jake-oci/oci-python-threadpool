# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttachManagedInstancesToManagedInstanceGroupDetails(object):
    """
    The managed instance OCIDs to attach to the managed instance group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AttachManagedInstancesToManagedInstanceGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param managed_instances:
            The value to assign to the managed_instances property of this AttachManagedInstancesToManagedInstanceGroupDetails.
        :type managed_instances: list[str]

        :param work_request_details:
            The value to assign to the work_request_details property of this AttachManagedInstancesToManagedInstanceGroupDetails.
        :type work_request_details: oci.os_management_hub.models.WorkRequestDetails

        """
        self.swagger_types = {
            'managed_instances': 'list[str]',
            'work_request_details': 'WorkRequestDetails'
        }

        self.attribute_map = {
            'managed_instances': 'managedInstances',
            'work_request_details': 'workRequestDetails'
        }

        self._managed_instances = None
        self._work_request_details = None

    @property
    def managed_instances(self):
        """
        Gets the managed_instances of this AttachManagedInstancesToManagedInstanceGroupDetails.
        The list of managed instance OCIDs to be attached.


        :return: The managed_instances of this AttachManagedInstancesToManagedInstanceGroupDetails.
        :rtype: list[str]
        """
        return self._managed_instances

    @managed_instances.setter
    def managed_instances(self, managed_instances):
        """
        Sets the managed_instances of this AttachManagedInstancesToManagedInstanceGroupDetails.
        The list of managed instance OCIDs to be attached.


        :param managed_instances: The managed_instances of this AttachManagedInstancesToManagedInstanceGroupDetails.
        :type: list[str]
        """
        self._managed_instances = managed_instances

    @property
    def work_request_details(self):
        """
        Gets the work_request_details of this AttachManagedInstancesToManagedInstanceGroupDetails.

        :return: The work_request_details of this AttachManagedInstancesToManagedInstanceGroupDetails.
        :rtype: oci.os_management_hub.models.WorkRequestDetails
        """
        return self._work_request_details

    @work_request_details.setter
    def work_request_details(self, work_request_details):
        """
        Sets the work_request_details of this AttachManagedInstancesToManagedInstanceGroupDetails.

        :param work_request_details: The work_request_details of this AttachManagedInstancesToManagedInstanceGroupDetails.
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

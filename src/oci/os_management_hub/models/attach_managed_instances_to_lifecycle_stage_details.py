# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttachManagedInstancesToLifecycleStageDetails(object):
    """
    The managed instances to attach to the lifecycle stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AttachManagedInstancesToLifecycleStageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param managed_instance_details:
            The value to assign to the managed_instance_details property of this AttachManagedInstancesToLifecycleStageDetails.
        :type managed_instance_details: oci.os_management_hub.models.ManagedInstancesDetails

        """
        self.swagger_types = {
            'managed_instance_details': 'ManagedInstancesDetails'
        }

        self.attribute_map = {
            'managed_instance_details': 'managedInstanceDetails'
        }

        self._managed_instance_details = None

    @property
    def managed_instance_details(self):
        """
        Gets the managed_instance_details of this AttachManagedInstancesToLifecycleStageDetails.

        :return: The managed_instance_details of this AttachManagedInstancesToLifecycleStageDetails.
        :rtype: oci.os_management_hub.models.ManagedInstancesDetails
        """
        return self._managed_instance_details

    @managed_instance_details.setter
    def managed_instance_details(self, managed_instance_details):
        """
        Sets the managed_instance_details of this AttachManagedInstancesToLifecycleStageDetails.

        :param managed_instance_details: The managed_instance_details of this AttachManagedInstancesToLifecycleStageDetails.
        :type: oci.os_management_hub.models.ManagedInstancesDetails
        """
        self._managed_instance_details = managed_instance_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

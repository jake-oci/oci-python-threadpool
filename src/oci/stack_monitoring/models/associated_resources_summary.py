# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssociatedResourcesSummary(object):
    """
    The information about monitored resource.
    """

    #: A constant which can be used with the lifecycle_state property of a AssociatedResourcesSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AssociatedResourcesSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AssociatedResourcesSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AssociatedResourcesSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AssociatedResourcesSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AssociatedResourcesSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new AssociatedResourcesSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AssociatedResourcesSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this AssociatedResourcesSummary.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this AssociatedResourcesSummary.
        :type display_name: str

        :param type:
            The value to assign to the type property of this AssociatedResourcesSummary.
        :type type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AssociatedResourcesSummary.
        :type compartment_id: str

        :param host_name:
            The value to assign to the host_name property of this AssociatedResourcesSummary.
        :type host_name: str

        :param external_id:
            The value to assign to the external_id property of this AssociatedResourcesSummary.
        :type external_id: str

        :param management_agent_id:
            The value to assign to the management_agent_id property of this AssociatedResourcesSummary.
        :type management_agent_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AssociatedResourcesSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param associated_resources:
            The value to assign to the associated_resources property of this AssociatedResourcesSummary.
        :type associated_resources: list[oci.stack_monitoring.models.AssociatedMonitoredResource]

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'display_name': 'str',
            'type': 'str',
            'compartment_id': 'str',
            'host_name': 'str',
            'external_id': 'str',
            'management_agent_id': 'str',
            'lifecycle_state': 'str',
            'associated_resources': 'list[AssociatedMonitoredResource]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'display_name': 'displayName',
            'type': 'type',
            'compartment_id': 'compartmentId',
            'host_name': 'hostName',
            'external_id': 'externalId',
            'management_agent_id': 'managementAgentId',
            'lifecycle_state': 'lifecycleState',
            'associated_resources': 'associatedResources'
        }

        self._id = None
        self._name = None
        self._display_name = None
        self._type = None
        self._compartment_id = None
        self._host_name = None
        self._external_id = None
        self._management_agent_id = None
        self._lifecycle_state = None
        self._associated_resources = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AssociatedResourcesSummary.
        Monitored resource identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this AssociatedResourcesSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AssociatedResourcesSummary.
        Monitored resource identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this AssociatedResourcesSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this AssociatedResourcesSummary.
        Monitored Resource Name.


        :return: The name of this AssociatedResourcesSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AssociatedResourcesSummary.
        Monitored Resource Name.


        :param name: The name of this AssociatedResourcesSummary.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this AssociatedResourcesSummary.
        Monitored resource display name.


        :return: The display_name of this AssociatedResourcesSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AssociatedResourcesSummary.
        Monitored resource display name.


        :param display_name: The display_name of this AssociatedResourcesSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """
        Gets the type of this AssociatedResourcesSummary.
        Monitored Resource Type.


        :return: The type of this AssociatedResourcesSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AssociatedResourcesSummary.
        Monitored Resource Type.


        :param type: The type of this AssociatedResourcesSummary.
        :type: str
        """
        self._type = type

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this AssociatedResourcesSummary.
        Compartment Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this AssociatedResourcesSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AssociatedResourcesSummary.
        Compartment Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this AssociatedResourcesSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def host_name(self):
        """
        Gets the host_name of this AssociatedResourcesSummary.
        Monitored Resource Host Name.


        :return: The host_name of this AssociatedResourcesSummary.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this AssociatedResourcesSummary.
        Monitored Resource Host Name.


        :param host_name: The host_name of this AssociatedResourcesSummary.
        :type: str
        """
        self._host_name = host_name

    @property
    def external_id(self):
        """
        Gets the external_id of this AssociatedResourcesSummary.
        External resource is any OCI resource identifier `OCID`__
        which is not a Stack Monitoring service resource.
        Currently supports only following resource types - Container database, non-container database,
        pluggable database and OCI compute instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The external_id of this AssociatedResourcesSummary.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this AssociatedResourcesSummary.
        External resource is any OCI resource identifier `OCID`__
        which is not a Stack Monitoring service resource.
        Currently supports only following resource types - Container database, non-container database,
        pluggable database and OCI compute instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param external_id: The external_id of this AssociatedResourcesSummary.
        :type: str
        """
        self._external_id = external_id

    @property
    def management_agent_id(self):
        """
        Gets the management_agent_id of this AssociatedResourcesSummary.
        Management Agent Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The management_agent_id of this AssociatedResourcesSummary.
        :rtype: str
        """
        return self._management_agent_id

    @management_agent_id.setter
    def management_agent_id(self, management_agent_id):
        """
        Sets the management_agent_id of this AssociatedResourcesSummary.
        Management Agent Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param management_agent_id: The management_agent_id of this AssociatedResourcesSummary.
        :type: str
        """
        self._management_agent_id = management_agent_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this AssociatedResourcesSummary.
        The current state of the monitored resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AssociatedResourcesSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AssociatedResourcesSummary.
        The current state of the monitored resource.


        :param lifecycle_state: The lifecycle_state of this AssociatedResourcesSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def associated_resources(self):
        """
        Gets the associated_resources of this AssociatedResourcesSummary.
        List of associated monitored resources.


        :return: The associated_resources of this AssociatedResourcesSummary.
        :rtype: list[oci.stack_monitoring.models.AssociatedMonitoredResource]
        """
        return self._associated_resources

    @associated_resources.setter
    def associated_resources(self, associated_resources):
        """
        Sets the associated_resources of this AssociatedResourcesSummary.
        List of associated monitored resources.


        :param associated_resources: The associated_resources of this AssociatedResourcesSummary.
        :type: list[oci.stack_monitoring.models.AssociatedMonitoredResource]
        """
        self._associated_resources = associated_resources

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

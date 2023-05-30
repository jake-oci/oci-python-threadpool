# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FilesystemSnapshotPolicy(object):
    """
    A file system snapshot policy is used to automate snapshot creation and deletion.
    It contains a list of snapshot schedules that define the frequency of
    snapshot creation for the associated file systems and the retention period of snapshots taken on schedule.

    For more information, see `Snapshot Scheduling`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/iaas/Content/File/Tasks/snapshot-policies-and-schedules.htm
    __ https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a FilesystemSnapshotPolicy.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a FilesystemSnapshotPolicy.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a FilesystemSnapshotPolicy.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a FilesystemSnapshotPolicy.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a FilesystemSnapshotPolicy.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a FilesystemSnapshotPolicy.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new FilesystemSnapshotPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this FilesystemSnapshotPolicy.
        :type compartment_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this FilesystemSnapshotPolicy.
        :type availability_domain: str

        :param id:
            The value to assign to the id property of this FilesystemSnapshotPolicy.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this FilesystemSnapshotPolicy.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "INACTIVE", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this FilesystemSnapshotPolicy.
        :type time_created: datetime

        :param display_name:
            The value to assign to the display_name property of this FilesystemSnapshotPolicy.
        :type display_name: str

        :param policy_prefix:
            The value to assign to the policy_prefix property of this FilesystemSnapshotPolicy.
        :type policy_prefix: str

        :param schedules:
            The value to assign to the schedules property of this FilesystemSnapshotPolicy.
        :type schedules: list[oci.file_storage.models.SnapshotSchedule]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this FilesystemSnapshotPolicy.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this FilesystemSnapshotPolicy.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'availability_domain': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'display_name': 'str',
            'policy_prefix': 'str',
            'schedules': 'list[SnapshotSchedule]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'availability_domain': 'availabilityDomain',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'display_name': 'displayName',
            'policy_prefix': 'policyPrefix',
            'schedules': 'schedules',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._availability_domain = None
        self._id = None
        self._lifecycle_state = None
        self._time_created = None
        self._display_name = None
        self._policy_prefix = None
        self._schedules = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this FilesystemSnapshotPolicy.
        The `OCID`__ of the compartment that contains the file system snapshot policy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this FilesystemSnapshotPolicy.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this FilesystemSnapshotPolicy.
        The `OCID`__ of the compartment that contains the file system snapshot policy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this FilesystemSnapshotPolicy.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this FilesystemSnapshotPolicy.
        The availability domain that the file system snapshot policy is in. May be unset using a blank or NULL value.

        Example: `Uocm:PHX-AD-2`


        :return: The availability_domain of this FilesystemSnapshotPolicy.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this FilesystemSnapshotPolicy.
        The availability domain that the file system snapshot policy is in. May be unset using a blank or NULL value.

        Example: `Uocm:PHX-AD-2`


        :param availability_domain: The availability_domain of this FilesystemSnapshotPolicy.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def id(self):
        """
        **[Required]** Gets the id of this FilesystemSnapshotPolicy.
        The `OCID`__ of the file system snapshot policy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this FilesystemSnapshotPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FilesystemSnapshotPolicy.
        The `OCID`__ of the file system snapshot policy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this FilesystemSnapshotPolicy.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this FilesystemSnapshotPolicy.
        The current state of the file system snapshot policy.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "INACTIVE", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this FilesystemSnapshotPolicy.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this FilesystemSnapshotPolicy.
        The current state of the file system snapshot policy.


        :param lifecycle_state: The lifecycle_state of this FilesystemSnapshotPolicy.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "INACTIVE", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this FilesystemSnapshotPolicy.
        The date and time the file system snapshot policy was created, expressed
        in `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this FilesystemSnapshotPolicy.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this FilesystemSnapshotPolicy.
        The date and time the file system snapshot policy was created, expressed
        in `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this FilesystemSnapshotPolicy.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def display_name(self):
        """
        Gets the display_name of this FilesystemSnapshotPolicy.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `policy1`


        :return: The display_name of this FilesystemSnapshotPolicy.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this FilesystemSnapshotPolicy.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `policy1`


        :param display_name: The display_name of this FilesystemSnapshotPolicy.
        :type: str
        """
        self._display_name = display_name

    @property
    def policy_prefix(self):
        """
        Gets the policy_prefix of this FilesystemSnapshotPolicy.
        The prefix to apply to all snapshots created by this policy.

        Example: `acme`


        :return: The policy_prefix of this FilesystemSnapshotPolicy.
        :rtype: str
        """
        return self._policy_prefix

    @policy_prefix.setter
    def policy_prefix(self, policy_prefix):
        """
        Sets the policy_prefix of this FilesystemSnapshotPolicy.
        The prefix to apply to all snapshots created by this policy.

        Example: `acme`


        :param policy_prefix: The policy_prefix of this FilesystemSnapshotPolicy.
        :type: str
        """
        self._policy_prefix = policy_prefix

    @property
    def schedules(self):
        """
        Gets the schedules of this FilesystemSnapshotPolicy.
        The list of associated snapshot schedules. A maximum of 10 schedules can be associated with a policy.


        :return: The schedules of this FilesystemSnapshotPolicy.
        :rtype: list[oci.file_storage.models.SnapshotSchedule]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """
        Sets the schedules of this FilesystemSnapshotPolicy.
        The list of associated snapshot schedules. A maximum of 10 schedules can be associated with a policy.


        :param schedules: The schedules of this FilesystemSnapshotPolicy.
        :type: list[oci.file_storage.models.SnapshotSchedule]
        """
        self._schedules = schedules

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this FilesystemSnapshotPolicy.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this FilesystemSnapshotPolicy.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this FilesystemSnapshotPolicy.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this FilesystemSnapshotPolicy.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this FilesystemSnapshotPolicy.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this FilesystemSnapshotPolicy.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this FilesystemSnapshotPolicy.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this FilesystemSnapshotPolicy.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

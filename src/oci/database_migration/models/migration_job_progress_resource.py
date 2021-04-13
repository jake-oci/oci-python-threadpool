# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MigrationJobProgressResource(object):
    """
    Progress details of a Migration Job.
    """

    #: A constant which can be used with the current_status property of a MigrationJobProgressResource.
    #: This constant has a value of "PENDING"
    CURRENT_STATUS_PENDING = "PENDING"

    #: A constant which can be used with the current_status property of a MigrationJobProgressResource.
    #: This constant has a value of "STARTED"
    CURRENT_STATUS_STARTED = "STARTED"

    #: A constant which can be used with the current_status property of a MigrationJobProgressResource.
    #: This constant has a value of "COMPLETED"
    CURRENT_STATUS_COMPLETED = "COMPLETED"

    #: A constant which can be used with the current_status property of a MigrationJobProgressResource.
    #: This constant has a value of "FAILED"
    CURRENT_STATUS_FAILED = "FAILED"

    #: A constant which can be used with the current_phase property of a MigrationJobProgressResource.
    #: This constant has a value of "ODMS_VALIDATE_TGT"
    CURRENT_PHASE_ODMS_VALIDATE_TGT = "ODMS_VALIDATE_TGT"

    #: A constant which can be used with the current_phase property of a MigrationJobProgressResource.
    #: This constant has a value of "ODMS_VALIDATE_SRC"
    CURRENT_PHASE_ODMS_VALIDATE_SRC = "ODMS_VALIDATE_SRC"

    #: A constant which can be used with the current_phase property of a MigrationJobProgressResource.
    #: This constant has a value of "ODMS_VALIDATE_GG_HUB"
    CURRENT_PHASE_ODMS_VALIDATE_GG_HUB = "ODMS_VALIDATE_GG_HUB"

    #: A constant which can be used with the current_phase property of a MigrationJobProgressResource.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_SETTINGS"
    CURRENT_PHASE_ODMS_VALIDATE_DATAPUMP_SETTINGS = "ODMS_VALIDATE_DATAPUMP_SETTINGS"

    #: A constant which can be used with the current_phase property of a MigrationJobProgressResource.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC"
    CURRENT_PHASE_ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC = "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC"

    #: A constant which can be used with the current_phase property of a MigrationJobProgressResource.
    #: This constant has a value of "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT"
    CURRENT_PHASE_ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT = "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT"

    #: A constant which can be used with the current_phase property of a MigrationJobProgressResource.
    #: This constant has a value of "ODMS_VALIDATE"
    CURRENT_PHASE_ODMS_VALIDATE = "ODMS_VALIDATE"

    #: A constant which can be used with the current_phase property of a MigrationJobProgressResource.
    #: This constant has a value of "ODMS_PREPARE"
    CURRENT_PHASE_ODMS_PREPARE = "ODMS_PREPARE"

    #: A constant which can be used with the current_phase property of a MigrationJobProgressResource.
    #: This constant has a value of "ODMS_INITIAL_LOAD_EXPORT"
    CURRENT_PHASE_ODMS_INITIAL_LOAD_EXPORT = "ODMS_INITIAL_LOAD_EXPORT"

    #: A constant which can be used with the current_phase property of a MigrationJobProgressResource.
    #: This constant has a value of "ODMS_DATA_UPLOAD"
    CURRENT_PHASE_ODMS_DATA_UPLOAD = "ODMS_DATA_UPLOAD"

    #: A constant which can be used with the current_phase property of a MigrationJobProgressResource.
    #: This constant has a value of "ODMS_INITIAL_LOAD_IMPORT"
    CURRENT_PHASE_ODMS_INITIAL_LOAD_IMPORT = "ODMS_INITIAL_LOAD_IMPORT"

    #: A constant which can be used with the current_phase property of a MigrationJobProgressResource.
    #: This constant has a value of "ODMS_POST_INITIAL_LOAD"
    CURRENT_PHASE_ODMS_POST_INITIAL_LOAD = "ODMS_POST_INITIAL_LOAD"

    #: A constant which can be used with the current_phase property of a MigrationJobProgressResource.
    #: This constant has a value of "ODMS_PREPARE_REPLICATION_TARGET"
    CURRENT_PHASE_ODMS_PREPARE_REPLICATION_TARGET = "ODMS_PREPARE_REPLICATION_TARGET"

    #: A constant which can be used with the current_phase property of a MigrationJobProgressResource.
    #: This constant has a value of "ODMS_MONITOR_REPLICATION_LAG"
    CURRENT_PHASE_ODMS_MONITOR_REPLICATION_LAG = "ODMS_MONITOR_REPLICATION_LAG"

    #: A constant which can be used with the current_phase property of a MigrationJobProgressResource.
    #: This constant has a value of "ODMS_SWITCHOVER"
    CURRENT_PHASE_ODMS_SWITCHOVER = "ODMS_SWITCHOVER"

    #: A constant which can be used with the current_phase property of a MigrationJobProgressResource.
    #: This constant has a value of "ODMS_CLEANUP"
    CURRENT_PHASE_ODMS_CLEANUP = "ODMS_CLEANUP"

    def __init__(self, **kwargs):
        """
        Initializes a new MigrationJobProgressResource object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param current_status:
            The value to assign to the current_status property of this MigrationJobProgressResource.
            Allowed values for this property are: "PENDING", "STARTED", "COMPLETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type current_status: str

        :param current_phase:
            The value to assign to the current_phase property of this MigrationJobProgressResource.
            Allowed values for this property are: "ODMS_VALIDATE_TGT", "ODMS_VALIDATE_SRC", "ODMS_VALIDATE_GG_HUB", "ODMS_VALIDATE_DATAPUMP_SETTINGS", "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC", "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT", "ODMS_VALIDATE", "ODMS_PREPARE", "ODMS_INITIAL_LOAD_EXPORT", "ODMS_DATA_UPLOAD", "ODMS_INITIAL_LOAD_IMPORT", "ODMS_POST_INITIAL_LOAD", "ODMS_PREPARE_REPLICATION_TARGET", "ODMS_MONITOR_REPLICATION_LAG", "ODMS_SWITCHOVER", "ODMS_CLEANUP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type current_phase: str

        :param phases:
            The value to assign to the phases property of this MigrationJobProgressResource.
        :type phases: list[oci.database_migration.models.PhaseStatus]

        """
        self.swagger_types = {
            'current_status': 'str',
            'current_phase': 'str',
            'phases': 'list[PhaseStatus]'
        }

        self.attribute_map = {
            'current_status': 'currentStatus',
            'current_phase': 'currentPhase',
            'phases': 'phases'
        }

        self._current_status = None
        self._current_phase = None
        self._phases = None

    @property
    def current_status(self):
        """
        **[Required]** Gets the current_status of this MigrationJobProgressResource.
        Current status of the job.

        Allowed values for this property are: "PENDING", "STARTED", "COMPLETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The current_status of this MigrationJobProgressResource.
        :rtype: str
        """
        return self._current_status

    @current_status.setter
    def current_status(self, current_status):
        """
        Sets the current_status of this MigrationJobProgressResource.
        Current status of the job.


        :param current_status: The current_status of this MigrationJobProgressResource.
        :type: str
        """
        allowed_values = ["PENDING", "STARTED", "COMPLETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(current_status, allowed_values):
            current_status = 'UNKNOWN_ENUM_VALUE'
        self._current_status = current_status

    @property
    def current_phase(self):
        """
        **[Required]** Gets the current_phase of this MigrationJobProgressResource.
        Current phase of the job.

        Allowed values for this property are: "ODMS_VALIDATE_TGT", "ODMS_VALIDATE_SRC", "ODMS_VALIDATE_GG_HUB", "ODMS_VALIDATE_DATAPUMP_SETTINGS", "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC", "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT", "ODMS_VALIDATE", "ODMS_PREPARE", "ODMS_INITIAL_LOAD_EXPORT", "ODMS_DATA_UPLOAD", "ODMS_INITIAL_LOAD_IMPORT", "ODMS_POST_INITIAL_LOAD", "ODMS_PREPARE_REPLICATION_TARGET", "ODMS_MONITOR_REPLICATION_LAG", "ODMS_SWITCHOVER", "ODMS_CLEANUP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The current_phase of this MigrationJobProgressResource.
        :rtype: str
        """
        return self._current_phase

    @current_phase.setter
    def current_phase(self, current_phase):
        """
        Sets the current_phase of this MigrationJobProgressResource.
        Current phase of the job.


        :param current_phase: The current_phase of this MigrationJobProgressResource.
        :type: str
        """
        allowed_values = ["ODMS_VALIDATE_TGT", "ODMS_VALIDATE_SRC", "ODMS_VALIDATE_GG_HUB", "ODMS_VALIDATE_DATAPUMP_SETTINGS", "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC", "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT", "ODMS_VALIDATE", "ODMS_PREPARE", "ODMS_INITIAL_LOAD_EXPORT", "ODMS_DATA_UPLOAD", "ODMS_INITIAL_LOAD_IMPORT", "ODMS_POST_INITIAL_LOAD", "ODMS_PREPARE_REPLICATION_TARGET", "ODMS_MONITOR_REPLICATION_LAG", "ODMS_SWITCHOVER", "ODMS_CLEANUP"]
        if not value_allowed_none_or_none_sentinel(current_phase, allowed_values):
            current_phase = 'UNKNOWN_ENUM_VALUE'
        self._current_phase = current_phase

    @property
    def phases(self):
        """
        **[Required]** Gets the phases of this MigrationJobProgressResource.
        List of phase status for the job.


        :return: The phases of this MigrationJobProgressResource.
        :rtype: list[oci.database_migration.models.PhaseStatus]
        """
        return self._phases

    @phases.setter
    def phases(self, phases):
        """
        Sets the phases of this MigrationJobProgressResource.
        List of phase status for the job.


        :param phases: The phases of this MigrationJobProgressResource.
        :type: list[oci.database_migration.models.PhaseStatus]
        """
        self._phases = phases

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedInstance(object):
    """
    Detail information for an OCI Compute instance that is being managed.
    """

    #: A constant which can be used with the location property of a ManagedInstance.
    #: This constant has a value of "ON_PREMISE"
    LOCATION_ON_PREMISE = "ON_PREMISE"

    #: A constant which can be used with the location property of a ManagedInstance.
    #: This constant has a value of "OCI_COMPUTE"
    LOCATION_OCI_COMPUTE = "OCI_COMPUTE"

    #: A constant which can be used with the location property of a ManagedInstance.
    #: This constant has a value of "AZURE"
    LOCATION_AZURE = "AZURE"

    #: A constant which can be used with the location property of a ManagedInstance.
    #: This constant has a value of "EC2"
    LOCATION_EC2 = "EC2"

    #: A constant which can be used with the architecture property of a ManagedInstance.
    #: This constant has a value of "X86_64"
    ARCHITECTURE_X86_64 = "X86_64"

    #: A constant which can be used with the architecture property of a ManagedInstance.
    #: This constant has a value of "AARCH64"
    ARCHITECTURE_AARCH64 = "AARCH64"

    #: A constant which can be used with the architecture property of a ManagedInstance.
    #: This constant has a value of "I686"
    ARCHITECTURE_I686 = "I686"

    #: A constant which can be used with the architecture property of a ManagedInstance.
    #: This constant has a value of "NOARCH"
    ARCHITECTURE_NOARCH = "NOARCH"

    #: A constant which can be used with the architecture property of a ManagedInstance.
    #: This constant has a value of "SRC"
    ARCHITECTURE_SRC = "SRC"

    #: A constant which can be used with the os_family property of a ManagedInstance.
    #: This constant has a value of "ORACLE_LINUX_9"
    OS_FAMILY_ORACLE_LINUX_9 = "ORACLE_LINUX_9"

    #: A constant which can be used with the os_family property of a ManagedInstance.
    #: This constant has a value of "ORACLE_LINUX_8"
    OS_FAMILY_ORACLE_LINUX_8 = "ORACLE_LINUX_8"

    #: A constant which can be used with the os_family property of a ManagedInstance.
    #: This constant has a value of "ORACLE_LINUX_7"
    OS_FAMILY_ORACLE_LINUX_7 = "ORACLE_LINUX_7"

    #: A constant which can be used with the status property of a ManagedInstance.
    #: This constant has a value of "NORMAL"
    STATUS_NORMAL = "NORMAL"

    #: A constant which can be used with the status property of a ManagedInstance.
    #: This constant has a value of "UNREACHABLE"
    STATUS_UNREACHABLE = "UNREACHABLE"

    #: A constant which can be used with the status property of a ManagedInstance.
    #: This constant has a value of "ERROR"
    STATUS_ERROR = "ERROR"

    #: A constant which can be used with the status property of a ManagedInstance.
    #: This constant has a value of "WARNING"
    STATUS_WARNING = "WARNING"

    #: A constant which can be used with the status property of a ManagedInstance.
    #: This constant has a value of "REGISTRATION_ERROR"
    STATUS_REGISTRATION_ERROR = "REGISTRATION_ERROR"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedInstance object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ManagedInstance.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ManagedInstance.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ManagedInstance.
        :type description: str

        :param tenancy_id:
            The value to assign to the tenancy_id property of this ManagedInstance.
        :type tenancy_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ManagedInstance.
        :type compartment_id: str

        :param location:
            The value to assign to the location property of this ManagedInstance.
            Allowed values for this property are: "ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type location: str

        :param time_last_checkin:
            The value to assign to the time_last_checkin property of this ManagedInstance.
        :type time_last_checkin: datetime

        :param time_last_boot:
            The value to assign to the time_last_boot property of this ManagedInstance.
        :type time_last_boot: datetime

        :param os_name:
            The value to assign to the os_name property of this ManagedInstance.
        :type os_name: str

        :param os_version:
            The value to assign to the os_version property of this ManagedInstance.
        :type os_version: str

        :param os_kernel_version:
            The value to assign to the os_kernel_version property of this ManagedInstance.
        :type os_kernel_version: str

        :param ksplice_effective_kernel_version:
            The value to assign to the ksplice_effective_kernel_version property of this ManagedInstance.
        :type ksplice_effective_kernel_version: str

        :param architecture:
            The value to assign to the architecture property of this ManagedInstance.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type architecture: str

        :param os_family:
            The value to assign to the os_family property of this ManagedInstance.
            Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type os_family: str

        :param status:
            The value to assign to the status property of this ManagedInstance.
            Allowed values for this property are: "NORMAL", "UNREACHABLE", "ERROR", "WARNING", "REGISTRATION_ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param profile:
            The value to assign to the profile property of this ManagedInstance.
        :type profile: str

        :param is_management_station:
            The value to assign to the is_management_station property of this ManagedInstance.
        :type is_management_station: bool

        :param primary_management_station_id:
            The value to assign to the primary_management_station_id property of this ManagedInstance.
        :type primary_management_station_id: str

        :param secondary_management_station_id:
            The value to assign to the secondary_management_station_id property of this ManagedInstance.
        :type secondary_management_station_id: str

        :param software_sources:
            The value to assign to the software_sources property of this ManagedInstance.
        :type software_sources: list[oci.os_management_hub.models.SoftwareSourceDetails]

        :param managed_instance_group:
            The value to assign to the managed_instance_group property of this ManagedInstance.
        :type managed_instance_group: oci.os_management_hub.models.Id

        :param lifecycle_environment:
            The value to assign to the lifecycle_environment property of this ManagedInstance.
        :type lifecycle_environment: oci.os_management_hub.models.Id

        :param lifecycle_stage:
            The value to assign to the lifecycle_stage property of this ManagedInstance.
        :type lifecycle_stage: oci.os_management_hub.models.Id

        :param is_reboot_required:
            The value to assign to the is_reboot_required property of this ManagedInstance.
        :type is_reboot_required: bool

        :param installed_packages:
            The value to assign to the installed_packages property of this ManagedInstance.
        :type installed_packages: int

        :param updates_available:
            The value to assign to the updates_available property of this ManagedInstance.
        :type updates_available: int

        :param security_updates_available:
            The value to assign to the security_updates_available property of this ManagedInstance.
        :type security_updates_available: int

        :param bug_updates_available:
            The value to assign to the bug_updates_available property of this ManagedInstance.
        :type bug_updates_available: int

        :param enhancement_updates_available:
            The value to assign to the enhancement_updates_available property of this ManagedInstance.
        :type enhancement_updates_available: int

        :param other_updates_available:
            The value to assign to the other_updates_available property of this ManagedInstance.
        :type other_updates_available: int

        :param scheduled_job_count:
            The value to assign to the scheduled_job_count property of this ManagedInstance.
        :type scheduled_job_count: int

        :param work_request_count:
            The value to assign to the work_request_count property of this ManagedInstance.
        :type work_request_count: int

        :param time_created:
            The value to assign to the time_created property of this ManagedInstance.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ManagedInstance.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'tenancy_id': 'str',
            'compartment_id': 'str',
            'location': 'str',
            'time_last_checkin': 'datetime',
            'time_last_boot': 'datetime',
            'os_name': 'str',
            'os_version': 'str',
            'os_kernel_version': 'str',
            'ksplice_effective_kernel_version': 'str',
            'architecture': 'str',
            'os_family': 'str',
            'status': 'str',
            'profile': 'str',
            'is_management_station': 'bool',
            'primary_management_station_id': 'str',
            'secondary_management_station_id': 'str',
            'software_sources': 'list[SoftwareSourceDetails]',
            'managed_instance_group': 'Id',
            'lifecycle_environment': 'Id',
            'lifecycle_stage': 'Id',
            'is_reboot_required': 'bool',
            'installed_packages': 'int',
            'updates_available': 'int',
            'security_updates_available': 'int',
            'bug_updates_available': 'int',
            'enhancement_updates_available': 'int',
            'other_updates_available': 'int',
            'scheduled_job_count': 'int',
            'work_request_count': 'int',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'tenancy_id': 'tenancyId',
            'compartment_id': 'compartmentId',
            'location': 'location',
            'time_last_checkin': 'timeLastCheckin',
            'time_last_boot': 'timeLastBoot',
            'os_name': 'osName',
            'os_version': 'osVersion',
            'os_kernel_version': 'osKernelVersion',
            'ksplice_effective_kernel_version': 'kspliceEffectiveKernelVersion',
            'architecture': 'architecture',
            'os_family': 'osFamily',
            'status': 'status',
            'profile': 'profile',
            'is_management_station': 'isManagementStation',
            'primary_management_station_id': 'primaryManagementStationId',
            'secondary_management_station_id': 'secondaryManagementStationId',
            'software_sources': 'softwareSources',
            'managed_instance_group': 'managedInstanceGroup',
            'lifecycle_environment': 'lifecycleEnvironment',
            'lifecycle_stage': 'lifecycleStage',
            'is_reboot_required': 'isRebootRequired',
            'installed_packages': 'installedPackages',
            'updates_available': 'updatesAvailable',
            'security_updates_available': 'securityUpdatesAvailable',
            'bug_updates_available': 'bugUpdatesAvailable',
            'enhancement_updates_available': 'enhancementUpdatesAvailable',
            'other_updates_available': 'otherUpdatesAvailable',
            'scheduled_job_count': 'scheduledJobCount',
            'work_request_count': 'workRequestCount',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._tenancy_id = None
        self._compartment_id = None
        self._location = None
        self._time_last_checkin = None
        self._time_last_boot = None
        self._os_name = None
        self._os_version = None
        self._os_kernel_version = None
        self._ksplice_effective_kernel_version = None
        self._architecture = None
        self._os_family = None
        self._status = None
        self._profile = None
        self._is_management_station = None
        self._primary_management_station_id = None
        self._secondary_management_station_id = None
        self._software_sources = None
        self._managed_instance_group = None
        self._lifecycle_environment = None
        self._lifecycle_stage = None
        self._is_reboot_required = None
        self._installed_packages = None
        self._updates_available = None
        self._security_updates_available = None
        self._bug_updates_available = None
        self._enhancement_updates_available = None
        self._other_updates_available = None
        self._scheduled_job_count = None
        self._work_request_count = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagedInstance.
        The OCID for the managed instance.


        :return: The id of this ManagedInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagedInstance.
        The OCID for the managed instance.


        :param id: The id of this ManagedInstance.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ManagedInstance.
        Managed instance identifier.


        :return: The display_name of this ManagedInstance.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ManagedInstance.
        Managed instance identifier.


        :param display_name: The display_name of this ManagedInstance.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ManagedInstance.
        Information specified by the user about the managed instance.


        :return: The description of this ManagedInstance.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ManagedInstance.
        Information specified by the user about the managed instance.


        :param description: The description of this ManagedInstance.
        :type: str
        """
        self._description = description

    @property
    def tenancy_id(self):
        """
        **[Required]** Gets the tenancy_id of this ManagedInstance.
        The OCID for the tenancy this managed instance resides in.


        :return: The tenancy_id of this ManagedInstance.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this ManagedInstance.
        The OCID for the tenancy this managed instance resides in.


        :param tenancy_id: The tenancy_id of this ManagedInstance.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ManagedInstance.
        The OCID for the compartment this managed instance resides in.


        :return: The compartment_id of this ManagedInstance.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ManagedInstance.
        The OCID for the compartment this managed instance resides in.


        :param compartment_id: The compartment_id of this ManagedInstance.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def location(self):
        """
        Gets the location of this ManagedInstance.
        location of the managed instance.

        Allowed values for this property are: "ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The location of this ManagedInstance.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this ManagedInstance.
        location of the managed instance.


        :param location: The location of this ManagedInstance.
        :type: str
        """
        allowed_values = ["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2"]
        if not value_allowed_none_or_none_sentinel(location, allowed_values):
            location = 'UNKNOWN_ENUM_VALUE'
        self._location = location

    @property
    def time_last_checkin(self):
        """
        Gets the time_last_checkin of this ManagedInstance.
        Time at which the instance last checked in, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_last_checkin of this ManagedInstance.
        :rtype: datetime
        """
        return self._time_last_checkin

    @time_last_checkin.setter
    def time_last_checkin(self, time_last_checkin):
        """
        Sets the time_last_checkin of this ManagedInstance.
        Time at which the instance last checked in, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_last_checkin: The time_last_checkin of this ManagedInstance.
        :type: datetime
        """
        self._time_last_checkin = time_last_checkin

    @property
    def time_last_boot(self):
        """
        Gets the time_last_boot of this ManagedInstance.
        Time at which the instance last booted, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_last_boot of this ManagedInstance.
        :rtype: datetime
        """
        return self._time_last_boot

    @time_last_boot.setter
    def time_last_boot(self, time_last_boot):
        """
        Sets the time_last_boot of this ManagedInstance.
        Time at which the instance last booted, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_last_boot: The time_last_boot of this ManagedInstance.
        :type: datetime
        """
        self._time_last_boot = time_last_boot

    @property
    def os_name(self):
        """
        Gets the os_name of this ManagedInstance.
        Operating System Name.


        :return: The os_name of this ManagedInstance.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """
        Sets the os_name of this ManagedInstance.
        Operating System Name.


        :param os_name: The os_name of this ManagedInstance.
        :type: str
        """
        self._os_name = os_name

    @property
    def os_version(self):
        """
        Gets the os_version of this ManagedInstance.
        Operating System Version.


        :return: The os_version of this ManagedInstance.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """
        Sets the os_version of this ManagedInstance.
        Operating System Version.


        :param os_version: The os_version of this ManagedInstance.
        :type: str
        """
        self._os_version = os_version

    @property
    def os_kernel_version(self):
        """
        Gets the os_kernel_version of this ManagedInstance.
        Operating System Kernel Version.


        :return: The os_kernel_version of this ManagedInstance.
        :rtype: str
        """
        return self._os_kernel_version

    @os_kernel_version.setter
    def os_kernel_version(self, os_kernel_version):
        """
        Sets the os_kernel_version of this ManagedInstance.
        Operating System Kernel Version.


        :param os_kernel_version: The os_kernel_version of this ManagedInstance.
        :type: str
        """
        self._os_kernel_version = os_kernel_version

    @property
    def ksplice_effective_kernel_version(self):
        """
        Gets the ksplice_effective_kernel_version of this ManagedInstance.
        The ksplice effective kernel version.


        :return: The ksplice_effective_kernel_version of this ManagedInstance.
        :rtype: str
        """
        return self._ksplice_effective_kernel_version

    @ksplice_effective_kernel_version.setter
    def ksplice_effective_kernel_version(self, ksplice_effective_kernel_version):
        """
        Sets the ksplice_effective_kernel_version of this ManagedInstance.
        The ksplice effective kernel version.


        :param ksplice_effective_kernel_version: The ksplice_effective_kernel_version of this ManagedInstance.
        :type: str
        """
        self._ksplice_effective_kernel_version = ksplice_effective_kernel_version

    @property
    def architecture(self):
        """
        Gets the architecture of this ManagedInstance.
        The CPU architecture type of the managed instance.

        Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The architecture of this ManagedInstance.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this ManagedInstance.
        The CPU architecture type of the managed instance.


        :param architecture: The architecture of this ManagedInstance.
        :type: str
        """
        allowed_values = ["X86_64", "AARCH64", "I686", "NOARCH", "SRC"]
        if not value_allowed_none_or_none_sentinel(architecture, allowed_values):
            architecture = 'UNKNOWN_ENUM_VALUE'
        self._architecture = architecture

    @property
    def os_family(self):
        """
        Gets the os_family of this ManagedInstance.
        The Operating System type of the managed instance.

        Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The os_family of this ManagedInstance.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this ManagedInstance.
        The Operating System type of the managed instance.


        :param os_family: The os_family of this ManagedInstance.
        :type: str
        """
        allowed_values = ["ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7"]
        if not value_allowed_none_or_none_sentinel(os_family, allowed_values):
            os_family = 'UNKNOWN_ENUM_VALUE'
        self._os_family = os_family

    @property
    def status(self):
        """
        **[Required]** Gets the status of this ManagedInstance.
        status of the managed instance.

        Allowed values for this property are: "NORMAL", "UNREACHABLE", "ERROR", "WARNING", "REGISTRATION_ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ManagedInstance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ManagedInstance.
        status of the managed instance.


        :param status: The status of this ManagedInstance.
        :type: str
        """
        allowed_values = ["NORMAL", "UNREACHABLE", "ERROR", "WARNING", "REGISTRATION_ERROR"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def profile(self):
        """
        Gets the profile of this ManagedInstance.
        The content profile of this instance.


        :return: The profile of this ManagedInstance.
        :rtype: str
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """
        Sets the profile of this ManagedInstance.
        The content profile of this instance.


        :param profile: The profile of this ManagedInstance.
        :type: str
        """
        self._profile = profile

    @property
    def is_management_station(self):
        """
        Gets the is_management_station of this ManagedInstance.
        Whether this managed instance is acting as an on-premise management station.


        :return: The is_management_station of this ManagedInstance.
        :rtype: bool
        """
        return self._is_management_station

    @is_management_station.setter
    def is_management_station(self, is_management_station):
        """
        Sets the is_management_station of this ManagedInstance.
        Whether this managed instance is acting as an on-premise management station.


        :param is_management_station: The is_management_station of this ManagedInstance.
        :type: bool
        """
        self._is_management_station = is_management_station

    @property
    def primary_management_station_id(self):
        """
        Gets the primary_management_station_id of this ManagedInstance.
        The OCID of a management station to be used as the preferred primary.


        :return: The primary_management_station_id of this ManagedInstance.
        :rtype: str
        """
        return self._primary_management_station_id

    @primary_management_station_id.setter
    def primary_management_station_id(self, primary_management_station_id):
        """
        Sets the primary_management_station_id of this ManagedInstance.
        The OCID of a management station to be used as the preferred primary.


        :param primary_management_station_id: The primary_management_station_id of this ManagedInstance.
        :type: str
        """
        self._primary_management_station_id = primary_management_station_id

    @property
    def secondary_management_station_id(self):
        """
        Gets the secondary_management_station_id of this ManagedInstance.
        The OCID of a management station to be used as the preferred secondary.


        :return: The secondary_management_station_id of this ManagedInstance.
        :rtype: str
        """
        return self._secondary_management_station_id

    @secondary_management_station_id.setter
    def secondary_management_station_id(self, secondary_management_station_id):
        """
        Sets the secondary_management_station_id of this ManagedInstance.
        The OCID of a management station to be used as the preferred secondary.


        :param secondary_management_station_id: The secondary_management_station_id of this ManagedInstance.
        :type: str
        """
        self._secondary_management_station_id = secondary_management_station_id

    @property
    def software_sources(self):
        """
        Gets the software_sources of this ManagedInstance.
        The list of software sources currently attached to the managed instance.


        :return: The software_sources of this ManagedInstance.
        :rtype: list[oci.os_management_hub.models.SoftwareSourceDetails]
        """
        return self._software_sources

    @software_sources.setter
    def software_sources(self, software_sources):
        """
        Sets the software_sources of this ManagedInstance.
        The list of software sources currently attached to the managed instance.


        :param software_sources: The software_sources of this ManagedInstance.
        :type: list[oci.os_management_hub.models.SoftwareSourceDetails]
        """
        self._software_sources = software_sources

    @property
    def managed_instance_group(self):
        """
        Gets the managed_instance_group of this ManagedInstance.

        :return: The managed_instance_group of this ManagedInstance.
        :rtype: oci.os_management_hub.models.Id
        """
        return self._managed_instance_group

    @managed_instance_group.setter
    def managed_instance_group(self, managed_instance_group):
        """
        Sets the managed_instance_group of this ManagedInstance.

        :param managed_instance_group: The managed_instance_group of this ManagedInstance.
        :type: oci.os_management_hub.models.Id
        """
        self._managed_instance_group = managed_instance_group

    @property
    def lifecycle_environment(self):
        """
        Gets the lifecycle_environment of this ManagedInstance.

        :return: The lifecycle_environment of this ManagedInstance.
        :rtype: oci.os_management_hub.models.Id
        """
        return self._lifecycle_environment

    @lifecycle_environment.setter
    def lifecycle_environment(self, lifecycle_environment):
        """
        Sets the lifecycle_environment of this ManagedInstance.

        :param lifecycle_environment: The lifecycle_environment of this ManagedInstance.
        :type: oci.os_management_hub.models.Id
        """
        self._lifecycle_environment = lifecycle_environment

    @property
    def lifecycle_stage(self):
        """
        Gets the lifecycle_stage of this ManagedInstance.

        :return: The lifecycle_stage of this ManagedInstance.
        :rtype: oci.os_management_hub.models.Id
        """
        return self._lifecycle_stage

    @lifecycle_stage.setter
    def lifecycle_stage(self, lifecycle_stage):
        """
        Sets the lifecycle_stage of this ManagedInstance.

        :param lifecycle_stage: The lifecycle_stage of this ManagedInstance.
        :type: oci.os_management_hub.models.Id
        """
        self._lifecycle_stage = lifecycle_stage

    @property
    def is_reboot_required(self):
        """
        Gets the is_reboot_required of this ManagedInstance.
        Indicates whether a reboot is required to complete installation of updates.


        :return: The is_reboot_required of this ManagedInstance.
        :rtype: bool
        """
        return self._is_reboot_required

    @is_reboot_required.setter
    def is_reboot_required(self, is_reboot_required):
        """
        Sets the is_reboot_required of this ManagedInstance.
        Indicates whether a reboot is required to complete installation of updates.


        :param is_reboot_required: The is_reboot_required of this ManagedInstance.
        :type: bool
        """
        self._is_reboot_required = is_reboot_required

    @property
    def installed_packages(self):
        """
        Gets the installed_packages of this ManagedInstance.
        Number of packages installed on the system.


        :return: The installed_packages of this ManagedInstance.
        :rtype: int
        """
        return self._installed_packages

    @installed_packages.setter
    def installed_packages(self, installed_packages):
        """
        Sets the installed_packages of this ManagedInstance.
        Number of packages installed on the system.


        :param installed_packages: The installed_packages of this ManagedInstance.
        :type: int
        """
        self._installed_packages = installed_packages

    @property
    def updates_available(self):
        """
        Gets the updates_available of this ManagedInstance.
        Number of updates available to be installed.


        :return: The updates_available of this ManagedInstance.
        :rtype: int
        """
        return self._updates_available

    @updates_available.setter
    def updates_available(self, updates_available):
        """
        Sets the updates_available of this ManagedInstance.
        Number of updates available to be installed.


        :param updates_available: The updates_available of this ManagedInstance.
        :type: int
        """
        self._updates_available = updates_available

    @property
    def security_updates_available(self):
        """
        Gets the security_updates_available of this ManagedInstance.
        Number of security type updates available to be installed.


        :return: The security_updates_available of this ManagedInstance.
        :rtype: int
        """
        return self._security_updates_available

    @security_updates_available.setter
    def security_updates_available(self, security_updates_available):
        """
        Sets the security_updates_available of this ManagedInstance.
        Number of security type updates available to be installed.


        :param security_updates_available: The security_updates_available of this ManagedInstance.
        :type: int
        """
        self._security_updates_available = security_updates_available

    @property
    def bug_updates_available(self):
        """
        Gets the bug_updates_available of this ManagedInstance.
        Number of bug fix type updates available to be installed.


        :return: The bug_updates_available of this ManagedInstance.
        :rtype: int
        """
        return self._bug_updates_available

    @bug_updates_available.setter
    def bug_updates_available(self, bug_updates_available):
        """
        Sets the bug_updates_available of this ManagedInstance.
        Number of bug fix type updates available to be installed.


        :param bug_updates_available: The bug_updates_available of this ManagedInstance.
        :type: int
        """
        self._bug_updates_available = bug_updates_available

    @property
    def enhancement_updates_available(self):
        """
        Gets the enhancement_updates_available of this ManagedInstance.
        Number of enhancement type updates available to be installed.


        :return: The enhancement_updates_available of this ManagedInstance.
        :rtype: int
        """
        return self._enhancement_updates_available

    @enhancement_updates_available.setter
    def enhancement_updates_available(self, enhancement_updates_available):
        """
        Sets the enhancement_updates_available of this ManagedInstance.
        Number of enhancement type updates available to be installed.


        :param enhancement_updates_available: The enhancement_updates_available of this ManagedInstance.
        :type: int
        """
        self._enhancement_updates_available = enhancement_updates_available

    @property
    def other_updates_available(self):
        """
        Gets the other_updates_available of this ManagedInstance.
        Number of non-classified updates available to be installed.


        :return: The other_updates_available of this ManagedInstance.
        :rtype: int
        """
        return self._other_updates_available

    @other_updates_available.setter
    def other_updates_available(self, other_updates_available):
        """
        Sets the other_updates_available of this ManagedInstance.
        Number of non-classified updates available to be installed.


        :param other_updates_available: The other_updates_available of this ManagedInstance.
        :type: int
        """
        self._other_updates_available = other_updates_available

    @property
    def scheduled_job_count(self):
        """
        Gets the scheduled_job_count of this ManagedInstance.
        Number of scheduled jobs associated with this instance.


        :return: The scheduled_job_count of this ManagedInstance.
        :rtype: int
        """
        return self._scheduled_job_count

    @scheduled_job_count.setter
    def scheduled_job_count(self, scheduled_job_count):
        """
        Sets the scheduled_job_count of this ManagedInstance.
        Number of scheduled jobs associated with this instance.


        :param scheduled_job_count: The scheduled_job_count of this ManagedInstance.
        :type: int
        """
        self._scheduled_job_count = scheduled_job_count

    @property
    def work_request_count(self):
        """
        Gets the work_request_count of this ManagedInstance.
        Number of work requests associated with this instance.


        :return: The work_request_count of this ManagedInstance.
        :rtype: int
        """
        return self._work_request_count

    @work_request_count.setter
    def work_request_count(self, work_request_count):
        """
        Sets the work_request_count of this ManagedInstance.
        Number of work requests associated with this instance.


        :param work_request_count: The work_request_count of this ManagedInstance.
        :type: int
        """
        self._work_request_count = work_request_count

    @property
    def time_created(self):
        """
        Gets the time_created of this ManagedInstance.
        The date and time the work request was created, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this ManagedInstance.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ManagedInstance.
        The date and time the work request was created, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this ManagedInstance.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ManagedInstance.
        The date and time the work request was updated, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this ManagedInstance.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ManagedInstance.
        The date and time the work request was updated, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this ManagedInstance.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

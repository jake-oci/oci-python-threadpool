# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutomaticCaptureFilter(object):
    """
    An automatic capture filter that enables you to capture only those SQL statements
    that you want, and exclude noncritical statements.
    """

    #: A constant which can be used with the name property of a AutomaticCaptureFilter.
    #: This constant has a value of "AUTO_CAPTURE_SQL_TEXT"
    NAME_AUTO_CAPTURE_SQL_TEXT = "AUTO_CAPTURE_SQL_TEXT"

    #: A constant which can be used with the name property of a AutomaticCaptureFilter.
    #: This constant has a value of "AUTO_CAPTURE_PARSING_SCHEMA_NAME"
    NAME_AUTO_CAPTURE_PARSING_SCHEMA_NAME = "AUTO_CAPTURE_PARSING_SCHEMA_NAME"

    #: A constant which can be used with the name property of a AutomaticCaptureFilter.
    #: This constant has a value of "AUTO_CAPTURE_MODULE"
    NAME_AUTO_CAPTURE_MODULE = "AUTO_CAPTURE_MODULE"

    #: A constant which can be used with the name property of a AutomaticCaptureFilter.
    #: This constant has a value of "AUTO_CAPTURE_ACTION"
    NAME_AUTO_CAPTURE_ACTION = "AUTO_CAPTURE_ACTION"

    def __init__(self, **kwargs):
        """
        Initializes a new AutomaticCaptureFilter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AutomaticCaptureFilter.
            Allowed values for this property are: "AUTO_CAPTURE_SQL_TEXT", "AUTO_CAPTURE_PARSING_SCHEMA_NAME", "AUTO_CAPTURE_MODULE", "AUTO_CAPTURE_ACTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type name: str

        :param values_to_include:
            The value to assign to the values_to_include property of this AutomaticCaptureFilter.
        :type values_to_include: list[str]

        :param values_to_exclude:
            The value to assign to the values_to_exclude property of this AutomaticCaptureFilter.
        :type values_to_exclude: list[str]

        :param time_last_modified:
            The value to assign to the time_last_modified property of this AutomaticCaptureFilter.
        :type time_last_modified: datetime

        :param modified_by:
            The value to assign to the modified_by property of this AutomaticCaptureFilter.
        :type modified_by: str

        """
        self.swagger_types = {
            'name': 'str',
            'values_to_include': 'list[str]',
            'values_to_exclude': 'list[str]',
            'time_last_modified': 'datetime',
            'modified_by': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'values_to_include': 'valuesToInclude',
            'values_to_exclude': 'valuesToExclude',
            'time_last_modified': 'timeLastModified',
            'modified_by': 'modifiedBy'
        }

        self._name = None
        self._values_to_include = None
        self._values_to_exclude = None
        self._time_last_modified = None
        self._modified_by = None

    @property
    def name(self):
        """
        Gets the name of this AutomaticCaptureFilter.
        The name of the automatic capture filter.

        - AUTO_CAPTURE_SQL_TEXT: Search pattern to apply to SQL text.
        - AUTO_CAPTURE_PARSING_SCHEMA_NAME: Parsing schema to include or exclude for SQL plan management auto capture.
        - AUTO_CAPTURE_MODULE: Module to include or exclude for SQL plan management auto capture.
        - AUTO_CAPTURE_ACTION: Action to include or exclude for SQL plan management automatic capture.

        Allowed values for this property are: "AUTO_CAPTURE_SQL_TEXT", "AUTO_CAPTURE_PARSING_SCHEMA_NAME", "AUTO_CAPTURE_MODULE", "AUTO_CAPTURE_ACTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The name of this AutomaticCaptureFilter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AutomaticCaptureFilter.
        The name of the automatic capture filter.

        - AUTO_CAPTURE_SQL_TEXT: Search pattern to apply to SQL text.
        - AUTO_CAPTURE_PARSING_SCHEMA_NAME: Parsing schema to include or exclude for SQL plan management auto capture.
        - AUTO_CAPTURE_MODULE: Module to include or exclude for SQL plan management auto capture.
        - AUTO_CAPTURE_ACTION: Action to include or exclude for SQL plan management automatic capture.


        :param name: The name of this AutomaticCaptureFilter.
        :type: str
        """
        allowed_values = ["AUTO_CAPTURE_SQL_TEXT", "AUTO_CAPTURE_PARSING_SCHEMA_NAME", "AUTO_CAPTURE_MODULE", "AUTO_CAPTURE_ACTION"]
        if not value_allowed_none_or_none_sentinel(name, allowed_values):
            name = 'UNKNOWN_ENUM_VALUE'
        self._name = name

    @property
    def values_to_include(self):
        """
        Gets the values_to_include of this AutomaticCaptureFilter.
        A list of filter values to include.


        :return: The values_to_include of this AutomaticCaptureFilter.
        :rtype: list[str]
        """
        return self._values_to_include

    @values_to_include.setter
    def values_to_include(self, values_to_include):
        """
        Sets the values_to_include of this AutomaticCaptureFilter.
        A list of filter values to include.


        :param values_to_include: The values_to_include of this AutomaticCaptureFilter.
        :type: list[str]
        """
        self._values_to_include = values_to_include

    @property
    def values_to_exclude(self):
        """
        Gets the values_to_exclude of this AutomaticCaptureFilter.
        A list of filter values to exclude.


        :return: The values_to_exclude of this AutomaticCaptureFilter.
        :rtype: list[str]
        """
        return self._values_to_exclude

    @values_to_exclude.setter
    def values_to_exclude(self, values_to_exclude):
        """
        Sets the values_to_exclude of this AutomaticCaptureFilter.
        A list of filter values to exclude.


        :param values_to_exclude: The values_to_exclude of this AutomaticCaptureFilter.
        :type: list[str]
        """
        self._values_to_exclude = values_to_exclude

    @property
    def time_last_modified(self):
        """
        Gets the time_last_modified of this AutomaticCaptureFilter.
        The time the filter value was last updated.


        :return: The time_last_modified of this AutomaticCaptureFilter.
        :rtype: datetime
        """
        return self._time_last_modified

    @time_last_modified.setter
    def time_last_modified(self, time_last_modified):
        """
        Sets the time_last_modified of this AutomaticCaptureFilter.
        The time the filter value was last updated.


        :param time_last_modified: The time_last_modified of this AutomaticCaptureFilter.
        :type: datetime
        """
        self._time_last_modified = time_last_modified

    @property
    def modified_by(self):
        """
        Gets the modified_by of this AutomaticCaptureFilter.
        The database user who last updated the filter value.


        :return: The modified_by of this AutomaticCaptureFilter.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """
        Sets the modified_by of this AutomaticCaptureFilter.
        The database user who last updated the filter value.


        :param modified_by: The modified_by of this AutomaticCaptureFilter.
        :type: str
        """
        self._modified_by = modified_by

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

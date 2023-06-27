# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobOutBind(object):
    """
    The details of the job out-bind variable.
    """

    #: A constant which can be used with the data_type property of a JobOutBind.
    #: This constant has a value of "NUMBER"
    DATA_TYPE_NUMBER = "NUMBER"

    #: A constant which can be used with the data_type property of a JobOutBind.
    #: This constant has a value of "STRING"
    DATA_TYPE_STRING = "STRING"

    #: A constant which can be used with the data_type property of a JobOutBind.
    #: This constant has a value of "CLOB"
    DATA_TYPE_CLOB = "CLOB"

    def __init__(self, **kwargs):
        """
        Initializes a new JobOutBind object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param position:
            The value to assign to the position property of this JobOutBind.
        :type position: int

        :param data_type:
            The value to assign to the data_type property of this JobOutBind.
            Allowed values for this property are: "NUMBER", "STRING", "CLOB", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_type: str

        """
        self.swagger_types = {
            'position': 'int',
            'data_type': 'str'
        }

        self.attribute_map = {
            'position': 'position',
            'data_type': 'dataType'
        }

        self._position = None
        self._data_type = None

    @property
    def position(self):
        """
        **[Required]** Gets the position of this JobOutBind.
        The position of the out-bind variable.


        :return: The position of this JobOutBind.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this JobOutBind.
        The position of the out-bind variable.


        :param position: The position of this JobOutBind.
        :type: int
        """
        self._position = position

    @property
    def data_type(self):
        """
        **[Required]** Gets the data_type of this JobOutBind.
        The datatype of the out-bind variable.

        Allowed values for this property are: "NUMBER", "STRING", "CLOB", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_type of this JobOutBind.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this JobOutBind.
        The datatype of the out-bind variable.


        :param data_type: The data_type of this JobOutBind.
        :type: str
        """
        allowed_values = ["NUMBER", "STRING", "CLOB"]
        if not value_allowed_none_or_none_sentinel(data_type, allowed_values):
            data_type = 'UNKNOWN_ENUM_VALUE'
        self._data_type = data_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

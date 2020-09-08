# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceType(object):
    """
    Type of Resource that Service provides.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ResourceType.
        :type name: str

        :param categories:
            The value to assign to the categories property of this ResourceType.
        :type categories: list[Category]

        """
        self.swagger_types = {
            'name': 'str',
            'categories': 'list[Category]'
        }

        self.attribute_map = {
            'name': 'name',
            'categories': 'categories'
        }

        self._name = None
        self._categories = None

    @property
    def name(self):
        """
        Gets the name of this ResourceType.
        Resource type name.


        :return: The name of this ResourceType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ResourceType.
        Resource type name.


        :param name: The name of this ResourceType.
        :type: str
        """
        self._name = name

    @property
    def categories(self):
        """
        Gets the categories of this ResourceType.
        categories for resources.


        :return: The categories of this ResourceType.
        :rtype: list[Category]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this ResourceType.
        categories for resources.


        :param categories: The categories of this ResourceType.
        :type: list[Category]
        """
        self._categories = categories

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

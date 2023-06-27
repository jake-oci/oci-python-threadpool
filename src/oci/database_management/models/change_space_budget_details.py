# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChangeSpaceBudgetDetails(object):
    """
    The details required to change the disk space limit for the SQL Management Base.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChangeSpaceBudgetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param space_budget_percent:
            The value to assign to the space_budget_percent property of this ChangeSpaceBudgetDetails.
        :type space_budget_percent: float

        :param credentials:
            The value to assign to the credentials property of this ChangeSpaceBudgetDetails.
        :type credentials: oci.database_management.models.ManagedDatabaseCredential

        """
        self.swagger_types = {
            'space_budget_percent': 'float',
            'credentials': 'ManagedDatabaseCredential'
        }

        self.attribute_map = {
            'space_budget_percent': 'spaceBudgetPercent',
            'credentials': 'credentials'
        }

        self._space_budget_percent = None
        self._credentials = None

    @property
    def space_budget_percent(self):
        """
        **[Required]** Gets the space_budget_percent of this ChangeSpaceBudgetDetails.
        The maximum percent of `SYSAUX` space that the SQL Management Base can use.


        :return: The space_budget_percent of this ChangeSpaceBudgetDetails.
        :rtype: float
        """
        return self._space_budget_percent

    @space_budget_percent.setter
    def space_budget_percent(self, space_budget_percent):
        """
        Sets the space_budget_percent of this ChangeSpaceBudgetDetails.
        The maximum percent of `SYSAUX` space that the SQL Management Base can use.


        :param space_budget_percent: The space_budget_percent of this ChangeSpaceBudgetDetails.
        :type: float
        """
        self._space_budget_percent = space_budget_percent

    @property
    def credentials(self):
        """
        **[Required]** Gets the credentials of this ChangeSpaceBudgetDetails.

        :return: The credentials of this ChangeSpaceBudgetDetails.
        :rtype: oci.database_management.models.ManagedDatabaseCredential
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this ChangeSpaceBudgetDetails.

        :param credentials: The credentials of this ChangeSpaceBudgetDetails.
        :type: oci.database_management.models.ManagedDatabaseCredential
        """
        self._credentials = credentials

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

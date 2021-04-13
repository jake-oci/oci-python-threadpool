# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .drg_route_distribution_match_criteria import DrgRouteDistributionMatchCriteria
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrgAttachmentTypeDrgRouteDistributionMatchCriteria(DrgRouteDistributionMatchCriteria):
    """
    The attachment type from which the DRG will import routes. Routes will be imported from
    all attachments of this type.
    """

    #: A constant which can be used with the attachment_type property of a DrgAttachmentTypeDrgRouteDistributionMatchCriteria.
    #: This constant has a value of "VCN"
    ATTACHMENT_TYPE_VCN = "VCN"

    #: A constant which can be used with the attachment_type property of a DrgAttachmentTypeDrgRouteDistributionMatchCriteria.
    #: This constant has a value of "VIRTUAL_CIRCUIT"
    ATTACHMENT_TYPE_VIRTUAL_CIRCUIT = "VIRTUAL_CIRCUIT"

    #: A constant which can be used with the attachment_type property of a DrgAttachmentTypeDrgRouteDistributionMatchCriteria.
    #: This constant has a value of "REMOTE_PEERING_CONNECTION"
    ATTACHMENT_TYPE_REMOTE_PEERING_CONNECTION = "REMOTE_PEERING_CONNECTION"

    #: A constant which can be used with the attachment_type property of a DrgAttachmentTypeDrgRouteDistributionMatchCriteria.
    #: This constant has a value of "IPSEC_TUNNEL"
    ATTACHMENT_TYPE_IPSEC_TUNNEL = "IPSEC_TUNNEL"

    def __init__(self, **kwargs):
        """
        Initializes a new DrgAttachmentTypeDrgRouteDistributionMatchCriteria object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.DrgAttachmentTypeDrgRouteDistributionMatchCriteria.match_type` attribute
        of this class is ``DRG_ATTACHMENT_TYPE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param match_type:
            The value to assign to the match_type property of this DrgAttachmentTypeDrgRouteDistributionMatchCriteria.
            Allowed values for this property are: "DRG_ATTACHMENT_TYPE", "DRG_ATTACHMENT_ID", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type match_type: str

        :param attachment_type:
            The value to assign to the attachment_type property of this DrgAttachmentTypeDrgRouteDistributionMatchCriteria.
            Allowed values for this property are: "VCN", "VIRTUAL_CIRCUIT", "REMOTE_PEERING_CONNECTION", "IPSEC_TUNNEL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type attachment_type: str

        """
        self.swagger_types = {
            'match_type': 'str',
            'attachment_type': 'str'
        }

        self.attribute_map = {
            'match_type': 'matchType',
            'attachment_type': 'attachmentType'
        }

        self._match_type = None
        self._attachment_type = None
        self._match_type = 'DRG_ATTACHMENT_TYPE'

    @property
    def attachment_type(self):
        """
        **[Required]** Gets the attachment_type of this DrgAttachmentTypeDrgRouteDistributionMatchCriteria.
        The type of the network resource to be included in this match. A match for a network type implies that all
        DRG attachments of that type insert routes into the table.

        Allowed values for this property are: "VCN", "VIRTUAL_CIRCUIT", "REMOTE_PEERING_CONNECTION", "IPSEC_TUNNEL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The attachment_type of this DrgAttachmentTypeDrgRouteDistributionMatchCriteria.
        :rtype: str
        """
        return self._attachment_type

    @attachment_type.setter
    def attachment_type(self, attachment_type):
        """
        Sets the attachment_type of this DrgAttachmentTypeDrgRouteDistributionMatchCriteria.
        The type of the network resource to be included in this match. A match for a network type implies that all
        DRG attachments of that type insert routes into the table.


        :param attachment_type: The attachment_type of this DrgAttachmentTypeDrgRouteDistributionMatchCriteria.
        :type: str
        """
        allowed_values = ["VCN", "VIRTUAL_CIRCUIT", "REMOTE_PEERING_CONNECTION", "IPSEC_TUNNEL"]
        if not value_allowed_none_or_none_sentinel(attachment_type, allowed_values):
            attachment_type = 'UNKNOWN_ENUM_VALUE'
        self._attachment_type = attachment_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

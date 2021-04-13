# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrgAttachmentNetworkDetails(object):
    """
    DrgAttachmentNetworkDetails model.
    """

    #: A constant which can be used with the type property of a DrgAttachmentNetworkDetails.
    #: This constant has a value of "VCN"
    TYPE_VCN = "VCN"

    #: A constant which can be used with the type property of a DrgAttachmentNetworkDetails.
    #: This constant has a value of "IPSEC_TUNNEL"
    TYPE_IPSEC_TUNNEL = "IPSEC_TUNNEL"

    #: A constant which can be used with the type property of a DrgAttachmentNetworkDetails.
    #: This constant has a value of "VIRTUAL_CIRCUIT"
    TYPE_VIRTUAL_CIRCUIT = "VIRTUAL_CIRCUIT"

    #: A constant which can be used with the type property of a DrgAttachmentNetworkDetails.
    #: This constant has a value of "REMOTE_PEERING_CONNECTION"
    TYPE_REMOTE_PEERING_CONNECTION = "REMOTE_PEERING_CONNECTION"

    def __init__(self, **kwargs):
        """
        Initializes a new DrgAttachmentNetworkDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.VcnDrgAttachmentNetworkDetails`
        * :class:`~oci.core.models.IpsecTunnelDrgAttachmentNetworkDetails`
        * :class:`~oci.core.models.VirtualCircuitDrgAttachmentNetworkDetails`
        * :class:`~oci.core.models.RemotePeeringConnectionDrgAttachmentNetworkDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DrgAttachmentNetworkDetails.
            Allowed values for this property are: "VCN", "IPSEC_TUNNEL", "VIRTUAL_CIRCUIT", "REMOTE_PEERING_CONNECTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param id:
            The value to assign to the id property of this DrgAttachmentNetworkDetails.
        :type id: str

        """
        self.swagger_types = {
            'type': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id'
        }

        self._type = None
        self._id = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'VCN':
            return 'VcnDrgAttachmentNetworkDetails'

        if type == 'IPSEC_TUNNEL':
            return 'IpsecTunnelDrgAttachmentNetworkDetails'

        if type == 'VIRTUAL_CIRCUIT':
            return 'VirtualCircuitDrgAttachmentNetworkDetails'

        if type == 'REMOTE_PEERING_CONNECTION':
            return 'RemotePeeringConnectionDrgAttachmentNetworkDetails'
        else:
            return 'DrgAttachmentNetworkDetails'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this DrgAttachmentNetworkDetails.
        Allowed values for this property are: "VCN", "IPSEC_TUNNEL", "VIRTUAL_CIRCUIT", "REMOTE_PEERING_CONNECTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this DrgAttachmentNetworkDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DrgAttachmentNetworkDetails.

        :param type: The type of this DrgAttachmentNetworkDetails.
        :type: str
        """
        allowed_values = ["VCN", "IPSEC_TUNNEL", "VIRTUAL_CIRCUIT", "REMOTE_PEERING_CONNECTION"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DrgAttachmentNetworkDetails.
        The `OCID`__ of the network attached to the DRG.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this DrgAttachmentNetworkDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DrgAttachmentNetworkDetails.
        The `OCID`__ of the network attached to the DRG.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this DrgAttachmentNetworkDetails.
        :type: str
        """
        self._id = id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

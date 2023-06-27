# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .sql_endpoint_network_configuration import SqlEndpointNetworkConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlEndpointVcnConfig(SqlEndpointNetworkConfiguration):
    """
    The VCN configuration for VCN network type selection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlEndpointVcnConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.data_flow.models.SqlEndpointVcnConfig.network_type` attribute
        of this class is ``VCN`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param network_type:
            The value to assign to the network_type property of this SqlEndpointVcnConfig.
            Allowed values for this property are: "VCN", "SECURE_ACCESS"
        :type network_type: str

        :param vcn_id:
            The value to assign to the vcn_id property of this SqlEndpointVcnConfig.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this SqlEndpointVcnConfig.
        :type subnet_id: str

        :param host_name_prefix:
            The value to assign to the host_name_prefix property of this SqlEndpointVcnConfig.
        :type host_name_prefix: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this SqlEndpointVcnConfig.
        :type nsg_ids: list[str]

        :param private_endpoint_ip:
            The value to assign to the private_endpoint_ip property of this SqlEndpointVcnConfig.
        :type private_endpoint_ip: str

        """
        self.swagger_types = {
            'network_type': 'str',
            'vcn_id': 'str',
            'subnet_id': 'str',
            'host_name_prefix': 'str',
            'nsg_ids': 'list[str]',
            'private_endpoint_ip': 'str'
        }

        self.attribute_map = {
            'network_type': 'networkType',
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId',
            'host_name_prefix': 'hostNamePrefix',
            'nsg_ids': 'nsgIds',
            'private_endpoint_ip': 'privateEndpointIp'
        }

        self._network_type = None
        self._vcn_id = None
        self._subnet_id = None
        self._host_name_prefix = None
        self._nsg_ids = None
        self._private_endpoint_ip = None
        self._network_type = 'VCN'

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this SqlEndpointVcnConfig.
        The VCN OCID.


        :return: The vcn_id of this SqlEndpointVcnConfig.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this SqlEndpointVcnConfig.
        The VCN OCID.


        :param vcn_id: The vcn_id of this SqlEndpointVcnConfig.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this SqlEndpointVcnConfig.
        The VCN Subnet OCID.


        :return: The subnet_id of this SqlEndpointVcnConfig.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this SqlEndpointVcnConfig.
        The VCN Subnet OCID.


        :param subnet_id: The subnet_id of this SqlEndpointVcnConfig.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def host_name_prefix(self):
        """
        Gets the host_name_prefix of this SqlEndpointVcnConfig.
        The host name prefix.


        :return: The host_name_prefix of this SqlEndpointVcnConfig.
        :rtype: str
        """
        return self._host_name_prefix

    @host_name_prefix.setter
    def host_name_prefix(self, host_name_prefix):
        """
        Sets the host_name_prefix of this SqlEndpointVcnConfig.
        The host name prefix.


        :param host_name_prefix: The host_name_prefix of this SqlEndpointVcnConfig.
        :type: str
        """
        self._host_name_prefix = host_name_prefix

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this SqlEndpointVcnConfig.
        The OCIDs of Network Security Groups (NSGs).


        :return: The nsg_ids of this SqlEndpointVcnConfig.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this SqlEndpointVcnConfig.
        The OCIDs of Network Security Groups (NSGs).


        :param nsg_ids: The nsg_ids of this SqlEndpointVcnConfig.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def private_endpoint_ip(self):
        """
        Gets the private_endpoint_ip of this SqlEndpointVcnConfig.
        Ip Address of private endpoint


        :return: The private_endpoint_ip of this SqlEndpointVcnConfig.
        :rtype: str
        """
        return self._private_endpoint_ip

    @private_endpoint_ip.setter
    def private_endpoint_ip(self, private_endpoint_ip):
        """
        Sets the private_endpoint_ip of this SqlEndpointVcnConfig.
        Ip Address of private endpoint


        :param private_endpoint_ip: The private_endpoint_ip of this SqlEndpointVcnConfig.
        :type: str
        """
        self._private_endpoint_ip = private_endpoint_ip

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

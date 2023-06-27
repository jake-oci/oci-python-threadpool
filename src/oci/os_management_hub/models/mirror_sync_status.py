# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MirrorSyncStatus(object):
    """
    Status summary of all repos
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MirrorSyncStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param unsynced:
            The value to assign to the unsynced property of this MirrorSyncStatus.
        :type unsynced: int

        :param queued:
            The value to assign to the queued property of this MirrorSyncStatus.
        :type queued: int

        :param syncing:
            The value to assign to the syncing property of this MirrorSyncStatus.
        :type syncing: int

        :param synced:
            The value to assign to the synced property of this MirrorSyncStatus.
        :type synced: int

        :param failed:
            The value to assign to the failed property of this MirrorSyncStatus.
        :type failed: int

        """
        self.swagger_types = {
            'unsynced': 'int',
            'queued': 'int',
            'syncing': 'int',
            'synced': 'int',
            'failed': 'int'
        }

        self.attribute_map = {
            'unsynced': 'unsynced',
            'queued': 'queued',
            'syncing': 'syncing',
            'synced': 'synced',
            'failed': 'failed'
        }

        self._unsynced = None
        self._queued = None
        self._syncing = None
        self._synced = None
        self._failed = None

    @property
    def unsynced(self):
        """
        **[Required]** Gets the unsynced of this MirrorSyncStatus.
        Total of mirrors in 'failed' state


        :return: The unsynced of this MirrorSyncStatus.
        :rtype: int
        """
        return self._unsynced

    @unsynced.setter
    def unsynced(self, unsynced):
        """
        Sets the unsynced of this MirrorSyncStatus.
        Total of mirrors in 'failed' state


        :param unsynced: The unsynced of this MirrorSyncStatus.
        :type: int
        """
        self._unsynced = unsynced

    @property
    def queued(self):
        """
        **[Required]** Gets the queued of this MirrorSyncStatus.
        Total of mirrors in 'queued' state


        :return: The queued of this MirrorSyncStatus.
        :rtype: int
        """
        return self._queued

    @queued.setter
    def queued(self, queued):
        """
        Sets the queued of this MirrorSyncStatus.
        Total of mirrors in 'queued' state


        :param queued: The queued of this MirrorSyncStatus.
        :type: int
        """
        self._queued = queued

    @property
    def syncing(self):
        """
        **[Required]** Gets the syncing of this MirrorSyncStatus.
        Total of mirrors in 'syncing' state


        :return: The syncing of this MirrorSyncStatus.
        :rtype: int
        """
        return self._syncing

    @syncing.setter
    def syncing(self, syncing):
        """
        Sets the syncing of this MirrorSyncStatus.
        Total of mirrors in 'syncing' state


        :param syncing: The syncing of this MirrorSyncStatus.
        :type: int
        """
        self._syncing = syncing

    @property
    def synced(self):
        """
        **[Required]** Gets the synced of this MirrorSyncStatus.
        Total of mirrors in 'synced' state


        :return: The synced of this MirrorSyncStatus.
        :rtype: int
        """
        return self._synced

    @synced.setter
    def synced(self, synced):
        """
        Sets the synced of this MirrorSyncStatus.
        Total of mirrors in 'synced' state


        :param synced: The synced of this MirrorSyncStatus.
        :type: int
        """
        self._synced = synced

    @property
    def failed(self):
        """
        **[Required]** Gets the failed of this MirrorSyncStatus.
        Total of mirrors in 'failed' state


        :return: The failed of this MirrorSyncStatus.
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """
        Sets the failed of this MirrorSyncStatus.
        Total of mirrors in 'failed' state


        :param failed: The failed of this MirrorSyncStatus.
        :type: int
        """
        self._failed = failed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

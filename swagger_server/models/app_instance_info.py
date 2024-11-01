# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.app_instance_id import AppInstanceId  # noqa: F401,E501
from swagger_server.models.app_instance_info_component_endpoint_info import AppInstanceInfoComponentEndpointInfo  # noqa: F401,E501
from swagger_server.models.edge_cloud_zone import EdgeCloudZone  # noqa: F401,E501
from swagger_server import util


class AppInstanceInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, app_instance_id: AppInstanceId=None, status: str='unknown', component_endpoint_info: List[AppInstanceInfoComponentEndpointInfo]=None, edge_cloud_zone: EdgeCloudZone=None):  # noqa: E501
        """AppInstanceInfo - a model defined in Swagger

        :param app_instance_id: The app_instance_id of this AppInstanceInfo.  # noqa: E501
        :type app_instance_id: AppInstanceId
        :param status: The status of this AppInstanceInfo.  # noqa: E501
        :type status: str
        :param component_endpoint_info: The component_endpoint_info of this AppInstanceInfo.  # noqa: E501
        :type component_endpoint_info: List[AppInstanceInfoComponentEndpointInfo]
        :param edge_cloud_zone: The edge_cloud_zone of this AppInstanceInfo.  # noqa: E501
        :type edge_cloud_zone: EdgeCloudZone
        """
        self.swagger_types = {
            'app_instance_id': AppInstanceId,
            'status': str,
            'component_endpoint_info': List[AppInstanceInfoComponentEndpointInfo],
            'edge_cloud_zone': EdgeCloudZone
        }

        self.attribute_map = {
            'app_instance_id': 'appInstanceId',
            'status': 'status',
            'component_endpoint_info': 'componentEndpointInfo',
            'edge_cloud_zone': 'edgeCloudZone'
        }
        self._app_instance_id = app_instance_id
        self._status = status
        self._component_endpoint_info = component_endpoint_info
        self._edge_cloud_zone = edge_cloud_zone

    @classmethod
    def from_dict(cls, dikt) -> 'AppInstanceInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AppInstanceInfo of this AppInstanceInfo.  # noqa: E501
        :rtype: AppInstanceInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_instance_id(self) -> AppInstanceId:
        """Gets the app_instance_id of this AppInstanceInfo.


        :return: The app_instance_id of this AppInstanceInfo.
        :rtype: AppInstanceId
        """
        return self._app_instance_id

    @app_instance_id.setter
    def app_instance_id(self, app_instance_id: AppInstanceId):
        """Sets the app_instance_id of this AppInstanceInfo.


        :param app_instance_id: The app_instance_id of this AppInstanceInfo.
        :type app_instance_id: AppInstanceId
        """

        self._app_instance_id = app_instance_id

    @property
    def status(self) -> str:
        """Gets the status of this AppInstanceInfo.

        Status of the application instance (default is 'unknown')  # noqa: E501

        :return: The status of this AppInstanceInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this AppInstanceInfo.

        Status of the application instance (default is 'unknown')  # noqa: E501

        :param status: The status of this AppInstanceInfo.
        :type status: str
        """
        allowed_values = ["ready", "instantiating", "failed", "terminating", "unknown"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def component_endpoint_info(self) -> List[AppInstanceInfoComponentEndpointInfo]:
        """Gets the component_endpoint_info of this AppInstanceInfo.

        Information about the IP and Port exposed by the Edge Cloud Platform. Application Client shall use these access points to reach this application instance   # noqa: E501

        :return: The component_endpoint_info of this AppInstanceInfo.
        :rtype: List[AppInstanceInfoComponentEndpointInfo]
        """
        return self._component_endpoint_info

    @component_endpoint_info.setter
    def component_endpoint_info(self, component_endpoint_info: List[AppInstanceInfoComponentEndpointInfo]):
        """Sets the component_endpoint_info of this AppInstanceInfo.

        Information about the IP and Port exposed by the Edge Cloud Platform. Application Client shall use these access points to reach this application instance   # noqa: E501

        :param component_endpoint_info: The component_endpoint_info of this AppInstanceInfo.
        :type component_endpoint_info: List[AppInstanceInfoComponentEndpointInfo]
        """

        self._component_endpoint_info = component_endpoint_info

    @property
    def edge_cloud_zone(self) -> EdgeCloudZone:
        """Gets the edge_cloud_zone of this AppInstanceInfo.


        :return: The edge_cloud_zone of this AppInstanceInfo.
        :rtype: EdgeCloudZone
        """
        return self._edge_cloud_zone

    @edge_cloud_zone.setter
    def edge_cloud_zone(self, edge_cloud_zone: EdgeCloudZone):
        """Sets the edge_cloud_zone of this AppInstanceInfo.


        :param edge_cloud_zone: The edge_cloud_zone of this AppInstanceInfo.
        :type edge_cloud_zone: EdgeCloudZone
        """

        self._edge_cloud_zone = edge_cloud_zone

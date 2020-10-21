# -*- coding: utf-8 -*-

from .resource import NamespacedResource


class Service(NamespacedResource):
    """
    OpenShift Service object.
    """

    api_version = NamespacedResource.ApiVersion.V1

    class Type:
        CLUSTER_IP = "ClusterIP"
        NODE_PORT = "NodePort"

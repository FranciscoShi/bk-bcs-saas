# -*- coding: utf-8 -*-
#
# Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community Edition) available.
# Copyright (C) 2017-2019 THL A29 Limited, a Tencent company. All rights reserved.
# Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
from django.conf.urls import include, url

from backend.resources.deployment.constants import DEPLOYMENT_REGEX
from backend.resources.namespace.constants import NAMESPACE_REGEX
from backend.resources.pod.constants import POD_REGEX

from .cluster import ClusterViewSet
from .deployment import DeploymentViewSet
from .namespace import NamespaceViewSet
from .node import NodeLabelsViewSet
from .pod import PodViewSet

urlpatterns = [
    url(r"^$", ClusterViewSet.as_view({"get": "list"})),
    url(r"^(?P<cluster_id>[\w\-]+)/crds/", include("backend.apis.resources.custom_object.urls")),
    url(
        r"^(?P<cluster_id>[\w\-]+)/namespaces/$",
        NamespaceViewSet.as_view({"get": "list_by_cluster_id", "post": "create_namespace"}),
    ),
    url(
        r"^(?P<cluster_id>[\w\-]+)/sync_namespaces/$",
        NamespaceViewSet.as_view({"put": "sync_namespaces"}),
    ),
    url(r"^(?P<cluster_id>[\w\-]+)/nodes/-/labels/$", NodeLabelsViewSet.as_view({"post": "set_labels"})),
    url(
        r"^(?P<cluster_id>[\w\-]+)/namespaces/(?P<namespace>%s)/deployments/$" % NAMESPACE_REGEX,
        DeploymentViewSet.as_view({"get": "list_by_namespace"}),
    ),
    url(
        r"^(?P<cluster_id>[\w\-]+)/namespaces/(?P<namespace>%s)/deployments/(?P<deploy_name>%s)/pods/$"
        % (NAMESPACE_REGEX, DEPLOYMENT_REGEX),
        DeploymentViewSet.as_view({"get": "list_pods_by_deployment"}),
    ),
    url(
        r"^(?P<cluster_id>[\w\-]+)/namespaces/(?P<namespace>%s)/pods/(?P<pod_name>%s)/$"
        % (NAMESPACE_REGEX, POD_REGEX),
        PodViewSet.as_view({"get": "get_pod"}),
    ),
]

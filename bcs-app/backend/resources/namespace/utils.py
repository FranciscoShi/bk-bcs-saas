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
from backend.components import paas_cc
from backend.components.bcs.k8s import K8SClient
from backend.utils.decorators import parse_response_data
from backend.utils.errcodes import ErrorCode
from backend.utils.error_codes import error_codes


def get_cc_namespaces(access_token, project_id):
    resp = paas_cc.get_namespace_list(access_token, project_id, desire_all_data=True)
    if resp.get("code") != ErrorCode.NoError:
        raise error_codes.APIError(f"get namespace error, {resp.get('message')}")
    return resp.get("data", {}).get("results", [])


@parse_response_data(default_data={})
def _get_cluster_namespace_list(access_token, project_id, cluster_id):
    return paas_cc.get_cluster_namespace_list(access_token, project_id, cluster_id, desire_all_data=True)


def get_namespaces_by_cluster_id(access_token, project_id, cluster_id):
    # TODO get_namespaces_by_cluster_id后续会调整成直接从集群获取，而不是从bcs-cc获取
    data = _get_cluster_namespace_list(access_token, project_id, cluster_id)
    return data.get('results', [])


@parse_response_data(default_data={})
def _get_namespace_list(access_token, project_id):
    return paas_cc.get_namespace_list(access_token, project_id, desire_all_data=True)


def get_namespaces(access_token, project_id):
    data = _get_namespace_list(access_token, project_id)
    return data.get('results', [])


@parse_response_data(default_data={})
def get_namespace_by_id(access_token, project_id, namespace_id):
    return paas_cc.get_namespace(access_token, project_id, namespace_id)


@parse_response_data(default_data=[])
def get_k8s_namespaces(access_token, project_id, cluster_id):
    """获取集群中实时的namespace"""
    client = K8SClient(access_token, project_id, cluster_id, env=None)
    return client.get_namespace()


def delete_cc_namespace(access_token, project_id, cluster_id, namespace_id):
    resp = paas_cc.delete_namespace(access_token, project_id, cluster_id, namespace_id)
    if resp.get("code") != ErrorCode.NoError:
        raise error_codes.APIError(f"delete namespace error, {resp.get('message')}")


@parse_response_data()
def create_cc_namespace(access_token, project_id, cluster_id, namespace, creator):
    return paas_cc.create_namespace(access_token, project_id, cluster_id, namespace, None, creator, "prod", False)

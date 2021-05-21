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
from typing import Any, Dict

from rest_framework import permissions, viewsets
from rest_framework.renderers import BrowsableAPIRenderer

from backend.utils.renderers import BKAPIRenderer

from .authentication import JWTAndTokenAuthentication
from .permissions import AccessProjectPermission, ProjectEnableBCS


class GenericMixin:
    @staticmethod
    def get_request_data(request, **kwargs) -> Dict[str, Any]:
        request_data = request.data.copy() or {}
        request_data.update(**kwargs)
        return request_data

    def params_validate(self, serializer, params=None):
        """
        检查参数是够符合序列化器定义的通用逻辑

        :param serializer: 序列化器
        :param params: 指定的参数
        :return: 校验的结果
        """
        # 获取 Django request 对象
        _request = self.request

        if params is None:
            if _request.method in ['GET']:
                params = _request.query_params
            else:
                params = _request.data

        # 参数校验，如不符合直接抛出异常
        slz = serializer(data=params)
        slz.is_valid(raise_exception=True)
        return slz.validated_data


class SystemViewSet(GenericMixin, viewsets.ViewSet):
    """
    容器服务 SaaS app 使用的 API view
    - 仅支持处理 url 路径参数中包含 project_id 或 project_id_or_code 的请求
    - 需要验证用户登录态
    - ProjectEnableBCS: 验证通过后，会创建 request.project、request.ctx_project 和 request.ctx_cluster，在 view 中使用
    """

    renderer_classes = (BKAPIRenderer, BrowsableAPIRenderer)
    # authentication_classes配置在REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"]中
    permission_classes = (permissions.IsAuthenticated, AccessProjectPermission, ProjectEnableBCS)


class UserViewSet(GenericMixin, viewsets.ViewSet):
    """
    提供给流水线等第三方服务的API view
    - 仅支持处理 url 路径参数中包含 project_id 或 project_id_or_code 的请求
    - JWTAndTokenAuthentication: 需要传入有效的 JWT 以便验证请求来源; 同时，也会将 HTTP_X_BKAPI_TOKEN 或平台的 access_token
    赋值给 request.user.token.access_token
    - ProjectEnableBCS: 验证通过后，会创建 request.project、request.ctx_project 和 request.ctx_cluster，在 view 中使用
    """

    renderer_classes = (BKAPIRenderer,)
    authentication_classes = (JWTAndTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, AccessProjectPermission, ProjectEnableBCS)

"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import dictresult as components_dictresult
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class TextTopicWrapperTextTopicPostRequest:
    UNSET='__SPEAKEASY_UNSET__'
    num_classes: str = dataclasses.field(metadata={'query_param': { 'field_name': 'num_classes', 'style': 'form', 'explode': True }})
    request_body: str = dataclasses.field(metadata={'request': { 'media_type': 'text/plain' }})
    explanation: Optional[bool] = dataclasses.field(default=True, metadata={'query_param': { 'field_name': 'explanation', 'style': 'form', 'explode': True }})
    api_key: Optional[str] = dataclasses.field(default=UNSET, metadata={'header': { 'field_name': 'api-key', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class TextTopicWrapperTextTopicPostResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    dict_result: Optional[components_dictresult.DictResult] = dataclasses.field(default=None)
    r"""Successful Response"""
    

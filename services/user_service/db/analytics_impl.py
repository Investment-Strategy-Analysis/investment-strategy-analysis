import logging
import os
from fastapi import status
from typing import List, Optional
from elasticsearch import Elasticsearch
from fastapi import HTTPException
from services.user_service.common.abstract import AnalyticItem, AnalyticQuery
from services.user_service.common.consts import ADMIN, ELASTICSEARCH_HOST, RESTRICTION_INDEX

es = Elasticsearch(ELASTICSEARCH_HOST, http_auth=(os.environ["ELASTICSEARCH_USERNAME"], os.environ["ELASTICSEARCH_PASSWORD"]))


def __check_login(login: str):
    if login != ADMIN:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User does not have permission to view analytics"
        )


def get_analytics_item(login: str, id: str) -> Optional[AnalyticItem]:
    __check_login(login)
    try:
        res = es.get(index=RESTRICTION_INDEX, id=id)
        return AnalyticItem.parse_obj(res['_source'])
    except:
        return None


def get_analytics(login: str, query: AnalyticQuery) -> List[str]:
    __check_login(login)
    es.indices.refresh(index=RESTRICTION_INDEX)
    try:
        res = es.search(index=RESTRICTION_INDEX, query=query.query)
        return list(map(lambda x: x["_id"], res['hits']['hits']))
    except:
        logging.warning(f"wrong query {query.query}")
    return []


def post_analytics_item(login: str, item: AnalyticItem) -> str:
    res = es.index(index=RESTRICTION_INDEX, document=item.dict())
    if res["result"] != "created":
        logging.warning("analytic item not saved, internal error")
    return res["_id"]

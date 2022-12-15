from typing import List, Optional
from services.user_service.common.abstract import AnalyticItem, AnalyticQuery
from services.user_service.db.analytics_impl import get_analytics_item as __get_analytics_item
from services.user_service.db.analytics_impl import get_analytics as __get_analytics
from services.user_service.db.analytics_impl import post_analytics_item as __post_analytics_item


def get_analytics_item(login: str, id: str) -> Optional[AnalyticItem]:
    return __get_analytics_item(login, id)


def get_analytics(login: str, query: AnalyticQuery) -> List[str]:
    return __get_analytics(login, query)


def post_analytics_item(login: str, item: AnalyticItem) -> str:
    return __post_analytics_item(login, item)

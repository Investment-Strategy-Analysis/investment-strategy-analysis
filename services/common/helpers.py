from services.common.abstract import AnalysisTime, AnalysisTimeInfo


def to_analysis_time(self) -> AnalysisTime:
    if self == AnalysisTime.DAY_1.value.id:
        return AnalysisTime.DAY_1
    if self == AnalysisTime.DAY_100.value.id:
        return AnalysisTime.DAY_100
    if self == AnalysisTime.YEAR_1.value.id:
        return AnalysisTime.YEAR_1
    if self == AnalysisTime.YEAR_3.value.id:
        return AnalysisTime.YEAR_3
    if self == AnalysisTime.YEAR_5.value.id:
        return AnalysisTime.YEAR_5
    if self == AnalysisTime.YEAR_10.value.id:
        return AnalysisTime.YEAR_10
    raise Exception("wrong analysis time")

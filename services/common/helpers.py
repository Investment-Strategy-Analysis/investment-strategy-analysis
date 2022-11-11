from services.common.abstract import AnalysisTime


def to_analysis_time(self) -> AnalysisTime:
    if self == AnalysisTime.DAY_1.name:
        return AnalysisTime.DAY_1
    if self == AnalysisTime.DAY_100.name:
        return AnalysisTime.DAY_100
    if self == AnalysisTime.YEAR_1.name:
        return AnalysisTime.YEAR_1
    if self == AnalysisTime.YEAR_3.name:
        return AnalysisTime.YEAR_3
    if self == AnalysisTime.YEAR_5.name:
        return AnalysisTime.YEAR_5
    if self == AnalysisTime.YEAR_10.name:
        return AnalysisTime.YEAR_10
    raise Exception("wrong analysis time")

from services.common.abstract import InvestStrategy

STRATEGIES = {
    "strategy_1": InvestStrategy(id="strategy_1", description="RTSI=1, RTSOG=0", profit=25, risk=10, distribution={"RTSI": 1, "RTSOG": 0}),
    "strategy_2": InvestStrategy(id="strategy_2", description="RTSI=0.75, RTSOG=0.25", profit=20, risk=7, distribution={"RTSI": 0.75, "RTSOG": 0.25}),
    "strategy_3": InvestStrategy(id="strategy_3", description="RTSI=0.5, RTSOG=0.5", profit=15, risk=5, distribution={"RTSI": 0.5, "RTSOG": 0.5}),
    "strategy_4": InvestStrategy(id="strategy_4", description="RTSI=0.25, RTSOG=0.75", profit=10, risk=4, distribution={"RTSI": 0.25, "RTSOG": 0.75}),
    "strategy_5": InvestStrategy(id="strategy_5", description="RTSI=0, RTSOG=1", profit=5, risk=5, distribution={"RTSI": 0, "RTSOG": 1})
}   # FIXME(rename ids)

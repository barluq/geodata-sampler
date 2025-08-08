from enum import Enum

class DatePeriod(Enum):
    YEAR = "year"
    MONTH = "month"
    DAY = "day"


def time_step_by_period_sec(desired_period: DatePeriod) -> int:

    if desired_period == DatePeriod.YEAR:
        return 1 * 365 * 24 * 60 * 60
    elif desired_period == DatePeriod.MONTH:
        return 12 * 30 * 24 * 60 * 60
    elif desired_period == DatePeriod.DAY:
        return 365 * 24 * 60 * 60
    else:
        raise ValueError(f"Unsupported period: {desired_period}")
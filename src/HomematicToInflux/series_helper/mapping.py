from dataclasses import dataclass
from typing import Type, TypeVar

from influxdb import SeriesHelper

from HomematicToInflux.series_helper import STHStateSeriesHelper, ETRV2StateSeriesHelper, FALMOTC12StateSeriesHelper, \
    STHOStateSeriesHelper, SWDOStateSeriesHelper, PSMStateSeriesHelper, ESTXWMStateSeriesHelper


SeriesHelperType = TypeVar('SeriesHelperType', bound=SeriesHelper)

helper_mapping: dict[str, type[SeriesHelperType]] = {
    "hmip-sth": STHStateSeriesHelper,
    "hmip-etrv-2": ETRV2StateSeriesHelper,
    "hmip-falmot-c12": FALMOTC12StateSeriesHelper,
    "hmip-stho": STHOStateSeriesHelper,
    'hmip-swdo': SWDOStateSeriesHelper,
    'hmip-psm': PSMStateSeriesHelper,
    #    'HmIP-RCV-50': RCV50StateSeriesHelper,
    'hm-es-tx-wm': ESTXWMStateSeriesHelper,
}

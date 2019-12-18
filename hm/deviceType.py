from enum import Enum, unique


@unique
class DeviceType(Enum):
    STH = "HmIP-STH"
    ETRV2 = "HmIP-eTRV-2"
    FALMOTC12 = "HmIP-FALMOT-C12"
    STHO = "HmIP-STHO"
    SWDO = 'HMIP-SWDO'
    PSM = 'HMIP-PSM'
    RCV50 = 'HmIP-RCV-50'

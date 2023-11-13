from enum import Enum


class ValueType(Enum):
    ivtBinary = 2
    ivtFloat = 4
    ivtInteger = 16
    ivtString = 20
    ivtRSSI = 8


class ValueSubType(Enum):
    istPresent = 23  # Anwesenheit
    istAlarm = 6  # Alarm
    istGeneric = 0  # zahl
    istBool = 2  # Logikwert
    istEnum = 29  # Werteliste
    istChar8859 = 11  # zeichenkette


class DeviceType(Enum):
    STH = "HmIP-STH"
    ETRV2 = "HmIP-eTRV-2"
    FALMOTC12 = "HmIP-FALMOT-C12"
    STHO = "HmIP-STHO"
    SWDO = "HMIP-SWDO"
    PSM = "HMIP-PSM"
    RCV50 = "HmIP-RCV-50"
    ESTXWM = "HM-ES-TX-WM"

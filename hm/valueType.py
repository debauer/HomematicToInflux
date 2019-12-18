from enum import Enum, unique


@unique
class ValueType(Enum):
    ivtBinary = 2
    ivtFloat = 4
    ivtInteger = 16
    ivtString = 20
    ivtRSSI = 8

@unique
class ValueSubType(Enum):
    istPresent = 23  # Anwesenheit
    istAlarm = 6  # Alarm
    istGeneric = 0  # zahl
    istBool = 2  # Logikwert
    istEnum = 29  # Werteliste
    istChar8859 = 11  # zeichenkette

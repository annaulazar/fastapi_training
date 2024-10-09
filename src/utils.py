from enum import StrEnum, IntEnum


class EducationLevel(StrEnum):
    SECONDARY = "Среднее образование"
    SPECIAL = "Среднее специальное образование"
    HIGHER = "Высшее образование"


class SolarObjects(IntEnum):
    Sun = 1392000
    Jupiter = 139822
    Saturn = 116464
    Uranus = 50724
    Neptune = 49224
    Earth = 12742
    Venus = 12104
    Mars = 6780
    Ganymede = 5262
    Titan = 5151
    Mercury = 4879


class Tag(StrEnum):
    T1 = 'immutable'
    T2 = 'mutable'

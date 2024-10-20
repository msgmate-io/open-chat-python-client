from enum import Enum


class DataTypeEnum(str, Enum):
    AUDIO_B64 = "audio_b64"
    CUSTOM = "custom"
    SIGNAL = "signal"

    def __str__(self) -> str:
        return str(self.value)

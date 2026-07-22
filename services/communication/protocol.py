from dataclasses import dataclass
from typing import Any


@dataclass
class ProtocolMessage:
    """
    Gói tin trao đổi giữa Server và Agent.
    """

    command: str

    payload: Any = None

    success: bool = True

    message: str = ""
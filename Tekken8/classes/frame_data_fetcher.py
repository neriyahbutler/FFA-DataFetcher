"""
d
"""

from abc import ABC, abstractmethod
from typing import List
import json

class FrameDataFetcher(ABC):
    """
    d
    """
    def __init__(self,
                 character_names):
        self.character_names: List[str] = character_names

    @abstractmethod
    def fetch_frame_data(self,
                         game_name: str,
                         character_name: str):
        pass

    @abstractmethod
    def save_frame_data(self,
                        game_name: str,
                        character_name: str,
                        json_conent: json):
        pass

    # def populate_raw_data_folder(self):
    #     for character in self.character_names:
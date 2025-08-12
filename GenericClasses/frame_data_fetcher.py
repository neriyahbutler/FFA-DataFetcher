"""
d
"""

from abc import ABC, abstractmethod
from typing import List
import json

class FrameDataFetcher(ABC):
    """
    An abstract class dedicated for fetching frame data

    Attributes:
    - character_names (str)
    """
    def __init__(self,
                 character_names,
                 game_name):
        self.character_names: List[str] = character_names
        self.game_name: str = game_name

    @abstractmethod
    def fetch_frame_data(self,
                         character_name: str) -> json:
        """
        An abstract method dedicated for fetching frame data
        on the specified character
        """
        pass

    @abstractmethod
    def save_frame_data(self,
                        game_name: str,
                        character_name: str,
                        json_conent: json):
        """
        An abstract method dedicated for saving the frame data
        json as an actual json data in the raw data folder
        """
        pass

    @abstractmethod
    def populate_raw_data_folder(self):
        """
        Iterates through each character in the 'character_names',
        obtains the frame data for each character and saves the data
        into a raw data folder
        """
        pass
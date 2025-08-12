"""
Class dedicated for obtaining the latest frame data for the Tekken 8 characters
"""

import os
import json
import time
import requests # pyright: ignore[reportMissingModuleSource]
from .character_list import character_list
from GenericClasses.frame_data_fetcher import FrameDataFetcher

class Tekken8DataFetcher(FrameDataFetcher):
    """
    A class dedicated for grabbing frame data specifically
    for Tekken 8 characters
    """

    def __init__(self,
                 game_name: str = "Tekken8"):
        FrameDataFetcher.__init__(self,
                                  character_names=character_list,
                                  game_name=game_name)

    def generate_frame_data_endpoint(self, character_name: str) -> str:
        """
        Returns a formatted string of the Tekken API endpoint
        """
        return f'https://tekkendocs.com/api/t8/{character_name}/framedata'

    def fetch_frame_data(self, character_name) -> json:
        """
        Fetches frame data using a generated endpoint
        """
        url: str = self.generate_frame_data_endpoint(character_name=character_name)
        response = requests.get(url, timeout=5)
        print(f'Response returned with value of {response.status_code}')

        return response.json()

    def save_frame_data(self, character_name, frame_data_json: json):
        """
        Saves frame data json content passed as parameter into 'raw_data' folder
        """
        directory_path: str = f'./T8/raw_data/{character_name}'
        file_path: str = f'{directory_path}/{character_name}.json'
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        with open(file_path, "w", encoding='utf-8') as f:
            print(f'Writing json content to file in "{file_path}"')
            f.write(frame_data_json)

    def populate_raw_data_folder(self):
        """
        The method dedicated for obtaining all of the frame data for the Tekken 8
        characters and saving them into the 'raw_data' folder to be processed.
        """
        for character in self.character_names:
            frame_data_json: json = self.fetch_frame_data(character_name=character)
            self.save_frame_data(character_name=character,
                                 frame_data_json= json.dumps(frame_data_json))
            time.sleep(1)

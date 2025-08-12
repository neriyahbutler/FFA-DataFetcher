from T8.tekken8_data_fetcher import Tekken8DataFetcher

def main():
    tekken8_frame_data_fetcher = Tekken8DataFetcher()
    tekken8_frame_data_fetcher.populate_raw_data_folder()

if __name__ == '__main__':
    main()

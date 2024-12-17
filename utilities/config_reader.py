import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FILE_PATH = os.path.join(PROJECT_ROOT, 'config', 'config.yaml')

class ConfigReader:

    def __init__(self):
        with open(FILE_PATH) as file:
            self.data = file.readlines()


    def get_file_path(self, dir_name):

         return os.path.join(PROJECT_ROOT, dir_name)


    def fetch_data_from_config_file(self, key: str) -> str:
        """
        Description:
            |   This function will read the data from the config file
        :return: string
        """
        try:
            return {x.split(": ")[0].replace("'", ""): x.split(": ")[1].strip() for x in self.data}[key].replace("'", "")
        except KeyError as e:
            print(f"Key {key} not found in the config file")
            return ""



if __name__ == '__main__':
    obj = ConfigReader()
    print(obj.fetch_data_from_config_file("driver_pat"))



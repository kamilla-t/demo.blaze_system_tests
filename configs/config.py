from configparser import ConfigParser
import os


class Config:

    def __init__(self, env = "") -> None:
        # get current dir for configs
        current_dir = os.path.dirname(__file__)

        # condition for multi environments
        config_path = ""
        if env == "":
            config_path = os.path.join(current_dir, "config.ini")
        else:
            config_path = os.path.join(current_dir, f"config.{env}.ini")
        self._config = ConfigParser(allow_no_value=True)
        self._config.read(config_path)


    @property
    def Url(self):
        return self._config["GENERAL"]["Url"]

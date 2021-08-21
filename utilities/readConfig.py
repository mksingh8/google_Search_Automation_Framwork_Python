import configparser

config = configparser.RawConfigParser()
config.read("/home/manish/Documents/Programming/Python/pythonProject/google_Search_Automation_Framwork_Python"
            "/Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common data', 'url')
        return url


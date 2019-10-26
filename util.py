import os


def setup_credentials():
    credential_path = "YHack-2019-a87246a5ff6d.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from utils.log import *
from utils.config import *

GLOBLA_CONFIG = config.loadConfig()

def check_version(speak=True):
    """
    check the version number for updates
    """
    version_url = "https://raw.githubusercontent.com/noobpk/frida-android-hook/master/frida-android-hook/core/hook.json"
    try:
        req = requests.get(version_url)
        content = req.text
        version_identification = content.find('"version": ')
        current_version = content[version_identification:version_identification + 16]
        current_version = str(current_version.strip().split('"')[3])
        my_version = GLOBLA_CONFIG['version']
        if not current_version == my_version:
            if speak:
                logger.info('[*] New version: {} is available'.format(current_version))
                return False
            else:
                return False
        else:
            if speak:
                logger.info('[*] AndroidHook already up to date.')
                return True
    except Exception:
        logger.error("[x_x] Error checking version, try again laster.")
        return True

# if __name__ == '__main__':
#     check_version()
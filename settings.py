import os
import platform

DOMAIN = 'https://www.thumbtack.com/pro'
driver_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          'driver')

if platform.system() == 'Windows':
    DRIVER = str(os.path.join(driver_dir,
                              'windows') + '\\' + 'chromedriver.exe')

if platform.system() == 'Linux':
    if platform.machine() == 'x86_64':
        pass
    if platform.machine() == 'i386':
        pass

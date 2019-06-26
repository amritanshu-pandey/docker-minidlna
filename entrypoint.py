import os
import subprocess

CONFIG_FILE = '/etc/minidlna'

for each_env in os.environ:
    if each_env.startswith('cfg_'):
        with open(CONFIG_FILE, 'a') as cfg:
            cfg.write(f'{each_env[4:]}={os.environ[each_env]}')


subprocess.call('/usr/sbin/minidlnad -d'.split())

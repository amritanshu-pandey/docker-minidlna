import os
import subprocess

CONFIG_FILE = '/etc/minidlna'

for each_env in os.environ:
    if each_env.startswith('cfg_'):
        if each_env.startswith('cfg_media_dir'):
            key = 'media_dir'
        else:
            key = each_env[4:]

        with open(CONFIG_FILE, 'a') as cfg:
            cfg.write(f'{key}={os.environ[each_env]}')


subprocess.call('/usr/sbin/minidlnad -d'.split())

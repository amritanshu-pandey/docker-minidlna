docker-minidlna
===============

Docker image for a minidlna media server.

## Features

1. Support for specifying multiple media directories along with media type.
> Any environment variable that starts with `cfg_media_dir` maps to a media directory.

for e.g. `cfg_media_dir_shows=V,/media/shows` maps to media directory `/media/shows` and media type `Video`

2. Ability to specify any option supported in `minidlna` config file, using environment variables
> Any environment variable that starts with `cfg_` but is not a media directory config, translates to an option
  specified in `/etc/minidlna.conf`.

for e.g. `cfg_friendly_name=xpsnas-docker` correspnds to `friendly_name=xpsnas-docker`


## How to use the image

### `Docker-Compose`

```yaml
version: '2'
services:
  server:
    image: amritanshu16/minidlna-server:latest
    read_only: true
    network_mode: "host"
    ports:
      - "8200:8200"
    volumes:
      - "/sharedfolders/Entertainment/Shows/:/media/shows"
      - "/sharedfolders/Entertainment/Movies/:/media/movies"
    environment:
      - cfg_media_dir_shows=V,/media/shows
      - cfg_media_dir_movies=V,/media/movies
      - cfg_friendly_name=xpsnas-docker
    restart: always
```

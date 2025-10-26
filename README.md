# Bustijden for Home Assistant

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=Remco+Kersten&repository=https%3A%2F%2Fgithub.com%2Fkerstenremco%2Fhacs-busvertrektijden)

## Installation

- Add repo to hacs
- Download hacs
- Add config

```
sensor:
  - platform: bustijden
    stop_ids: '3390096,3390097,3430629,3430630,3470439,3470440'
    stop_name: 'Rembrand van Rijnstraat'
    stop_amount: 8
```

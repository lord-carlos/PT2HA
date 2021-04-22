#!/usr/bin/env python3

class HomeAssistant:
    def __init__(self, devices, url, auth_key):
        self.devices = devices
        self.url = url
        self.auth_key = auth_key

    def change_color(self, color):
        from requests import get
        import requests, json

        url = self.url + "/api/services/light/turn_on"
        headers = {
            "Authorization": "Bearer " + self.auth_key,
            "content-type": "application/json",
        }
        data = {"entity_id": self.devices, "color_name": color}

        response = requests.post(url, data=json.dumps(data), headers=headers)
        print(response.text)


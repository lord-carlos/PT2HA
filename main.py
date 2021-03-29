#!/usr/bin/env python3

import configparser


def main():

    config = configparser.ConfigParser()
    config.read('config.ini')

    username = config['twitch']['username']
    client_id = config['twitch']['client_id']
    token = config['twitch']['token']
    channel = config['twitch']['channel']

    devices = config['homeassistant']['devices']
    auth_key = config['homeassistant']['auth_key']
    url = config['homeassistant']['url']
    print(username)



if __name__ == "__main__":
    main()
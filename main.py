#!/usr/bin/env python3

import configparser
from bot import TwitchBot
from home_assistant import HomeAssistant


def main():

    config = configparser.ConfigParser()
    config.read('config.ini')

    username = config['twitch']['username']
    client_id = config['twitch']['client_id']
    token = config['twitch']['token']
    channel = config['twitch']['channel']
    reward_id = config['twitch']['reward_id']

    devices = config['homeassistant']['devices']
    auth_key = config['homeassistant']['auth_key']
    url = config['homeassistant']['url']
    
    # print(username)
    # print(client_id)
    # print(token)
    # print(channel)
    # print(devices)
    # print(auth_key)
    # print(url)

    homeassistant = HomeAssistant(devices, url, auth_key)

    bot = TwitchBot(username, client_id, token, channel, reward_id, homeassistant)
    bot.start()



if __name__ == "__main__":
    main()
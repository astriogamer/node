from sys import prefix
from random import randint
from weakref import proxy
from xmlrpc import server
from requests.api import request
from discord.utils import get
import re
import random
import threading
import fade
from discord import channel, message
from discord.enums import Theme
from urllib.request import Request, urlopen
import discord, requests, json, os, shutil, subprocess, aiohttp, asyncio, sys, colorama, time, discum, random, datetime, ctypes
from discord.ext.commands.core import command
import fade
from pypresence import Presence
from discord.ext.commands import CommandNotFound
from time import gmtime, sleep, strftime
from colorama import Fore, init
from discord.ext import commands    
from itertools import cycle
import threading
token = "NDc2ODAxNjQ5MTY4NjEzNDA3.YgiMMg.PQ6CZqE6gBt51v116RsaSpCxi1w"
hummus = discord.Client()
hummus = commands.Bot(command_prefix=">", self_bot=True, case_insensitive=True, auto_reconnect=True)
hummus.remove_command('help')
@hummus.event
async def on_connect():
    print(hummus.user )
headers = {
        "Authorization":    token,
        "accept":    "*/*",
        "accept-language":    "en-US",
        "accept-encoding" : "gzip, deflate, br",
        "cookie":    f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
        "origin":    "https://discord.com",
        "sec-fetch-dest":    "empty",
        "sec-fetch-mode":    "cors",
        "sec-fetch-site":    "same-origin",
        "referer":    "https://discord.com/channels/@me",
        "x-context-properties": "eyJsb2NhdGlvbiI6IkFkZCBGcmllbmQifQ==",
        "User-Agent":    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
        "X-Super-Properties":    "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"}

@hummus.command()
async def spam(ctx):
    spams = input("balls")
    for i in range(50):
        for channels in ctx.guild.channels:
            try:
                msg = await channels.send(spams)
                print(f"Sent msg in {channels}")
                await msg.delete()
                print(f"deleted msg in {msg.channel}")
            except Exception as e:
                pass


@hummus.command()
async def e(ctx):
    for channels in ctx.guild.channels:
        json = {"name": "Hi", "type": "11", "auto_archive_duration": "1440", "location": "Thread Browser Toolbar"}
        try:
            channel = channels.id
            r = requests.post(f"https://discord.com/api/v9/channels/{channel}/threads", headers=headers, json=json)
        except:
            pass
        print(r.json())
        rj = r.json()
        print(r.status_code)
        if r.status_code == 429:
            time.sleep(2)
            r = requests.post(f"https://discord.com/api/v9/channels/{channel}/threads", headers=headers, json=json)
@hummus.command()
async def w(ctx):
    for channels in ctx.guild.channels:
        print(channels.id)

def statuschange():
    while True:
        json = {"status" : "invisible"}
        headers = {
        "Authorization":    token,
        "accept":    "*/*",
        "accept-language":    "en-US",
        "accept-encoding" : "gzip, deflate, br",
        "cookie":    f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
        "origin":    "https://discord.com",
        "sec-fetch-dest":    "empty",
        "sec-fetch-mode":    "cors",
        "sec-fetch-site":    "same-origin",
        "referer":    "https://discord.com/channels/@me",
        "x-context-properties": "eyJsb2NhdGlvbiI6IkFkZCBGcmllbmQifQ==",
        "User-Agent":    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
        "X-Super-Properties":    "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"}
        r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers,json=json)
        time.sleep(5)
        json = {"status" : "online"}
        r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers,json=json)
        time.sleep(5)
        json = {"status" : "dnd"}
        r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers,json=json)
        time.sleep(5)
        json = {"status" : "idle"}
        r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers,json=json)
        time.sleep(5)
def namechange():
    while True:
        headers = {
        "Authorization":    token,
        "accept":    "*/*",
        "accept-language":    "en-US",
        "accept-encoding" : "gzip, deflate, br",
        "cookie":    f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
        "origin":    "https://discord.com",
        "sec-fetch-dest":    "empty",
        "sec-fetch-mode":    "cors",
        "sec-fetch-site":    "same-origin",
        "referer":    "https://discord.com/channels/@me",
        "x-context-properties": "eyJsb2NhdGlvbiI6IkFkZCBGcmllbmQifQ==",
        "User-Agent":    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",}
        json = {"text": "I love You", "expires_at": "2022-02-12T07:59:59.999Z"}
        r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers,json=json)
        print(r.status_code)
        time.sleep(10)
        json = {"text": "I love two", "expires_at": "2022-02-12T07:59:59.999Z"}
        r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers,json=json)
        print(r.status_code)
        time.sleep(10)
@hummus.command()
async def a(ctx):
    threading.Thread(target=statuschange, args=(),).start()
    threading.Thread(target=namechange, args=(),).start()
@hummus.command()
async def k(ctx):
    x = 79208
    while x >= 0:
        randbyte = random.randbytes(17)
        time.sleep(60)
        headers = {
            "Authorization":    token,
            "accept":    "*/*",
            "accept-language":    "en-US",
            "accept-encoding" : "gzip, deflate, br",
            "cookie":    f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "origin":    "https://discord.com",
            "sec-fetch-dest":    "empty",
            "sec-fetch-mode":    "cors",
            "sec-fetch-site":    "same-origin",
            "referer":    "https://discord.com/channels/@me",
            "x-context-properties": "eyJsb2NhdGlvbiI6IkFkZCBGcmllbmQifQ==",
            "User-Agent":    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",}
        json = {"name" : f"Cutecat is Cool"}
        r = requests.patch("https://discord.com/api/v9/channels/941538575558799421", headers=headers, json = json)
        time.sleep(60)
        json = {"name" : f"13280 Pierce Rd"}
        r = requests.patch("https://discord.com/api/v9/channels/941538575558799421", headers=headers, json = json)
        time.sleep(60)
        json = {"name" : f"<3 in a Friend Way"}
        r = requests.patch("https://discord.com/api/v9/channels/941538575558799421", headers=headers, json = json)
        json = {"name" : f"https://media.discordapp.net/attachments/941538575558799421/942238856315564042/IMG_0557.jpg?width=440&height=330"}
        r = requests.patch("https://discord.com/api/v9/channels/941538575558799421", headers=headers, json = json)
        print(r.status_code)
hummus.run(token)

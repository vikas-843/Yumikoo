import os
from os import getenv


API_ID = int(getenv("API_ID", "25826048"))
API_HASH = getenv("API_HASH", "b486ee260537697fdfc56b2b61cbc049")
BOT_USERNAME = getenv("BOT_USERNAME", "naruto_renamer_robot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "6881733978:AAEJWAsLegNjXdzWGrpVUDGk22RZs6hXqjw")
OWNER_ID = int(getenv("OWNER_ID", "6584511650"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6584511650").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BQGKEwAAipc5xv-CMRznisLC0E9H5nrNfEewgxQ92ef82IbycsXZdc8iKk28UxFckSevIcSSoXWWgqcFouTQkUTRa6dNddDhwGVEOwxv5c_23C0A0zu0XYAdnkRozHRr_QzOcTyvtlthy2KDh-LqZWVvjzF2V_xdVbbA0hyQhiRNs0Cku-hsJAvhrUjNFjAH3D_bNDsUEwWeycqwJ67gkbF6Hd0fAHuhPp_TELtwjdk4xzn863aNAwcOxmgbWg4fUyR4Ba8qp1dv6CMJiJZaYx62IcB9j5Q5P0yYQh19yQtA9s7WO2pPqQNgeGsHCRnu0CX6tVyBdc0B-s6ifQ7ihf2Qt8NYuwAAAAFhlqkyAA")

from config import *
from pytgcalls import PyTgCalls
from pyrogram import Client, filters

API_ID = "21055228"
API_HASH = "1fac2ebdf068d0f4d9e619abf49db06c"
SESSION = "AQCLEaBFTWRd8O3nvOEBQNwMKFQRdyl9dUxryIJMbvSQFTF1ft2CgLf_2T4R8hZyunVR-rV_RPNeZ3BzpMuheUE9CR1uVv9g88mVj4RWZp42hsGBfwQE4OU-OaLvlB2llVIGagYJWFBd5BQ6jPf0VpmOpNYYSbWl8M09avEju5wCfXPLKkmwmLy1MqiRjcoG6JGqzy72F2IdZzyOwnW4rr81bfpcVc6GBA99CLYAeWWf6Uf0MmvFvvb0LNRUufnTGcrbqjj4UcF69Mijrqys1hHGJVJHA9_7o42ifcr3oa_HbXzw4udGysd_bM8xQxYMNw734a7iQOnkhNcWYUzmRSbVAAAAAVsoCHAA"
SUDO_USERS = "5700727404"

contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="VCRAID.plugins"))
call_py = PyTgCalls(bot)

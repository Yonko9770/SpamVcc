from config import *
from pytgcalls import PyTgCalls
from pyrogram import Client, filters

API_ID = 21884763
API_HASH = da0f54c91d30d9d9a61a80df3a3c1637
SESSION = BQC2ivrDj18PCJCQMjRkAGsdEmScxIjzkjIjx2JgAGOTPlX5nY1hw2XnQBgqfojYYYVdK3S9U7R1iggBMK8PyMUvgIjQqGVzdt8e6dKVp1gzhyx_U5irb5uU7ap58LAnP9bLKCRSKyEt9MhXN7NdTAJa5CnBM2szSJTjcBlyg7rvVAPOD797IvlAA5rslph4YgGkfNWQrg5EJTHgpXgMRbPzJEbSj_4d-OMGw5En_BIStRd-Oo4aM8eZv9U6zpvb63AefBqtC8ZCL_8nJuX3v0aGJjZ-uSe0Csrvd3j1EGTCFjemHNaR68sDyBrpEtEsP6w6t_ckKGsE02gBe1FJBDE0AAAAAWAjt5kA
SUDO_USERS = 5940604852 6155155325 5598242384 5700727404 5645927490  5943074175 1571208389  2081609972 5924163122


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="VCRAID.plugins"))
call_py = PyTgCalls(bot)

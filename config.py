# FILES BELONGS TO @THEDEADLYBOTS 

import os
from dotenv import load_dotenv

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "25591955"))
API_HASH = os.getenv("API_HASH", "190867151075b43a1d0ffb1213b16c7d")
SESSION = os.getenv("SESSION", "BQC2ivrDj18PCJCQMjRkAGsdEmScxIjzkjIjx2JgAGOTPlX5nY1hw2XnQBgqfojYYYVdK3S9U7R1iggBMK8PyMUvgIjQqGVzdt8e6dKVp1gzhyx_U5irb5uU7ap58LAnP9bLKCRSKyEt9MhXN7NdTAJa5CnBM2szSJTjcBlyg7rvVAPOD797IvlAA5rslph4YgGkfNWQrg5EJTHgpXgMRbPzJEbSj_4d-OMGw5En_BIStRd-Oo4aM8eZv9U6zpvb63AefBqtC8ZCL_8nJuX3v0aGJjZ-uSe0Csrvd3j1EGTCFjemHNaR68sDyBrpEtEsP6w6t_ckKGsE02gBe1FJBDE0AAAAAWAjt5kA")
OWNER = os.getenv("OWNER", "5940604852")
SUPPORT = os.getenv("SUPPORT", "bonten_mainchat")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS","6155155325","5598242384","5700727404","5645927490","5943074175","1571208389","2081609972","5924163122").split()))

# FILES BELONGS TO @THEDEADLYBOTS 

import os
from dotenv import load_dotenv

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "21055228"))
API_HASH = os.getenv("API_HASH", "1fac2ebdf068d0f4d9e619abf49db06c")
SESSION = os.getenv("SESSION", "AQCLEaBFTWRd8O3nvOEBQNwMKFQRdyl9dUxryIJMbvSQFTF1ft2CgLf_2T4R8hZyunVR-rV_RPNeZ3BzpMuheUE9CR1uVv9g88mVj4RWZp42hsGBfwQE4OU-OaLvlB2llVIGagYJWFBd5BQ6jPf0VpmOpNYYSbWl8M09avEju5wCfXPLKkmwmLy1MqiRjcoG6JGqzy72F2IdZzyOwnW4rr81bfpcVc6GBA99CLYAeWWf6Uf0MmvFvvb0LNRUufnTGcrbqjj4UcF69Mijrqys1hHGJVJHA9_7o42ifcr3oa_HbXzw4udGysd_bM8xQxYMNw734a7iQOnkhNcWYUzmRSbVAAAAAVsoCHAA
")
OWNER = os.getenv("OWNER", "5477247654")
SUPPORT = os.getenv("SUPPORT", "Xd_Bot_Support")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS","5700727404").split()))

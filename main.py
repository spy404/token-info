# ------ libs ------ #
import os
import pwinput
import requests
import datetime
from pystyle import Center
from colorama import Fore, init
from rich.console import Console
from rich.table import Table

# ------ setup ------ #
init()
if os.name == "nt":
    os.system("title Token information - spy404#6985")
os.system("cls" if os.name == "nt" else "clear")

# ------ vars ------ #
banner = Center.XCenter("""
 ######  ########  ##    ## ##          #####   ##
##    ## ##     ##  ##  ##  ##    ##   ##   ##  ##    ##
##       ##     ##   ####   ##    ##  ##     ## ##    ##
 ######  ########     ##    ##    ##  ##     ## ##    ##
      ## ##           ##    ######### ##     ## #########
##    ## ##           ##          ##   ##   ##        ##
 ######  ##           ##          ##    #####         ##
""")
print(Fore.GREEN + Center.XCenter(banner))
token = pwinput.pwinput(prompt = "Token: \n>>> ", mask = "*")
headers = {
    'Authorization': token,
    'Content-Type': 'application/json'
}
r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
console = Console()

if r.status_code == 200:
    user_name = r.json()['username'] + '#' + r.json()['discriminator']
    user_id = r.json()['id']
    phone = r.json()['phone']
    email = r.json()['email']
    mfa = str(r.json()['mfa_enabled'])
    avatar = r.json()['avatar']
    avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar}.gif'
    flags = r.json()['flags']
    lang = r.json()['locale']
    verified = r.json()['verified']
    creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=headers)
    nitro_data = res.json()
    nitro = bool(len(nitro_data) > 0)

table = Table(
    title = Fore.RESET + "Token information"
)

table.add_column("Title", justify = "center")
table.add_column("info", justify = "center")
table.add_row("avatar", avatar_url)
table.add_row("username", user_name)
table.add_row("user id", user_id)
table.add_row("phone", phone)
table.add_row("email", email)
table.add_row("flags", str(flags))
table.add_row("language", lang)
table.add_row("verify", str(verified))
table.add_row("creation date", creation_date)
table.add_row("nitro", str(nitro))

console.print(table)
# ------ libs ------ #
import os
import pwinput
import requests
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
r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
console = Console()

if r.status_code == 200:
    user_name = r.json()['username'] + '#' + r.json()['discriminator']
    user_id = r.json()['id']
    phone = r.json()['phone']
    email = r.json()['email']
    mfa = str(r.json()['mfa_enabled'])

table = Table(
    title = Fore.RESET + "Token information"
)

table.add_column("Title", justify = "center")
table.add_column("info", justify = "center")
table.add_row("username", user_name)
table.add_row("user id", user_id)
table.add_row("phone", phone)
table.add_row("email", email)
table.add_row("mfa", mfa)

console.print(table)
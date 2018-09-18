import hashlib
from colorama import Fore

RED = Fore.RED
CYAN = Fore.LIGHTCYAN_EX
RESET = Fore.RESET


print(RED + "The system, is CASE SENSITIVE, please copy it as BitMax team sent to you" + RESET)
key = input(CYAN + "Please copy and paste your PUBLIC API KEY: " + RESET)

hmac_key = hashlib.blake2b(key.encode("utf-8")).hexdigest()
print(hmac_key)

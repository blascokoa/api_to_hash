import hashlib

print("The system, is CASE SENSITIVE, please copy it as BitMax team sent to you")
key = input("Please copy and paste your PUBLIC API KEY: ")

hmac_key = hashlib.blake2b(key.encode("utf-8")).hexdigest()
print(hmac_key)

with open("practice_auth.log") as log:
    text = log.read()
lines = text.splitlines()
print("Failed password" in lines[0])
print("Failed password" in lines[186])

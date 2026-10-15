import json

with open("python-basics/router.json") as file:
    data = json.load(file)

print(f"Hostname: {data['hostname']}")
print(f"IP: {data['ip']}")
print(f"Status: {data['status']}")

if data["status"] == "up":
    print("Router operacional")
else:
    print("Router indisponivel")
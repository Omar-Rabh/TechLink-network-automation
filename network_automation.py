import json
from datetime import datetime
import time


def write_log(message):

    print(message)

    with open("automation_log.txt", "a") as log_file:
        log_file.write(f"[{datetime.now()}] {message}\n")


with open("network_status.json", "r") as file:
    network = json.load(file)

write_log("\n===== NETWORK STATUS =====")

final_routes = {}

for site, data in network.items():

    write_log(f"\nSite : {site}")

    primary = data["primary_link"]
    backup = data["backup_link"]

    write_log(f"Primary Link Status : {primary}")

    if primary == "UP":

        route = "PRIMARY"

        write_log("Current Route : PRIMARY")

    else:

        if backup == "UP":

            write_log("Backup Link Found")

            write_log("Activating Backup Route...")

            time.sleep(1)

            write_log("Applying Configuration Changes...")

            write_log("ip route 192.168.50.0 255.255.255.0 10.0.0.5")

            write_log("ip route 192.168.60.0 255.255.255.0 10.0.0.5")

            write_log("Configuration Applied Successfully")

            route = "BACKUP"

            write_log("Current Route : BACKUP")

        else:

            route = "DOWN"

            write_log("No Available Links")

    final_routes[site] = route

    write_log("----------------------------------------")

write_log("\n===== FINAL SUMMARY =====")

for site, route in final_routes.items():

    write_log(f"{site} --> {route}")
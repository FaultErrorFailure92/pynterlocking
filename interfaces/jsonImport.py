import json

# JSON-Datei laden
with open("station_topology.json", "r") as file:
    data = json.load(file)

# Beispiel: Alle Gleise ausgeben
for track in data["tracks"]:
    print(f"Gleis-ID: {track['id']}, Name: {track['name']}")
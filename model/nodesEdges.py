def create_node_edge_model(json_data):
    nodes = {}  # Knoten
    edges = []  # Kanten

    # Weichen als Knoten hinzufügen
    for point in json_data["points"]:
        point_id = point["id"]
        connected_tracks = point["connectedTracks"]
        nodes[point_id] = {"type": "point", "connectedTracks": connected_tracks}
    
    # Gleise als Kanten hinzufügen
    for track in json_data["tracks"]:
        track_id = track["id"]
        edges.append({
            "id": track_id,
            "type": "track",
            "connections": [point for point in nodes if track_id in nodes[point]["connectedTracks"]]
        })
    
    # Zusätzlich: Weichen untereinander verbinden
    for point in json_data["points"]:
        connections = [
            other_point["id"]
            for other_point in json_data["points"]
            if set(point["connectedTracks"]) & set(other_point["connectedTracks"])
        ]
        nodes[point["id"]]["connections"] = connections

    return nodes, edges

nodes, edges = create_node_edge_model(station_topology)

# Ausgabe
print("Knoten:")
for node_id, node_data in nodes.items():
    print(f"{node_id}: {node_data}")

print("\nKanten:")
for edge in edges:
    print(edge)

import random, json

contraband_items = [
    ("Toothbrush Shiv", ["Toothbrush", "Razor Blade"]),
    ("Foil Gum Keycard", ["Gum", "Foil", "Ink Pen"]),
    ("Battery Lockpick", ["AA Battery", "Paperclip"])
]

tiles = [
    ("dirty_cell", "A dirty concrete floor"),
    ("vent_duct", "Rusty air duct cover"),
    ("guard_room", "Locked guard surveillance room")
]

output = {
    "contraband": [
        {"name": c[0], "components": c[1], "risk": random.randint(1, 10)}
        for c in contraband_items
    ],
    "tiles": [
        {"id": t[0], "description": t[1]} for t in tiles
    ]
}

with open("game_data.json", "w") as f:
    json.dump(output, f, indent=2)

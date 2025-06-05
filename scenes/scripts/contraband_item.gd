extends Node3D
@onready var pickup_area = $Area3D

func _ready():
    pickup_area.body_entered.connect(_on_pickup)

func _on_pickup(body):
    if body.name == "CogitoPlayer":
        if body.has_method("add_to_inventory"):
            body.add_to_inventory("Toothbrush Shiv")
        queue_free()

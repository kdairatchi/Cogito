extends Area3D

func _ready():
    self.body_entered.connect(_on_area_entered)

func _on_area_entered(body):
    if body.name == "CogitoPlayer":
        if body.has_method("has_item") and body.has_item("Keycard"):
            print("ESCAPE!")
            get_tree().change_scene_to_file("res://scenes/escape_success.tscn")


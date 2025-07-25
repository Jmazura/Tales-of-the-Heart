extends Node2D

@onready var body: CharacterBody2D = get_node("CharacterBody2D")
@onready var anim: AnimationPlayer = get_node("CharacterBody2D/AnimationPlayer")
@export var speed: float = 40.0

var last_direction := "down"  # Default starting direction

func _ready() -> void:
	anim.play("idle")

func _process(delta: float) -> void:
	var input := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
	
	# Force 4-directional movement
	if input.x != 0:
		input.y = 0

	# Apply movement
	body.velocity = input * speed
	body.move_and_slide()

	# Play walk or idle animation based on input
	if input != Vector2.ZERO:
		if input.x > 0:
			anim.play("walk_right")
			last_direction = "right"
		elif input.x < 0:
			anim.play("walk_left")
			last_direction = "left"
		elif input.y > 0:
			anim.play("walk_down")
			last_direction = "down"
		elif input.y < 0:
			anim.play("walk_up")
			last_direction = "up"
	else:
		anim.play("idle_" + last_direction)

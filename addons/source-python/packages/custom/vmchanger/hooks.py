##

from entities.entity import Entity
from entities.hooks import EntityCondition
from entities.hooks import EntityPostHook
from listeners import OnEntitySpawned
from players.entity import Player
from memory import make_object
from messages import SayText2

from .helpers import get_predicted_view_model
from .manager import viewmodel_manager, worldmodel_manager, all_class_names

##

@OnEntitySpawned
def _change_model_world_model(entity):
	'Changes a weapons world model upon being created.'
	## Technically a <BaseEntity> instance, but who cares? hehe
	if entity.classname not in worldmodel_manager:
		return
	model = worldmodel_manager[entity.classname]
	weapon = Entity(entity.index)
	weapon._set_model(model.path)

@EntityPostHook(EntityCondition.is_human_player, 'weapon_switch')
def _change_weapon_view_model(stack_data, return_value):
	'Changes the weapons view model for the player.'
	weapon = make_object(Entity, stack_data[1])
	if weapon.class_name not in viewmodel_manager:
		return

	player = make_object(Player, stack_data[0])
	weapon.owner_handle = player.inthandle
	weapon.model_index = 0
	prediction = get_predicted_view_model(player)
	prediction.model_index = viewmodel_manager[weapon.class_name].index
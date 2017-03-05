##

from filters.entities import EntityIter

##

__all__ = ('get_predicted_view_model', )

##

def get_predicted_view_model(player):
	'Retrieves the current view model predictor representative of the player.'
	for entity in EntityIter('predicted_viewmodel'):
		if entity.owner_handle == player.inthandle:
			return entity

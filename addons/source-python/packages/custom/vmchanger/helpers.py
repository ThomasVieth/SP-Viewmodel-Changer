##

from filters.entities import EntityIter

##

__all__ = ('get_predicted_view_model', )

##

def get_predicted_view_model(player):
	'Retrieves the current view model predictor representative of the player.'
	for entity in EntityIter('predicted_viewmodel'):
		if entity.get_property_int('m_hOwner') != player.inthandle:
			continue
		return entity
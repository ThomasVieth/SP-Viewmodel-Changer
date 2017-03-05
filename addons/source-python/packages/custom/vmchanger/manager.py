##

from engines.precache import Model
from filters.weapons import WeaponClassIter

##

__all__ = (
	'viewmodel_manager',
	'worldmodel_manager',
	'all_weapons',
	'all_projectiles',
	'all_class_names',
)

##

all_weapons = [weapon.name for weapon in WeaponClassIter()]
all_projectiles = ['decoy_projectile', 'flashbang_projectile', 'hegrenade_projectile']
all_class_names = all_weapons + all_projectiles

##

class ViewmodelManager(dict):
	'''
	A simplistic dictionary to store all changed
	view models. This will raise exceptions if
	users try to apply more than 1 view model
	to a single weapon.
	'''

	def __setitem__(self, item, value):
		'Overriden __setitem__ to ensure no multiple setting of viewmodels.'
		self.add_weapon_remodel(item, value)

	def add_weapon_remodel(self, class_name, viewmodel):
		'Stores a new view model for a weapon, and raises exceptions if problems are met.'
		if class_name in self:
			raise KeyError('Cannot assign a new viewmodel to {}.'.format(class_name))

		if class_name not in all_class_names:
			raise ValueError('False weapon class name given for remodelling.')

		if isinstance(viewmodel, str):
			viewmodel = Model(viewmodel, download=True)

		super().__setitem__(class_name, viewmodel)

viewmodel_manager = ViewmodelManager()

class WorldmodelManager(dict):
	'''
	A simplistic dictionary to store all changed
	world models. This will raise exceptions if
	users try to apply more than 1 world model
	to a single weapon.
	'''

	def __setitem__(self, item, value):
		'Overriden __setitem__ to ensure no multiple setting of worldmodels.'
		self.add_weapon_remodel(item, value)

	def add_weapon_remodel(self, class_name, worldmodel):
		'Stores a new world model for a weapon, and raises exceptions if problems are met.'
		if class_name in self:
			raise KeyError('Cannot assign a new worldmodel to {}.'.format(class_name))

		if class_name not in all_class_names:
			raise ValueError('False weapon class name given for remodelling.')

		if isinstance(worldmodel, str):
			worldmodel = Model(worldmodel, download=True)

		super().__setitem__(class_name, worldmodel)

worldmodel_manager = WorldmodelManager()
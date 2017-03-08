##

from engines.precache import Model
from filters.weapons import WeaponClassIter
from weapons.manager import weapon_manager

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
all_projectiles = list(weapon_manager.projectiles)
all_class_names = all_weapons + all_projectiles

##

class ModelManager(dict):
	'''A simplistic dictionary to store all changed models.

	This will raise exceptions if users try to apply more than 1 view model to
	a single weapon.
	'''

	def __init__(self, name):
		self._name = name

	def __setitem__(self, class_name, model):
		'''Override __setitem__ to ensure no multiple setting of models.'''
		if class_name in self:
			raise KeyError(
				'Cannot assign a new {name} to {class_name}.'.format(
					name=self._name,
					class_name=class_name,
				)
			)

		if class_name not in all_class_names:
			raise ValueError('False weapon class name given for remodelling.')

		if isinstance(model, str):
			model = Model(model, download=True)

		super().__setitem__(class_name, model)

	def add_weapon_remodel(self, class_name, model):
		'''Stores a new view model for a weapon.'''
		self[class_name] = model

viewmodel_manager = ModelManager('viewmodel')
worldmodel_manager = ModelManager('worldmodel')

# SP-Viewmodel-Changer
Gives the develloper access to easily change weapon view models and world models. Works with all weapons and grenade projectiles.

TODO: Change the core to be individual to players, rather than a global change to the weapon entirely.

Example of usage is below:

```
## IMPORTS

from engines.precache import Model
from vmchanger import viewmodel_manager, worldmodel_manager

## GLOBALS

Model('models/weapons/futuristicgrenades/v_eq_decoy.dx90.vtx',
	download=True)
Model('models/weapons/futuristicgrenades/v_eq_decoy.dx80.vtx',
	download=True)
decoy_view_model = Model('models/weapons/futuristicgrenades/v_eq_decoy.mdl',
	download=True)
Model('models/weapons/futuristicgrenades/v_eq_decoy.vvd',
	download=True)
Model('models/weapons/futuristicgrenades/v_eq_decoy.sw.vtx',
	download=True)
Model('models/weapons/futuristicgrenades/w_eq_decoy.dx90.vtx',
	download=True)
Model('models/weapons/futuristicgrenades/w_eq_decoy.dx80.vtx',
	download=True)
decoy_world_model = Model('models/weapons/futuristicgrenades/w_eq_decoy.mdl',
	download=True)
Model('models/weapons/futuristicgrenades/w_eq_decoy.phys',
	download=True)
Model('models/weapons/futuristicgrenades/w_eq_decoy.vvd',
	download=True)
Model('models/weapons/futuristicgrenades/w_eq_decoy.sw.vtx',
	download=True)

##

def load():
	viewmodel_manager.add_weapon_remodel('weapon_decoy', decoy_view_model)
	worldmodel_manager.add_weapon_remodel('decoy_projectile', decoy_world_model)
	viewmodel_manager.add_weapon_remodel('weapon_flashbang', decoy_view_model)
	worldmodel_manager.add_weapon_remodel('flashbang_projectile', decoy_world_model)

def unload():
	del viewmodel_manager['weapon_decoy']
	del worldmodel_manager['decoy_projectile']
	del viewmodel_manager['weapon_flashbang']
	del worldmodel_manager['flashbang_projectile']
```

![Test Screenshot](http://images.akamai.steamusercontent.com/ugc/91600296843538906/868E24538700A26D3472961B027D71BA96BBFA09/)

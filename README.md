# TUG
Misc TUG things

"Chest": priority.
"Hair": priority.
"Helmet": priority.
"Hips": priority.
"Left Arm": submesh, priority.
"Left Foot": priority.
"Left Hand": submesh, priority.
"Left Leg": priority.
"Left Shoulder": priority.
"Neck": priority.
"Right Arm": priority.
"Right Foot": priority.
"Right Leg": priority.
"Right Shoulder": priority.

Affects: "Wood", "Vegetation", "Edible", "Rock", "Ore", "Metal", "Flesh", "Dirt", "Grass".

Alchemy Table: craftTime, energyCost, Tag.
Alchemy Table Recipe: Script.

Alert: path.
Alert_Loop: path.
Alert_Search: path.

AllowedGrowthStates: "Teen", "Child".

Alloy: "Latten".

AltWallVisibilitySettings: Idle, Activate, Hold, Release, Rearm.

AnimatedGraphics: scale, Offset, model, skeleton.

Artisan Workbench: spawnOffsetOverride, craftTime, Tag.
Artisan Workbench Recipe: Script.

Attached: handlerClass.
Attack: path.
Attack_Idle: path.
Back: "Lotus Teeth Leaf".
BackToDefault: destinationState, animation, blendOutTime.

BambooBiome: Mud, Dirt, Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.

Barren Flat: depositSet, dayAmbiance, nightAmbiance, mainMaterialStrength, geome, skyState.

Base: "Bamboo Log", "Large Mushroom Cap".

Bavaria: amplitude, wavelength, roughness, snowHeight, noiseFunction.

Bayou Caves: caveFunction, wallMaterial, floorMaterial, depthBelowSurface, spacing, horizontalAmplitude, horizontalFrequency, verticalAmplitude, verticalFrequency, minRadius, maxRadius.

Bedrock: depositSet, dayAmbiance, nightAmbiance, mainMaterialStrength, geome, skyState, amplitude, wavelength, roughness, snowHeight, stepMultiplier, noiseFunction.
BedrockBiome: Clay, Dirt, Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.
BedrockPlains: Clay, Dirt, Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.
BedrockTerraces: Clay, Dirt, Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.

Billboard Culling Controller: Tag.

Binding: "Vines", "Leather Strips".
Binding1: "Vine Arm Wraps".
Binding2: "Leather Strips".
Bindings: "Vines", "Leather Strips".

BlendByBoneMask: name.
BlendByDirection: name, blendSpeed.
BlendByFall: name, transitionTime.
BlendByGraph: name, initialState, stateVariable.
BlendLeaf: name, animation, loop, start_offset, restartOnActivate.
BlendSlot: name.
BlendState: name, state_name, transitionTime, initialState.
BlendTree: root.

Blocking: Node.

Box: trigger, extents, center, mass, convex.

Break_Item: path.

BurnTerrain: time, active, activate.
Burnt: texture, diffuse, normal, scale.

Cancel: destinationState, animation, blendInTime, blendOutTime.

Capsule: Height, Feet, Radius, height, radius.

Cast: path, destinationState, animation.
Cast_Cancel: path.
Cast_Hold: path.
Cast_In: path.
CastedItem: "Bamboo Vest", "Pumpkin Helmet", "Pumpkin Skull Cap", "Bamboo Anklets".
Casting: Node.
Casting2: Node.

Channel: destinationState, animation.
Channeling: Node.
Channeling_Hold: path.
Channeling_In: path.
Channeling_Out: path.

CharacterGear: Tag.

Chase: path.
Chasing: name, animIndex, maxspeed, acceleration, turnrate.

Child: submesh.

Clay: horizontalScaleX, horizontalScaleZ, verticalScale, frequency, perlinShift, minDepth, maxDepth, texture, diffuse, normal, scale.

Clip Clop Breakdown: Script.
Clip Clop Recipe: Script.

Clover: Tag, offset, minScale, maxScale, object, weight, minDepth, maxDepth.

Coal: duration, canStart, isConsumed, dropChance, dropMinAmount, dropMaxAmount, horizontalScaleX, horizontalScaleZ, verticalScale, frequency, perlinShift, minDepth, maxDepth, texture, diffuse, normal, scale.
Coal Burn: texture, diffuse, normal, scale.
Coal Burn Clump: offset.

Cone: trigger, height, radius, material.

Config: Test, Test2.

ConnectTo: component, attachpoint.

Consume: path, destinationState, animation.
Consume_In: path.
Consume_Loop: path.
Consume_Out: path.
Consuming: Node.

Copper Ore: dropChance, dropMinAmount, dropMaxAmount, horizontalScaleX, horizontalScaleZ, verticalScale, frequency, perlinShift, minDepth, maxDepth, texture.

Cotton: billboard, density, chance, minangle, maxangle, minscale, maxscale.

CraftSwing: path.
Craft_Default: path.
Crafting Rock: craftTime, energyCost, spawnOffsetOverride, Tag, object, weight.

Crafting Stump: craftTime, energyCost, spawnOffsetOverride, Tag, object, weight.
Crafting Tool: category, tier.

Cut Log: Tag.

Data: duration, value, stacks, damage, ticksPerSecond, dropObjectLoot.

Day: color, intensity.

DeadCapsule: Height, Feet, Radius.

Death: path.
Death_Left: path.

Deep Forest: depositSet, mainMaterialStrength, dayAmbiance, nightAmbiance, geome, skyState.

Deep Forest Hills: amplitude, wavelength, roughness, snowHeight, noiseFunction.

DeepForestBiome: Mud, Dirt, Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.

Default: Node.

Desert: depositSet, dayAmbiance, nightAmbiance, mainMaterialStrength, geome, skyState.

Desert Caverns: caveFunction, wallMaterial, floorMaterial, minCavernDepth, maxCavernDepth, cavernFrequency, cavernSize.
Desert Cliffs: amplitude, wavelength, roughness, snowHeight, stepMultiplier, noiseFunction.
Desert Dunes: amplitude, wavelength, roughness, snowHeight, noiseFunction.
Desert Surface Channels: caveFunction, wallMaterial, floorMaterial, depthBelowSurface, spacing, horizontalAmplitude, horizontalFrequency, verticalAmplitude, verticalFrequency, minRadius, maxRadius.
DesertBiome: Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.

Directions: Forward, Left, Right, Backward, Idle, ForwardLeft, ForwardRight, BackLeft, BackRight.

Dirt: horizontalScaleX, horizontalScaleZ, verticalScale, frequency, perlinShift, minDepth, maxDepth, texture, diffuse, normal, scale.

Dragon Glass: object, weight, minDepth, maxDepth.

DurabilityDamage: Player, Character, GameObject, Terrain.

Dying: name, animIndex, maxspeed, acceleration, turnrate.

EffectOverTime: ticksPerSecond, player, character, gameObject.

Equipable: name, resource, maxStackCount, minScale, maxScale, icon, category, tier, durability, damageToCharacters, damageToObjects, placementSound, miningEmitter, miningEmitterAlt, handleType, durabilityLossOnCorrect, durabilityLossOnIncorrect, placeWithNoPhysics, orientsToSurface, survivalRotOffset, survivalPosOffset, gridSizeX, gridSizeY, vfSizeX, vfSizeY, vfSizeZ, craftingArchetype, staminaDamage, staminaRegenDelay, attackSpeedModifier, weaponRange, movementSpeedModifier, consumable, impactFailSound.

Explode: jsonFile, player, character, gameObject, terrain, time, active, abortOnRemove.
Exploding Pumpkin Attractor: offset, emitter.
Explosion Sound: name, minDist, maxDist.

Failed Results: "Mad Mushroom Man".

First Material: "Bronze Chunks".
First Ore: "Copper Ore".

Flap: path.

Flat: amplitude, wavelength, roughness, snowHeight, noiseFunction, htDistribution.
Flat Rock: offsetOverride, craftTime, Tag, offset, object, minScale, maxScale, weight, minDepth, maxDepth.
Flat Snow: depositSet, dayAmbiance, nightAmbiance, mainMaterialStrength, geome, skyState.
FlatWorld: Clay, Dirt, Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.

Flint: horizontalScaleX, horizontalScaleZ, verticalScale, frequency, perlinShift, minDepth, maxDepth.

Fly_Idle: path.

Foothill Caverns: caveFunction, wallMaterial, floorMaterial, minCavernDepth, maxCavernDepth, cavernFrequency, cavernSize.

Forest Ground: inherit, top, billboard, billboard1, billboard2, billboard3.
Forest Ground Swap: inherit, top, billboard, billboard1, billboard2, billboard3.

Forest Mountain Dirt: inherit, top.
Forest Mountain Moss: inherit, top.
Forest Mountain Mud: inherit, top.
Forest Mountains: amplitude, wavelength, roughness, snowHeight, noiseFunction.

Forest Tall Grass: inherit, top, billboard.
Forest Tall Grass Swap: inherit, top, billboard.

Generation: version.

Giant Ice Holes: caveFunction, wallMaterial, floorMaterial, depthBelowSurface, spacing, horizontalAmplitude, horizontalFrequency, verticalAmplitude, verticalFrequency, minRadius, maxRadius.

Gold Ore: horizontalScaleX, horizontalScaleZ, verticalScale, frequency, perlinShift, minDepth, maxDepth, texture.

Graze_In: path.
Graze_Loop: path.
Graze_Out: path.

Halloween Town: depositSet, dayAmbiance, nightAmbiance, mainMaterialStrength, geome, skyState.

Handle: "Forked Stick", archetype, default, useAsHandAtch, "Hardened Wood Shaft".

HandslotItemContainer: Tag.

Head: "Bronze Headshell", "Crude Hammer", "Crude Pick", "Crude Axe", "Crude Hoe", "Crude Shovel", "Crude Knife", "Wood Spear", "Bamboo Spear", "Crude Sword", "Club", "Jagged Rock", "Small Rock Spire", "Round Rock", archetype, attachpoint, default, "Cactus Chunk", "Loose Pebbles", "Knapped Rock Spire".

Head_Shake: path.

Hoe_In: path.
Hoe_Loop: path.
Hoe_Out: path.
Hoeing: Node.

Hold: destinationState, animation, blendInTime, blendOutTime.
HoldPotion: destinationState, animation.

Holding: Node.
HoldingPotion: Node.

Hswing: destinationState, animation, blendInTime.
Hswing_In: path.
Hswing_Loop: path.
Hswing_Out: path.
Hswinging: Node.

Hunger: maxHunger, regenPerSecond.

Hurt: path.
Hurt_2H: path.
Hurt_Right: path.

Ice Caves: caveFunction, wallMaterial, floorMaterial, depthBelowSurface, spacing, horizontalAmplitude, horizontalFrequency, verticalAmplitude, verticalFrequency, minRadius, maxRadius.
Ice Cliffs: depositSet, dayAmbiance, nightAmbiance, mainMaterialStrength, geome, skyState.

Ice Mountains: depositSet, dayAmbiance, nightAmbiance, geome, skyState, amplitude, wavelength, roughness, snowHeight, noiseFunction.
IceCliffsBiome: Snow, Dirt, Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.
IceMountains: Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.
Icehill Caverns: caveFunction, wallMaterial, floorMaterial, minCavernDepth, maxCavernDepth, cavernFrequency, cavernSize.

Idle: name, animIndex, maxspeed, acceleration, turnrate, path.
Idle_Misc: path.
Idle_Shield: path.
Idle_Two_Handed: path.
Idle_Two_Handed_Left: path.
Idle_Two_Handed_Left_Mask: path.
Idle_Two_Handed_Mask: path.

Iron Ore: horizontalScaleX, horizontalScaleZ, verticalScale, frequency, perlinShift, minDepth, maxDepth, texture.

ItemContainer: Tag.
ItemHSwing: path.
ItemIdle: path.
ItemVSwing: path.
Item_2H_H_Swing: path.
Item_2H_Left_H_Swing: path.
Item_2H_Left_V_Swing: path.
Item_2H_V_Swing: path.

Jump_End_Two_Handed_Left: path.
Jump_Idle_Land: path.
Jump_Land: path.
Jump_Land_2hnd_Rt: path.
Jump_Land_Shield: path.
Jump_Land_Two_Handed_Left: path.
Jump_Land_Wpn: path.
Jump_Loop: path.
Jump_Loop_2hnd_Rt: path.
Jump_Loop_Shield: path.
Jump_Loop_Two_Handed: path.
Jump_Loop_Two_Handed_Left: path.
Jump_Loop_Wpn: path.
Jump_Run_Bk_Land: path.
Jump_Run_Fwd_Land: path.
Jump_Run_Lf_Land: path.
Jump_Run_Rt_Land: path.
Jump_Start: path.
Jump_Start_2hnd_Rt: path.
Jump_Start_Shield: path.
Jump_Start_Two_Handed: path.
Jump_Start_Two_Handed_Left: path.
Jump_Start_Wpn: path.
Jump_Walk_Bk_Land: path.
Jump_Walk_Fwd_Land: path.
Jump_Walk_Lf_Land: path.
Jump_Walk_Rt_Land: path.

Jungle: depositSet, mainMaterialStrength, dayAmbiance, nightAmbiance, geome, skyState.
Jungle Channels: caveFunction, wallMaterial, floorMaterial, depthBelowSurface, spacing, horizontalAmplitude, horizontalFrequency, verticalAmplitude, verticalFrequency, minRadius, maxRadius.
Jungle Cliffs: amplitude, wavelength, roughness, snowHeight, stepMultiplier, noiseFunction.
JungleBiome: Mud, Dirt, Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.
JungleGenerator: Mud, Dirt, Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.

Lay_In: path.
Lay_Out: path.
Laying: path.

Legs: "Long Shaft".

Light: "Purple Gourd", lightRadius, lightOffset, lightColor.

LightFlickers: active, inactive.
LightRadius: active, inactive.
Lighting Controller: Tag.

LuaData: craftingActionName, craftingDisplayName, priority, stackResults, energyCost, craftTime, unconsumedDamage, repairPercentage.

MaterialLayers: "Snow", "Frozen Rock", "Cliff Rock Dark", "Rock", "Obsidian", "Mud", "Dirt", "Cliff Rock Light", "Clay", "Gravel", "Desert Rock", "Sand", "Sandstone", "Painted Rock", "Mesa Rock", "White Sand".

Mesa: depositSet, dayAmbiance, nightAmbiance, mainMaterialStrength, geome, skyState, texture, diffuse, normal, scale.
Mesa Caverns: caveFunction, wallMaterial, floorMaterial, minCavernDepth, maxCavernDepth, cavernFrequency, cavernSize.
Mesa Rock: inherit, side.
Mesa Surface Channels: caveFunction, wallMaterial, floorMaterial, depthBelowSurface, spacing, horizontalAmplitude, horizontalFrequency, verticalAmplitude, verticalFrequency, minRadius, maxRadius.
MesaBiome: Clay, Dirt, Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.

Mesh: mass, convex, material, mesh, decompose, name.

Metal: "Latten".

Model Viewer Axis: Tag.

ModificationInput: "modificationType", "dimensions", "radius", "brushType".
ModifiedMaterial: baseMaterial, minAngle, maxAngle, placementSize, maxHeight, minHeight.
ModifyPhysics: simulate, motion.
ModifyVisibility: render.

More Wood: "Chopped Wood".

MorphGraphics: scale, model, Offset.

Mountain Caves: caveFunction, wallMaterial, floorMaterial, depthBelowSurface, spacing, horizontalAmplitude, horizontalFrequency, verticalAmplitude, verticalFrequency, minRadius, maxRadius.

MountainPineyWoodsBiome: Dirt, Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.
Mountainous: amplitude, wavelength, roughness, snowHeight, noiseFunction.
Mountains: depositSet, dayAmbiance, nightAmbiance, geome, skyState, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.
MountainsJungle: Mud, Dirt, Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.
MountainsPlains: Clay, Dirt, Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.

Mud: horizontalScaleX, horizontalScaleZ, verticalScale, frequency, perlinShift, minDepth, maxDepth, texture, diffuse, normal, scale.

Multi-Colored Cobblestone Conversion: Script.

Natural Flat: depositSet, dayAmbiance, nightAmbiance, mainMaterialStrength, geome, skyState.

NetworkedItemContainer: Tag.

Night: color, intensity.

NoShield: Node.

ObjectDamage: ticksPerSecond, active.

OnHitEmitter: Name, Offset.
OnLootEmitter: Name, Offset.

Paddlesnip: Tag, offset.

Pickup: path.

Pierce: player, character, gameObject, terrain.

Place: path.

Placeable: name, icon, minScale, maxScale, category, tier, resource, placeWithNoPhysics, survivalFaceCamera, survivalRotOffset, placementSound, health, durabilityLossOnCorrect, durabilityLossOnIncorrect, removalSound, miningEmitter, miningEmitterAlt, maxStackCount, durability, tetherDistanceModifier, craftingArchetype, consumable, stepSound, useAlphaShadows, weaponRange, impactFailSound, handleType, dontCastShadows, damageToCharacters, damageToObjects, cateogry, materialRep.

PlaceableMaterial: material, gridSizeX, gridSizeY, category, tier, objectRep, durabilityLossOnCorrect, durabilityLossOnIncorrect, placementSound, removalSound, stepSound, miningEmitter, miningEmitterAlt.

Plains: depositSet, dayAmbiance, nightAmbiance, mainMaterialStrength, geome, skyState.
PlainsBiome: Clay, Dirt, Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.
PlainsGenerator: Clay, Dirt, Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.

Polar: depositSet, dayAmbiance, nightAmbiance, mainMaterialStrength, geome, skyState.
Polar Geome: amplitude, wavelength, roughness, snowHeight, noiseFunction, htDistribution.
Polar Surface Channels: caveFunction, wallMaterial, floorMaterial, depthBelowSurface, spacing, horizontalAmplitude, horizontalFrequency, verticalAmplitude, verticalFrequency, minRadius, maxRadius.
PolarLakes: Snow, Dirt, Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.
PolarSnowmounds: Snow, Dirt, Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.

Poor: damageEmitter, durabilityThreshold, model.

Pour: destinationState, animation.
Pour_In: path.
Pour_Loop: path.
Pour_Out: path.
Pouring: Node.

Projectile: name, handlerFile, handlerClass, speed, acceleration, contactProbeLength, debugging, lookAhead, strikeThreshold, force, damage, triggerIgnoreSource.

Punch: path.

RadiusDamage: radius, characterDamage, gameObjectDamage, incorrectTierCap, playerDamage.

Ravines: amplitude, wavelength, roughness, snowHeight, noiseFunction, htDistribution, depositionThreshold, depositionScale.

RedCliffsBiome: Clay, Dirt, Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.

ReleaseAtState: Release.

Remove: time, abortOnRemove.

Rigidbody: keyframed, mass.

River Beds: caveFunction, wallMaterial, floorMaterial, depthBelowSurface, spacing, horizontalAmplitude, horizontalFrequency, verticalAmplitude, verticalFrequency, minRadius, maxRadius.

Rocky Foothills: amplitude, wavelength, roughness, snowHeight, noiseFunction, htDistribution.

Rolling Hills: depositSet, dayAmbiance, nightAmbiance, mainMaterialStrength, geome, skyState, amplitude, wavelength, roughness, snowHeight, noiseFunction, htDistribution.
Rolling Plains: amplitude, wavelength, roughness, snowHeight, noiseFunction, htDistribution.
RollingHillsBiome: Mud, Dirt, Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.

Run: path.
Run_Back: path.
Run_Backward_Two_Handed_Mask: path.
Run_Forward_Two_Handed_Mask: path.
Run_Shield_Forward: path.
Run_Shield_Right: path.
Run_Strafe_Back_Left: path.
Run_Strafe_Back_Right: path.
Run_Strafe_Forward_Left: path.
Run_Strafe_Forward_Right: path.
Run_Strafe_Left: path.
Run_Strafe_Right: path.
Run_Two_Handed: path.
Run_Two_Handed_Left: path.
Run_Two_Handed_Left_Mask: path.
Run_Wpn: path.

Scoreboard: Tag.

Script: file, class.

ShieldBlock: destinationState, animation.
ShieldBlocking: Node.
ShieldEquipped: destinationState, duration.
ShieldOn: Node.
ShieldUnequipped: destinationState, duration.
Shield_Block_In: path.
Shield_Block_Loop: path.
Shield_Block_Out: path.
Shield_Crouch_Block_In: path.
Shield_Crouch_Block_Loop: path.
Shield_Crouch_Block_Out: path.

Shoot: destinationState, animation.
ShootLast: destinationState, animation.

Shovel: destinationState, animation, blendInTime.
ShovelDig: path.
Shovel_In: path.
Shovel_Loop: path.
Shovel_Out: path.
Shoveling: Node.

Sit_In: path.
Sit_Out: path.
Sitting: path.

Skin: destinationState, animation.
Skin_In: path.
Skin_Loop: path.
Skin_Out: path.
Skinning: Node.

Sky Dome: Tag.

SlingshotHold: destinationState, animation.
SlingshotHolding: Node.
SlingshotHolding2: Node.
Slingshot_Hold: path.
Slingshot_Hold2: path.
Slingshot_In: path.
Slingshot_Out: path.
Slingshot_Shoot: path.

Sneak_Back: path.
Sneak_Back_Left: path.
Sneak_Back_Right: path.
Sneak_Fast_Weapon: path.
Sneak_Forward: path.
Sneak_Forward_Left: path.
Sneak_Forward_Right: path.
Sneak_Idle: path.
Sneak_Idle_Shield: path.
Sneak_Left: path.
Sneak_Right: path.
Sneak_Run_Back: path.
Sneak_Run_Backward_Left: path.
Sneak_Run_Backward_Right: path.
Sneak_Run_Forward: path.
Sneak_Run_Forward_Left: path.
Sneak_Run_Forward_Right: path.
Sneak_Run_Left: path.
Sneak_Run_Right: path.
Sneak_Shield_Back: path.
Sneak_Shield_Forward: path.
Sneak_Shield_Left: path.
Sneak_Shield_Right: path.
Sneak_Shield_Run_Back: path.
Sneak_Shield_Run_Forward: path.
Sneak_Shield_Run_Left: path.
Sneak_Shield_Run_Right: path.
Sneak_Slow_Weapon: path.

Snowcaps: depositSet, mainMaterialStrength, dayAmbiance, nightAmbiance, geome, skyState.
Snowcaps Ravines: amplitude, wavelength, roughness, snowHeight, noiseFunction, htDistribution, depositionThreshold, depositionScale.

Soar: path.

Spawn Point: Tag.

Sphere: trigger, radius, material, name, center.

Stalk: path.
Stalking: name, animIndex, maxspeed, acceleration, turnrate.

StartBlocking: destinationState, animation.
StartBlockingCrouch: destinationState, animation.
StartingAngles: Idle, Activate, Hold, Release, Rearm.

States: Malnutrition, Starving, Hungry, Satisfied, Full, 0, 1, 2, 3, 4, 5, 6, 15, 12, 13, 11, Up, Loop, Ground, Land, LandRun.

StaticGraphics: model, dontCastShadows, hideMesh, useAlphaShadows, mirror.

StopBlocking: destinationState, animation.
StopBlockingCrouch: destinationState, animation.

Strafe_Back_Left: path.
Strafe_Back_Right: path.
Strafe_Forward_Left: path.
Strafe_Forward_Right: path.
Strafe_Left: path.
Strafe_Right: path.

Surface Caverns: caveFunction, wallMaterial, floorMaterial, minCavernDepth, maxCavernDepth, cavernFrequency, cavernSize.
Surface Channels: caveFunction, wallMaterial, floorMaterial, depthBelowSurface, spacing, horizontalAmplitude, horizontalFrequency, verticalAmplitude, verticalFrequency, minRadius, maxRadius.

Survival: SpawnBiome.
Survival Center Large: Tag.
Survival Center Medium: Tag.
Survival Center Small: Tag.

Swamplands: depositSet, mainMaterialStrength, dayAmbiance, nightAmbiance, geome, skyState.
SwamplandsBiome: Clay, Dirt, Sand, Gravel, Cliff Rock Light, Cliff Rock Dark, Rock, Obsidian.
Swampy Hills: amplitude, wavelength, roughness, snowHeight, noiseFunction.

SwapToItem: path.
SwapToNone: path.

TargetDamage: breakdown, damage, gameObjectDamage, incorrectTierCap.
TargetSound: name, minDist, maxDist, player, character.
TargetTimer: time, restarting, callback.

TerrainDamage: radius.
TerrainSettings: biomeSize, biomeOverlap, survivalRadius.
TerrainSwap: radius, material.

The Valley: depositSet, dayAmbiance, nightAmbiance, mainMaterialStrength, geome, skyState.

Throw: path, destinationState, animation, logic.
Throw_Cancel: path.
Throw_Hold: path.
Throw_In: path.
Throw_Potion: path.
Throw_Potion_Cancel: path.
Throw_Potion_Hold: path.
Throw_Potion_In: path.

TimedStates: Hold, Rearm.

Trajectory: handlerClass.

Tree Growth Controller: Tag.
Tree Sprout: Tag, offset.

Trot: path.

Unable: path.

Underground Fog: object, weight, minDepth, maxDepth.

Used: damageEmitter, durabilityThreshold, model.

Vegetation: duration, canStart, isConsumed.

Vswing: destinationState, animation, blendInTime.
Vswing_In: path.
Vswing_Loop: path.
Vswing_Out: path.
Vswinging: Node.

Walk: path.
Walk_Back: path.
Walk_Forward_Two_Handed_Mask: path.
Walk_Two_Handed: path.
Walk_Two_Handed_Left: path.
Walk_Two_Handed_Left_Mask: path.
Walking: name, animIndex, maxspeed, acceleration, turnrate.

World Caverns: caveFunction, wallMaterial, floorMaterial, minCavernDepth, maxCavernDepth, cavernFrequency, cavernSize.
World Center: Tag.
World Tunnels: caveFunction, wallMaterial, floorMaterial, depthBelowSurface, spacing, horizontalAmplitude, horizontalFrequency, verticalAmplitude, verticalFrequency, minRadius, maxRadius.
World Tunnels Deeper: caveFunction, wallMaterial, floorMaterial, depthBelowSurface, spacing, horizontalAmplitude, horizontalFrequency, verticalAmplitude, verticalFrequency, minRadius, maxRadius.
Worm Tunnels: caveFunction, wallMaterial, floorMaterial, depthBelowSurface, horizontalAmplitude, horizontalFrequency, verticalAmplitude, verticalFrequency, minRadius, maxRadius.

Wrap: archetype, default, proxy, attachpoint.

arguments: speed, acceleration, contactProbeLength, offset, category, tier, HitPoints, AttackDamage, dataMetricCategory, UBPdefeat, LBPdefeat, XPdefeat, UBPskin, LBPskin, XPskin, aggressive, encumbrance, failChance, UBPcraft, LBPcraft, XPcraft, consumesFuel, defaultBurnTime, activeSound, ambSound, UBPdestroy, LBPdestroy, XPdestroy, slot, incorrectTierCap, equipSound, emptyContainer, energyUsed, spellName, spellIcon, castingSound, endCastingSound, noEnergySound, noEnergyEmitter, stoneBreakEmitter, persistent, castingTimerTick, energyPerTick, durabilityPerTick, swingtransition, CriticalHitPoints, CreakingSound, BreakSound, ammoUsed, forceModifier, damageModifier, materialSwap, gestationTime, TetherDistance, ContainerSize, ContainerView, Top, TopAttach, BottomAttach, RotationAxis, timeToOpen, angleToOpen, encumberance, staminaModifier, energyModifier, healthModifier, seedModel, TORPconsume, nextFormName, growableMaterialName, minimumGrowthTime, maximumGrowthTime, bodyToCheck, clearanceRadius, ammoType, controllerName, timeBetweenGrowths, timeBetweenGrowthsVariance, growableLimit, totalGrowables, spawningCenter, spawningRegionHeight, spawningRegionMinDistance, spawningRegionMaxDistance, defaultState, triggersOnByDefault, captureHoldOffset, releaseOffset, checkForTerrain, freeControllerWhenFinished, checkForPlacement, DeleteOnRestore, durability, damageBonus, headType, forwardContactEvents, canDig, placementSound, consumeSound, spawnRate, spawnLimit, spawnObject, revolvingDoorSpawn, creativeRotation, UBPfarm, LBPfarm, XPfarm, decayWhenFinished, baseGrowableRotation, colliderName, defaultPickupState, Category, spawningBounds.

events: "OnDeathComplete", "OnAttack", "OnAttackComplete", "OnDeath", "TransitionToDefault", "OnSwing", "OnShoot", "OnThrow", "OnPickup".

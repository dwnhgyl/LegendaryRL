# Perks && Powers

## *Spells*

Spells are activated from the spell menu, putting the player into a “channeling” state, doing nothing else for the duration. The player can continue channeling by pressing the wait/hide button, or cancel the channel by performing any other action, including casting a new spell. Channeling has the same effect on stealth value that moving around does. After channeling for a number of rounds determined by the spell, the spell takes effect and the player reverts to a normal state.

The effects that spells have scale with spell power, a hidden stat determined by wisdom and item bonuses.

**Befuddle**: 4 turns. A moderate aoe around a space in medium range. Enemies within this range gain the "befuddled" debuff for a short time. Beffudled enemies function as if the player were invisible (they can still hear the player).

**Brilliance**: 4 turns. Targeted space becomes the center of a very powerful light source. A moderate area of effect around the origin of this light source (such that it covers the same tiles as the ones "brightly lit" by the light source) grants a moderate accuracy malus to anything inside of it, except the caster.

**Call Lightning**: 5 turns. Deals a large amount of lightning damage in a small aoe radius, centered on a targeted point that can be placed through obstructions, but must be in an area without a ceiling, and must be within line of sight.

**Call Fog**: 4 turns. Creates a large hidden area of effect centered on a targeted space (place anywhere, line of sight unnecessary). Spaces in this area of effect will randomly emit “Fog” gas for a long duration. The result is fog appearing in that area over a number of turns, potentially spilling into areas outside the radius if possible. 3 consecutive tiles of fog block line of sight for everything but the player, and any creature standing a fog space receives a significant hide bonus and a small sneak bonus. Unlike other effects that alter terrain, this makes no noise.

**Chilling Coalescence**: 5 turns. Target a point in medium range. All enemies in a small aoe around that point suffer the "coalescence" debuff for a short time, taking light cold damage and suffering slow movement for the duration. Empty tiles within the aoe have a 20% chance of becoming ice block walls for the duration of the spell.

**Conjure Explosive**: 6 turns. Target an empty space in sight. A "magic bomb" is spawned there. On its turn, the bomb has a 10% chance to explode if the player is still in its blast radius. If the player is not, it has a 50% chance to explode. When it does explode, it deals large physical and fire damage in a big AOE around it. The bomb has moderate hide and sneak (not modified by spell power) and a small pool of HP. If they spot it, Relentless and Ranged enemies will attack it, and all other enemies will flee it. If destroyed, the bomb immediately detonates, but with half its spell power effect.

**Deadly Flood**: 4 turns. A large aoe around a point in medium range. Does not go through walls. Has a minimum number of spaces it will affect equal to its unobstructed aoe: if it is blocked by walls it will fill adjacent empty spaces until this condition is met. All affected spaces become "Spell Acid" terrain. This works just like an acid pool, except damage scales with spellpower, and the caster takes only (50-Spellpower)% damage. This effect lasts for a moderate amount of time.

**Earthwall**: 4 turns. The player is prompted to select a number of continuous spaces. "Stone Pillars" immediately spawn in these spaces, functioning as walls. Enemies standing in one of these spaces take light physical damage and are moved to one of the nearest empty spaces. The stone pillars remain for a moderate duration. This spell comes with a special spell, "Dispel Pillar", that takes 1 turn to cast and removes a target pillar.

**Fireball**: 3 turns. Shoots a projectile which, upon hitting an enemy, a wall, or the targeted space, deals moderate fire damage in a moderate aoe. Notably, damage dropoff only reaches half damage at the edge of the radius, unlike other aoe damage effects. The projectile has a speed of 4 spaces per round. Fireball deals (60-Spellpower)% damage to the caster.

**Heroism**: 2 turns. Grants the heroism buff to the player for a short duration. This buff gives a small bonus to many stats, such as stealth, accuracy, defenses, etc. Additionally, the player gains a tiny amount of temporary hit points, which will expire with the buff if not lost by then.

**Lightning Bolt**: 3 turns. Shoots an instantaneous projectile which can travel through any number of enemy spaces, dealing moderate lightning damage to each enemy it passes through.

**Divination**: 7 turns. Establishes a moderate area of effect around a targeted space, chosen with no restrictions. That area is immediately mapped, including traps and items, and player has complete telepathy within that area for a short duration, detecting all creatures regardless of stealth value.

**Acid Splash**: 3 turns. Shoots a projectile which, upon hitting an enemy, a wall, or the targeted space, creates acid terrain on the location. At wisdom 5, this means an acid puddle on the space itself and two other adjacent spaces, but at high spellpower this could mean a large area with deep acid in the middle. Any enemy struck by the projectile takes moderate acid damage.

**Chilling Grip**: 2 turns. Targeted enemy in sight immediately takes light cold damage, ignoring armor.

**Conjure Ammunition**: 7 turns. Spawns a full quiver of a type of ammo corresponding to an equipped ranged weapon (if no such weapon is equipped, spawns a Belt of Knives). This ammo will have a small enhancement bonus determined by spellpower. This object is temporary and will disappear between levels.

**Premonition**: 6 turns. When cast, the game remembers the complete state of the level that instant. Play continues normally for a short duration, except that the player has a un-removable "premonition" buff for a short duration. When the buff expires or the player dies, the game returns to the state when premonition was cast.

**Static Charge**: 5 turns. Applies a buff to the caster for a short duration. Each turn, an enemy within a short range will be targeted by a highly accurate instantaneous projectile that deals light lighting damage.

**Succor**: 11 turns. Grants a small amount of temporary hit points to the player for a long duration.

**Treachery**: 8 turns. Target an enemy in line of sight. That enemy gains the "treachery" debuff for a long duration. All enemies are hostile to the target, and the target is hostile to all enemies.

**Wind Step**: 4 turns. Causes targeted creature (including the player) to gain the Wind Step buff for a short duration. This buff makes movement instant on a 2 turn cooldown, grants Flight, and grants a moderate dodge bonus.

**Cold Wind**: 5 turns. The player is prompted to target a space, and then set a direction. A special effect fills a moderate-size, roughly rectangular area. Enemies within this effect take light cold damage and are knocked back a very short distance in the direction that was set. The player is unaffected.
  
**Dispel**: 3 turns. Affects a targeted space within line of sight. An instant anti-magic effect is applied to all creatures and objects in that space, removing any ongoing magical effects. Magical enemies gain the “nullified” debuff for a short duration, losing the ability to channel any spells, and possibly certain intrinsics. Undead are dealt light damage. Constructs are dealt heavy damage.

**Flash**: 2 turns. A small area of effect a short range away from the caster. Spaces in this area become Brightly Lit for 1 round. Enemies in this area take light fire damage, and are blinded for a short duration if the space they were standing in was formerly Dark, or they have Light Sensitivity.

**Scouring Wind**: 4 turns. A targeted enemy is afflicted with the "scoured" debuff for a very short period of time. This debuff has the following effects each round: the enemy will take light physical damage each round. The enemy will be disarmed if possible. The enemy will suffer a small amount of armor corrosion. The enemy will be knocked back with a low probability each turn, in a direction set by the caster upon casting the spell.

**Shardspray**: 3 turns. This spell creates a scaling number of projectiles that immediately fire off in random directions. If cast on the floor, these can be in any of 16 directions (the 8 movement directions, plus 1 in between each of them). If cast on a wall, adjacent walls will prevent shards from firing in their direction, resulting in a more concentrated burst of shards. Each shard deals light physical damage and has high accuracy. These projectiles go through the player without triggering any effects. With this spell, the projectiles originate adjacent to the space targeted, and thus an enemy on a targetted floor space will be undamaged.

**Eruption**: 5 turns. Targetted space in short range, no los required. A small area around the targetted space becomes highly dangerous "spell-lava" terrain. This terrain is identical to lava, except that all damage it causes scales with spellpower and is reduced by (50+Spellpower)% when applied to the player. The lava terrain will become stone terrain after a short duration.

**Bless Equipment**: 10 turns. Applies a “blessed” trait to a piece of equipment, increasing its effective enhancement bonus by a figure that scales with spellpower. This trait is removed when the spell is cast again, and between levels. (Enemies who use a scroll of bless equipment gain a permanent attack buff, and lose “keeps distance”)

**Blast of Wind**: 3 turns. Fires a short-range projectile that can penetrate any number of enemies. Enemies hit take light physical damage and are knocked back a short distance.

**Stone Body**: 6 turns. The player gains the “Stone Body” buff, gaining a small bonus to armor for a moderate duration and increasing armor apply chance by a small amount. The player also gains resistance to lightning and fire, and slow movement, for the same duration.

**Shadows**: 5 turns. Creates a moderate-sized area of effect. This effect makes the spaces inside dark with a high priority. It also applies a "fade" buff to the caster as long as they are within the area, granting a small bonus to Hide. This spell only makes noise if it affects a space that is brightly lit.

**Brutish Transformation**: 10 turns. For a long duration, the player gains a moderate bonus to melee damage, melee attack rolls, parry value, and armor value. The player cannot access the inventory, interact with items, or use Feats or Tricks.

**Craven Transformation**: 10 turns. For a long duration, the player gains a moderate bonus to stealth value, bonus damage from stealth, and movement speed, and a small bonus to dodge. The player cannot make attack rolls against aware enemies, and has their “Guard” down for the duration.

**Torpid Transformation**: 8 turns. For a long duration, the player gains +5 spellpower, casts spells at 125% spellpower, subtracts 1 from the channel time for all spells, and gains temporary ability to cast 2 additional random spells. The player suffers a crippling penalty to speed, does not receive armor bonuses from equipment, cannot make melee attacks or fire ranged weapons, cannot dodge, and has the “guard down” debuff for the duration.

**Command**: 6 turns. Target an enemy in line-of-sight, within a moderate range. For a short duration, this enemy is afflicted with the command status. An enemy with this status does not act on its own, but prompts the player to act for it each time it would take a turn. Actions taken this way can anger neutrals, causing them to become permantly hostile to the commanded enemy's pack. Creatures friendly to the commanded target, including the target's own packmates, can become temporarily angered and hostile, ONLY to the commanded target. They will become friendly again when the effect ends.

**Read Magic**: 2 turns. Once cast, the player is prompted to choose a scroll from their inventory. If an unidentified scroll is chosen, that scroll is identified. If an identified scroll is chosen, the player begins to cast that spell as if from their spell list without consuming the scroll (this is cast at 75% normal spellpower).


## *Tricks*

**Assassinate**: Unlocks a critical strike option with a 200% damage multiplier. If the enemy dies, their death does not make any extra noise (same sneak/hide malus as moving). If the attack deals sneak attack damage (such as against an unaware target) that damage is tripled as well.

**Bushwhack**: Improves the rate at which Cunning increases sneak attack damage. If an enemy is reduced to less than (2 x Cunning)% HP by an attack that dealt sneak attack damage, that enemy dies.

**Blindspots**: Tightens the vision cones of all enemies slightly.

**Careful Aim**: Whenever you add sneak attack damage to your attack, you reduce the likelihood that armor will apply to that attack by 5% for each point of Cunning you have. A similar effect applies to any critical strike.

**Camoflage**: At the start of each mission, a number of "camoflage" items spawn on the floor of the level. Upon pick-up, these items disappear and grant you a small bonus to hide that will last until you leave the level. The number of camoflage items in a level depends on your Cunning.

**Crowd Cover**: If an enemy is aware of hostiles besides the player, and those hostiles are within 6 spaces of the player, it will ignore the player to attack them, even if the player is closer.

**Disguise**: At the start of each mission, a number of "disguise" items spawn on the floor of the level. Upon pick-up, these items disappear, and a random enemy pack on that floor will receive the "Fooled" status. Fooled enemies do not check the player's stealth, and do not become aware on their own. Shouts, taking damage, etc. can still make them aware of a player in their vision zone. If a fooled enemy becomes aware, they lose the fooled status. The number of disguise items in a level depends on your Cunning.

**Healer's Art**: At the start of each mission, a number of "healing supply" items spawn on the floor of the level. Healing supplies are an item with 1 encumberance. When used from the inventory, the player enters a "Healing" state, much like channeling or reloading. If they stand still for 10 turns, the healing supplies are consumed and you recover 25 hit points. The number of healing items in a level depends on your Cunning.

**Leg It**: Speed bonus from Sprinting increases by 25. You gain a cunning-scaled dodge bonus while sprinting. When standing still, 2 stacks of fatigue are removed instead of 1.

**Looter**: Slightly improves the rate at which Cunning increases the amount of loot that spawns on a level.

**Misdirection**: Enemies who become alerted but are NOT aware of the player's true location receive the "Distracted" debuff, lowering their sight and hearing scores by a significant amount.

**Poisoncraft**: Damage dealt to enemies that is caused by the effects of coating a weapon with a potion is increased by a figure that scales with your Cunning. 1 extra Potion of Poison is spawned on the floor of every mission.

**Scrappy**: When you dodge a melee attack, gain a "scrappy" buff that increases melee accuracy and damage slightly, scaling with Cunning.

**Disappearing Act**: Activate from the special abilities menu. For 5 turns, you gain a large bonus to Sneak and Hide and enemies can lose track of you even if you are still in their vision zone. Usable once per mission.

**Statue Gambit**: You receive a small (additional) bonus to Sneak and a large (additional) bonus to Hide when standing still.

**Alchemist**: Immediately identify random potions equal to your cunning, starting with those in your inventory. Each time your cunning increases, identify a random potion. At the start of each level, receive a random potion. If you pick up “alchemical scraps” you will be prompted to turn it into one of three potions (taken from the list of identified potions).

**Sniper**: While standing still (and not casting/reloading), while holding a ranged weapon, you gain a stacking “aim” bonus that greatly improves accuracy and slightly improves damage multiplier. The number of aim stacks you can accrue is equal to Cunning. Stacks are removed if you do anything besides stand still.

**Opportunist**: Every enemy with its guard up has a % chance to drop it at the end of its turn equal to twice your Cunning. Sneak attack damage is applied to critical hits on aware enemies.

**Elocution**: You now gain a spellpower bonus from Cunning, applicable only when using scrolls. Scrolls are cast in 2 fewer turns.

**Uncanny Dodge**: Increase the rate of scaling for dodge bonus from Cunning slightly. You are not limited to dodging once per round, and can even dodge the same attack multiple times. This can allow the player to dodge their way out of AOE effects by making multiple checks in a row.

**Thief**: Unlocks a critical strike option that deals no damage and always hits. The player is prompted to take any items in the enemy’s inventory that they choose. If possible, the enemy suffers the “disarmed” debuff. This does not make any extra noise (same sneak/hide malus as moving), and the target is not automatically alerted to the player. Additionally, the first time you pick an item off the ground each round, the action is instant and silent.

**Trapsmith**: Used from the special abilities menu. Prompts the player to select an adjacent trap. Different traps can be disabled, triggered, re-enabled, or even rendered "friendly", depending on the trap. Some traps can be taken, and will appear in the inventory as items with 1 encumberance. When used, these items allow the player to place the trap on an adjacent space. Disabled traps now appear in levels, depending on your Cunning.

⋅⋅⋅ **Efficacy Unwitnessed**: All traps that deal damage now allow the "upgrade" action. This takes several turns and results in the trap dealing addtional damage according to the player's cunning. Disabled traps spawn more often. 

**Quick Hands**: Automatically activates when you draw a weapon, put one away, throw something, or spend a turn reloading. That action becomes instant. After it activates, it goes on cooldown for two turns.

**River’s Current**: The base speed bonus from sprinting is increased (25->35). Sprinting is not unstealthy (Same hide/sneak malus as normal movement). Sprinting grants a dodge bonus for its duration. You suffer only 3 stacks of fatigue for each 5 rounds spent sprinting.


## *Feats*

**Arsenal**: For each weapon in your inventory with an encumberance of at least 1, treat your valor as 1 higher for the purposes of ignoring encumberance penalties. Switching weapons is a free action.

**Brigand**: All enemies drop a tiny amount of gold on death, depending on their tier.

**Charge**: When moving while sprinting, you gain stacks of a buff which increases the damage modifier of the next melee attack you make. An attack benefiting from any number of these stacks increases its Cleave value by 1. You can accrue a number of these stacks up to your Valor. While fatigued, you do not take penalties to your combat stats.

**Disarm**: Unlocks a normal attack and a critical attack. The normal attack has a 20% damage modifier, but applies the "Disarmed" debuff to any armed enemy it hits. The critical attack has a 130% damage modifier, and applies the "Severed Arm" debuff to enemies it hits. This debuff works like disarm, but it is permanent.

**Discretion**: Valor now lowers effective encumberance for all penalties, including stealth and speed penalties.

**Duelist**: Once per turn, you parry an attack as if your valor were 50% higher. This applies to first attack that targets you after your turn ends.

**Battle Stamina**: Whenever you kill an enemy with a weapon attack, heal HP equal to 5 plus the enemy's tier, times the enemy's tier, plus 3. So for tiers 0, 1, 2, and 3, that's 3, 6, 17, and 27.

**Berserk**: When you make a “Reckless” attack, any critical attack except “Cautious”, or spend a turn bonestuck, you gain a stack of the “Berserk” buff that grants small bonuses to dodge and armor and large bonuses to melee damage and accuracy. You can accrue a number of berserk stacks equal to your Valor. Stacks are lost at a rate of 1 each round you do not gain a stack.

⋅⋅⋅ **Blood Rage**: Whenever you kill an enemy with an attack, gain stacks of Berserk equal to its tier+2. Whenever you take damage from an attack, gain a stacks of berserk equal to 1/10th the damage, rounded down.

**Sunder**: Unlockes a basic and a critical strike option. The basic option has a damage mod 125% and causes the player to drop their guard. It never bypasses armor. When it lands on an enemy with armor, it applies stacks of armor damage equal to half of your valor (rounded up). The critical strike is similar except it has a 200% damage mod, applies stacks of armor damage equal to your valor, and stuns the target for a round.

**Soften 'Em Up**: Whenever you hit an enemy with a ranged weapon attack, they gain the "Softened Up" debuff permanently. When attacking a softened up enemy, the player gets a bonus to accuracy and damage mod. This only affects melee attacks, and only when the softened enemy is below 60% HP.

**Throwing Arm**: Thrown weapons and potions travel faster and max throw range is increased. Grants a valor-based bonus to the accuracy and damage of thrown weapons.

⋅⋅⋅ **Throw Anything**: Any item or piece of equipment can be thrown if it has a an encumberance value. Items with higher encumberance values will deal more damage, but have a shorter range. Items named "Rock" "Log" etc. will spawn on every map, having no function but having very high encumberance values.

**Toe-to-Toe**: For each enemy that is adjacent to you, aware, and hostile, you gain a bonus to Accuracy and Parry. This bonus is higher for higher-tier enemies. You are immune to disarm.

⋅⋅⋅ **Tooth-to-Tooth**: You now also receive a bonus to the damage modifier of all your attacks for each enemy in melee with you. When blinded, you can still see spaces adjacent to you. When stunned, you can make a melee attack instead of standing still.

**Overwhelm**: Every melee attack, regardless of outcome against an enemy has a 20% chance to apply the "Overwhelmed" debuff to an enemy for exactly 2 turns. Overwhelmed enemies have their guard down, cannot cast spells, and cannot move.

**Rapid Strikes**: Unlocks a normal attack and a critical attack. The normal attack consists an unmodified attack that, once resolved, triggers another unmodified attack next turn, followed by a third attack which is instantaneous but otherwise unmodified. This effectively allows the player to make 3 attacks against the same space in 2 turns. The critical version of this attack has a 1.2 damage multiplier. If it hits, the target is stunned for 1 round. This attack triggers additional attacks, much like the normal version, except with the 1.2 damage multiplier.

**Follow-Through**: Increases the Cleave value of all your melee attacks by 1. Increases the number of enemies your projectile weapons can penetrate before stopping by 1. Grants a new critical strike, "Hewing Strike". This attack deals triple damage and drops guard. Like other critical strikes, it does not cleave normally. However, it checks cleave, and targets adjacent enemies with attack using the "Reckless Attack" profile, according to the cleave number.

**Power Blow**: Standing still while holding a melee weapon causes you to gain stacks of the “Power Blow” buff, that are lost if you do anything else. When you’ve accrued any stacks you may use the “Power Blow” melee attack from the strike menu, which cannot be parried, has a large damage multiplier, and causes small knockback. The effects of power blow scale with the stacks accrued.

**Atlas Strength**: Double your Valor for the purpose of negating Encumbrance penalties.

**Diehard**: Once per level, when you would be killed, remain at 1 HP and become immune to HP loss for a number of rounds equal to your Valor.

**Dual-Wield**: When holding a weapon in your off-hand, each time you make an attack, you make an additional attack with the off-hand weapon with a -25% damage mod and no other modifiers except Valor bonuses.

**Uncanny Parry**: Increase the bonus to parry from Valor slightly. You can parry melee attacks that are normally unparry-able, such as those from large enemies. You can parry missile weapons. You can parry normal melee attacks from enemies outside your field of vision, as long as you are aware of those enemies.

**Bastion Stance**: Activate and deactivate from the special abilities menu. Gain “Strafe”, become unable to parry or dodge (guard is not down), and gain extra armor proportional to your parry bonus to all melee and ranged attacks that originate from enemies in front of you (180 degrees). While this feat is active, you have a single-width line blindspot in the middle of your vision field.

**Point Blank**: Guard is not dropped when reloading or firing a ranged weapon. Ranged attacks targeting spaces within 5 spaces receive a small accuracy and damage multiplier bonus that scales with valor.

**Grit**: At the start of each turn, heal 1 HP unless your current HP is a multiple of 10.

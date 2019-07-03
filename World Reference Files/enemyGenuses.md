# *Enemy Genuses*

**Orcs**:

Found in: Cave, Ruins, Swamp, Forest, Stronghold*, Pirate*, Town Raid*, Battlefield*

Orcs spawn in packs that are friendly to each other, with one higher tier orc as the “leader”. The others will try to stay within a certain distance of their leader. By default, every orc is Neutral to all orcs not in its pack. If two leaders of different packs enter each other’s line of sight for the first time, they will gain the “Parleying” status and approach each other. Once they are a few spaces away from each other, they will spend a few rounds shouting. Then, one of 3 things will happen.

    1- A duel. If the Leaders are equal tier, they become hostile to each other. When one dies, the other becomes Leader of both packs. If one leader is lower tier than the other, he and his pack will instead become part of the other leader’s pack.
    2- Orc war! Both orc packs become hostile to the other.
    3- Accord. The Leaders will wander in opposite directions and ignore each other from then on.

If either leader spots the player while “Parleying” the “Accord” result is immediately chosen. Every orc in both packs has perception 0 for the duration of the parley.
When an orc pack’s leader is killed outside of a parley, nothing happens if the pack is hunting the player. But the second a leaderless pack is not hunting the player, the pack undergoes succession. Succession takes place as follows:

If there is only one of the highest tier of orcs present, that orc becomes the new leader. If ALL the orcs are the same tier, a random leader is chosen. Otherwise, all orcs of the highest present tier become hostile and fight to the death. When only one remains, that orc becomes leader.

ALL orcs described here are blinded for 1-4 rounds whenever they receive lightening damage.
*When orcs spawn as the main genus in these environments, fewer orcs will spawn and they will all be friendly to each other. When they are a side genus, they spawn as normal.

*Orc Runt*

Shouts, Armed, Keeps distance (unless other orcs hostile), Guards Hallways, panicky, dark vision, light blindness, reckless, tier 0.

    “A dwarfed and stunted specimen, standing waist-high, and as cowardly as it is vicious. It will not face you alone, unless it is cornered, though it will try to scout for its pack.”

*Common Orc*

Shouts, Armed, Armored, Guards Hallways, panicky, dark vision, light blindness, reckless, tier 1.

    “Resembling a large, ugly ape in battered, scavenged armor and wielding crude weaponry, this creature’s head comes almost to your chest. It is little more than a clever predator, possessing only rudimentary language, though it can see in the dark.”

*Orc Bowman*

Keeps Distance, Armed, Ranged attack, reload=1, tier 1, dark vision, ammo=12 panicky, light blindness, perception=2.

    “A particularly stunted orc who compensates with cleverness. It has learned to use a bow, and does so at the slightest opportunity.”

*Orc Alpha*

Armed, Armored, dark vision, light blindness, reckless, tier 2.

    “This orc is larger than its kin, and while still possessing gangly, ape-like proportions, its posture is straight, and proud. It is fearless, stands head-height to your chin, and has taken the best looted weapons and armor for itself. Its face is bestial, but not so misshapen as other orcs’.”

*Orc Smith*

Armed, Armored, dark vision, light blindness, reckless, collects weapons and armor, tier 2.

This enemy gains an attack bonus for each weapon in their inventory, and an armor bonus for each piece of armor in their inventory.

    "This cunning creature has inherited the advanced technological secrets brought by its ancestors when they invaded centuries ago. It is scrounging this area for equipment to incorporate into its personal arsenal."

*Orc Priest*

Keeps Distance, Shouts, Armed, Armored, dark vision, light sensitivity, tier 2, Perception=1.

Only spawns as the leader of a lower-tier pack. If it reaches the “Duel” result during parley with a leader who is not an Orc Priest, that orc and its pack immediately join the Orc Priest’s band, as if it were a lower tier orc. Orcs in its pack act as if they had “Relentless” and no other special behaviors.

    “Judging by its dress, this is an emissary from the orcish homeland, preaching the pointless faith of the orcs’ dead god to the mongrel barbarians. Religion will almost certainly give his followers courage, but likely not wisdom. These orc-priests are famous for leading their packs into traps.”

*Orc Brute*

Relentless, Slow movement, Slow attack, dark vision, light blindness, tier 2.

When spawned as a leader of an orc pack in an Orc level, it has a 50% chance to be the only one in its pack.

    “Hulking and powerful, but cripplingly malformed, bulbous muscle spasms grotesquely under this monster’s black hide. Legends attribute the origin of these massive orcs to everything from interbreeding with trolls to the consequence of cannibalism.”

*Orc Soldier*

Armed, Armored, dark vision, light sensitivity, tier 2.

    “Man-sized and disciplined, this orc is decked out in orc-wrought gear. He carries a curved sword—favored by orcish armies because they enable the hacking and slashing that comes so naturally to orcs, while compensating for their lesser strength.”

*Orc Arbalest*

Armed, Armored, ranged attack, reload 4, ammo=10, Keeps distance, dark vision, light sensitivity, tier 2.

    “A stout warrior wielding a stout weapon, which was built to lay low strong men in strong armor. A dangerous ranged fighter, a group of these could bring down a giant in a single withering volley.”

*Orc Captain*

Armed, Armored, dark vision, light sensitivity, tier 3.

The orc captain only spawns as a leader of lower-tier orcs.

    “This orc’s man-like proportions and posture see it loom above lesser orcs. Its strength and skill at arms dwarfs theirs, and likely yours as well.”

*Orc Berserker*

Armed, fast attack, dark vision, light blindness, reckless, relentless, tier 3.

This enemy gains beserk stacks much like the player feat "Berserker".

    "Wild-eyed and snarling, this orc flings itself at prey with reckless abandon that makes other orcs seem tame. Nigh twenty stone of orcish muscle powered by a deep well of orcish bloodlust."

*Giant Orc*

Armed, Armored, dark vision, light blindness, Slow movement, Slow attack, reckless, relentless, tier 3.

    "This orc must weigh at least fifty stone. It effortlessly carries a tree-trunk club and armor improvised from broadshields and rope."

*Orc Elder*

Armed, Armored, dark vision, light sensitivity, keeps distance, ranged attack, ammo=5, reload=5, tier 3.

These orcs only spawn as leaders of a pack. If it reaches the “Duel” result during parley with a leader who is not an Orc Priest, that orc and its pack immediately join the Orc Priest’s band, as if it were a lower tier orc. This enemy will not reload if aware of the player. This enemy spends its turn in a "Commanding" state when not moving or shooting, which grants the other members of its pack a bonust to Accuracy and Dodge.

    "The visage of this ancient orc has been weathered by years in the wilderness and maimed by countless raids. It busies itself constantly with the sisyphean task of enforcing military discipline among the ranks of its raucous following."
    
*Warforged Orc*

Armed, Armored, dark vision, collects weapons, armor, and quivers, ranged attack, reload=1, ammo=1, tier 3.

This enemy gains an attack bonus for each weapon in their inventory, an armor bonus for each piece of armor in their inventory, and 3 additional ammo for each quiver in their inventory.

    "This orc is so covered in iron and steel that you cannot tell where prosthesis ends and armor begins. It's blades are long and sharp, and within its arm-mounted crossbow some strange machination whirs disconcertingly." 

# **Kobolds**:

Found in: Cave, Ruins, Forest, Swamp, Stronghold
All kobolds on a level will always be friendly to each other, though they spawn and wander in separate packs. Maps in which kobolds are present always feature special “kobold den” terrain, similar to cave terrain, but with more traps and treasure. If kobolds are the main genus, this terrain will be large, multi-chambered, and located centrally in the map. If they are a side genus, a single-room den will spawn, and the kobolds will spawn around it. Kobolds always spawn with one “boss”, of a higher tier than any other kobold in the level, even if there is no boss quest objective, and it always carries a valuable item.

*Kobold*

Armed, stealth=1, avoids traps, shouts, guards hallways, tier 0.

Spawn rate heavily favors large groups of these basic kobolds over stronger mobs.

    “Standing knee-high and armed with a primitive spear, these bipedal reptilian savages live in burrows filled with traps.”

*Red Kobold*

Armed, reach, avoids traps, res: fire, shouts, guards hallways, extra spawn weight (climate: hot), tier 1.

    “Taller and stronger, this kobold’s scales have a reddish hue, and his spear is long and sharp.”

*Black Kobold*

Armed, stealth=3, perception=1, avoids traps, flees when spotted, aquatic, extra spawn weight (terrain: swamp), tier 1.

When this stealth enemy successfully sneak attacks the player, it does triple damage instead of double.

    “Slinking low with a vicious stone dagger in its jaws, this black kobold skulks around, hoping to ambush you.”

*White Kobold*

Relentless, cleave=4, friendly fire, res: cold, repulsive, extra spawn weight (climate: cold), tier 1.

    “This white kobold is as tall as your waist, and its features are bestial and exaggerated. It thrashes its wicked claws and clubbed tail about haphazardly.”

*Blue Kobold*

Armed, stealth=1, res: lightning, ranged attack, reload=1, keeps distance, lures for traps, tier 1.

When this enemy spawns, two extra traps spawn within the kobold den terrain.

    “This kobold carries equipment seemingly intended for building or crafting, and hurls stones at you with a crude sling.”

*Green Kobold*

Keeps distance, res: acid, stealth=1, avoids traps, throws potions, drinks potions, picks up potions, tier 1.

This enemy spawns carrying 1 random potion.

    “This strange green kobold scurries around collecting herbs, insects, and the filth of its brethren. It covets alchemical potions greatly, and will use them to defend itself.”

*Kobold Warlord*

Armed, Armored, spear effect, immune: fire, avoids traps, guards hallways, call to arms, extra spawn weight (climate: hot, terrain: stronghold), tier 2.

This enemy casts firebolt after channeling for 5 turns, which it does whenever it has no path to the player or it sees the player from very far away.

    “Lean and agile, this kobold stands even with your chest. Bright red scales shine through the gaps between pillaged armor, large horns jut from under its helmet, and fire dribbles from its jaw as it looses a warcry.”

*Kobold Assassin*

Armed, stealth=5, perception=1, poison attack, avoids traps, flees when spotted, emboldened by: player poisoned, aquatic, extra spawn weight (terrain: swamp), tier 2.

When this stealth enemy successfully sneak attacks the player, it deals triple damage (instead of double like most enemies) and applies extra poison damage.

    “Slithering like a shadow through the underbrush on all fours, black spikes growing menacingly from its joints and skull. This creature drools vicious clear venom from its wicked jaws onto an iron stiletto as it draws it.”

*Kobold Berserker*

Relentless, immune: cold, emits Frost Gas in low volume, cleave=4, friendly fire, repulsive, extra spawn weight (climate: cold), tier 2.

    “Larger than a man and covered in natural weapons, this immense white kobold looks like it could tear you limb from limb. Whenever it exhales, a biting cold mist pours out of its mouth.”

*Kobold Engineer*

Armed, stealth=2, immune: lightning, perception=2, keeps distance, lures to traps, ranged attack, reload=3, tier 2.

When this enemy spawns, 5 extra traps spawn within the kobold den terrain.
This enemy casts the enemy spell “Charge Attack” after channeling for 5 rounds, and does so whenever it is unaware of the player or has lost line of sight.

    “This kobold’s scales are a vivid blue, and its possessions are oddly sophisticated. Of particular note is its crossbow, which is connected by a series of snaking tubes to a bizarre muzzle-like apparatus that it wears. The tell-tale crackling of electricity accompanies the whole affair.”

*Kobold Alchemist*

Stealth=2, immune: acid, keeps distance, uses potions, picks up potions, avoids traps, tier 2.

This enemy spawns carrying 2 random potions, and 1 “flask of acid” potion.

    “Its scales a brilliant hue of green, this kobold carries a bandolier of crude canteens. It obsesses over them, sniffing each one before thoughtfully adding a glob of its acidic saliva.”

*Female Kobold*

Immobile.

This enemy spawns in small vaults inside kobold dens as scenery/quest objective.

    “Resembling an engorged brown alligator, it doesn’t look like this kobold female has ever left the den it was spawned in. There’s no telling if it’s intelligent; it doesn’t seem the kobolds bothered to teach it language.”

*Red Drake*

Immune: fire, flying, avoids hovering over hazards, extra spawn weight (climate: hot), tier 3.

This enemy can cast firebolt after channeling for 4 turns, which it does whenever it has no path to the player or it sees the player from very far away.

    “Proportioned like a lion, and as tall as a horse, adolescent red dragons are terrifyingly agile for a creature so strong. And then of course, there’s the fire.”

*White Drake*

Immune: ice, relentless, cleave=4, friendly fire, emits Frost Gas in large volume, extra spawn weight (climate: cold), tier 3.

    “The rolling icy mist that follows this creature would conceal its form were it not so damn big. It breathes a killing wind out from in between teeth the size of your arm, and spikes grow from the bone club at the end of its tail.”

*Blue Drake*

Immune: lightning, no melee, perception=3 flying, lures for traps, keeps distance, avoids bad gasses, tries to hover over hazards, tier 3.

This enemy can cast lightning bolt after channeling for 3 rounds, which it does whenever it has line of sight and isn’t fleeing. However, it will not do so when surrounded by any flammable gas.
Whenever this enemy spawns, a premade vault from the “blue drake” list is placed (within the kobold den if it exists), and the blue drake spawns inside of it.

    “Only about the size of a man, this cunning blue dragon makes up for it partly by being clever, but mostly by shooting lightning at things. Blue dragons hate nothing more than a fair fight, and have a reputation for building ingenious underground lairs.”

*Black Drake*

Aquatic, stealth=4, flees when spotted, emboldened by: player poisoned, extra spawn weight (terrain: swamp), poison attack, perception=2, avoids traps, tier 3.

    “This serpentine creature glistens in the dim light, its mouth slavering with a deadly venom. It must be the size of a horse, though it coils itself low to the ground.

*Green Drake*

Immune: acid, flying, avoids traps, keeps distance, Stealth=1, Perception=1, tier 3.

This enemy can cast Acid Bolt after channeling for 4 rounds, which is its main form of attack. It can also cast Emit Acid Gas after channeling for 3 rounds, which it does once the player draws near.

    “The lizard-like proportions look odd, even comical on a creature larger than you are. The way it hurls great blobs of acid while hiding behind acidic vapors is less funny. At least it doesn’t have a throwing arm.”

*Red Wyrm*

Immune: fire, flying, avoids hovering over hazards, extra spawn weight (climate: hot), breaks walls, massive, tier 4.

This enemy can cast Cone of Fire after channeling for 4 rounds, and does so whenever it sees the player from very far away or is unable to approach. It ignores basic Kobolds, but will not channel if advanced kobolds are in the way.

    “With limbs like tree trunks and the power to destroy a town by breathing, it’s little wonder that kobolds revere red dragons as gods of war.”

*White Wyrm*

Immune: ice, relentless, cleave=5, friendly fire, emits Frost Gas in absurd volume, extra spawn weight (climate: cold), massive, breaks walls, tier 4.

    “This titanic white lizard carries the heart of winter inside of it wherever it goes, and the air that enters its body leaves as a blizzard. Kobolds revere these creatures as elemental forces of destruction.”

*Blue Wyrm*

Immune: lightning, perception=4, flying, lures for traps, keeps distance, avoids bad gasses, tries to hover over hazards, avoids projectiles, tier 4.

Whenever this enemy spawns, a premade vault from the “blue wyrm” list is placed (within the kobold den if it exists), and the blue wyrm spawns inside of it.
This enemy can cast “lightning bolt” after channeling for 2 rounds, which it will do whenever it isn’t retreating. It will only use melee if cornered.

    “This blue dragon hovers above the ground in a bi-pedal posture, its forelegs crossed in front of it. Kobolds revere these creatures as gods of trickery, because apparently kobolds consider “waiting in an advantageous position and shooting anyone who comes near” to be the height of cunning.”

*Black Wyrm*

Aquatic, stealth=3, extra spawn weight (terrain: swamp), poison attack, perception=2, avoids traps, massive, grapple attack, tier 4.

    “This great black dragon has grown too large to rely too heavily on stealth, though it still moves silently, and with an incredible serpentine grace. The stench of its venomous slaver stings your nose and eyes as it approaches. Kobolds revere these creatures, perhaps as gods of being backstabbing bastards.”

*Green Wyrm*

Immune: acid, flying, avoids traps, massive, emits acid vapor in low volume, Perception=2, tier 4.

This enemy can cast “acid bolt” after channeling for 3 rounds, and does so at long range. It can also cast “acid splash” after channeling for 3 rounds, which it does as long as it is within range to and the player is not adjacent.

    “This absurd creature has great bulbous body, massive wings, and a great long neck, all the better for hocking deadly loogies at anyone unfortunate enough to draw its ire. Kobolds revere these creatures as gods. Probably gods of good table manners.”

**The Army of the Dead**:

Found in: Stronghold, Town Raid, Battlefield

All army of the dead units are friendly to each other.

*Wretch*

Armed, shouts, guards hallways, tier 1.

This enemy, and all other wretches in its pack, loses the guards hallways behavior and gains the relentless behavior whenever it is hit with a ranged attack, or it has line of sight to the player for 15 consecutive turns.

    “Of all the creatures that attack in great raucous swarms, few possess the size and intellect of a fully-grown human being. This dirty man wielding a crude weapon is a soldier in the Army of the Dead, and has sworn an oath to die on the battlefield. His caution is born of cunning, not fear, and he is quick to abandon it if needs must.”

*Looter*

Armed, armored, drops gold, shouts, guards hallways, picks up weapons, picks up armor, tier 2.

This enemy spawns carrying a melee weapon. Each time it picks up a weapon, it gains a small buff to its attack, and each time it picks up a piece of armor, it gains a point of armor. As long as it is carrying at least one ranged weapon, it gains a ranged attack it can use 10 times.

    “In every situation, there are some who thrive. This wretch has stolen a large collection of weapons and armor from the battlefield, making him much more dangerous than his fellow soldiers.”

*Survivor*

Armed, relentless, slow movement, regen=1, tier 2.

    “Limping, slowly but resolutely, across the fields of carnage is a man whose broken body tells a bloody and terrible story. All fear of death has left him, and yet he lives still.”

*Craven*

Armed, stealth=2, flees when spotted, emboldened by: player health<40%, tier 2.

    “The Army of the Dead are not all so stoic. This one takes advantage of the chaos to stab the enemy in the back, and lets his battle-brothers do the dying, bitterly prolonging his own cursed existence.”

*The Dead*

Armed, armored, relentless, tier 3.

    “Unassuming amidst the gore and debris strewn across the battlefield, this man’s arms and armor are simple, but practical and well maintained. His eyes however, betray the grim baptism of countless nights lying wounded among the rotting dead. He has felt the sickening feeling of slaying his fellow man more times than you ever hope to. His cold, empty eyes barely acknowledge you as he approaches; to him you are just another victim.”

*Eliminator*

Armed, armored, stealth=3, ranged attack, clip=4, reload=10, ammo=12, flees to reload, tier 3.

    “The Army of the Dead does not shirk from casualties, but when losses to do not yield progress, these mysterious men appear to deal with whatever is impeding the horde, and they are amply equipped and supplied. If the problem is terrain, they come as scouts. If it is a fortress, they come as saboteurs. If it is you, they come as assassins, armed with dangerous repeating crossbows.”

**Outlaws**:

Found in: Forest, Cave, Coast, Pirate, Stronghold, Ruins, Town Raid.

Outlaws spawn in packs. All outlaw packs are neutral and potentially hostile to each other.

*Bandit*

Armed, ranged attack, reload 1, ammo=4, guards hallways, stealth=1, tier 1.

    “Poorly equipped, half-starved, and ragged, months of surviving outside of civilization have left this man’s body weakened, but sharpened his resolve to a killing edge. They ambush their prey in groups, firing withering volleys of arrows before closing in with knives, clubs, and hatchets. They trust the men they break bread with, but can turn on other gangs in an instant.”

*Sellsword*

Armed, armored, random attack ability, shouts, tier 2.

    “Well equipped and experienced, this is either a mercenary turned thug due to scarce times, or a thug turned mercenary thanks to plenty ones. Either way, he sells these outlaws raw combat ability to fill out their ranks.”

*Dashing Rogue*

Armed, monologues, lunge attack, disarm attack, flees when hp<35%, immune to drowning, entanglement, and blinding, tier 2.

    “In the interest of affecting a roguish persona, this outlaw has cultivated a respectable mustache and invested in multiple gold teeth. While these things might impress frightened travelers, you’re more concerned with his rapier, which he flourishes with intimidating grace.”

*Mountebank*

Keeps distance, uses scrolls, picks up scrolls, monologues, flees when hp<50%, tier 1.

This enemy spawns with 0-2 enemy-usable scrolls in its inventory.

    “People fear magic, and the unscrupulous sometimes use parlor tricks to pose as fearsome wizards. Their simple understanding of the arcane allows them the use of scrolls, for the purpose of demonstrating their fictional powers on any brave enough to challenge their claims. While he could easily have some very dangerous spells within the folds of his voluminous robes, you are not about to surrender your possessions to this knave.”

*Spellbreaker*

Shouts, armed, 3 random enemy spells, tier 2.

    “An escaped Strandian spellslave, as evidenced by the remains of the now shattered spellcage apparatus, which clings tenaciously to his body in ragged pieces. Free will has given him access to a greater range of powers, but with the spellcage broken his potency suffers.”

*Bandit King*

Armed, Armored, drops gold, call to arms, stealth=1, perception=2, avoids bad gasses, avoids projectiles, flees at hp<35%, emboldened by: health%>playerhealth%, lures for traps, tier 3.

    “Thief turned warrior turned merchant, this man rose from rags into wealth on the winds of his unflagging confidence, ruthlessness, and ability. His weapons and armor make him a truly fearsome melee combatant, and he is ever watchful for hidden blades and skulking bowmen, living as he does among his army of cutthroats.”

**Wizards**:

Found in: Tower, ruins, town raid, hellscape.
All packs that spawn as a part of this group are neutral to one another, and all include one enemy with spells, either wandering alone or as a leader of a group of non-spellcasters.

*Clay Golem*

Relentless, construct, perception=-1, immune to burning, slow attack, forgives neutrals, tier 1.

    “The wizards of Valakazaht enchant these large humanoid statues to serve them. They deem physical labors beneath them, but have need for some of them, primarily violence. This monster has prodigious strength, but is slow, clumsy, and predictable.

*Apprentice*

Keeps distance, 1 random enemy spell, flees if can’t cast, tier 1.

    “A neophyte among the Valakazaht, this person commands real supernatural powers, and is therefore not to be underestimated. These apprentices are subjected to a lengthy hazing period during which they are mostly ignored or abused by their masters. This hazing period typically ends when they kill one of their seniors, plunder their notes, and assume their identities.”

*Stone Golem*

Relentless, res fire/cold, construct, perception=-2, slow attack, slow movement, forgives neutrals, tier 2.

    “Assembled from large rough-hewn blocks of stone, this construct is incredibly resistant to damage. It also possesses prodigious strength, though its limbs move slowly. To engage this… thing in combat would be akin to demolishing a rather thick stone wall, and you don’t relish the idea.”

*Wizard*

Keeps distance, shouts, flees if can’t cast, drops gold, friendly fire, 3 random enemy spells, tier 2.

    “This person’s ornate red robe and abundance of jewelry out them as a member of a loose fraternity of magicians known as the Wizards of Valakazaht. This order is devoted to little more than strength in numbers, in order to subject the rest of the world to their conceited whims. Each wizard guards their secrets jealously, and unleashes a personalized hail of death on any who threaten them.”

*Iron Golem*

Relentless, construct, res fire/cold/lightning, perception=-3, slow attack, forgives neutrals, tier 3.

    “These massive slabs of sharpened iron are held by some unseen force in the rough shape of a man. Iron golems are considered by the Valakazaht to be the ultimate proof that their magic is utterly superior to physical ability, and you are inclined to think they have a point. These iron monsters are even stronger than other golems, and all but impervious to harm.”

*Golem Master*

Keeps distance, shouts, flees if can’t cast, 1 random enemy spell, drops gold, tier 3.

This enemy always has the enemy spells “Heal Other” and “Haste Other” and always has a pack of at least two golems.

    “Specialists in the art of constructing and maintaining golems, these wizards can imbue their constructs with a quickening energy, and reform their bodies from thin air when damaged.

*Archwizard*

Keeps distance, shouts, flees if can’t cast, drops gold, friendly fire, quick cast=1, 5 random enemy spells, tier 3.

    “Archwizard is a self-granted title, but one that is not lightly claimed. It requires a wealth of prestige and some truly vulgar displays of magical power to claim this title without being laughed into ostracization. Toward that end, when one among the Wizards of Valakazaht reaches a level of incredible arcane power, having learned libraries of forbidden wisdom, and after years of careful preparation, they kill an existing archwizard, plunder their notes, and assume their identities.”

*Quicksilver Golem*

Fast movement, fast attack, construct, res cold, immune to burning, tier 4. 

    “Not known for their subtlety or finesse, the Wizards of Valakazaht rarely put more thought into their golem designs than “bigger and harder”. This specimen however, is a man-sized marvel of craftsmanship, possessed of an elegant, ornate design and sophisticated internal clockwork governing the movement of its joints and retractable blades. While more delicate than its simpler counterparts, it is still a man-sized hunk of steel, and one that moves with unnatural grace and incredibly quickly.”

*Titanic Golem*

Slow movement, slow attack, relentless, cleave=3, friendly fire, massive, res fire/cold/lightning, unbuffable, perception=-5, breaks walls, tier 4.

    “Not known for their subtlety or finesse, the Wizards of Valakazaht rarely put more thought into their golem designs than “bigger and harder”. And this monstrosity is no exception. It is an immense tower of steel-plated lead, arranged in the shape of a titanic squat humanoid. This thing could squash you like an insect, but thankfully is ill equipped to do so considering the slow, clumsy way it moves. To say nothing of its poor senses. In the legends, the hero would usually bait something like this into destroying a particular wall or enemy. Letting it take a swing at you would be incredibly risky though.”

*Lich*

Keeps distance, flees if can’t cast, drops gold, friendly fire, undead, 5 random spells, quick cast=1, tier 4.

When this enemy spawns, it also spawns an item called a phylactery. If there are any treasure chests extant on the map, there is a 50% chance the phylactery will spawn within one of those chests. Otherwise, the lich spawns carrying it. This item registers as strong, evil magic for detect magic effects. When this item is affected by anti-magic, submerged in acid or lava, or picked up by the player, it is immediately destroyed.
Each phylactery belongs to a specific lich. If a lich dies and its phylactery still exists, the lich will respawn in 20 turns without the “drops gold” trait nearby the spot where it died. If a lich dies while leading a pack, its followers guard the spot where it died.
If a lich sees its own phylactery, it will collect it.

    “One of the most feared and dangerous abominations to walk the earth, liches are created in dark rituals, whereby a human spellcaster becomes undead, its preserved corpse forever serving the corrupted will of its lingering spirit. If slain, it will rise again in mere moments. Only by destroying its phylactery, the magical vessel in which it secrets its soul, can the creature be made mortal.”

*Archlich*

Keeps distance, flees if can’t cast, drops gold, friendly fire, undead, 6 random spells, quick cast=2, tier 5.

This enemy spawns with 3 phylacteries associated with it. 1 is always carried by the Archlich itself. The others each have a 50% chance to spawn into random treasure chests, if there are any, and otherwise are carried by a random other pack leader of the wizards group. All 3 must be destroyed, otherwise the Archlich revives itself in the same way a lich would.

    “This desiccated undead creature styles itself as a lich-king of ancient Valakazaht, from before that mythical civilization was flung into ruin almost a thousand years ago. It may be an imposter, having assumed the title in the typical Valakazaht way, but you’re not about to argue the issue with something that could rout armies with a flick of its finger. Ever covetous of its longevity, the Archlich keeps multiple phylacteries, hidden in secure locations or guarded by its lieutenants. Paranoid of its conniving followers, it always keeps one on its person.”

**Strandian Forces**:

Found in: Ruins, cave, coast, battlefield, stronghold.

Strandian soldiers are all friendly to each other. Every enemy but Conscripts is limited to 1 per pack.

*Conscript*

Guards hallways, armed, armored, blocks when stationary, spear effect, panicky, tier 1.

When conscripts are adjacent to 2 other conscripts, they gain a bonus to armor and dodge. They will attempt group up with other conscripts until they receive this bonus and then move as a group.

    “An entire continent of different cultures has been brought low beneath the countless boots of the Strandian Army. Various innovations, including standardized government issue equipment and tactics emphasizing formation fighting make them a much more effective force than any before them, and their numbers vastly outmatch any other army the continent has ever seen, bar the dead. Working as a unit, conscripts form a shield wall, bristling with pikes.”

*Champion*

Armed, armored, blocks when stationary, disarm attack, avoids projectiles, ranged attack, reload 6, ammo=4, tier 2.

This enemy only reloads when in wandering, following, or guarding states, not when alert or searching.

    “Hand to hand combat is considered an honorable, yet common and coarse craft in Strandian culture. As a consequence, only the lower class, typically veteran conscripts, are recruited to ply this craft in earnest as part of the Strandian Volunteer Corps. In contrast to their radically modern army, these champions reflect traditional conservative battle-sense, fighting defensively and focusing on disarming their opponents.”

*Commander*

Armed, keeps distance, ranged attack, reload 3, ammo=5, panicky, tier 2.

This enemy always spawns as the leader of a pack of conscripts. This enemy buffs all conscripts in its line of sight passively whenever he is not panicking. This buff, which cannot stack, gives a small bonus to accuracy and dodge, and prevents them from panicking.

    “Considered a wholly separate endeavor from grand strategy, the task of commanding troops directly on the battlefield is still considered too delicate a task to entrust to commoners. Volunteers from the middle class and uninherited nobility form the battlefield command, whose task it is keep conscripts organized and fighting at peak efficiency. They are equipped with a light crossbow, for when particularly troublesome threats require executive attention.”

*Agent*

Armed, armored, uses potions, picks up potions, ranged attack, ammo=5, stealth=3, perception=2, tier 2.

This enemy will not use its ranged attack until it is spotted. It spawns with 1 random potion in its inventory. This enemy always spawns alone.

    “A highly trained operative in service to some arm of the Strandian rulership, this agent is a capable, methodical assassin. No part of the Strandian army, this person’s presence here indicates interests at play beyond the strategic value of the local territory. His weapons of choice are the shortsword and the throwing knives.”

*Spellslave*

Armored, relentless, 1 random spell, no melee, tier 2.

If this enemy is unable to cast spells, it will pass all its turns until it can again.
If this enemy gains 4 stacks of “corrosion” or the “sundered armor” condition, it becomes a “Spellbreaker”—see “Outlaws”. It then becomes neutral to the player, and all enemy types except Strandians, to which it is hostile.

    “Strandian culture has long viewed magic as vulgar and unholy, but to forge their new empire they had to recognize its usefulness. To that end, enslaved foreigners are encased in a nightmarish restraint known as a spellcage, which dominates their minds even as it amplifies their meager magical potential. Like all slave soldiers, they pose a risk of mutiny.”

**Vampires**:

Found in: Forest, cave, ruins, swamp, tower.

Enemies with vampire in their names will spawn as leaders of packs of enemies of factions they dominate, or else they will spawn alone. High tier vampires spawn relatively early, meaning that the total number of enemies will be few.

*Vampiric Thrall*

Armed, shouts, stealth=1, tier 1.

If all vampires in the level are killed, all Vampire Thralls become neutral to the player

    “His features are that of the local common folk, though his gaze carries the intensity of a fanatic. He clutches his improvised weapon with a similar enthusiasm. Ensorcelled by vampires, only his own death or that of his masters can free him.”

*Feral Vampire*

Dominates wolves, shouts, stealth=1, perception=1, light blindness, damaged by bright light, dark vision, tier 2.

    “A fresh inductee into undeath, this wretch does not yet understand its condition, nor its true power, but only the nightmarish hunger that afflicts it. It has no plan beyond a brutal ambush with tooth and claw.”

*Composed Vampire*

Armed, dominates outlaws, monologues, shouts, perception=1, dark vision, damaged by bright light, tier 2.

    “Clinging stubbornly to a semblance of life has denied this vampire supernatural strength or durability, but allowed it to bring a group of outlaws under its sway, the promise of coin delivered with a force no mortal could muster.”

*Vampire Sorcerer*

Perception=2, stealth=5, damaged by bright light, dark vision, cowardly, emboldened by player blind, tier 2.

This enemy constantly emits an invisible gas that causes the spaces it occupies to be Dark. This gas also blinds the player when it occupies their space.

    "For a fresh vampire, embracing what they have become begins with embracing darkness. Such creatures carry it with them wherever they go, and will use it to hide and to hunt."

*Vampire Noble*

Armed, armored, dominates outlaws, monologues, shouts, perception=1, dark vision, damaged by bright light, tier 3.

    "Nobles are often the target of a vampire curse. Combat training, expensive weapons and armor, and artful command of men are all useful to a vampire."


**Wolves**:
Found in: forest, cave.

*Wolves*

Grapple attack, fast movement, shouts, cowardly, tier 1.

If a wolf that is not dominated enters line of sight with a monster that dominates wolves, it immediately joins that monster’s pack and loses cowardly. Wolves regain the cowardly trait when that monster dies or is nullified.

    “These grey, dog-like predators work together to immobilize and surround prey larger than themselves, but they fear men. If they are attacking, it means they are being controlled with dark magic.”

*Warg*

Grapple attack, dominates wolves, fast movement, keeps distance, emboldened by: playerhealth<35%, OR no allies, tier 2.

Wargs spawn in packs of wolves and nothing else.

    “Though it looks like a large, black, ugly wolf, this creature is actually an evil spirit taken physical form. As cunning as any man, and able to bend common wolves to their will, these monsters exist only to cause violence and spread fear. Though they relish the killing blow, they have little stomach for a fair fight, and prefer to let their slaves weaken their prey before they approach.”

*Barghest*

Dominates wolves, fast movement, flees when hp<50%, tier 3.

This creature is hostile to wargs. Wargs in its line of sight are slowed. This creature dominates wolves in its line of sight even if they are already dominated. Only one barghest will spawn in a level.

    “If wargs are a cruel joke of the gods, then the Barghest is the punchline. These horrid creatures have bodies only passingly dog-like, hairless and with long spines sprouting from their back, and a head more like an orc’s than anything else. They allow wargs to gather large groups of wolves together in one area, then move in with nightfall, stealing their packs and slaying them one by one. If you do not kill this creature, all the wolves in the area will soon be under its control.”


**Elves**

Found in: Forest, cave, swamp, ruins.

While elves are never neutral to the player, by default they will not attack. They will simply follow the player, keeping sight of them. Because of their cowardly behavior, if spotted they will flee. An individual elf or pack or elves will lose cowardly and begin attacking the player if they witness one of the following things occuring:
-The player attacking an elf or an animal
-The player opening a treasure chest or taking an item off a pedestal
-The player is attacked by an elf

*Elven Hunter*

Ranged attack, reload=1, ammo=10, keeps distance, stealth=3, perception=3, cowardly, emboldened by elf rules, armed, tier 1.

This enemy's ranged attack is 20% less likely to apply the targets's armor to its damage roll than a normal attack.

    "Covered head-to-toe in natural camoflage, this figure is small and lithe like an adolescent, but it strings a bow with the sureness of a killer. Elves hate men bitterly, and will not suffer trespassers to steal their game or their treasures. Say the tales: For each elf you spot, there's a dozen you don't..."

*Elven Gladeguard*

Fast attack, cowardly, stealth=2, perception=4, emboldened by elf rules, armed, tier 2.

This enemy's attack is 25% less likely to apply the target's armor to its damage roll.

    "The elves hold the land sacred, and from certain special places they must not give any ground, even momentarily. Gladeguards make that possible. Agile enough to avoid any blow, and they wield a razor-sharp stone dagger in each hand. They show their contempt for armor by walking into battle all but naked."

*Elven Beastmaster*

Keeps distance, cowardly, stealth=3, perception=3, emboldened by elf rules, tier 2.

This enemy always spawns with at least 1 agressive animal as part of its pack, and has a healing spell that can only heal animals.

    "Elves can tame any beast, and purportedly have found use for nearly all of them. The use this elf has for its charges almost certainly invovles disembowling adventurers. It carries only a strange, ornate pipe, which seems to make no sound and yet holds complete sway over the creatures nearby."

*Elven Earthtalker*

Keeps distance, cowardly, stealth=3, perception=5, Tracker(40) emboldened by elf rules, tier 2.

This enemy has a very large hearing zone, and does not lose track of the player if they are still in the hearing zone. Once emboldened, this enemy will cast an "Earthcall" spell that alerts elves (and predators) to the player's location and embolden them in a big radius.

    "The legends are clear, elf troupes often punish acts that could not possibly have been observed by eyes alone. This elf carries a treebranch staff and wears a trancelike expression. They watch you through the eyes of wilderness itself, and can call out through it to call their wrath on you. Fortunately, the bent body of this hedge witch offers no intrinsic danger."

*Elven Manfeller*

Ranged attack, reload=1, ammo=10, keeps distance, stealth=4, perception=4, cowardly, emboldened by elf rules, armed, tier 3

This enemy's attack is 40% less likely to apply the target's armor to its damage roll.

    "All elven fighters train exclusively with a single weapon. Most favor the bow, but as hunters of beasts, not men. This small, camoflagued figure is one of the exceptions, and can put an arrow in an armpit or eyeslit at impressive range and with shocking precision."

*Silverpelt*

Cowardly, fast movement, drops gold, tier 0.

    "A large, four-legged beast with a thick, luxious coat of fur. The color is actually green, red, or white, depending on the season and the breed. The 'silver' refers to the coin a hunter can make by hawking even the messiest of kills."

*Bladefang*

Stealth=3, perception=1, tier 2.

When this enemy moves adjacent to a target, it immediately makes an instant attack against one such target.

    "A giant cat with long, sturdy, foreward-facing tusks. Thick knots of muscle form its fore-body, which can propel its tusks through steel plate with ease, and gore a man apart with one vicious wrench."

*Snaretongue*

Stealth=1, Slow Movement, tier 2.

This enemy uses a ranged attack that pulls the target toward it on hit. If the target would be pulled into the Snaretongue's space, it is "swallowed whole". The two share a space, the swallowed target cannot move, has certain penalities on checks, and takes automatic acid and physical damage each round. This effect typically ends when the swallowed target dies or kills the Snaretongue with melee attacks.

    "A massive but squat lizard lurks there in the underbrush. A thick, pink tongue lashes out of its gaping maw... dragging its living prey into its waiting jaws."

**Beyond Things**

Found in: Hellscape, Tower, Dungeon
Beyond Things mostly spawn individually and are neutral to each other, but each have their own behaviors.

*Organizer*

Invisible, Stealth=3, fast attack, Tier 2.

This enemy is hostile to everything but Beyond Things. When it kills something with a melee attack, it begins "organizing", during which it will not act for 20 rounds (it stops early only if it takes damage).
    
    "Likened to skulking predators by frightened survivors, these things can only be known by the sounds of frenzied scratching they make as they move. They seem to posses a morbid interest with the creatures of our world, and, after tearing them to shreds with invisible blades, will arrange their organs in neat little rows."

*Mirror-Thing*

Special attack, Tracker (25), Tier 2

This enemy is hostile only to the player. It is nuetral to everything else, and that cannot be changed except by effects that over-write normal loyalty rules (like certain spells). Each round that a Mirror-Thing is seen by the player, the player gains stacks of a "mirror" debuff. The closer the Mirror-Thing is, the more stacks the player will gain at once. This debuff does nothing, except that if the player ever has 100 stacks they immediately die.
Instead of dealing damage, this enemy's attack causes the player's facing to center on the enemy.

    "These entities resemble lumpy black clay in the rough shape of a human. They are thought to steal the souls of men, explaining the irecoverable catatonia of their victims. As you see a distorted reflection of yourself in the figure's inky surface, you know only that you feel a deep, wordless terror, and that you cannot, struggle as you might, shut your eyes."

*Ghost Beast*

Slow Attack, unparryable, physical immunity, wide sight arc, invisible in bright light, stealth=1, Tier 2

This enemy is nuetral to other Beyond Things, and to everything else, initially. It has a 15% chance to become hostile with any non-Beyond Thing it is aware of each round. If it stops being aware of anything it's hostile to, it will become nuetral to them again (even if it became hostile through other means, like being attacked).

    "A dim green glow the size of a bear is all that belies the presence of these things. While they appear spectral, the threat they pose is physical, brutish even. Their forms are solid, yes, harder than any stone or steel, and when some unknowable thing brings their ire upon a nearby creature they pulverize it with amorphous limbs. The tales say to kill it with fire, but warn it does not burn quickly."

*The Glow*

Invisible, Stealth=3, keeps distance, does not attack, Regeneration, Tier 2

This enemy emits a large quanitity of gas that produces dim light and drains the HP of anything that occupies it.

    "The source of the eerie light that pervades this area cannot be seen. But from deep within the glow is the faintest rythmic sound, like the beating of a heart made of tinny brass. The tales speak of ghosts dwelling within the deadly light, that a stout man might seize upon and slay, to banish the glow for good. Could it be something mortal lies, invisible, within this terror?"

*You-Meen*

Armed, Armored, panicky, reckless, Tier 1

    "A dumb, ugly animal in the rough shape of a man. Its armor and weapon are of strangly fine craftsmanship, but they are lashed to its body as it seemingly lacks the cunning to keep them itself. It's eyes glow with uncontained rage and it jabbers gibberish constantly."
    
*Bogeyman*

Fast move, stealth=4, cowardly, 

If this enemy begins its turn within the player's vision zone (but not seen) it is stunned. If the player is aware of this enemy, and it starts its turn within the player's vision zone, it takes half of its max HP in damage at the start of its turn.

    "What you had only a moment before mistaken for a rock or a tree, is actually a wildly alien creature, whose features are indescribable, fleeing from your memory even as you stand in awe of them. Human sight is anathema to these skulking predators, but comprehension, it seems, is deadly."

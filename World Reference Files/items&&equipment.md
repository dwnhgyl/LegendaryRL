# Items && Equipment

## *Items*

Items represent a collection of small, useful, and expendable tools.

**Potions**: Potions are identifiable items. Before a type of potion is identified, it appears as an “unknown potion.” When a potion’s unique effects are observed, the potion is immediately identified. There are three ways to interact with potions, but not all potions have unique results for every interaction. For instance, if a potion of might or speed is thrown, it will be destroyed without being identified. Typically, if a potion with no coat or drink effect is drunk or used to coat a weapon, it will act as if thrown onto the player’s space (and be identified as normal). Likewise, if a potion with no thrown effect is thrown at an enemy, it will resolve its drink effect on the enemy struck.

    Some enemies can use potions. Enemies use each type of potion a specific way. t indicates a potion enemies will throw at the player. d indicates a potion enemies will drink. c indicates a potion enemies will use to coat their weapon (this applies an enemy-only buff, since enemies don’t actually use equipment).
    
**Potion of Brilliance<sup>d</sup>**: When drunk, the drinker gains a large bonus to spellpower, their channeling time is reduced by 1, and they gain telepathy in a large oblong shape in front of them.

**Potion of Lightning<sup>t</sup>**: When drunk, the drinker gains lightning resistance. When thrown, causes lightening damage in a small aoe around where it lands. When used to coat a weapon, deals lightning damage to the wielder.

**Potion of Paralysis<sup>t</sup>**: If thrown, releases a cloud of paralytic gas. If drunk, ???

**Potion of Fire<sup>t</sup>**: If thrown, creates a fiery explosion. If drunk, applies fire immunity buff. If used to coat weapon, applies extra fire damage on hit. For as long as weapon coating is in effect the weapon acts as a light source.

**Fragmentation Potion<sup>t</sup>**: When thrown, this potion creates an effect similar in many respects to the shardspray spell. One significant difference: any projectiles aimed in the general direction it was thrown in originate on the space it detonates, rather than the adjacent spaces. This means that an enemy struck with this potion will be struck with on average half of the shards produced.

**Potion of Might<sup>d</sup>**: If drunk, player gains the mighty buff, applying a large buff to weapon damage, weapon accuracy, and armor, as well as health regeneration and fast attack. If used to coat a weapon, that weapon gains a large buff to base damage, accuracy, and is immune to damage for the duration.

**Potion of Darkness<sup>t</sup>**: If drunk, applies the shadows buff, gaining a bonus to stealth when in darkness. If thrown, creates an area of magical darkness in radius 10.

**Potion of Acid<sup>t</sup>**: If thrown, deals acid damage to whatever it hits, and creates an acid puddle beneath it, similar to acid glob. If drunk, applies acid immunity buff, AFTER dealing a small amount of irreducible damage. If used to coat a weapon, damages the weapon.

**Potion of Frost**<sup>t</sup>: If thrown, releases a cloud of frost gas. If drunk, applies cold immunity buff.

**Potion of Poison**<sup>t</sup>: If thrown, releases a cloud of poison gas. If drunk, poisons the drinker. If used to coat a weapon, applies significant poison on hit.

**Potion of Speed<sup>d</sup>**: If drunk, hastes the drinker. If used to coat a weapon, applies fast attack buff. If the weapon is ranged, it will also apply a special buff that increases projectile speed and damage.

**Potion of Healing<sup>d</sup>**: If thrown, fully heals the creature it hits. If drunk, fully heals the drinker.

**Potion of Confusion<sup>t</sup>**: If thrown, releases a cloud of confusion gas. If drunk, applies the hallucination effect to the player.

**Scrolls**: Scrolls are identifiable items. Before a type of scroll is identified, it appears as “unknown scroll.” Reading a scroll uses it. Reading an unidentified scroll identifies it before the effects take place.
    
    Scrolls scale with your base spellpower, determined by your wisdom. Most scrolls can be found and used by certain enemies. Those that can never be used by enemies are marked with *. Scrolls without a description function exactly as the player spell of the same name.

**Scroll of Identify**: These scrolls immediately self-identify when picked up. They have a low price in shops, and spawn in shops quite often. They prompt the player to specify an unidentified item, and identify the item selected. At higher levels of spellpower, they will prompt the player to repeat the process, resulting in 2 or more items being identified.

**Scroll of Remove Curse**: This scroll has no effect unless you are cursed (and NPCs will not use it). If you are cursed, it will grant you a buff that turns off the effects of all curses affecting you, which will last until you finish the current level. At higher levels of spellpower, it will remove 1 random curse entirely, in addition to giving you the buff. At very high spellpower, it will give you the option of removing 1 random curse or gain that curse's adaption perk.

**Scroll of Divination**

**Scroll of Lightning Bolt**

**Scroll of Fireball**

**Scroll of Acid Splash**

**Scroll of Call Lightning**

**Scroll of Call Fog**

**Scroll of Conjure Ammunition**

**Scroll of Haste**

**Scroll of Bless Equipment**

**Scroll of Stone Body**

**Scroll of Shadows**

## *Equipment*

Equipment represents larger, heavier objects which must be held at the ready or laboriously carried. Most equipment is some kind of weapon or armor. Equipment has a “Enc” value, which is a cumulative penalty to many values at different linear rates. Equipment carried contributes its Enc value regardless of whether it is equipped.

Enc affects:

Accuracy and Parry at a low rate.
Hide, Sneak and Dodge at a high rate.
Damage from drowning and other exhaustion damage.
Sprint speed at a high rate.

*Melee Weapons*

Weapons are an important part of every adventurer’s equipment. Melee weapons are used by moving towards an adjacent enemy or with a designated strike key. 

Weapons take up hand slots when equipped. Ranged weapons typically take up both the mainhand and offhand slots. Most melee weapons take up only the mainhand slot, but receive a 50% bonus to their maximum damage when the offhand is empty. Weapons with the “2hander” tag must be wielded this way, and always receive this bonus.

Weapons with the “throwable” tag can be thrown at no malus. This emits a projectile with a speed of 5 spaces per turn, having the same attack stats as normally using that weapon. Weapons with “throwmalus” can be thrown, but apply the listed number as a penalty to the roll to determine whether the projectile hits ANY creature it comes into contact with. The weapon falls to the floor wherever the projectile stops.

Placeholder damage and accuracy values are relative to other weapons of their type.

**Dagger**

Poor damage, good accuracy, fair parry, Enc=*, backup, quintuple crit damage, no twohand, throwable.

*The first dagger carried applies no encumbrance, but each other one counts as encumbrance 1.

    “Used across the continent as everything from a craftsman’s tool to an instrument of ritual killing, the daggers greatest virtues are efficiency and control. While ill-suited for a stand-up fight, adventurers often keep a dagger in their boot in case they lose their weapon or need something to throw. Those who rely on the element of surprise may make use of daggers in combat, if only because they have eschewed larger weapons entirely.”

**Spear**

Fair damage, fair accuracy, poor parry, Enc=2, reach, throwable.

    “Spears are relatively easy to manufacture, and afford their user a key advantage of superior reach. For these reasons, they see use everywhere from kobold dens to the armies of men. Adventurers, often finding themselves in long, brutal, chaotic melees, put less stock in the value of improved reach, but still recognize the weapon as versatile, lightweight, and effective.”

**Greatspear**

Good damage, fair accuracy, fair parry, 2hander, Enc=4, reach, knockback, throwmalus=2.

    “Heavier, harder to throw, and requiring two hands to use, these large spears are mostly used for hunting large game, due to its ability to deliver grievous wounds to the animals while keeping them at bay. Some heroes of old turned these advantages towards the purpose of monster-slaying.”

**Axe**

Good damage, poor accuracy, poor parry, Enc=2, cleave=1, throwmalus=3.

    “Once a staple on the battlefield, battleaxes have fallen out of favor in recent times, and most axes used as weapons today were built as tools. Among your people, however, these weapons still come well recommended, as they are excellent for confronting an armored opponent or a horde of kobolds.”

**Greataxe**

Very good damage, poor accuracy, fair parry, 2-hander, Enc=5, cleave=2.

    “Likely built for decorative purposes, this greataxe is a throwback to the tribal warlords that once roamed the northern steppes. Heavy and unwieldly, this immense two-handed axe would be viewed as impractical by most human denizens of the modern Strandian continent. That said, most of those people don’t wake up in the morning fully intending to slay entire tribes of monsters single-handed.”

**Shortsword**

Fair damage, good accuracy, fair parry, Enc=1, backup, throwmalus=2.

    “Once people might have just called this a sword, but new smithing methods have resulted in longer blades. Blades of this length typically begin life as back-up weapons issued to Strandian conscripts, but many are sold off by the less scrupulous men of that descriptor, some going so far as to sell each one they are issued. Demand is high, as many warriors want a back-up weapon with a bit more bite than a bootknife, and many footpads see the weapons as a good compromise between the dagger and larger blades.

**Longsword**

Good Damage, good accuracy, good parry, Enc=3.

    “Blades of this length were once used exclusively by heroes and nobility, giving them a prominent position in legend and myth. Today’s smiths can make them more easily, and so many poseurs and outlaws have taken up the longsword that their storied reputation has been sullied somewhat. Speaking practically, it is still a versatile and efficient weapon, reliable in any situation an adventurer might find themselves in.”

**Greatsword**

Very good damage, good accuracy, good parry, 2-hander, Enc=5.

    “The integrity of this long blade is preserved by its width. The result is increased weight, and a weapon as suited to bashing as to thrusting. These blades first saw use in warfare, used by units meant to charge and break archer formations. Most of these blades that exist today were built for duelists. Though deadly, these weapons only ever found popular use among adventuring heroes, whose supernatural abilities free them of the need for a shield.”

**Mace**

Very good damage, fair accuracy, fair parry, slow attack, unparry-able, Enc=3.

    “Eschewing a cutting edge for pure weight, blunt weapons require extreme effort to bring to bear against an enemy. This flaw has seen it abandoned by most serious fighters, and this weapon probably began its life as a town guardsman’s cudgel. However, a mighty warrior could slay an armored opponent right through their shield with a weapon like this. The tales say it plain.”

**Greatmace**

Exceptional damage, fair accuracy, fair parry, slow attack, unparry-able, 2-hander, Enc=6.

    “A towering mass of steel and lead, this weapon would look impractical to most denizens of the Strandian continent. It was almost certainly forged in your homeland, for the use of adventurers like yourself. More than one hero of legend has borne the weight of such a weapon through rivers and across mountains, in order to slay monstrous opponents no other weapon could harm.”
    
**Hookblade**
Fair damage, poor accuracy, fair parry, push-on-hit, Enc=2
When this weapon hits, the player can push the enemy (or corpse) one space in any direction.
    
    "A slender metal shaft ends in a hook with a pyramidal point. Hookblades are scoffed at by many master duelists for being difficult for a warrior to use to full effect, there is a school of thought that prizes them as an invaluable positioning tool."

**Buckler**

Poor damage, fair accuracy, poor parry, Enc=1

When holding a buckler, you can use items instantly and throw unequipped weapons, just like if you had an empty off-hand. When you perform “Reckless” strikes, or other attacks that cause you to drop your guard, your maximum damage is increased as if your off-hand were empty.

    “So called for the way they are often strapped to the forearm or back of the hand. While it provides limited protection, the buckler leaves your hand free, allowing you to throw knife or grip a weapon with both hands, as long as you’re not busy blocking!”

**Shield**

Good damage, terrible accuracy, great parry, ranged parry, Enc=4

(when wielded, grants a special "Ranged Parry" bonus, that allows you make a special parry roll against any missile attacks that you wouldn't otherwise be able to parry. You still need to be facing the missile. Only "ranged parry" weapons add their bonus to such parry attempts)

    “Thick, sturdy wood plated in steel. This is an invaluable tool of the warrior, and has served countless fighters as a sound defense, a canvas for heraldry, and a blunt object.”

**Greatshield**

Fair damage, terrible accuracy, phenomenal parry, ranged parry, Enc=6

(when wielded, grants a special "Ranged Parry" bonus, that allows you make a special parry roll against any missile attacks that you wouldn't otherwise be able to parry. You still need to be facing the missile. Only "ranged parry" weapons add their bonus to such parry attempts)
    
    “Standard-issue for Strandian infantry, not just as personal equipment, but for reinforcing siege equipment, walls, and officer tents as well! This shield is so large it can guard your thighs and your face at the same time. Not easy to carry or fight with, but gives you a welcome advantage in a melee.”
    
**Ward**

Weak damage, poor accuracy, fair parry, ranged parry, Enc=1
While channeling a spell while a ward is held, the player does not lower their guard, gains a parry bonus from wisdom, but loses any parry bonus from valor.

    "This small icon of the god of men fits snugly in a clenched fist. Practitioners of magic can protect themselves from harm by brandishing such a symbol as they channel the power of the world around them."

**Staff**

Fair damage, fair accuracy, fair parry, 2-hander Enc=3
Holding this weapon lowers the channeling time on all spells by 1, to a minimum of 1.
    
    "The staff is a symbol of the man-god's power, representing how the world around it may be bent to its will with craft and cunning. Mortal mages imitate this in their own works, and indeed, it is well known that brandishing a staff makes it much easier to cast any spell."

**Alchemical Torch**

Light damage, good accuracy, poor parry, throwmalus=2 Enc=2
All damage dealth with this weapon is fire damage. Whenever this weapon is equipped or on the ground, it emits a 1 space radius of high priority bright light and a 6 space radius of high priority dim light. An equipped torch gives the player a serious malus to Hide.

    "An adventurer's quest often takes them into places where no light shines, and stumbling blindly in the dark means certain death. But fumbling with traditional light sources, like oily rags, only to have them go out when least expected, can be deadly as well. The miraculous chemical infused in the head of this torch will burn as long it's exposed to air, providing you light, warmth, and a source of fire."

## *Ranged Weapons*

Ranged weapons are used with a designated shoot key, which prompts the player to pick a target. All ranged weapons need to reload after shooting. Reloading happens automatically when the player waits with a reloadable ranged weapon in hand. The player must wait for a number of consecutive turns equal to the weapon’s reload number in order to reload. Every ranged weapon has built-in quiver, which allows it to be used a certain number of times.

**Sling**

Poor damage, fair accuracy, quiver=8, reload=1, projectile speed=7, Enc=1.

A sling can be used one-handed, perhaps with a one-handed melee weapon. In this case, it takes 2 turns to reload instead of one.

This weapon can be fired without ammo, though this increases reload time by one, and the shot will have less accuracy and damage. While the player has a sling equipped, there is no limit on the distance they can throw potions, and thrown potions travel at 7 spaces a round instead of 4.

    “Hardly the deadliest of weapons, the sling is not highly regarded nor widely used. It is most commonly used among your own people, as the weapon and its bullets are lightweight and compact and, in a pinch, it can be loaded with rocks from the ground.

**Bow**

Fair damage, fair accuracy, quiver=10, reload=1, projectile speed=10, Enc=2.

    “A weapon that has changed little over hundreds of years, these come in many shapes and sizes, though only smaller bows are used by adventurers. Meant for hunting and target shooting, these bows offer accuracy and ease of use for the short-distance confrontations.

**Light Crossbow**

Good damage, good accuracy, quiver=8, reload=3, projectile speed=10, Enc=2
Light Crossbows can be used one-handed, but suffer an accuracy penalty in this case. They take 5 rounds to reload without an empty off-hand.

    “The design of this crossbow emphasizes portability, economy, and usability. It is a little too heavy to be easily used in one hand. This hasn’t stopped thugs, pirates, and adventurers from brandishing two at a time for deadly close-range ambushes.”

**Heavy Crossbow**

Very good damage, good accuracy, quiver=8, reload=4, projectile speed=10, Enc=4.

    “These weapons are often found in the possession of mercenaries; they are effective tools of war, but too expensive to fill out the ranks of the Strandian archer regiments. Too new a weapon to have much of a place in the legends, these bulky hunks of wood and steel are sure to gain one thanks to their ease of use and sheer killing power. Despite how cumbersome they are, they are still effective ambush weapons.”

**Throwing Knife**

Fair damage, poor accuracy, thrown only, projectile speed=5, Enc=NA
Throwing knives are not equipment, but can be thrown when a “Brace of Knives” is equipped. Their listing is here for consistency.

## **Extra Quivers**
Ranged weapons have ammunition stores "attached" to them, from which they are reloaded. But you can find and buy extra quivers, which will potentially let you get more use out of a ranged weapon. Enchanted quivers apply an attack buff to the accuracy and damage of weapons loaded with one of their ammo, and also have larger quiver values. The Brace of Knives works a little differently... a character with the item equipped can access throwing knives from the throw menu. Each time a knife is thrown, the brace of knives loses 1 ammo. An enchanted Brace of Knives yields knives with an enhancement bonus to their weapon profile.

**Brace of Knives**
quiver=6, Enc=1

    "Sharp little knives all in a row, perfectly weighted to be flung like darts into something unfriendly."

**Case of Bolts**
quiver=8, Enc=1
This quiver can reload Light Crossbows and Heavy Crossbows.
    
    "A metal case containing short darts meant to be shot from a crossbow."

**Quiver of Arrows**
quiver=10, Enc=1
This quiver can reload Bows.

    "A leather holster with a long strap. The feathers of arrows stick out of the top, waiting to be taken."

**Bag of Bullets**
quiver=8, Enc=1
This quiver can reload slings.

    "A bag of round leaden sling shot. Better than rocks, and closer at hand."

## *Body Armor*

Unless otherwise specified, enhancement bonus on body armor will improve the bonuses they provide at base.

**Cloak**

Small dodge bonus, middling hide bonus. Enc=1.

    “Travelers use cloaks like these to stay warm on the road. Thieves and adventurers wear them to obscure their silhouette, making them harder to spot and attack. They also use them to impersonate travelers, and perhaps also to stay warm on the road.”

**Silk Shirt**

Tiny armor bonus, Enc=0.

As enhancement bonus increases, a silk shirt provides a bonus to Armor and Spellpower.

    “A fine shirt of the strongest silk. No more restrictive than bare flesh, marginally more resilient, and much more fashionable.

**Leather Cuirass**

Small armor bonus, Enc=2.

    “The uniform of the Strandian army, tanners across the continent make their living providing Strand with fresh cuirasses. A tight, flexible vest covers the chest while a skirt of wide and rigid leather strips reliably protects the thighs.”

**Chain Shirt**

Medium armor bonus, Enc=4.

    “An expensive kind of armor used by many of the opposing forces in the wars of Strandian expansion. A shirt made of fine interlocking steel segments, the Strandians rendered it obsolete with use of special arrowheads that pierced it easily. Given how unlikely a traveling warrior is to face a Strandian archer battalion, the surplus found eager recipients among outlaws and mercenaries.”

**Breastplate**

Good armor bonus, Enc=6.

    “Plate armor is assembled from many pieces onto the bodies of soldiers representing organizations with immense resources. However, with a few scraps of chainmail, some belts here and there, and some good adventuring know-how, a breastplate can be maintained and used by a lone warrior.”

## **Headgear**

**Hat**

Enc=0

A +0 hat provides no effect. As enhancement bonus increases, magic hats give a bonus to spellpower.

    “More fit for a night on the town than a trek through a swamp, this practical yet foppish hat fits snuggly enough on your head that the latter is possible. Why not? After all, no proper wizard would be without their hat!”

**Light Helm**

Enc=1

A +0 light helm provides a 10% bonus to armor apply chance. As enhancement bonus increases, a light helm grants bonuses to Armor and Spot.
    
    "Skullcap. Noseguard. Strap. A simple, reliable design that has protected the skulls of conscripts and kings for centuries."  

**Greathelm**

Enc=2

A +0 greathelm provides a 15% bonus to armor apply chance, but grants a malus to Spot and Listen. As enhancement bonus increases, a greathelm grants a bonus to Armor.
        
     "Looking at the world through the slits of a faceguard is hardly ideal. On the other hand, it is ideal for looking at sharpened blades swung with murderous intent. The tales are clear: all the armor in the world won't save you if you go into battle with your head exposed."
        
**Hood**

Enc=0

A +0 hood provides a small bonus to Hide. As enhancement bonus increases, a hood provides a bonus to Hide and Spot.

**Headband**

Enc=0

A +0 headband provides a small bonus to accuracy and spot, which increases as enhancement bonus increases.

    "This scrap of silk should be sturdy enough to make a good headband. Keep it clean, keep it tight, and keep it on your head, the tales say. It will keep your hair out of your eyes. Your hair and your blood."
    
**Mask**

Enc=0

A +0 mask provides no effect. As enhancement bonus increases, masks gain egos at a rapid rate.

    "Ask not who is behind the mask, say the tales. Ask not after the man inside. Ask instead after the nature of the mask, for that is what the man inside has become."


## **Hand Equipment**

**Gloves**
Enc=0

A +0 set of gloves gives a bonus to accuracy. As enhancement bonus increases, gloves grant a bonus to accuracy, parry, and weapon damage.

    "To keep hold of a weapon in the hellish tempest of hand-to-hand combat taxes the skin and flesh of any warrior. A good pair of gloves like these can help keep your grip fresh."

**Bracers**
Enc=1

A +0 pair of braces gives a tiny parry bonus and a 5% bonus to armor apply chance. As enhancement bonus increases, bracers grant a parry bonus.

    "The forearm needn't bend. Actually, the forearm really ought not to bend, nor be crushed, nor cut in twain. For these reasons, metal plate makes for welcome protection. Though the weight will slow your arms, a pair of bracers can turn aside otherwise deadly blows."
    
**Gauntlets**
Enc=2

A +0 pair of guantlets gives a small parry bonus and a 10% bonus to armor apply chance, but give a penalty to accuracy. As enhancement bonus increases, gauntlets grant a bonus to armor.

    "Gloves lined with steel are heavy and awkward, but the ability to catch a swung blade unharmed is invaluable while fighting."

## **Shoes**

**Armored Boots**
Enc=2

A +0 pair of Armored Boots grants a 10% bonus to armor apply chance, but gives a penalty to sprint speed. As enhancement bonus increases, armored boots grant a bonus to armor.

    "Steel plates between leather hide makes these boots heavy. Footwork is hard, and running is harder, but when the blade strikes your calf only to bounce off with a resounding "twang", it will all be worth it."
    

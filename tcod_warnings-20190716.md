# WARNINGS

**#1**: SOLVED


    engine.py:302: DeprecationWarning: A renderer should be given, see the online documentation.
    constants['window_title'], False)


**#2**: SOLVED


    engine.py:304: DeprecationWarning: Create a console using `tcod.console.Console(...)` instead.
    con = libtcod.console_new(constants['screen_width'], constants['screen_height'])


**#3**: SOLVED


    engine.py:305: DeprecationWarning: Create a console using `tcod.console.Console(...)` instead.
    panel = libtcod.console_new(constants['screen_width'], constants['panel_height'])


**#4**: UNSOLVED


    engine.py:321: DeprecationWarning: Use the tcod.event module to check for "QUIT" type events.
    while not libtcod.console_is_window_closed():


**#5**: UNSOLVED


    engine.py:322: DeprecationWarning: Use tcod.event.get to check for events.
    libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)

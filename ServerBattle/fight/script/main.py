from fight.corearena.arena import Arena
from fight.corearena.arenaconf import TRANSARENA, ArenaState
from fight.data.const import FOETEAM, OWNTEAM
from transitions import Machine

arena = Arena()
arenafsm = Machine(model=arena,
                   states=ArenaState,
                   initial=ArenaState.NONE,
                   transitions=TRANSARENA)
arena.createteam(own=OWNTEAM, foe=FOETEAM)

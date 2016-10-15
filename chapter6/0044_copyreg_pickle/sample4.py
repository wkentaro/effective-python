# -----------------------------------------------------------------------------
class GameState(object):

    def __init__(self, level=0, lives=4, points=0, magic=5):
        self.level = level
        self.lives = lives
        self.points = points
        self.magic = magic
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    return unpickle_game_state, (kwargs,)
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
def unpickle_game_state(kwargs):
    return GameState(**kwargs)
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
import copyreg
copyreg.pickle(GameState, pickle_game_state)
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
import pickle
state = GameState()
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
class GameState(object):
    def __init__(self, level=0, points=0, magic=5):
        self.level = level
        self.points = points
        self.magic = magic
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
try:
    pickle.loads(serialized)  # raises error
except TypeError as e:
    print(e)
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    kwargs['version'] = 2
    return unpickle_game_state, (kwargs,)
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
def unpickle_game_state(kwargs):
    version = kwargs.pop('versoin', 1)
    if version == 1:
        kwargs.pop('lives')
    return GameState(**kwargs)
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
copyreg.pickle(GameState, pickle_game_state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
class GameState(object):
    def __init__(self, level=0, lives=4, points=0):
        self.level = level
        self.lives = lives
        self.points = points
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
state.points += 1000
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
class GameState(object):

    def __init__(self, level=0, lives=4, points=0, magic=5):
        self.level = level
        self.lives = lives
        self.points = points
        self.magic = magic
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
state_after = pickle.loads(serialized)
print(state_after.__dict__)
# -----------------------------------------------------------------------------

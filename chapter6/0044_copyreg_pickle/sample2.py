# -----------------------------------------------------------------------------
class GameState(object):
    def __init__(self):
        self.level = 0
        self.lives = 4
        self.points = 0
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
import pickle
state = GameState()
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
state_path = 'game_state.bin'
with open(state_path, 'rb') as f:
    state_after = pickle.load(f)
assert isinstance(state_after, GameState)
print(state_after.__dict__)
# -----------------------------------------------------------------------------

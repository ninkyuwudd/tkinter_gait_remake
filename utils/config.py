


_video_running = True

_video_gf_running = True



def get_video_state():
    return _video_running

def set_video_state(state):
    global _video_running
    _video_running = state



def get_video_gf_state():
    return _video_gf_running

def set_video_gf_state(state):
    global _video_gf_running
    _video_gf_running = state
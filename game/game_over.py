from gui.result_screen import show_result_screen
import time

def check_game_over(state, root):

    if len(state.matched_buttons) == 16:
        state.end_time = time.time()
        root.destroy()
        show_result_screen(state)
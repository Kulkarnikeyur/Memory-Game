import time
import pygame

class MemoryGameCard:

    def __init__(self, button, image, state, on_match_complete=None):

        self.button = button
        self.image = image
        self.state = state
        self.on_match_complete = on_match_complete

    def click(self):

        start_ui = time.perf_counter()

        if self.button not in self.state.open_buttons:

            self.state.open_images.append(self.image)
            self.state.open_buttons.append(self.button)

            self.button.configure(image=self.image)

            self.button.update_idletasks()

            end_ui = time.perf_counter()

            print(f"Card reveal response time: {(end_ui - start_ui)*1000:.2f} ms")

            if len(self.state.open_images) == 2:

                self.button.update_idletasks()
                time.sleep(0.4)

                if self.state.open_images[0] != self.state.open_images[1]:

                    for btn in self.state.open_buttons:
                        btn.configure(image=self.state.back_image)

                else:

                    pygame.mixer.init()
                    pygame.mixer.music.load("sounds/correct response.mp3")
                    pygame.mixer.music.play(loops=0)

                    for btn in self.state.open_buttons:
                        btn.configure(command=lambda: None)
                        self.state.matched_buttons.append(btn)

                self.state.open_images.clear()
                self.state.open_buttons.clear()

                self.state.moves += 1

                if self.on_match_complete:
                    self.on_match_complete(self.state)
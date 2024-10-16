import pygame
import sys
from memory_manager.memory import MemoryManager
from visualization.renderer import Renderer
import config

class MemoryVisualizer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("Memory Management Visualizer")
        
        self.memory_manager = MemoryManager(config.MEMORY_SIZE)
        self.renderer = Renderer(self.screen, self.memory_manager)
        
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    size = int(input("Enter allocation size (MB): "))
                    start = self.memory_manager.allocate(size)
                    if start is not None:
                        print(f"Allocated {size}MB at position {start}")
                    else:
                        print("Allocation failed: Not enough memory")
                elif event.key == pygame.K_d:
                    start = int(input("Enter start position to deallocate: "))
                    if self.memory_manager.deallocate(start):
                        print(f"Deallocated memory at position {start}")
                    else:
                        print("Deallocation failed: Invalid start position")
                elif event.key == pygame.K_c:
                    algorithm = input("Enter allocation algorithm (First Fit, Best Fit, Worst Fit): ")
                    self.memory_manager.set_algorithm(algorithm)
        return True

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.renderer.render()
            self.clock.tick(config.FPS)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    visualizer = MemoryVisualizer()
    visualizer.run()
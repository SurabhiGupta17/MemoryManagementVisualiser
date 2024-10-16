import pygame
import config

class Renderer:
    def __init__(self, screen, memory_manager):
        self.screen = screen
        self.memory_manager = memory_manager
        self.font = pygame.font.Font(None, 24)

    def render(self):
        self.screen.fill(config.COLOR_BACKGROUND)
        self._draw_memory_blocks()
        self._draw_info()
        pygame.display.flip()

    def _draw_memory_blocks(self):
        blocks = self.memory_manager.get_blocks()
        total_memory = self.memory_manager.total_size
        for block in blocks:
            x = config.MEMORY_RECT_X + (block.start / total_memory) * config.MEMORY_RECT_WIDTH
            width = (block.size / total_memory) * config.MEMORY_RECT_WIDTH
            color = config.COLOR_FREE_MEMORY if block.is_free else config.COLOR_ALLOCATED_MEMORY
            pygame.draw.rect(self.screen, color, (x, config.MEMORY_RECT_Y, width, config.MEMORY_RECT_HEIGHT))
            
            # Draw block size
            size_text = f"{block.size}MB"
            text_surface = self.font.render(size_text, True, config.COLOR_TEXT)
            text_rect = text_surface.get_rect(center=(x + width/2, config.MEMORY_RECT_Y + config.MEMORY_RECT_HEIGHT/2))
            self.screen.blit(text_surface, text_rect)

    def _draw_info(self):
        algorithm_text = f"Current Algorithm: {self.memory_manager.algorithm}"
        algorithm_surface = self.font.render(algorithm_text, True, config.COLOR_TEXT)
        self.screen.blit(algorithm_surface, (10, 10))

        instructions = [
            "Press 'A' to allocate memory",
            "Press 'D' to deallocate memory",
            "Press 'C' to change allocation algorithm"
        ]
        for i, instruction in enumerate(instructions):
            text_surface = self.font.render(instruction, True, config.COLOR_TEXT)
            self.screen.blit(text_surface, (10, 40 + i * 30))

        # Draw allocation percentage
        allocation_percent = self.memory_manager.get_allocation_percentage()
        allocation_text = f"Allocated Memory: {allocation_percent:.2f}%"
        allocation_surface = self.font.render(allocation_text, True, config.COLOR_TEXT)
        self.screen.blit(allocation_surface, (10, config.SCREEN_HEIGHT - 30))
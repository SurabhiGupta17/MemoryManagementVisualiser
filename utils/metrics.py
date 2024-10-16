class MetricsTracker:
    def __init__(self, memory_manager):
        self.memory_manager = memory_manager
        self.fragmentation = 0
        self.allocated_memory = 0

    def update(self):
        blocks = self.memory_manager.get_blocks()
        free_blocks = [block for block in blocks if block.is_free]
        allocated_blocks = [block for block in blocks if not block.is_free]

        self.fragmentation = len(free_blocks) - 1 if free_blocks else 0
        self.allocated_memory = sum(block.size for block in allocated_blocks)

    def get_fragmentation(self):
        return self.fragmentation

    def get_allocated_memory(self):
        return self.allocated_memory

    def get_allocation_percentage(self):
        return (self.allocated_memory / self.memory_manager.total_size) * 100
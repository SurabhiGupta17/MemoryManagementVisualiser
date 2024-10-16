import config

class MemoryBlock:
    def __init__(self, start, size, is_free=True):
        self.start = start
        self.size = size
        self.is_free = is_free

class MemoryManager:
    def __init__(self, total_size):
        self.total_size = total_size
        self.blocks = [MemoryBlock(0, total_size)]
        self.algorithm = config.DEFAULT_ALGORITHM

    def allocate(self, size):
        if self.algorithm == 'First Fit':
            return self._first_fit(size)
        elif self.algorithm == 'Best Fit':
            return self._best_fit(size)
        elif self.algorithm == 'Worst Fit':
            return self._worst_fit(size)
        return None

    def _first_fit(self, size):
        for i, block in enumerate(self.blocks):
            if block.is_free and block.size >= size:
                return self._split_block(i, size)
        return None

    def _best_fit(self, size):
        best_fit = None
        best_index = -1
        for i, block in enumerate(self.blocks):
            if block.is_free and block.size >= size:
                if best_fit is None or block.size < best_fit.size:
                    best_fit = block
                    best_index = i
        if best_index != -1:
            return self._split_block(best_index, size)
        return None

    def _worst_fit(self, size):
        worst_fit = None
        worst_index = -1
        for i, block in enumerate(self.blocks):
            if block.is_free and block.size >= size:
                if worst_fit is None or block.size > worst_fit.size:
                    worst_fit = block
                    worst_index = i
        if worst_index != -1:
            return self._split_block(worst_index, size)
        return None

    def _split_block(self, index, size):
        block = self.blocks[index]
        if block.size > size:
            new_block = MemoryBlock(block.start + size, block.size - size)
            self.blocks.insert(index + 1, new_block)
            block.size = size
        block.is_free = False
        return block.start

    def deallocate(self, start):
        for i, block in enumerate(self.blocks):
            if block.start == start and not block.is_free:
                block.is_free = True
                self._merge_free_blocks()
                return True
        return False

    def _merge_free_blocks(self):
        i = 0
        while i < len(self.blocks) - 1:
            if self.blocks[i].is_free and self.blocks[i+1].is_free:
                self.blocks[i].size += self.blocks[i+1].size
                self.blocks.pop(i+1)
            else:
                i += 1

    def get_blocks(self):
        return self.blocks

    def set_algorithm(self, algorithm):
        if algorithm in config.ALGORITHMS:
            self.algorithm = algorithm

    def get_allocation_percentage(self):
        allocated_memory = sum(block.size for block in self.blocks if not block.is_free)
        return (allocated_memory / self.total_size) * 100
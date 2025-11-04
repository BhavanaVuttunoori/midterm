class History:
    def __init__(self):
        self.history = []
        self.redo_stack = []

    def add(self, calc):
        self.history.append(calc)
        self.redo_stack.clear()  # clear redo when new op done

    def undo(self):
        if not self.history:
            return None
        calc = self.history.pop()
        self.redo_stack.append(calc)
        return calc

    def redo(self):
        if not self.redo_stack:
            return None
        calc = self.redo_stack.pop()
        self.history.append(calc)
        return calc

    def clear(self):
        self.history.clear()
        self.redo_stack.clear()

    def get_all(self):
        return list(self.history)

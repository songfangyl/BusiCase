import Product, Recipe, Step


class Process:

    def __init__(self, product: "Product", recipe: "Recipe", step: "Step"):
        self.product = product
        self.recipe = recipe
        self.step = step

    def total_usage(self):
        return self.recipe.total_usage()

    def get_product(self):
        return self.product

    def __str__(self):
        return f"[{self.product}, {self.recipe}, {self.step}]"

    def __eq__(self, other):
        if not isinstance(other, Process):
            return False
        return (
            self.product == other.product
            and self.recipe == other.recipe
            and self.step == other.step
        )


class SwitchProcess(Process):
    def __init__(self):
        super().__init__(None, None, None)

    def total_usage(self):
        return [0, 0, 0]

    def __str__(self):
        return f"[switch]"

    def __eq__(self, other):
        if not isinstance(other, SwitchProcess):
            return False
        return True


class IdleProcess(Process):
    def __init__(self):
        super().__init__(None, None, None)

    def total_usage(self):
        return [0, 0, 0]

    def __str__(self):
        return f"[idle]"

    def __eq__(self, other):
        if not isinstance(other, IdleProcess):
            return False
        return True

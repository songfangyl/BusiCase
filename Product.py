from Step import STEP1, STEP2, STEP3, STEP4, STEP5


class Product:

    steps = [STEP1, STEP2, STEP3, STEP4, STEP5]

    def __init__(self, product_number: int):
        self.product_number = product_number
        self.product_price = 0
        self.step_index = 0

    def next_step(self):
        if self.step_index < 5:
            return self.steps[self.step_index]
        return False

    def complete_step(self):

        self.step_index += 1
        if self.is_completed():
            self.product_price = 40000

    def is_completed(self):
        return self.step_index > 4

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.product_number == other.product_number

    def __hash__(self):
        return hash(self.product_number)

    def __str__(self):
        return f"Product: {self.product_number}"

from Recipe import A, B, C, D, E
import random


class Step:
    def __init__(self, recipes: list["Recipe"], step_number: int):
        self.recipes = recipes
        self.step_number = step_number

    def get_available_recipes(self):
        return self.recipes

    def __eq__(self, other):
        if not isinstance(other, Step):
            return False
        return self.step_number == other.step_number and self.recipes == other.recipes

    def __str__(self):
        return f"Step: {self.step_number}"


STEP1 = Step([A, B, D], 1)
STEP2 = Step([C, E], 2)
STEP3 = Step([B, D, E], 3)
STEP4 = Step([B, C], 4)
STEP5 = Step([A, C, D], 5)

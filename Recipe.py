class Recipe:

    convert_index = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    switching_matrix = [
        [0, 1, 1, 3, 1],
        [1, 0, 1, 1, 2],
        [1, 1, 0, 1, 2],
        [3, 1, 1, 0, 2],
        [1, 2, 2, 2, 0],
    ]

    def __init__(self, recipe_type: str, processing_time: int, list_of_material):
        self.recipe_type = recipe_type
        self.processing_time = processing_time
        self.list_of_material = list_of_material

    def total_usage(self):
        return self.list_of_material

    @classmethod
    def switching_time(cls, recipe_from: "Recipe", recipe_to: "Recipe"):
        i = cls.convert_index[recipe_from.recipe_type]
        j = cls.convert_index[recipe_to.recipe_type]
        return cls.switching_matrix[i][j]

    def __eq__(self, other):
        if not isinstance(other, Recipe):
            return False
        return self.recipe_type == other.recipe_type

    def __str__(self):
        return f"Recipe: {self.recipe_type}"


A = Recipe("A", 4, [24, 0, 0])
B = Recipe("B", 3, [0, 22, 0])
C = Recipe("C", 5, [6, 9, 0])
D = Recipe("D", 2, [20, 15, 6])
E = Recipe("E", 6, [0, 8, 4])

# print(Recipe.switching_time(A, D))

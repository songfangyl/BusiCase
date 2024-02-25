import Equipment, Product, Recipe
import random


class State:

    def __init__(self, equipments: list["Equipment"]):
        self.equipments = equipments

    def total_cost(self):
        usage = [0, 0, 0]
        for equipment in self.equipments:
            current_usage = equipment.total_usage()
            usage[0] += current_usage[0]
            usage[1] += current_usage[1]
            usage[2] += current_usage[2]

        total_cost = 0
        X, Y, Z = usage

        if X <= 50:
            total_cost += 200 * X
        elif X <= 500:
            total_cost += 190 * X
        else:
            total_cost += 175 * X

        if Y <= 50:
            total_cost += 300 * Y
        elif Y <= 500:
            total_cost += 275 * Y
        else:
            total_cost += 250 * Y

        if Z <= 50:
            total_cost += 240 * Z
        elif Z <= 500:
            total_cost += 220 * Z
        else:
            total_cost += 205 * Z

        return total_cost

    def total_revenue(self, total_completed_product):
        return total_completed_product * 40000

    def evaluate(self, total_completed_product):
        return self.total_revenue(total_completed_product) - self.total_cost()

    def next_valid_state(self, list_of_products):
        if not list_of_products:
            return False

        sorted_equipments = sorted(self.equipments, key=lambda equipment: equipment.get_length())

        random.shuffle(list_of_products)

        minimum_unuse_hour = 168
        best_product = None
        best_recipe = None
        best_equipment = None
        for equipment in sorted_equipments:

            for product in list_of_products:

                start_hour = 0
                for x in self.equipments:  # Check the latest hour of the current product
                    start_hour = max(x.product_latest_hour(product) + 1, start_hour)

                list_of_recipes = (
                    product.next_step().get_available_recipes()
                )  # List of recipe can be used
                random.shuffle(list_of_recipes)

                for recipe in list_of_recipes:
                    unuse_hour = equipment.count_unuse_hour(product, recipe, start_hour)
                    if unuse_hour < minimum_unuse_hour and equipment.is_compatible(
                        recipe, start_hour - 1
                    ):
                        minimum_unuse_hour = unuse_hour
                        best_recipe = recipe
                        best_product = product
                        best_equipment = equipment

                    if unuse_hour == 0:
                        break

                if minimum_unuse_hour == 0:
                    break

            if minimum_unuse_hour <= 5:
                break

        if not best_equipment:
            return False

        start_hour = 0

        for equipment in self.equipments:
            start_hour = max(equipment.product_latest_hour(product) + 1, start_hour)

        best_equipment.fill_new_process(best_product, best_recipe, start_hour)

        return True

    def __str__(self):
        equipments_str = "\n__________________________\n".join(
            str(equipment) for equipment in self.equipments
        )
        return f"{equipments_str}"

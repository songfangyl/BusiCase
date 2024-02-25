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

        # print(
        #     f"Sorted Equipments: {sorted_equipments[0].name}: {sorted_equipments[0].get_length()}, {sorted_equipments[1].name}: {sorted_equipments[1].get_length()}, {sorted_equipments[2].name}: {sorted_equipments[2].get_length()}"
        # )

        random.shuffle(list_of_products)

        minimum_unuse_hour = 168
        best_product = None
        best_recipe = None
        best_equipment = None
        for equipment in sorted_equipments:
            # print(f"Equipment: {equipment.name}")

            for product in list_of_products:
                # print(f"Product: {product}")

                start_hour = 0
                for x in self.equipments:  # Check the latest hour of the current product
                    start_hour = max(x.product_latest_hour(product) + 1, start_hour)

                list_of_recipes = (
                    product.next_step().get_available_recipes()
                )  # List of recipe can be used
                random.shuffle(list_of_recipes)

                for recipe in list_of_recipes:
                    # print(f"Recipe: {recipe}")
                    unuse_hour = equipment.count_unuse_hour(product, recipe, start_hour)
                    # print(f"Minimum_unuse: {minimum_unuse_hour}")
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

        # print(f"{best_equipment.name}, {best_product}, {best_recipe}")
        best_equipment.fill_new_process(best_product, best_recipe, start_hour)

        return True

        # start_hour = 0
        # list_of_equipments = []
        # for equipment in self.equipments:
        #     start_hour = max(equipment.product_latest_hour(product) + 1, start_hour)
        #     if equipment.is_compatible(recipe, product, start_hour - 1):
        #         list_of_equipments.append(equipment)
        # if list_of_equipments:
        #     choosen_equipment = random.choice(list_of_equipments)
        #     choosen_equipment.fill_new_process(product, recipe, start_hour)
        #     return True
        # else:
        #     return False

    def __str__(self):
        equipments_str = "\n__________________________\n".join(
            str(equipment) for equipment in self.equipments
        )
        return f"{equipments_str}"


# state1 = State([Equipment.ALPHA, Equipment.BETA, Equipment.GAMMA])
# product2 = Product.Product(1)
# product3 = Product.Product(2)
# state1.next_valid_state([product2, product3])
# print(state1)
# state1.next_valid_state([product2, product3])
# print(state1)

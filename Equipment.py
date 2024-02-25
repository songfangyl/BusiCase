from Recipe import A, B, C, D, E
import Recipe, Process, Product, Step


class Equipment:

    def __init__(
        self, list_of_recipe: list["Recipe"], name: str, list_of_process: list[object] = []
    ):
        self.list_of_recipe = list_of_recipe
        self.list_of_process = list_of_process
        self.name = name

    def product_latest_hour(self, product):
        latest_hour = -1
        for i in range(len(self.list_of_process)):
            if product == self.list_of_process[i].product:
                latest_hour = i
        return latest_hour

    def is_compatible(self, recipe: "Recipe", current_hour):
        if recipe in self.list_of_recipe:
            if self.list_of_process:
                current_hour = max(current_hour, len(self.list_of_process))
                previous_recipe = self.list_of_process[-1].recipe
                switching_time = Recipe.Recipe.switching_time(previous_recipe, recipe)
                total_hour = switching_time + recipe.processing_time + current_hour
                return total_hour <= 168
            return True
        return False

    def count_unuse_hour(self, product, recipe, start_hour):
        total_hour = 0
        if self.list_of_process:
            total_hour += Recipe.Recipe.switching_time(self.list_of_process[-1].recipe, recipe)

        total_hour += max(start_hour - len(self.list_of_process), 0)

        return total_hour

    def fill_new_process(self, product, recipe, start_hour):
        switching_time = 0
        if self.list_of_process:
            switching_time = Recipe.Recipe.switching_time(self.list_of_process[-1].recipe, recipe)

        for i in range(switching_time):
            self.list_of_process.append(Process.SwitchProcess())

        while len(self.list_of_process) < start_hour:
            self.list_of_process.append(Process.IdleProcess())

        new_process = Process.Process(product, recipe, product.next_step())

        for i in range(recipe.processing_time):
            self.list_of_process.append(new_process)

        product.complete_step()

    def total_usage(self):

        total_usage = [0, 0, 0]

        if not self.list_of_process:
            return total_usage

        currect_usage = self.list_of_process[0].total_usage()  # Add the first process usage
        total_usage[0] += currect_usage[0]
        total_usage[1] += currect_usage[1]
        total_usage[2] += currect_usage[2]

        prev = self.list_of_process[0]

        for process in self.list_of_process[1:]:  # Prevent duplicate
            if process != prev:
                currect_usage = process.total_usage()
                total_usage[0] += currect_usage[0]  # Add the rest of process usage
                total_usage[1] += currect_usage[1]
                total_usage[2] += currect_usage[2]
                prev = process  # Update the previous element

        return total_usage

    def get_length(self):
        return len(self.list_of_process)

    def total_completed_product(self):

        unique_products = {process.get_product() for process in self.list_of_process}

        total_count = 0

        for product in unique_products:

            if product and product.is_completed():
                total_count += 1
        return total_count

    def __str__(self):
        process_str = (
            "\n".join(
                f"{i}: {process}" for i, process in enumerate(self.list_of_process, start=1)
            )
            if self.list_of_process
            else "None"
        )

        return f"{self.name}, \n{process_str}"

    def __eq__(self, other):
        if not isinstance(other, Equipment):
            return False
        return (
            self.name == other.name
            and self.list_of_recipe == other.list_of_recipe
            and self.list_of_process == other.list_of_process
        )



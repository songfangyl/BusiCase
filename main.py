import State, Equipment, Product, time
from Recipe import A, B, C, D, E

max_score = 0
max_state = None

for i in range(10000):

    ALPHA = Equipment.Equipment([A, B, D, E], "alpha", [])
    BETA = Equipment.Equipment([B, C, E], "beta", [])
    GAMMA = Equipment.Equipment([A, C, D], "gamma", [])

    print(f"Loop: {i}")

    state = State.State([ALPHA, BETA, GAMMA])

    initial_number_of_prodcut = 22

    list_of_products = [Product.Product(j) for j in range(1, 23)]

    while state.next_valid_state(list_of_products):
        list_of_products = [product for product in list_of_products if not product.is_completed()]

    completed_product = initial_number_of_prodcut - len(list_of_products)

    if state.evaluate(completed_product) > max_score:
        max_score = state.evaluate(completed_product)
        max_state = state

    print(f"Profit: {state.evaluate(completed_product)}")


with open("output_file.txt", "a") as f:
    print(
        f"_____________________________________state_______________________________________",
        file=f,
    )
    print(max_state, file=f)
    print(f"total_cost: {max_state.total_cost()}", file=f)
    print(f"Profit: {max_score}", file=f)

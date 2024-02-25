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

# data = str(max_state)

# sections = data.split("\n__________________________\n")

# result = []

# # Iterate over each section
# for section in sections:
#     # Split the section into title and items based on the comma
#     title, items = section.split("\n", 1)
#     items = items.split("\n")

#     # Remove any leading or trailing whitespaces from the title
#     title = title.strip()

#     new_items = []
#     for item in items:
#         new_item = []
#         row_number, item_datas = item.split(": ", 1)
#         new_item.append(row_number)

#         if len(item_datas) <= 8:
#             new_item.append(item_datas[0][1:-1])
#             new_items.append(new_item)
#             continue

#         item_datas = item_datas.split(", ")

#         for item_data in item_datas:
#             new_item.append(item_data.split()[1])

#         new_items.append(new_item)

#     # Append the title and its corresponding list of items to the result list
#     result.append((title, new_items))

# # print(result)

# to_excel(4, 2, result[0][1][1])
# row_counter += 1

# to_excel(row_counter, 1, "Total Cost:")
# write_to_excel(row_counter, 2, max_state.total_cost())
# row_counter += 1

# write_to_excel(row_counter, 1, "Profit:")
# write_to_excel(row_counter, 2, max_score)
# row_counter += 1

# # Save the workbook
# wb.save("existing_file.xlsx")

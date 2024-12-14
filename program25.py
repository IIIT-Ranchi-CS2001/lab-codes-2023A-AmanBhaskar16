customer_name = ["Aman", "Ram", "Satyam", "Ivan"]
customer_id = ["Cs001", "Cs002", "Cs003"]
shopping_points = [100, 200, 300, 400, 500]
strct = True
if strct and (len(customer_name) != len(customer_id) or len(customer_name) != len(shopping_points)):
    print("Lists must be of equal length when strct is True")
else:
    min_length = min(len(customer_name), len(customer_id), len(shopping_points))
    zipped_data = []
    for i in range(min_length):
        zipped_data.append((customer_name[i], customer_id[i], shopping_points[i]))
    print(zipped_data)
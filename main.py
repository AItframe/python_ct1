#Задание 1
def get_books(file_path):
    all_records = []
    file = open(file_path, 'r', encoding='utf-8')
    
    file.readline()
    
    for line in file:
        line = line.strip()
        if not line:
            continue
            
        parts = line.split('|')

        item = [
            parts[0], 
            parts[1], 
            parts[2], 
            int(parts[3]), 
            float(parts[4])
        ]
        all_records.append(item)
        
    file.close()
    return all_records
    
print("\n\nЗадание 1\n")
books = get_books("books.csv")
for row in books:
    print(row)

#Задание 2
def filtered_books(book_list, search_word):
    filtered_res = []
    for b in book_list:
        if search_word.lower() in b[1].lower():
            merged_info = b[1] + ", " + b[2]
            new_entry = [b[0], merged_info, b[3], b[4]]
            filtered_res.append(new_entry)
    return filtered_res

print("\n\nЗадание 2\n")
only_python = filtered_books(books, "python")
for row in only_python:
    print(row)


#Задание 3
def get_totals(filtered_list):
    total_costs = []
    for b in filtered_list:
        cost = b[2] * b[3]
        total_costs.append( (b[0], (cost, 2)) )
    return total_costs

print("\n\nЗадание 3\n")
final_prices = get_totals(only_python)
for row in final_prices:
    print(row)
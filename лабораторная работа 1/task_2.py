inf_volume = 1.44 * 1024 * 1024
count_pages = 100
count_str = 50
count_symbol = 25
bytes_for_one_symbol = 4

volume_one_book = count_pages * count_str * count_symbol * bytes_for_one_symbol
count_books = inf_volume // volume_one_book

# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", int(count_books))

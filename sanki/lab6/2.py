# Створення множин з літер прізвища, імені та по батькові
set1 = set("греділь")
set2 = set("олександр")
set3 = set("михайлович")

# Всі літери українського алфавіту у нижньому регістрі
ukrainian_alphabet = set("абвгґдежзийіїклмнопрстуфхцчшщьюя")

# a. Всі літери, які є в set2 і set3
intersection_set2_set3 = set2 & set3
print("a. Всі літери, які є в set2 і set3:", intersection_set2_set3)

# b. Літери, які є і в set1 або set2
union_set1_set2 = set1 | set2
print("b. Літери, які є і в set1 або set2:", union_set1_set2)

# c. Літери set2, яких немає в set1
difference_set2_set1 = set2 - set1
print("c. Літери set2, яких немає в set1:", difference_set2_set1)

# d. Чи є set1 підмножиною set3
is_set1_subset_of_set3 = set1 <= set3
print("d. Чи є set1 підмножиною set3:", is_set1_subset_of_set3)

# e. Літери, які є в set1 або set2, але не в обидвох
symmetric_difference_set1_set2 = set1 ^ set2
print("e. Літери, які є в set1 або set2, але не в обидвох:", symmetric_difference_set1_set2)

# f. Всі літери, які є в двох множинах з трьох
two_of_three_sets = (set1 & set2) | (set1 & set3) | (set2 & set3)
print("f. Всі літери, які є в двох множинах з трьох:", two_of_three_sets)

# g. Всі літери, які є лише в одній множині з трьох
only_in_one_set = (set1 - set2 - set3) | (set2 - set1 - set3) | (set3 - set1 - set2)
print("g. Всі літери, які є лише в одній множині з трьох:", only_in_one_set)

# h. Всі літери алфавіту, яких немає в жодній з множин
letters_not_in_any_set = ukrainian_alphabet - (set1 | set2 | set3)
print("h. Всі літери алфавіту, яких немає в жодній з множин:", letters_not_in_any_set)

# i. Всі літери алфавіту, яких немає у кожній з трьох множин
letters_not_in_all_sets = ukrainian_alphabet - (set1 & set2 & set3)
print("i. Всі літери алфавіту, яких немає у кожній з трьох множин:", letters_not_in_all_sets)

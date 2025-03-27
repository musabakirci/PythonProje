#1. Liste Düzleştirme Fonksiyonu (Flatten)
def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output = flatten(input_list)
print(output)  


#2. İç İçe Listeleri Tersine Çevirme Fonksiyonu
def reverse_nested(lst):
    reversed_list = []
    for item in reversed(lst):
        if isinstance(item, list):
            reversed_list.append(reverse_nested(item))
        else:
            reversed_list.append(item)
    return reversed_list


input_list = [[1, 2], [3, 4], [5, 6, 7]]
output = reverse_nested(input_list)
print(output) 
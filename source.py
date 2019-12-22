sentence = input("entre your sentence here:",)
count = 0
list_sentence = list(sentence)
unique_sentence = set(list_sentence)
print(list_sentence)
print(unique_sentence)
final_list = []

for y in unique_sentence:
    for x in list_sentence:
        if(y == x):
            count += 1
    final_list.append((y, count))
    count = 0
final_list.sort(key=lambda final_lis: final_lis[1])
print(final_list)
print("the most common charis: ", final_list[-1])

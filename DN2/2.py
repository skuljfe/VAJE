our_list = [1,2,3,4,5,6,7]
our_dict = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": 12,
    "e": 357,
    "f": 12
}
our_tuple = (357, 12, 12, 8, 5, 2, 2)

index=4
new_tuple=()

vrednost=our_list[index]
our_list.pop(index)
our_dict["d"]=vrednost

for i in our_dict:
    new_tuple+=(our_dict[i],)

print(new_tuple==our_tuple)
print(our_list)
print(our_dict)
print(new_tuple)
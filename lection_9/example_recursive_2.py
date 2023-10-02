
list_of_data = [
    1, "2", "cat", 99, "dog",
    (4, 44, ["red", "green", ("mother", "father",)]),
    ["one", "two", "55", {1, 4, "big", True}, ["milk", 1, "bread"]],
    "End"
]


def find_data(data, list_data):
    result = False

    for iterator in list_data:
        # isinstance() - перевіряє чи переший обʼєкт відповідає вимогам пошуку, тобто другому обʼєту
        if isinstance(iterator, str) and iterator == data: 
            result = True
            break

        elif isinstance(iterator, (tuple, list, set)):
            result = find_data(data, iterator)
            if result is True:
                break
            # if data in iterator:
            #     result = True
            #     break

    return result


def main():
    while True:
        user_input = input("Enter word to search: ")

        if not user_input:
            print("Enter something.")
            continue
        elif find_data(user_input, list_of_data):
            print(f"The search was successful. \"{user_input}\" is in my storage.")
        else:
            print(f"\"{user_input}\", no math.")

        user_exit = input("Do tou wanna out? (Y/n): ").strip().lower()

        if user_exit == "y":
            break
        else:
            continue


main()

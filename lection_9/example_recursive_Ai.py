list_of_data = [
    1, "2", "cat", 99, "dog",
    (4, 44, ["red", "green", ("mother", "father",)]),
    ["one", "two", "55", {1, 4, "big", True}, ["milk", 1, "bread"]],
    "End"
]


def find_data(data, list_data, depth=0, case_sensitive=False):
    result = False

    for iterator in list_data:
        if isinstance(iterator, str):
            if not case_sensitive and iterator.lower() == data.lower():
                result = True
                break
            elif case_sensitive and iterator == data:
                result = True
                break

        elif isinstance(iterator, (tuple, list, set)) and depth > 0:
            if find_data(data, iterator, depth-1, case_sensitive):
                result = True
                break

    return result


def main():
    while True:
        user_input = input("Enter word to search: ")

        if not user_input:
            print("Enter something.")
            continue
        elif find_data(user_input, list_of_data, depth=2, case_sensitive=False):
            print(f"The search was successful. \"{user_input}\" is in my storage.")
        else:
            print(f"\"{user_input}\", no math.")

        user_exit = input("Do tou wanna out? (Y/n): ").strip().lower()

        if user_exit == "y":
            break
        else:
            continue


main()

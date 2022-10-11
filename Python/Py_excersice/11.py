phone_book = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781,
    "Jake": 938273443,
}
# your code goes here
phone_book.pop("Jill")


# testing code
if "Jake" in phone_book:
    print("Jake is listed in the phonebook.")

if "Jill" not in phone_book:
    print("Jill is not listed in the phonebook.")

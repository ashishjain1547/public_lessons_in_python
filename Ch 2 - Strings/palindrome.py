text = input("Enter a word or phrase: ").lower()
if text == text[::-1]:
    print("Yes, the input text is a palindrome.")
else:
    print("No, the input text is not a palindrome.")
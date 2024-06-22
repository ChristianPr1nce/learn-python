# Define your main dictionary
my_data = {
  "africans": ["apple", "banana", "tallpeople"]
  # You can add more key-value pairs here (e.g., "asians": [...])
}

# Get user input (converted to lowercase for case-insensitive comparison)
user_input = input("Enter a key from the data: ").lower()

# Check if user input matches a key in the dictionary
if user_input in my_data:
  # Access the corresponding list and print its elements
  selected_data = my_data[user_input]
  print(f"The elements in '{user_input}' are:")
  for item in selected_data:
    print(item)
else:
  print(f"Key '{user_input}' not found in the data.")

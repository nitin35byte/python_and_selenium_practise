# Step 1: Create and write initial names to the file
with open("test_data_text.txt", 'w') as file:
    file.write("rahul\n"
               "Nitin\n"
               "Sumit\n")

# Step 2: Read and process the data
with open('test_data_text.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

# Print the first three names
print(f"First name is: {data[0]}")
print(f"Second name is: {data[1]}")
print(f"Third name is: {data[2]}")

# Step 3: Append additional names to the file
with open("test_data_text.txt", 'a') as f:
    f.write("Rohit\n"
            "Rohan\n"
            "Nishant\n"
            "Nitish\n")

# Step 4: Read and process the updated data
with open('test_data_text.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

# Access data from index 3 to 5
try:
    print(f"Fourth name is: {data[3]}")
    print(f"Fifth name is: {data[4]}")
    print(f"Sixth name is: {data[5]}")
except IndexError as e:
    print("Error accessing names:", e)

# Print the length of the data to verify
print("Total names in the file:", len(data))

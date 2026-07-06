# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("First number: ")
#     if first_number == 'q':
#         break
#     second_namber = input("Second number: ")
#     try:
#         answer = int(first_number) / int(second_namber)
#     except ZeroDivisionError: 
#         print("You can't divide by zero!")
#     else:
#         print(answer)


# def count_words(filename):
#     try:
#         with open(filename) as f:
#             contents = f.read()
#     except FileNotFoundError:
#         msg = "Sorry, the file " + filename + " does not exist."
#         print(msg)
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print("The file" + filename + "has about" + str(num_words) + " words.")

# # filename = 'alice.txt'
# # count_words(filename)

# filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt'] 
# for filename in filenames: 
#     count_words(filename)

# # title = "Alice in Wonderland"
# # print(title.split())

#你希望程序在发生异常时一声不吭，就像什么都没有发生一样继续运行
# def count_words(filename):
#     try:
#         with open(filename) as f:
#             contents = f.read()
#     except FileNotFoundError:
#         pass  #还充当占位符
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print("The file" + filename + "has about" + str(num_words) + " words.")

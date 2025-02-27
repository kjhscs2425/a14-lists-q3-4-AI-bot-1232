
def make_list_of_files(n):
    """
    make a lists of n file names with the format "file_0.txt"
    assume n greater than or equal to 1
    hint: use a loop and append
    """
    file_list = []
    for i in range(n):  # Use n, not file_list, in the range function
        file_list.append(f"file_{i}.txt")  # Use .txt, not .text
    return file_list

print(make_list_of_files(5)) #['file_0.txt', 'file_1.txt', 'file_2.txt', 'file_3.txt', 'file_4.txt']
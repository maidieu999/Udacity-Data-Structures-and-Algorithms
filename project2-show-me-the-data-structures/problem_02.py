
import os

def find_files(suffix, path):
    if not os.path.exists(path):
        print("Invalid path:", path)
        return []

    file_list = os.listdir(path)
    file_paths = list()

    # Iterate over all the entries
    for entry in file_list:
        full_path = os.path.join(path, entry)
         # If entry is a file and ends with suffix then append it to the list
        if os.path.isfile(full_path) and full_path.endswith(suffix):
            file_paths.append(full_path)
         # If entry is a directory then get the list of files in this directory
        elif os.path.isdir(full_path):
            file_paths.extend(find_files(suffix, full_path))

    return file_paths

## Add your own test cases: include at least three test cases
# Test Case 1: Finding all .c files in the test directory
case_1 = find_files(".c", "testdir")
print("Test Case 1 - should return ['testdir/subdir3/subsubdir1/b.c', 'testdir/t1.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c']")
print(case_1)

# Test Case 2: Finding all .h files in a non-existent directory (should return an empty list)
case_2 = find_files(".h", "testdir")
print("Test Case 2 - should return ['testdir/subdir3/subsubdir1/b.h', 'testdir/subdir5/a.h', 'testdir/t1.h', 'testdir/subdir1/a.h']")
print(case_2)

# Test Case 3: Finding all .txt files in a test directory
case_3 = find_files(".txt", ".")
print("Test Case 3 - should return [./analysis.txt]")
print(case_3)

# Test Case 3: Finding all .txt files in a non exist directory
print("Test Case 4 - should return [] for invalid path")
case_4 = find_files(".txt", "./nonexistdir")
print(case_4)
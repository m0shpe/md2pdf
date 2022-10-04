import os
import aspose.words as aw

md_files = {}
directory = str(input("Enter path: "))
result_directory = "created_pdf_files"
result_path = directory + "\\" + result_directory 

os.chdir(directory)
print("starting...")
print("Directory: " + directory)
for root, dirs, files in os.walk(directory, topdown=True):
    for file in files:
        path_to_file = os.path.join(root, file)
        filename, file_extension = os.path.splitext(path_to_file)
        if file_extension == ".md":
            md_files[file] = root.split(directory + "\\")[1]

print()
print("Found...")
for filename in md_files:
    print(md_files[filename] + "\\" + filename + "\n")
print()

for filename in md_files:
    file_rel_path = md_files[filename]
    file_abs_path = result_path + "\\" + file_rel_path
    if not os.path.exists(file_abs_path):
        os.makedirs(file_abs_path)
    name, extension = os.path.splitext(filename)
    doc = aw.Document(file_rel_path + "\\" + filename)
    doc.save(file_abs_path + "\\" + name + ".pdf")
print("Finished...")

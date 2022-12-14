import os
import aspose.words as aw
import sys

md_files = {}
directory = str(input("Enter path: "))
mode = str(input("Convert to (pdf/md): "))
if(mode == "pdf"):
    search_extension = ".md"
    mode_extension = ".pdf"
elif(mode == "md"):
    search_extension = ".pdf"
    mode_extension = ".md"
else:
    sys.exit("Wrong mode: " + mode)
result_directory = "created_pdf_files"
result_path = directory + "\\" + result_directory 

os.chdir(directory)
print("Starting...")
print("Directory: " + directory + "\n")
for root, dirs, files in os.walk(directory, topdown=True):
    for file in files:
        path_to_file = os.path.join(root, file)
        filename, file_extension = os.path.splitext(path_to_file)
        if file_extension == search_extension:
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
    doc.save(file_abs_path + "\\" + name + mode_extension)
print("Finished...")

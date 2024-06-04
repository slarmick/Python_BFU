with open('input.txt') as file_in:
    children = file_in.readlines()
oldest = children[0]
youngest = children[0]
for child in children:
    if int(child.split()[2]) > int(oldest.split()[2]):
        oldest = child
    if int(child.split()[2]) < int(youngest.split()[2]):
        youngest = child
with open('oldest.txt', 'w') as out_file:
    out_file.write(oldest)
with open('youngest.txt', 'w') as out_file:
    out_file.write(youngest)
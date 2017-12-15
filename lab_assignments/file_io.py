# #read **sample code only**
# open('text_file.tx', 'r')
# f =  open('text name', 'r')
# print(f.read())

# content = f.read()
# new_content = content.replace('l','1')
# f.close()

# wf = open('text_file.txt', 'w')
# wf.write(new_content)
# wf.close()
# #write a file / overright everything
# open('', 'w')
# wf = open('text_file.txt', 'w')
# wf.write(new_content)
# wf.close()

# #delete
# open(<filename>, 'x')
# #open a file that already exist
# open(<filename>, 'a')
# with open('text_file.txt', 'r+') as f:
#     lines = [i.replace('\n', '') for i in f.readlines()]
    
#     #this is just the same line above in a different syntax
    
#     #for i in f.readlines():
#     #   lines.append(i.replace('\n', ''))
    
#     # lines = f.readlines()
#     # lines_no_newlines = []
#     # for i in lines:
#     #     lines_no_newlines.append(i.replace('\n', ''))
#     # lines = lines_no_newlines[:]

# print(lines)
# for l in lines:
#     print(l)

import json

with open('data_example.json', 'r') as f:
    data = json.loads(f.read())

for i in range(len(data)):
    data[i]['glossary']['title'] = 'A new title for this thing x {'.format('*'(i+1))
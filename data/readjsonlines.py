import json_lines

with open('Arma_3.jsonlines', 'rb') as f: # opening file in binary(rb) mode    
    for item in json_lines.reader(f):
        if item['rating'] == 'Recommended' :
            print(item['review'],item['rating'])

    #or use print(item['X']) for printing specific data
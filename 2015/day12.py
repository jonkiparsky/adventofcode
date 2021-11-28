import json

input_file = open("day12_input.txt")
json_blob = json.load(input_file)

def count_json(blob):
    sub = 0
    if type(blob) == list:
        for i in blob:
            sub += count_json(i)
        return sub
    if type(blob) == dict:
        if "red" in blob.values():
            return sub
        else:
            for i in blob.values():
                sub += count_json(i)
        return sub
    if type(blob) == int:
        return blob
    return 0

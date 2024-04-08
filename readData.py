import json
import os

def clear_json(filepath):
    # clear the json file 
    with open(filepath, "w") as file:
        file.truncate()

def write_json(data):
    # write data to json file
    # data written to csv
    
    with open("good_annotations.json", "r") as file:
        try:
            file_data = json.load(file) # file content to python list
        except json.decoder.JSONDecodeError:
                file_data = []
                print("file empty")
    
    file_data.append(data) 
    
    with open("good_annotations.json", 'w') as file:
        json.dump(file_data, file, indent=2) # dict to array (json)  

def read_json(filepath):
    
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON data from file '{filepath}'.")
        return {}   

def get_image_data(data, image_name, shots=5):
    image_name = image_name.split("_")
    index = ((int(image_name[0]) - 1) * shots) + (int(image_name[1]) - 1)
    return data[index]

if __name__ == "__main__":
    
    # Clear good_annotations.json
    clear_json("good_annotations.json")
    
    # Read all the annotations
    data = read_json("annotations.json")
    image_anno = get_image_data(data, "2_4")
    # print(value["image"], value["shot"])
    
    # Read the good images
    # and write their annotations to a file
    directory = "dataset\\train\\good"
    files = os.listdir(directory)
    print(files)
    # write_json(image_anno)
    
    image_anno = get_image_data(data, "1_1")
    # write_json(image_anno)
    
    
    
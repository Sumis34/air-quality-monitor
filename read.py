import serial
import json

arduino = serial.Serial(port = 'COM4', timeout=0)

#Json base value
#{
#    "measurements": []
#}
   
def get_value():
    value = None
    while not value:
        a = arduino.readline().strip()
        try:
            value = float(a)
        except:
            pass

    return value

def append_measurement(measurement_dict, json_file="C:\\Users\\Noé\\Documents\\Arduino\\air\\air2\\data.json"):
    # Load existing measurements from the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Append the new measurement to the measurements property
    data['measurements'].append(measurement_dict)

    # Write the updated data to the JSON file
    with open(json_file, 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    location = input("Location: ")
    description = input("Description: ")
    val = get_value()
    # write_json({'location': location, 'description': description,'c02': val})
    append_measurement({'location': location, 'description': description,'c02': val})


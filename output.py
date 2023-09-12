def append_to_txt_file(filename, input_list):
    # Convert the input list to a comma-separated string
    new_line = ','.join(map(str, input_list)) + '\n'
    # Open the file in append mode ('a+'), which creates the file if it doesn't exist
    with open(filename, 'a+') as file:
        file.write(new_line)
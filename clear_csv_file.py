def clear(file_name):
    # clear the file
    with open(file_name, "w") as csv_file:
        csv_file.write("")
        csv_file.close()
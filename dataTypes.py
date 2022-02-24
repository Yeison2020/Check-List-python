myfile = open('new_files.txt')


myfile.read()

myfile.seek(0)
reading = myfile.readline()

print(reading)
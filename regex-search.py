import os, sys

if len(sys.argv) < 2:
    print('please put an argument')
    sys.exit()

expression = sys.argv[1]

for filename in os.listdir('folder'):
    files = open('folder/%s' % filename)

    datafile = files.readlines()
    for line in datafile:
        if expression in line:
            print(line)

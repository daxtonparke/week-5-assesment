log_file = open("um-server-01.txt")
# opens data file

def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)
            
# creates a function that prints out the line if the day is tuesday

sales_reports(log_file)
# invokes function
log_file = open("um-server-01.txt")
# opens data file

def sales_reports(log_file):
    for line in log_file:
        # for loop
        line = line.rstrip()
        # strips whitespace
        day = line[0:3]
        # defines day as location on each line
        if day == "Mon":
            print(line)
            # if day is = x print that line
            
# creates a function that prints out the line if the day is tuesday

sales_reports(log_file)
# invokes function
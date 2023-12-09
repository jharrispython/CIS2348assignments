#James Harris
#2078031

import datetime

month_list = {"january": "1", "february": "2", "march": "3",
              "april": "4", "may": "5", "june": "6", "july": "7",
             "august": "8", "september": "9", "october": "10",
              "november": "11", "december": "12"}

input_file = open('inputDates.txt', 'r')
output_file = open('parsedDates.txt', 'w')

for each in input_file:
    if each != "-1":
        comma_position = each.find(",")
        if (comma_position >= 0):
            month_date = each[:comma_position]
            month = month_date[:month_date.find(" ")].strip()
            day = month_date[month_date.find(" "):].strip()
            year = each[comma_position + 1:].strip()

            if month.lower() in month_list:
                monthNum = month_list[month.lower()]
                result = monthNum + "/" + day + "/" + year
                date_time_obj = datetime.datetime.strptime(result, '%m/%d/%Y')

                if (date_time_obj.date() <= datetime.datetime.now().date()):
                    output_file.write(result)
                    output_file.write("\n")

        else:
            pass

output_file.close()
input_file.close()

import statistics
data = []
def add_marks():
    subject = input("Enter subject name: ")
    mark = int(input("Enter marks: "))
    return (subject, mark)
n = int(input("How many subjects? "))
for i in range(n):
    data.append(add_marks())sude
marks_list = [item[1] for item in data] # extract only marks
print("\nAll Data:", data)
print("Average marks:", statistics.mean(marks_list))
highest = max(data, key=lambda x: x[1])
print("Highest marks:", highest)

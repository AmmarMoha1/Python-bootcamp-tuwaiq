# Path Objects build locations portably
from pathlib import Path

data_file = Path("data") / "students.txt"

print(data_file)  # data/students.txt
print(data_file.name)  # students.txt
print(data_file.suffix)  # .txt


#Inspect Paths before using them
from pathlib import Path
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

data_file = data_dir / "students.txt"

print(data_dir.is_dir())
print(data_file.exists())


#files modes decide what may change
# "r" read an existing file
# "w" write and replace contents
# "a" append after existing contents
# "x" create only when absent

with open("notes.txt)", "a", encoding="utf-8") as file:
    file.write("New note\n")



#with closes the file automatically
from pathlib import Path

path = Path("notes.txt")

with path.open("r", encoding="utf-8") as file:
    content = file.read()

print(content)
print(file.closed)
    

# iterate over lines without loading everything
from pathlib import Path

path = Path("notes.txt")

with path.open("r", encoding="utf-8") as file:
    for line in file:               #dont use 'w' in for loop
        name = line.strip()
        if name:
            print(name)


# writing replaces exsting contents
from pathlib import Path

path = Path("student.txt")

with path.open("w", encoding="utf-8") as file:
    count = file.write("Sara\nAli\n")

print(count)  #9


#appending preserves existing contents
from pathlib import Path

path = Path("activity.txt")

with path.open("a", encoding="utf-8") as file:
    count = file.write("Student enrolled: Sara\n")

print("Activity saved")



from pathlib import Path

names = ["Sara", "Ali", "عمار"]
text = "\n".join(names)
path = Path("student.txt")

Path("student.txt").write_text(text,encoding="utf-8")


import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)       #list all the file on the folder if we use listdir
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        if files:                                                      //check file is non empty :true
            print(f"Files in {folder_path}:")                         //print /tmp all the files(folder path=/tmp)
            for file in files:                                       
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()
--------------------------------------------------------------------------------------------------------------------
Here’s the input to your program (when you run it and type at prompt):

/tmp /dev /feb


Meaning: folder_paths = ["/tmp", "/dev", "/feb"].

Then the code loops over each of these and calls list_files_in_folder(...). Let’s go through each iteration.

✅ First iteration: folder_path = "/tmp"

Call list_files_in_folder("/tmp").

Since /tmp exists and is (almost always) accessible with list permissions, os.listdir("/tmp") executes successfully. It returns a list of entries currently in /tmp (files, temporary files, sub‑directories, maybe leftover temp files from previous runs, etc.).

The function returns (files, None), where files is a (non‑empty or empty) list of strings, and error_message=None.

Back in main, you check if files:.

If files is non‑empty, this is true. So you go into the “success” branch:

Print: Files in /tmp:

Then loop over each file in files and print the filename.

If the directory happened to be empty (rare for /tmp, but possible if clean), files == [], which is “falsy” in Python, so you’d go to the else branch — but that would treat an empty folder as an “error”, which is misleading (something to be careful about).

Example output (assuming /tmp has files):

Files in /tmp:
tmp_file1.txt
some-app-cache
xYZ123.tmp
...   # (all items listed, one per line)


(The actual file names depend on what’s in /tmp at runtime.)

✅ Second iteration: folder_path = "/dev"

Call list_files_in_folder("/dev").

On a typical Linux system, /dev exists. os.listdir("/dev") should succeed because /dev is readable to normal users (device files are visible). 
Baeldung on Kotlin
+1

It returns a list of entries (device files, symlinks, subdirectories under /dev, etc.). For example, things like null, zero, tty, maybe sda, loop0, directories like bus, block, etc. The exact contents depend on the system.

The function returns (files, None). Back in main, if files: passes (list is non‑empty), so you print:

Files in /dev:
null
zero
tty
sda
loop0
bus
block
...  # etc., one per entry


So the program will list all device‑file names under /dev.

🚫 Third iteration: folder_path = "/feb"

Call list_files_in_folder("/feb").

Since we assume /feb does not exist on the filesystem, os.listdir("/feb") raises a FileNotFoundError.

This is caught by your except FileNotFoundError: block, and the function returns (None, "Folder not found").

Back in main, you get files = None, error_message = "Folder not found". The condition if files: is false (because files is None). So you go into the else branch and print:

Error in /feb: Folder not found

📄 Full (possible) output of the program for this input

Putting together all three iterations, a possible program output (with arbitrary example file names) might be:

Files in /tmp:
temp1234
session-ABCD
mytempfile
cache_xyz

Files in /dev:
null
zero
tty
sda
loop0
bus
block
...   # (a long list of device‑file and subsystem names)

Error in /feb: Folder not found


-----------------------------------------------------------------------------------------
🟢 Program starts running
Line 1
import os


Python loads the os module into memory

Nothing is printed

Program continues

🟢 Function definitions (no execution yet)
Line 3
def list_files_in_folder(folder_path):


Python defines the function

Code inside is not executed now

Python moves on

Line 14
def main():


Python defines the main() function

Still no execution

🟢 Entry point check
Line 30
if __name__ == "__main__":


Python checks:

Is this file run directly? → Yes

Condition is True

Line 31
main()


Python calls main()

Execution jumps into main()

🟢 Inside main()
Line 16
folder_paths = input(
    "Enter a list of folder paths separated by spaces: "
).split()


Step by step:

input() pauses the program

User types:

/tmp /wrongfolder


input() returns the string:

"/tmp /wrongfolder"


.split() breaks it into a list:

['/tmp', '/wrongfolder']


folder_paths now stores that list

🟢 Loop starts
Line 20
for folder_path in folder_paths:


Loop starts

First value:

folder_path = '/tmp'

🟢 First loop iteration (/tmp)
Line 21
files, error_message = list_files_in_folder(folder_path)


Calls list_files_in_folder('/tmp')

Execution jumps into that function

🟢 Inside list_files_in_folder('/tmp')
Line 5
try:


Python prepares to catch errors

Line 6
files = os.listdir(folder_path)


OS is asked to list files inside /tmp

Suppose /tmp contains:

['a.txt', 'b.log']

Line 7
return files, None


Function returns:

(['a.txt', 'b.log'], None)


Execution goes back to main()

🟢 Back in main()
Line 23
if files is not None:


files is ['a.txt', 'b.log']

Condition is True

Line 24
print(f"Files in {folder_path}:")


Prints:

Files in /tmp:

Line 25–26
for file in files:
    print(file)


Prints each file:

a.txt
b.log


# Primer\_Inventory\_To\_Benchling
Here's a Python script that converts the MatreyekLab primer google sheet into a csv file that is easily imported into benchling.

1) Go to the lab primer inventory google sheet -> 
"https://docs.google.com/spreadsheets/d/15RD_WrP_xZXN34KhymHYkKeOglDYzfkhz5-x2PMkPo0/edit?usp=sharing"

2) Go to file -> download -> Microsoft Excel (.xlsx)

3) Then take above file (MatreyekLab\_Primer\_Inventory.xlsx) and put it in the same directory as the Google\_sheet\_to\_benchling.py file.

4) Open terminal, go to the right directory, and then enter:

> Python3 Google\_sheet\_to\_benchling.py

5) It should make a new file called "Matreyeklab\_primers\_benchling.csv". The text in this file can be copy-pasted into benchling and imported into the "Primer" folder.

## Uploading the list to Benchling

6) Next, Log onto Benchling, go into the "MatreyekLab" project and into the "O_Primers" folder. Make a new folder named with the date (eg. "20200130" for January 30th, 2020). Once in the folder, select "Import Oligos", and copy-paste the contents of the csv file (Opened using a basic text editor like "TextEdit" or "Sublime Text 3". 

7) You'll have to scroll down all the way to the bottom, but then you can hit insert. Benchling is nice enough to get back to work as it uploads. 

## Using the new primer list

8) Once it does finishes uploading, you can go to whatever plasmid map you want to annotate with our current primers. Go to the right-hand side, two icons down to "Primers". Hit attach existing, add the new folder as the new location, and hit "find binding sites". Select all of the primers (top check box), and then hit the "Attach Selected Primers" button in the top right.

9) Now click on hte sequence map tab and Voila!, you can see the plasmid map now annotated. Find the primer you want (sequencing or otherwise) and go do some science.
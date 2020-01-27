#tail -n +2 ../data/Pacifici2013_data.csv | cut -d ";" -f 2-6 | tr -s ";" " " | sort -r -n -k 6 > /home/eebc177student/Developer/repos/eeb-c177-scripts/BodyM.csv$
#"tail -n +2 ../data/Pacifici2013_data.csv" reads everything after the first line of the Pacifici2013_data.csv file in the ../data repo
#"| cut -d ";" -f 2-6" takes that data, cuts it at the delimiter ";" and excludes everything except for columns 2-6
#"| tr -s ";" " "" takes that data and replaces the delimiter with a space
#"| sort -r -n -k 6" sorts that data in reverse numerical order based on column 6
#"> /home/eebc177student/Developer/repos/eeb-c177-scripts/BodyM.csv" moves the data to the BodyM.csv file in the ../eeb-c177-scripts repo
#"chmod +x ExtractBodyM.sh" gives me permission to execute the file
#"mv ExtractBodyM.sh ~/bin" moves the file to ../bin so that it can run automatically without typing bash

#"chmod +x BodyM.sh" gives me permission to execute the file
#! /bin/bash BodyM.csv
#the command above moves the file to the bin 
#"chmod u+x ~/.profile" adjusts permissions
#"nano ~/.profile"
#type PATH="$PATH:$HOME/Developer/repos/eeb-c177-scripts"


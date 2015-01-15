# How To Set Up

1. Pull this repository using the command ```git pull https://github.com/Aadeshp/Youtube-Search.git```
2. Change directory into the folder: ```cd Youtube-Search```
3. Move the script inside the folder to the local bin folder: ```mv youtube.py ~/bin/``` (If you do not have a local bin folder, follow the steps under <b>Set Up Bin</b>
4. Change directory to the local bin folder
5. Run the command ```ls``` to double check that the file ```youtube.py``` is in the bin folder, if not retrace your steps
6. Now you need to add the executable permission to the script, so run the command ```chmod +x ~/bin/youtube.py```
7. Now you can use ```youtube.py``` as a command (For help on how to use it run ```youtube.py -h```
8. OPTIONAL: Instead of having to run the command ```youtube.py [OPTION] [ARGUMENT]```, you can get rid of the .py extension by changing directory into the local bin folder ```cd ~/bin``` and changing the name of the script with the command ```mv youtube.py youtube```. Now you can run the command as ```youtube [OPTION] [ARGUMENT]```

# Set Up Bin

1. Create a local bin folder: ```mkdir ~/bin```
2. Open up either .bashrc or .bash_profile (Depending on Machine) in a text editor: ```vim ~/.bashrc``` or ```vim ~/.bash_profile```
3. Add ```PATH=$PATH:$HOME/bin``` at the top of the file and save
4. Now run the command ```source ~/.bashrc``` or ```source ~/.bash_profile``` (Depending on which you used from step 2)
5. Now run the command ```$PATH``` to double check that your local bin folder is now in $PATH

# How To

Below I will briefly explain how to use this script and the types of arguments:

<b>Positional (Mandatory) Argument(s): 
- Search</b>
  - ```youtube.py [SEARCH TEXT]``` (```[SEARCH TEXT]``` would be your search text surrounded by <b>QUOTES</b>) - This will open up the youtube video search page with the provided <b>SEARCH TEXT</b>

<b>Optional Argument(s):</b>
- ```youtube.py "SEARCH TEXT" --upload-date [DATE ARG]``` - This will do the same as the above command, except it will add the filter for Upload Date. Below are appropriate arguments to replace the ```[DATE ARG]``` placeholder
  - hour
  - today
  - week
  - month
  - year
- For Additional Options/Filters, run the command ```youtube.py -h```

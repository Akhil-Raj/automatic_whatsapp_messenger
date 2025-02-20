# Steps to run

- Clone the repo
- Download the myf followup sheet in the project's root. Rename it as "MYF followup Master - MYF attendees.csv", replacing any existing file with that name.
- Store the image that you want to attach with the message as 'Image.jpeg' in the project's root.
- Open the file 'mainFollowupSheet.py' and do these changes :
- - To send message to all those with status "Registered", change the "registered_message" variable.
- - To send message to all those with status "To be reached out", change the "first_message" variable.
- - To send message to all those having statuas one of ["Yes, Registration link sent", "didn't pick message sent", "Didn't pick up", "Registration sent w/o calling", "Call back/Not sure", "Switched Off/Out of Range"], change the "reminder_message" variable.
- - To send message to all those with status "Present", change the "present_message" variable.
- - Filter the statuses to which you want to send the message by commenting-uncommenting the 'continue' line in the if-elseif statements which are applied to the status values. Uncommenting the line would skip those people with the respective status. Commenting would send appropriate message to them depending on their status.
- If you want to attach image "Image.jpeg" with your message, keep the "kit.sendwhats_image" function call(the function is called towards the end of the script) uncommented and comment the "kit.sendwhatmsg_instantly" function. Similarly, if you do not want to attach an image with the message, reverse the commenting.
- See the file script.sh. It contains a sample command that you would need to run on the terminal to run the code. The last two arguments are start and end index of the row from the MYF Followup Sheet to whom you want to send the message. Note the start and end row number through which you want to send the message and change the last two arguments accordingly.
- Run the command. When you will run the command, you must have whatsapp logged-in in the browser in which the messages will be sent. If not logged-in, please do so by yourself. Also, you will face some modules not found errors. Install them using 'pip install' or 'conda install' command, whichever you prefer.
- While the script will be running, it will take screenshots after the message is sent and store it in the "screenshots" folder of your project. You can use those images to verify that the messages were indeed sent correctly. If you see an error that such a folder does not exists, create one and re run the command.
- Note that while the script to send the automated messages is running, the laptop must be kept idle.

If you face any issues in the steps above, please reach out to me(Akhil).
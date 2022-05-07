# spire_app

This app is for SPIRE LAB @IISc, Bangalore

requirements.txt has the list of all modules required for the app.
python3.8 has been used for this.

Use following commands for starting the app after installing all the requirements

For linux users

  export FLASK_APP=main
  flask run

Important Files:
1. Audio files are in static folder
2. model.py has configuration for creating database. 

you can run 

  python model.py 

to create database again with correction.






1. First page will list down all the examples and option to edit if correct or not.
On clicking "Not Correct". Radio button edit option should be enabled.
By default the radio button will show "correction" state  of the example in database.

2. Once clicked on edit this it will route to another page where example can be played.

3. The speed of example audio is slowed down to hear clearly. At the same time it will highlight the corresponding text.
4. Text can be highlight which are wrong. If correct text is highlighted then it can unhighlighted. 
5. On clicking updatecorrection button the correction flag in database corresponding to relevant text will update. 

...............
About database
...............

There are 2 tables linked to each other:
 1. Example table: Corresponding to Each Example with correction flag as well as whole text
 2. Correction Table: Corresponding to list of words in each Example as well as their correction flag. 



 


- This is a simple password manager program written using Python.
- The GUI was made with the tkinter package.
---------------------------------------------------------------------------------------------------------
The program is very straightforward:
---------------------------------------------------------------------------------------------------------
If You want to save a password:
  * You have to enter a website name and an email or username in the appropriate fields. Otherwise a pop-up window will apear reminding You not to leave any fields empty.
      - The email field is by default filled in with Your email of choice, to maximize productivity.
  * If You want, You can type in your password of choice, or generate a random one by utilizing the "Generate" button next to the input field. The input field to the right is for You to choose, how many characters You want in your password.
      - By default, the number of characters is set to 15, however You can set it to whatever you want.
      - The password is generated with an "equal" amount of letters (both upper and lower case), digits, and special characters, in a completely random order.
      - After generation, it will be automatically copied to Your clipboard.
  * After filling in all of the required fields, You can save the password to the database by clicking the "Add" button.
      - The program will show You a pop-up window with all the credentials that You have filled in, and if they seem right, click "Ok" and the password will be saved.
---------------------------------------------------------------------------------------------------------
If You want to check for a password in the database:
  * Fill in the website name and email fields.
  * Click the "Search" button.
      - Whether there is a password or not, the program will show you a message that is has, or hasn't found Your password.
  * If there is a password linked with the credentials given above, the password will be copied to Your clipboard, and it will be displayed in the "Password" field.
---------------------------------------------------------------------------------------------------------
If You want to quickly change the email field:
  * Simply click the "Clear" button and the text in that field will be erased

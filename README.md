# BankServerTask

##### This REST api is hosted at  https://fylework.herokuapp.com/
 - It accepts POST/GET requests of 2 types having the following definitions
 - It does not have any views on it. It is just basic REST api interface


##### Request 1 (For Given a bank branch IFSC code, get branch details problem)
 - {"type":1,"ifsc":anyIFSCNumber}

##### Request 2 (  Given a bank name and city, gets details of all branches of the bank in the city problem)
 - {"type":2,"bankname":anyBranchName,"city":anyCity}
 

##### The server is made by using Flask Framework of Python Programming language

### Outputs : 

![case1](https://github.com/Rohitpa7824/BankServerTask/blob/master/demo1.PNG)
![case2](https://github.com/Rohitpa7824/BankServerTask/blob/master/demo2.PNG)
![case3](https://github.com/Rohitpa7824/BankServerTask/blob/master/demo3.PNG)
![case4](https://github.com/Rohitpa7824/BankServerTask/blob/master/demo4.PNG)
![case5](https://github.com/Rohitpa7824/BankServerTask/blob/master/demo5.PNG)

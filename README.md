# Entry-Management-Software
Here I have created an entry management system using Python for programming and Mysql for the purpose of database management.

## Software Used  
1-> Pycharm Community Edition  For IDE  
2-> Mysql -8.0.13 - For Database  

## API used  
1-> smtplib & email - For sending mail  
2-> mysql.connector - For connecting Database  
3-> Twilio API - For sending SMS  
  
## Database Management & Schemas   
For the purpose of database, we make use of 3 tables namely host, visitor and visit.

1-> Host table contains three columns
		a) Name: Contains name of the host.
		b) Mobile: Contains mobile number of host.
		c) Mail: Contains mail-id of the host.

In this table mobile number of the host is taken as primary key.

2-> Visitor table contains three columns
		a) Name: Contains name of the visitor.
		b) Mobile: Contains mobile number of visitor.
		c) Mail: Contains mail-id of the visitor.

In this table mobile number of the visitor is taken as primary key.

3-> Visit table contains four columns
		a) vphone: Contains mobile number of the visitor.
		b) hphone: Contains mobile number of the host.
		c) Intime: Contains in-time of the visitor.
		d) Outtime: Contains out-time of the visitor.
		
In this table a tuple of (Visitor's Mob. No, Host's Mob. No, In-time) is taken as the primary key.

Here, in this table, Visitor's Mob No is taken as a foreign key which is referencing Visitor Table and Host's Mob No is also a foreign key which is referencing Host table.  
  
# Actual Working of the Application  
1-> When we run the the scratch.py file a window will pop-up consisting of two forms. First form is to be filled by the visitor to enter the information during the check in time. 
  
2-> This information is then sent to the *entry* function from where the database is updated using the information such as visitor's name, host name,
visitor's phone number, in-time etc using mysql.connector and sql queries.

3-> Here, we are storing the information of visitors and host if they are not already stored in the database. If they are already stored in the database we do not need to make any new entry and just gather the information of both visitor as well as host from Visitor and Host table respectively. 

4-> We will also check whether the visitor already checked out or not from the previous visit. We are updating visit table by making a new entry using visitor's mobile number, host's mobile number and the time of visiting in the Intime column and setting Outtime column to be 'Null'.

5-> Also inside the function *entry*, *emailh* function is called. In the function emailh (host's email, visitor's email, visitor's name and visitor's phone no) is passed as parameter. The main purpose of this emailhost function is to send the details of the visitor to the host via email
  
6-> Now after the entry function is completely executed, *hmessage* function is called. In the function hsms (visitor's email, visitor's name , visitor's phone no, host's name and visitor's in-time) is passed as parameters. The function *hmessage* is used to send sms to the host about the information of the visitor via text message over the mobile phone.  
In this function , Twilio API is used to send message to the host.  
  
Till here, we have handled the entry of the visitor. 

7-> Now if a visitor wants to check-out. To do this user has to fill the check-out form at the execution of the program. There visitor has to fill the mobile number which he entered during the time of check in. 
  
8-> This number is then sent to the *exit1* function as a parameter. We then check our visit table whether this number is present in the database or not and if this particular has already checked-out.

9-> If this person has not checked-ot already then we will update the Outtime column of the Visit table with the current time.
We will use the host's mobile number from this entry to gather all the information like host's mail id, visitor's mail id, visitor's phone number and host's name, in-time and out-time of the visitor.

10-> After this we will call *emailv* function with (host's mail id, visitor's mail id, visitor's phone number and host's name, in-time and out-time of the visitor) as parameters. This function is used to send an email to the visitor regarding his visit via email.

11->  Also, in the emailv function we are calling *vmessage* function. This function is used to send sms to the visitor about the information regarding his/her last visit like in-time, out-time, host's name, host's mail id etc.

# Demonstration of the use of the Application  
  
  
1-> After running our scratch.py file, a window will open consisting of two forms for both check-in as well as check-out option. 
![enter image description here](https://lh3.googleusercontent.com/fc4WPhF8ywUljA9lC2d1j2mUOm9LRUQzbmKaajKfRb6YWx-zW55II9O8HsWFnN0O1eFnYM2qxXYz)

2-> First entering the visitor's name, visitor's email, and visitor's mobile number, Host's name, Host's email id and Host's mobile number.  
![enter image description here](https://lh3.googleusercontent.com/bKr247WV2_ea23I0g6ZPB24NMM6YzpIV7FH-o_4rQDskcxNFyLrMk76BLe52nRt3qz_Ko-5Tv3hb)

  
3-> After filing details click on check-in button.  
  
4-> The host will recieve an email with the subject Visitor's detail.    
  ![enter image description here](https://lh3.googleusercontent.com/Q7mpryn6jsC3wILrAq-KP9PoyygR1uA1Cz6dHDDBvSsA_JpTok_2kieBU-FLm2DY9P4oYFllXG9N)

5-> Also the sms will be sent to the host's mobile no giving the details of the visitor.

6-> Now the user has successfully checked-in.
  
10-> Entering visitor's mobile number during check-out. 
![enter image description here](https://lh3.googleusercontent.com/in52hhJ_w1kVju_wI6q8tWD8BPwe3XDDKiISwv1U9s1fZX1Mmpm-MBsdIPdY0HcDtLgOZA-jnwqY)
  
10- And now finally, the visitor will recieve a message and an email as shown.  
![enter image description here](https://lh3.googleusercontent.com/7vXSvbqKHRBI-ZTEyL4OaogcRSevWpoAm1dgDb8HGv5AUSyZFu0piMu2nliB0xvq1PesHnZ95jVU)

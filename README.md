# Entry-Management-Software
I have created an entry management system using Python for programming and Mysql for the purpose of database management.

## Software Used  
1. Pycharm Community Edition  For IDE  
2. Mysql -8.0.13 - For Database  

## API used  
1. smtplib & email - For sending mail  
2. mysql.connector - For connecting Database  
3. Twilio API - For sending SMS  
  
## Database Management & Schemas   
For the purpose of database, we make use of 3 tables namely host, visitor and visit.

1. Host table contains three columns
		a) Name: Contains name of the host.
		b) Mobile: Contains mobile number of host.
		c) Mail: Contains mail-id of the host.

In this table mobile number of the host is taken as primary key.

2. Visitor table contains three columns
		a) Name: Contains name of the visitor.
		b) Mobile: Contains mobile number of visitor.
		c) Mail: Contains mail-id of the visitor.

In this table mobile number of the visitor is taken as primary key.

3. Visit table contains four columns
		a) vphone: Contains mobile number of the visitor.
		b) hphone: Contains mobile number of the host.
		c) Intime: Contains in-time of the visitor.
		d) Outtime: Contains out-time of the visitor.
		
In this table a tuple of (Visitor's Mob. No, Host's Mob. No, In-time) is taken as the primary key.

Here, in this table, Visitor's Mob No is taken as a foreign key which is referencing Visitor Table and Host's Mob No is also a foreign key which is referencing Host table.  
  
# Actual Working of the Application  
1. When we run the the scratch.py file a window will pop-up consisting of two forms. First form is to be filled by the visitor to enter the information during the check in time. 
  
2. This information is then sent to the *entry* function from where the database is updated using the information such as visitor's name, host name,
visitor's phone number, in-time etc using mysql.connector and sql queries.

3. Here, we are storing the information of visitors and host if they are not already stored in the database. If they are already stored in the database we do not need to make any new entry and just gather the information of both visitor as well as host from Visitor and Host table respectively. 

4. We will also check whether the visitor already checked out or not from the previous visit. We are updating visit table by making a new entry using visitor's mobile number, host's mobile number and the time of visiting in the Intime column and setting Outtime column to be 'Null'.

5. Also inside the function *entry*, *emailh* function is called. In the function emailh (host's email, visitor's email, visitor's name and visitor's phone no) is passed as parameter. The main purpose of this emailhost function is to send the details of the visitor to the host via email
  
6. Now after the entry function is completely executed, *hmessage* function is called. In the function hsms (visitor's email, visitor's name , visitor's phone no, host's name and visitor's in-time) is passed as parameters. The function *hmessage* is used to send sms to the host about the information of the visitor via text message over the mobile phone.  
In this function , Twilio API is used to send message to the host.  
  
Till here, we have handled the entry of the visitor. 

7. Now if a visitor wants to check-out. To do this user has to fill the check-out form at the execution of the program. There visitor has to fill the mobile number which he entered during the time of check in. 
  
8. This number is then sent to the *exit1* function as a parameter. We then check our visit table whether this number is present in the database or not and if this particular has already checked-out.

9. If this person has not checked-ot already then we will update the Outtime column of the Visit table with the current time.
We will use the host's mobile number from this entry to gather all the information like host's mail id, visitor's mail id, visitor's phone number and host's name, in-time and out-time of the visitor.

10. After this we will call *emailv* function with (host's mail id, visitor's mail id, visitor's phone number and host's name, in-time and out-time of the visitor) as parameters. This function is used to send an email to the visitor regarding his visit via email.

11.  Also, in the emailv function we are calling *vmessage* function. This function is used to send sms to the visitor about the information regarding his/her last visit like in-time, out-time, host's name, host's mail id etc.


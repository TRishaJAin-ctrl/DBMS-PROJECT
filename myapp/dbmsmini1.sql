drop database vehicle_renting;
create database vehicle_renting;

\c vehicle_renting

CREATE TABLE 	Office
 (	Branch_ID Varchar(5) NOT NULL,
 	Office_Name Varchar NOT NULL,
 	Office_Addr Varchar NOT NULL,
 	UNIQUE (Office_Addr),
 	PRIMARY KEY (Branch_ID)
 );

CREATE TABLE 	Employee
 (	E_ID Varchar(5) NOT NULL,
 	Branch_ID Varchar(5) NOT NULL,
 	E_FName Varchar NOT NULL,
 	E_LName Varchar NOT NULL,
 	E_DOB date NOT NULL,
 	E_Addr Varchar,
 	E_PhNo char(10) NOT NULL,
 	UNIQUE (E_PhNo),
 	PRIMARY KEY (E_ID),
	FOREIGN KEY (Branch_ID) REFERENCES Office(Branch_ID)  
 );
 
 CREATE TABLE 	Customer
 (	C_ID Varchar(5) NOT NULL,
 	E_ID Varchar(5),
 	C_FName Varchar NOT NULL,
 	C_LName Varchar NOT NULL,
 	C_DOB date,
 	C_Addr Varchar,
 	C_EmailID Varchar, 
 	C_PhNo char(10) NOT NULL,
 	C_License Varchar(16),
 	UNIQUE (C_PhNo),
 	PRIMARY KEY (C_ID),
	FOREIGN KEY (E_ID) REFERENCES Employee(E_ID)
 );
 
 CREATE TABLE 	Driver
 (	D_ID Varchar(5) NOT NULL,
 	C_ID Varchar(5),
 	E_ID Varchar(5),
 	D_FName Varchar NOT NULL,
 	D_LName Varchar NOT NULL,
 	D_DOB date,
 	D_Addr Varchar,
 	D_PhNo char(10) NOT NULL,
 	D_Payment decimal,
 	D_License Varchar(16) NOT NULL,
 	UNIQUE (D_PhNo),
 	PRIMARY KEY (D_ID),
	FOREIGN KEY (E_ID) REFERENCES Employee(E_ID),
	FOREIGN KEY (C_ID) REFERENCES Customer(C_ID)
 );
 
 CREATE TABLE 	V_Owner
 (	O_ID Varchar(5) NOT NULL,
 	E_ID Varchar(5),
 	O_FName Varchar NOT NULL,
 	O_LName Varchar NOT NULL,
 	O_DOB date,
 	O_Addr Varchar,
 	O_EmailID Varchar, 
 	O_PhNo char(10) NOT NULL,
 	O_Payment decimal,
 	UNIQUE (O_PhNo),
 	PRIMARY KEY (O_ID),
	FOREIGN KEY (E_ID) REFERENCES Employee(E_ID)
 );
 
 CREATE TABLE 	Vehicle
 (	V_Number Varchar(13) NOT NULL,
 	O_ID Varchar(5) NOT NULL,
 	C_ID Varchar(5),
 	Vehicle_Type Varchar NOT NULL, 
 	Model_Type Varchar NOT NULL,
 	Company_Name Varchar NOT NULL,
 	Mileage decimal,
 	Color Varchar,
 	Rental_Price decimal NOT NULL,
 	Available_from TIMESTAMP,
 	Available_till TIMESTAMP,
 	R_from TIMESTAMP,
 	R_till TIMESTAMP,
 	R_ID Varchar(5),
 	PRIMARY KEY (V_Number),
	FOREIGN KEY (O_ID) REFERENCES V_Owner(O_ID),
	FOREIGN KEY (C_ID) REFERENCES Customer(C_ID)
 );
 
 CREATE TABLE 	Office_PhNo
 (	
 	Branch_ID Varchar(5) NOT NULL,
 	Branch_PhNo char(11) NOT NULL,
 	PRIMARY KEY (Branch_ID, Branch_PhNo),
 	UNIQUE (Branch_PhNo),
	FOREIGN KEY (Branch_ID) REFERENCES Office(Branch_ID)
 );
 
 CREATE TABLE 	Payment
 (	
 	Payment_ID Varchar(5) NOT NULL,
 	C_ID Varchar(5) NOT NULL,
 	Payment_Method Varchar,
 	Payment_Date date,
 	Advance decimal NOT NULL,
 	Balance decimal NOT NULL,
 	PRIMARY KEY (Payment_ID, C_ID),
	FOREIGN KEY (C_ID) REFERENCES Customer(C_ID)
 );
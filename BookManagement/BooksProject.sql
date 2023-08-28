use master 

create database BookManagement

create table Books
(
ID int primary key identity (1,1),
Name varchar (40) not null,
Author varchar (40) not null,
Year_Published int not null,
Type int not null,
)


create table Customers
(
ID int primary key identity(1,1),
Name varchar (40) not null,
City varchar (40) not null,
Age int not null,
)

create table Loans 
(
CustID int foreign key references Customers(ID) not null,
BookID int foreign key references Books(ID) not null,
Loandate date not null, 
Returndate date, 
)


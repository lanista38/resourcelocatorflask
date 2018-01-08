-- This file contains the definitions of the tables used in the application.
--

create table Resource(Rid serial primary key, Rname varchar(20), Cid integer references Category(Cid), Sid integer references Person(Pid), Rprice double, Rqty integer, Rregion varchar(20));

create table Supplier(Pid serial primary key, company varchar(150));

create table Customer(Pid serial primary key, city varchar(20), region varchar(20)

create table Category(Cid serial primary key, Cname varchar(20));

create table Admin(Aid serial primary key, Aname varchar(20), AlastName varchar(20), user varchar(20), password varchar(150), email varchar(20));

create table Person(Pid serial primary key, name varchar(20), lastName varchar(20), gpsx double, gpsy double, address varchar(120), region varchar(20));

create table ResourceRequest(Rid integer references Resource(Rid), RPid integer references Rperson(RPid),
  Rdate varchar(10), primary key(Rid, RPid));

-- Relationships
create table ResourceRequest(Pid serial primary key, Rid serial primary key, RRqty integer, RRDate date);
create table Reserve(Pid serial primary key, Rid serial primary key, RDate date, Rqty integer);
create table Announcement(Pid serial primary key, Rid serial primary key, ADate date, APqty integer);
create table Purchase(Pid serial primary key, Rid serial primary key, Pdate varchar(20), Pprice varchar(20), Pqty integer);
create table isSubCategory(Cid serial primary key, Cname varchar(20));

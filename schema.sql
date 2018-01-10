-- This file contains the definitions of the tables used in the application.
--

create table Resource(Rid serial primary key, Rname varchar(20), Cid integer references Category(Cid), Sid integer references Person(Pid), Rprice double, Rqty integer, Rregion varchar(20));

create table Supplier(Sid serial primary key, company varchar(150));

create table Customer(Cuid serial primary key, city varchar(20), region varchar(20)

create table Category(Cid serial primary key, Cname varchar(20));

create table Admin(Aid serial primary key, Aname varchar(20), AlastName varchar(20), user varchar(20), password varchar(150), email varchar(20));

create table Person(Pid serial primary key, name varchar(20), lastName varchar(20), gpsx double, gpsy double, address varchar(120), region varchar(20));

create table ResourceRequest(Rid integer references Resource(Rid), Cuid integer references Customer(Cuid),
  Rdate varchar(10), primary key(Rid, Cuid));

-- Relationships
create table ResourceRequest(Cuid serial primary key references Customer(Cuid), Rid serial primary key references Resource(Rid), RRqty integer, RRDate date);
create table Reserve(Cuid serial primary key references Customer(Cuid), Rid serial primary key references Resource(Rid), RDate date, Rqty integer);
create table Announcement(Sid serial primary key references Supplier(Sid), Rid serial primary key references Resource(Rid), ADate date, APqty integer);
create table Purchase(Pid primary key, Cuid serial  references Customer(Cuid), Rid serial references Resource(Rid), Pdate varchar(20), Pprice varchar(20), Pqty integer);
create table isSubCategory(Cid serial primary key, Cname varchar(20));

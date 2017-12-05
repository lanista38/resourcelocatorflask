-- This file contains the definitions of the tables used in the application.
--
-- Resource table
create table Resource(Rid serial primary key, Rname varchar(20), RlastName varchar(20),
  Rprice double, Rqty int, Rregion varchar(10), Sid integer references Supplier(sid));

-- Supplier table
create table Supplier(Sid serial primary key, Sname varchar(10), SlastName varchar(20),
  Sgpsx double, Sgpsy double, Saddress varchar(20));



create table Rperson(RPid serial primary key, RPname varchar(20), RPlastName varchar(20),
  RPcity varchar(20), RPgpsx double, RPgpsy double, RPaddress varchar(20), RPregion varchar(20));

create table ResourceRequest(Rid integer references Resource(Rid), RPid integer references Rperson(RPid),
  Rdate varchar(10), primary key(Rid, RPid));

create table Purchase(Pdate varchar(10));

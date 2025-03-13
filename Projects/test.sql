create schema Museum2;

create table Painter (ptr_id int not null,
ptr_fname varchar(25) not null,
ptr_dob date,
ptr_gender enum('M', 'F'),
Primary Key(ptr_id)
);

create table Customer (cust_id int not null,
cust_fname varchar(25) not null,
cust_lname varchar(25) not null, 
cust_num int,
cust_dob date,
cust_gender enum('M', 'F'),
primary key(cust_id)
);

create table Gallery (gall_id int not null,
gall_name varchar(25) not null,
gall_location varchar(45) not null,
primary key(gall_id)
);

create table Painting (ptng_id int not null,
ptng_title varchar(25),
ptng_price decimal(10,2),
gall_id int,
cust_id int,
ptr_id int,
foreign key (gall_id) references Gallery(gall_id),
foreign key (cust_id) references Customer(cust_id),
foreign key (ptr_id) references Painter(ptr_id),
primary key(ptng_id)
);

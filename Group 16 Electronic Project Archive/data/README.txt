Tables in the Azure SQL databse (Transact-SQL):
"""
TABLE [User] (
	id INT PRIMARY KEY Identity(1,1),
	username VARCHAR(64),
	first_name VARCHAR(64),
	last_name VARCHAR(64),
	password_hash VARCHAR(128),
	latitude DECIMAL(10,8),
	longitude DECIMAL(11,8)
)

TABLE [Friendship] (
	first_id INT,
	second_id INT
)	

TABLE [Post] (
	id INT PRIMARY KEY Identity(1,1),
	user_id INT,
	group_id INT,
	title VARCHAR(64),
	body TEXT,
	time DATETIME,
	latitude DECIMAL(10,8),
	longitude DECIMAL(11,8)
)

TABLE [Message] (
	id INT PRIMARY KEY Identity(1,1),
	from_id INT,
	to_id INT,
	body TEXT,
	time DATETIME
)

TABLE [Group] (
	id INT PRIMARY KEY Identity(1,1),
	owner INT,
	name VARCHAR(32),
	private BIT,
	latitude DECIMAL(10,8),
	longitude DECIMAL(11,8)
)

TABLE [Comment] (
	id INT PRIMARY KEY Identity(1,1),
	user_id INT,
	post_id INT,
	time DATETIME,
	body TEXT
)

TABLE [Event] (
	id INT PRIMARY KEY Identity(1,1),
	owner INT,
	title VARCHAR(64),
	latitude DECIMAL(10,8),
	longitude DECIMAL(11,8),
	time DATETIME
)

TABLE [Attendee] (
	id INT PRIMARY KEY Identity(1,1),
	event_id INT,
	user_id INT
)
"""
        
 
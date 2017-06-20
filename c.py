import sqlite3

def create_table():
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS mytable (counter INTEGER)")
	c=retrieve()
	# cur.execute("DELETE FROM mytable")
	conn.commit()
	conn.close()

def insert(counter):
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO mytable VALUES(?)",(counter,))
	conn.commit()
	conn.close()

def update(counter):
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute("UPDATE mytable SET counter=(?)",(counter,))
	conn.commit()
	conn.close()

def retrieve():
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM mytable")
	counter = cur.fetchall()
	conn.close()
	return counter


# def main():
# 	create_table()
# 	if(retrieve() == []):
# 		insert(0)
# 	c=retrieve()
# 	x= c[0][0]
# 	x += 1
# 	update(x)
# 	print x
# 	# filename="abc"+str(x)+".txt"
# 	# f= open(filename,"w")
# 	# f.close()

# 	import os.path
# 	save_path = 'example/'
# 	filename="abc"+str(x)+".txt"
# 	completeName = os.path.join(save_path, filename)         
# 	f = open(completeName, "w")
# 	f.close()

# if __name__ == "__main__":
# 	main()
	

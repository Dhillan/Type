import MySQLdb
# open a connection to the server
db = MySQLdb.connect("127.0.0.1","root1","pudding123","userfiles")
cursor = db.cursor()
sql = """CREATE TABLE User_credentials (
         UserID int NOT NULL AUTO_INCREMENT,
         Username char(255),
         Password char(255),
         PRIMARY KEY(UserID)
         )"""
cursor.execute(sql)

import MySQLdb
# open a connection to the server
db = MySQLdb.connect("127.0.0.1","root1","pudding123","userfiles")
cursor = db.cursor()
sql = """CREATE TABLE User_scores (
         UserName Char(20),
         Difficulty int,
         Accuracy int,
         WordsPerMinute int,
         Total_Score int
         )"""
cursor.execute(sql)

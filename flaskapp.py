from flask import Flask, request
import psycopg2
from flask import render_template


app = Flask("Job Site")
items = ["python", "perl", "Ruby", "CPP", "Java"]

dbconn = psycopg2.connect("dbname=naukri")
	

@app.route("/")
def index():
	cursor = dbconn.cursor()
	cursor.execute("select count(*) from openings")
	njobs = cursor.fetchall()[0][0]
	return render_template("main.html", njobs=njobs)
	
@app.route("/jobs")

def jobs():
	
	cursor = dbconn.cursor()
	cursor.execute("select title, company_name, jd_text from openings")
	ret = []
	
	
	for title, company_name, jd in cursor.fetchall():
		item = f"<h3><li> {title} </h3></b> <i><u>{company_name}</u></i> <br/> {jd}</li>"
		ret.append(item)
	jobs = "".join(ret)
	
	return f"""<html>
	<head>
	<title> Welcome to the Jobs page </title>
	</head>
	<body>
	<h2> This is where I store my jobs </h2>
	<br>
	<ol>  {jobs}  </ol>
	</br>
	</body>
	</html>"""
	
		
	
# http://127.0.0.1:5000/add?item="your argument"	
@app.route("/add")
def add_item():
	item = request.args.get("item")
	items.append(item)
	return f"No. of items is now {len(items)}"
	
if __name__ == "__main__":
	app.run(debug = True)

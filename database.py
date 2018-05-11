import csv, records

f = open('running_times.csv', encoding = "ISO-8859-1")
csv_f = csv.reader(f)

db = records.Database('sqlite:///movie_data.db')

db.query('DROP TABLE IF EXISTS movies')
db.query('CREATE TABLE movies (title text, year text, votes text, rank text)')

rows = 0
for row in csv_f:
    print(row)
    if rows == 0:
        rows += 1
    else:
        title = row[0]
        year = row[1]
        votes = row[2]
        rank = row[3]

        db.query('INSERT INTO movies values(:title, :year, :votes, :rank)', title=title, year=year, votes=votes, rank=rank)
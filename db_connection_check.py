from fixture.orm import ORMFixture


db = ORMFixture(host="127.0.0.1", name="bugtracker", user="root", password="")

try:
    l = db.get_projects_list()
    print(type(len(l)))
    for item in l:
        print(item)
    print(len(l))
finally:
    # connection.close()
    pass

from Classes.database_access import DB_Connect

my_db = DB_Connect('root', '', 'python_projects')

# my_db.executeQuery("INSERT INTO course_info (course_discipline, course_number, course_title) VALUES ('IT', '650', 'Software Principles')")

#my_db.executeQuery("UPDATE course_info SET letter_grade='A-', course_gpa='3.7' WHERE course_id ='2'")

#my_db.conn.commit()

my_result = my_db.executeSelectQuery("SELECT * FROM course_info")

print(my_result)
for record in my_result:
    print(record["course_id"])
    print(record["course_discipline"])
    print(record["course_number"])

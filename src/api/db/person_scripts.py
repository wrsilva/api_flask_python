# Person

PERSON_INSERT = "INSERT INTO person \
                  (`age`, `first_name`, `last_name`)\
                        VALUES (%s,%s, %s);"

PERSON_HISTORY = "SELECT id_person ,age ,first_name ,last_name FROM db_estudo.person;"

PERSON_DELETE = "DELETE FROM db_estudo.person WHERE id_person = %s;"

# Person

PERSON_INSERT = "INSERT INTO person \
                  (`age`, `fist_name`, `last_name`)\
                        VALUES (%s,%s, %s);"

PERSON_HISTORY = "SELECT * FROM db_estudo.person"

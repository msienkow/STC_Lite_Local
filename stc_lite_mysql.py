# Copyright 2023 Sani-Matic Inc. (sanimatic.com)

from dataclasses import dataclass
import mysql.connector
from stc_logging import SaniTrendLogging

mysql_log = SaniTrendLogging('mysql_errors')


# SaniTrend® Lite Data Table Layout for Grafana
table_layout = 'id INT UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT, '
table_layout += 'time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, '
table_layout += 'Analog_In_1 FLOAT NOT NULL, '
table_layout += 'Analog_In_2 FLOAT NOT NULL, '
table_layout += 'Analog_In_3 FLOAT NOT NULL, '
table_layout += 'Analog_In_4 FLOAT NOT NULL, '
table_layout += 'Analog_In_5 FLOAT NOT NULL, '
table_layout += 'Analog_In_6 FLOAT NOT NULL, '
table_layout += 'Analog_In_7 FLOAT NOT NULL, '
table_layout += 'Analog_In_8 FLOAT NOT NULL, '
table_layout += 'Digital_In_1 TINYINT NOT NULL, '
table_layout += 'Digital_In_2 TINYINT NOT NULL, '
table_layout += 'Digital_In_3 TINYINT NOT NULL, '
table_layout += 'Digital_In_4 TINYINT NOT NULL, '
table_layout += 'Digital_In_5 TINYINT NOT NULL, '
table_layout += 'Digital_In_6 TINYINT NOT NULL, '
table_layout += 'Digital_In_7 TINYINT NOT NULL, '
table_layout += 'Digital_In_8 TINYINT NOT NULL, '
table_layout += 'Digital_In_9 TINYINT NOT NULL, '
table_layout += 'Digital_In_10 TINYINT NOT NULL, '
table_layout += 'Digital_In_11 TINYINT NOT NULL, '
table_layout += 'Digital_In_12 TINYINT NOT NULL'


def does_mysql_database_exist(
    host: str, 
    user: str, 
    password: str, 
    database: str,
) -> bool:
    """Connects to mysql server and checks if given database exists.

    Args:
        host (str): mysql server host address / hostname
        user (str): mysql server user name
        password (str): mysql server password
        database (str): database to check

    Returns:
        bool: Returns True if database exists. 
        Returns False if database does not exist or upon failure.
    """
    try:
        mysqldb = mysql.connector.connect(
            host = host, user = user, 
            password = password
        )
        
        cursor = mysqldb.cursor()
        cursor.execute('SHOW DATABASES')
        for x in cursor:
            db_name = x[0]
            if db_name == database:
                cursor.reset()
                cursor.close()
                return True

        cursor.reset()
        cursor.close()
        return False

    except Exception as e:
        mysql_log.logger.error(repr(e))
        return False


def create_mysql_database(
    host: str, 
    user: str, 
    password: str, 
    database: str,
) -> int:
    """Creates new database on mysql server.

    Args:
        host (str): mysql server host address / hostname
        user (str): mysql server user name
        password (str): mysql server password
        database (str): database to check

    Returns:
        int: 0 if database created successfully, else 1 for error.
    """
    try:
        mysqldb = mysql.connector.connect(
            host = host,
            user = user,
            password = password
        )
        
        cursor = mysqldb.cursor()
        cursor.execute(f'CREATE DATABASE {database}')
        cursor.reset()
        cursor.close()
        return 0

    except Exception as e:
        mysql_log.logger.error(repr(e))
        return 1


def does_mysql_table_exists(
    host: str, 
    user: str, 
    password: str, 
    database: str, 
    table: str,
) -> bool:
    """Checks if table exists in give database.

    Args:
        host (str): mysql server host address / hostname
        user (str): mysql server user name
        password (str): mysql server password
        database (str): database schema to use
        table (str): table to check

    Returns:
        bool: Returns True if table exists, otherwise False
    """
    try:
        mysqldb = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        
        cursor = mysqldb.cursor()
        cursor.execute('SHOW TABLES')
        for x in cursor:
            table_name = x[0]
            if table_name == table:
                cursor.reset()
                cursor.close()
                return True
        
        cursor.reset()
        cursor.close()
        return False

    except Exception as e:
        mysql_log.logger.error(repr(e))
        return False


def create_mysql_table(
    host: str, 
    user: str, 
    password: str, 
    database: str, 
    table: str, 
    params: str,
) -> int:
    """Creates new table on mysql database.

    Args:
        host (str): mysql server host address / hostname
        user (str): mysql server user name
        password (str): mysql server password
        database (str): database schema to use
        table (str): table to create
        params (str): parameters for table

    Returns:
        int: 0 if table created successfully, else 1 for error.
    """
    try:
        sql_commmand = f'CREATE TABLE {table} ({params})'
        mysqldb = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        
        cursor = mysqldb.cursor()
        cursor.execute(sql_commmand)
        cursor.reset()
        cursor.close()
        return 0

    except Exception as e:
        mysql_log.logger.error(repr(e))
        return 1


def does_mysql_user_exist(
    host: str, 
    user: str, 
    password: str, 
    username: str,
) -> bool:
    """Checks mysql server to see if given username exists.

    Args:
        host (str): mysql server host address / hostname
        user (str): mysql server user name
        password (str): mysql server password
        username (str): username being checked

    Returns:
        bool: Returns True if username exists on mysql server, 
        else returns false
    """
    try:
        mysqldb = mysql.connector.connect(
            host = host,
            user = user,
            password = password
        )
        
        cursor = mysqldb.cursor()
        cursor.execute(f'select user from mysql.user where user = {username}')
        exists = True if len(cursor) > 0 else  False
        cursor.reset()
        cursor.close()
        return exists

    except Exception as e:
        mysql_log.logger.error(repr(e))
        return False


def create_mysql_user(
    host: str, 
    user: str, 
    password: str, 
    new_user: str, 
    new_pass: str, 
    permissions: str = 'SELECT', 
    database: str = '*.*',
) -> int:
    """Create new mysql user with permissions

    Args:
        host (str): mysql server host address / hostname
        user (str): mysql server user name
        password (str): mysql server password
        new_user (str): username for new user
        new_pass (str): password for new user
        permissions (str): permissions for new user separated by 
        commas (ex: SELECT, UPDATE, etc...)
        database (str): data base for permissions to apply

    Returns:
        int: returns 0 if successful, else returns 1
    """
    try:
        mysqldb = mysql.connector.connect(
            host = host,
            user = user,
            password = password
        )
        
        cursor = mysqldb.cursor()
        sql = f'CREATE USER "{new_user}"@"%" IDENTIFIED BY "{new_pass}"'
        cursor.execute(sql)
        if len(permissions) > 0:
            sql = f'GRANT {permissions} ON {database}.* TO "{new_user}"@"%"'
            cursor.execute(sql)
        cursor.reset()
        cursor.close()
        return 0

    except Exception as e:
        mysql_log.logger.error(repr(e))
        return 1


def add_mysql_data(
    host: str, 
    user: str, 
    password: str,
    database: str,
    table: str, 
    
) -> int:


@dataclass
class MySqlGrafanaDB:
    mysql_host: str = ''
    mysql_user: str = ''
    mysql_password: str = ''
    mysql_db_name: str = 'sanitrend'
    mysql_db_exists: bool = False
    mysql_table_exists: bool = False
    mysql_grafana_user: str = 'grafana'
    mysql_grafana_user_exists: bool = False
    
    def __post_init__(self):
        try:
            if does_mysql_database_exist(
                self.mysql_host, 
                self.mysql_user, 
                self.mysql_password, 
                self.mysql_db_name
            ):
                self.mysql_db_exists = True
            else:
                create_db_result = create_mysql_database(
                    self.mysql_host, 
                    self.mysql_user, 
                    self.mysql_password, 
                    self.mysql_db_name
                )
                if create_db_result == 0:
                    self.mysql_db_exists = True
                else:
                    mysql_log.logger.error('Unable to create mysql database.')
                    self.mysql_db_exists = False

            if self.mysql_db_exists:
                if does_mysql_table_exists(
                    self.mysql_host, 
                    self.mysql_user, 
                    self.mysql_password, 
                    self.mysql_db_name, 
                    self.mysql_db_name
                ):
                    self.mysql_table_exists = True
                else:
                    create_table_result = create_mysql_table(
                        self.mysql_host, 
                        self.mysql_user, 
                        self.mysql_password, 
                        self.mysql_db_name, 
                        self.mysql_db_name, 
                        table_layout
                    )

                    if create_table_result == 0:
                        self.mysql_table_exists = True
                    else:
                        mysql_log.logger.error('Unable to create table.')
                        self.mysql_table_exists = False

                    grafana_user_exists = does_mysql_user_exist(
                        self.mysql_host, 
                        self.mysql_user, 
                        self.mysql_password, 
                        self.mysql_grafana_user
                    )

                    if grafana_user_exists:
                        self.mysql_grafana_user_exists = True
                    else:
                        create_user_result = create_mysql_user(
                        self.mysql_host, 
                        self.mysql_user, 
                        self.mysql_password, 
                        self.mysql_grafana_user, 
                        self.mysql_grafana_user, 'SELECT', 
                        self.mysql_db_name
                    )

                    if create_user_result == 0:
                        self.mysql_grafana_user_exists = True
                    else:
                        mysql_log.logger.error('Unable to create user.')
                        self.mysql_grafana_user_exists = False

        except Exception as e:
            mysql_log.logger.error(repr(e))

            


def main():
    pass
    db = MySqlGrafanaDB('10.10.135.200', 'root', 'root')

if __name__ == '__main__':
    main()
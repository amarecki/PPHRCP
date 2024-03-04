import pyodbc
from datetime import datetime, timedelta


class AeosDB:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        #cur = self.cnxn.cursor()

    def rcpHourReport(self, hour, accessPointIds):
        #print(hour)
        startTime = datetime.strptime(hour, "%Y%m%d%H")
        endTime = startTime + timedelta(hours=1)
        #print(startTime, endTime)

        cur = self.cnxn.cursor()
        sql = ("SELECT "
            "accesspointid "
            ", personnelnr "
            ", timestamp "
            ", intvalue " # chyba kierunek
            ", hostname, accesspointname, entrancename "
            ", lastname, initials "
            "FROM view_eventlog WHERE "
            f"timestamp between \'{startTime.strftime('%Y-%m-%d %H:00:00')}\' and \'{endTime.strftime('%Y-%m-%d %H:00:00')}\' "
            "and eventtype=5 "
            "and carriertype=1 " #pracownik
            f"and accesspointid in ({accessPointIds})" #wybrane przejścia
            )
        print(sql)
        cur.execute(sql)
        return cur

    def rcpHourReport2(self, hour, accessPointIds):
        startTime = datetime.strptime(hour, "%Y%m%d%H")
        endTime = startTime + timedelta(hours=1)
        #print(startTime, endTime)

        cur = self.cnxn.cursor()
        sql = ("SELECT "
            "el.accesspointid "
            ", el.personnelnr "
            ", el.timestamp "
            ", el.intvalue " # chyba kierunek
            ", el.hostname, el.accesspointname, el.entrancename "
            ", el.lastname, el.initials "

            ", business = (select count(*) "
                          "from view_eventlog el2 "
		                  "where el2.accesspointid=305 " #accesspoint RCP
			                    "and el2.personnelnr = el.personnelnr "
			                    "and ABS(DATEDIFF(SECOND, el.timestamp, el2.timestamp)) < 8) " #różnica 6 sekund # powiększona do 8, bo niektórych zdarzeń nie było

            ", bike     = (select count(*) "
                          "from view_eventlog el2 "
		                  "where el2.accesspointid=320 " #accesspoint Rower
			                    "and el2.personnelnr = el.personnelnr "
			                    "and ABS(DATEDIFF(SECOND, el.timestamp, el2.timestamp)) < 8) " #różnica 6 sekund # powiększona do 8, bo niektórych zdarzeń nie było

            "FROM view_eventlog el WHERE "
            f"timestamp between \'{startTime.strftime('%Y-%m-%d %H:00:00')}\' and \'{endTime.strftime('%Y-%m-%d %H:00:00')}\' "
            "and eventtype=5 " #BadgeAccessEvent
            "and carriertype=1 " #pracownik
            f"and accesspointid in ({accessPointIds}) " #wybrane przejścia
            f"order by el.timestamp" # na prośbę Majki
            )
        print(sql)
        cur.execute(sql)
        return cur

    def rcpHourReport3(self, t1, t2, accessPointIds):
        startTime = datetime.strptime(t1, "%Y%m%d%H%M%S")
        endTime = datetime.strptime(t2, "%Y%m%d%H%M%S")
        #print(startTime, endTime)

        cur = self.cnxn.cursor()
        sql = ("SELECT "
            "el.accesspointid "
            ", el.personnelnr "
            ", el.timestamp "
            ", el.intvalue " # chyba kierunek
            ", el.hostname, el.accesspointname, el.entrancename "
            ", el.lastname, el.initials "

            ", business = (select count(*) "
                          "from view_eventlog el2 "
		                  "where el2.accesspointid=1412 " #accesspoint RCP
			                    "and el2.personnelnr = el.personnelnr "
			                    "and ABS(DATEDIFF(SECOND, el.timestamp, el2.timestamp)) < 6) " #różnica 6 sekund

            ", bike     = (select count(*) "
                          "from view_eventlog el2 "
		                  "where el2.accesspointid=1413 " #accesspoint Rower
			                    "and el2.personnelnr = el.personnelnr "
			                    "and ABS(DATEDIFF(SECOND, el.timestamp, el2.timestamp)) < 6) " #różnica 6 sekund

            "FROM view_eventlog el WHERE "
            f"timestamp between \'{startTime.strftime('%Y-%m-%d %H:%M:%S')}\' and \'{endTime.strftime('%Y-%m-%d %H:%M:%S')}\' "
            "and eventtype=5 " #BadgeAccessEvent
            "and carriertype=1 " #pracownik
            f"and accesspointid in ({accessPointIds}) " #wybrane przejścia
            f"order by el.timestamp" # na prośbę Majki
            )
        print(sql)
        cur.execute(sql)
        return cur
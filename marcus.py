# -*- coding: utf-8 -*-

import json
from influxdb import InfluxDBClient
from pprint import pprint

db = InfluxDBClient("localhost", 8086, "root", "root", "gpsdb")

with open("dataraw.json") as f:
  for line in f:
    d=json.loads(line)
    # check class=TPV and mode=3 (mode=2 does not include alt)
    if d["class"]=="TPV" and d["mode"]==3:
      # measurement, time and fields are mandated by influxdb
      json_body = [
        {
          "measurement": d["class"],
          "time": d["time"],
          "fields": {
            "alt": d["alt"],
            "lat": d["lat"],
            "lon": d["lon"],
            "speed": d["speed"]
          }
        }
      ]
      db.write_points(json_body)
      pprint(json_body)

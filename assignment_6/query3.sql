select avg(fare_feb1 -fare_jan18) as broadway_ff_avg_diff
from stations
join (select station, sum(ff) as fare_jan18
      from fares_jan18
      group by station) as j18
    on stations.name = j18.station
join (select station, sum(ff) as fare_feb1
      from fares_feb1
      group by station) as f1
    on j18.station = f1.station
where stations.line = "Broadway";

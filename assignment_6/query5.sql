select stations.name as station_with_largest_decrease
from stations
join (select station, sum(ff) as total18
      from fares_jan18
      group by station) as j18
    on stations.name = j18.station
join (select station, sum(ff) as total1
      from fares_feb1
      group by station) as f1
    on j18.station = f1.station
order by total18-total1 desc
limit 1;
select lat, lng, ff
from stations
join (select station, sum(ff) as ff
      from fares_jan18
      group by station) as jan18
    on jan18.station = stations.name
where stations.line = "Broadway"
order by jan18.ff desc;
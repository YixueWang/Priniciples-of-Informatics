select name, total1-total18 as diff_feb1_jan18
from (select station,sum(ff)as total1
      from fares_feb1
      group by station) as f1
join (select station,sum(ff) as total18
      from fares_jan18
      group by station) as j18
    on j18.station = f1.station 
join stations on stations.name = j18.station
where stations.line = "Broadway";

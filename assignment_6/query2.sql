select rtrim(f1.station) as name
from (select station, sum(ff) as total1
      from fares_feb1
      group by station) as f1 
join (select station, sum(ff) as total18
      from fares_jan18
      group by station) as j18
     on f1.station = j18.station
where total18-total1 > 1000;

select name, total_7d_1-total_7d_18 as diff_7d, total_30d_1-total_30d_18 as diff_30d
from (select station, sum(7d) as total_7d_1, sum(30d) as total_30d_1
     from fares_feb1
     group by station) as f1
join(select station, sum(7d) as total_7d_18, sum(30d) as total_30d_18
     from fares_jan18
     group by station) as j18
    on j18.station = f1.station
join stations on stations.name = j18.station
where stations.line = "Broadway";

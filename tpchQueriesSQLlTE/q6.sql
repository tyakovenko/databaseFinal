select
         sum(l_extendedprice * l_discount) as revenue
 from
         lineitem
 where
         l_shipdate >= date ('1997-01-01')
         and l_shipdate < date ('1997-01-01', '+1 years')
         and l_discount between 0.07 - 0.01 and 0.07 + 0.01
         and l_quantity < 24;

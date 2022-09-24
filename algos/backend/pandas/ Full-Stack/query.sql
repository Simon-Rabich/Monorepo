SELECT   day ,
		camapign_id,
		camapign_name,
		SUM(revenue) as total_revenue,
		SUM(cost) as total_cost,
		SUM(profit) as total_profit,
		SUM(roi) as total_roi,
		AVG(uv) as avg_uv,
		AVG(cpc) as avg_cpc

FROM  (


        SELECT * ,
               uv / cpc as roi


        FROM (

                    SELECT

                    DATE(t.data_date + interval ‘1h’ * 5) as day ,  // TO UTC

                    t.camapign_id,

                    t.campaign_name,

                    revenue,

                    cost,

                    clicks,

                    revenue / clicks as uv,

                    cost / clicks as cpc ,

                    revenue – cost  as profit,

                    FROM cost t

                    JOIN  revenue r

                    On t.campaign_id = r.campaign_id and t.data_date = r.data_date

                    Where DATE(t.data_date + interval ‘1h’ * 5) between ${date_from} and ${date_to}
        )
)

Group by
        day ,
        camapign_id,
        camapign_name
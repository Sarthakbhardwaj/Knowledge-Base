# # FACEBOOK ADS:

# # sampling looks at a portion of data that represents a larger population included in an entire set of data. metrices that count are sampled because it takse a lrage amount of data to caclulate them

# # there are three user access levels:
# # 1) admin 
# # 2) advertiser
# # 3) analyst

# # we need atleast analyst user access to view and access reports 


# # COMMON ISSUES:

# # DATA MISMTAHC/MISSING:
# # 1. mismatch between the user dashboard attribution settings and hevo click_attribution and view_attribution settings.
# # 1.a.) this can laso happen if user runs differnt attribution settings for different ad sets. there will be a mismatch due to different setting ad sets. 

# # 2. comparing different time and aggregation windows in the dashboard and hevo report. 
# # 2.a. discrepancies in aggregation window. user has to mathc their dashboard reporting times and hevo report date times for values to match 
# # 2.b if the user is checking latest numbers in their dashboard and hevo's last ingestion + refresh happened x minutes back (refresher frequnecy is 6 hours by default)

# from optparse import Option


# # 3. there might be a difference in aggregated metric values on aggregation levels as well (ad,ad set, campaign)
# # 3.a. this can happen as FB provides the most accurate info at an ad level. 

# # 4. If ad action report time is incorrectly configured some fields canot be fetched as they have null values. in such cases, users want t a mix of conversion + impression ad action report time i.e. mixed Option

# 5. if source does not have data about a certain field, we cannot replicate it and hence it can be missing , ask user to use graph api explorer

from asyncio import tasks


ASYNC JOB FAILURES:

they are intermittent in nature and genreally fucntions normally in the next iteration, but have al imit of 40,000 recors per poll job, if the user has more data than this, it becomes a recurring error. 

HIGH EVENT INGESTION CAN BE DUE TO: 
 high pipeline frequency 
 refresher tasks

 recommeneded pipeline frequency should be 6 hours

async_job_retry_count: the marketing api provides delevopers the option to request for data in an asynchronous manner, these fail intemrittently and we have set the coutner to 5 retires,  which can be increased as per requirement. 



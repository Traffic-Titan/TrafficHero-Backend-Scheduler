from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import aiohttp
from dotenv import load_dotenv
import os

scheduler = AsyncIOScheduler()

load_dotenv()
basic_url = os.getenv("basic_url")
bazaar_token = os.getenv("token")
headers = {"Authorization": f"Bearer {bazaar_token}"}

# # 排程更新 - 大眾運輸 - 營運狀況
# global count_updateOperationalStatus
# count_updateOperationalStatus = 0

# async def updateOperationalStatus():
#     global count_updateOperationalStatus
#     count_updateOperationalStatus += 1
    
#     print(f"S: 更新大眾運輸 - 營運狀態 - 第{count_updateOperationalStatus}次")
    
#     await OperationalStatus.update()
    
#     print(f"E: 更新大眾運輸 - 營運狀態 - 第{count_updateOperationalStatus}次")

# scheduler.add_job(updateOperationalStatus, 'interval', minutes = 1)

# 排程更新 - 各縣市路邊停車費 - 系統狀態
global count_updateParkingFee_SystemStatus
count_updateParkingFee_SystemStatus = 0

async def updateParkingFee_SystemStatus():
    global count_updateParkingFee_SystemStatus
    count_updateParkingFee_SystemStatus += 1
    
    print(f"S: 更新各縣市路邊停車費 - 系統狀態 - 第{count_updateParkingFee_SystemStatus}次")
    
    async with aiohttp.ClientSession() as session:
        async with session.put(basic_url + "/Website/Home/ParkingFee/SystemStatus", headers=headers) as response:
            print(f"回應狀態: {response.status}")
    
    print(f"E: 更新各縣市路邊停車費 - 系統狀態 - 第{count_updateParkingFee_SystemStatus}次")

scheduler.add_job(updateParkingFee_SystemStatus, 'interval', minutes = 1)

# 排程更新 - 中央氣象署 - 無人氣象測站
global count_updateWeatherStation
count_updateWeatherStation = 0

async def updateWeatherStation():
    global count_updateWeatherStation
    count_updateWeatherStation += 1
    
    print(f"S: 更新中央氣象署 - 無人氣象測站資料 - 第{count_updateWeatherStation}次")
    
    async with aiohttp.ClientSession() as session:
        async with session.put(basic_url + "/Website/Home/Weather/Station", headers=headers) as response:
            print(f"回應狀態: {response.status}")
    
    print(f"E: 更新中央氣象署 - 無人氣象測站資料 - 第{count_updateWeatherStation}次")

scheduler.add_job(updateWeatherStation, 'interval', minutes = 10)

# 排程更新 - 中央氣象署 - 無人氣象測站清單
global count_updateWeatherStationList
count_updateWeatherStationList = 0

async def updateWeatherStationList():
    global count_updateWeatherStationList
    count_updateWeatherStationList += 1
    
    print(f"S: 更新中央氣象署 - 無人氣象測站清單 - 第{count_updateWeatherStationList}次")
    
    async with aiohttp.ClientSession() as session:
        async with session.put(basic_url + "/Website/Home/Weather/StationList", headers=headers) as response:
            print(f"回應狀態: {response.status}")
    
    print(f"E: 更新中央氣象署 - 無人氣象測站清單 - 第{count_updateWeatherStationList}次")

scheduler.add_job(updateWeatherStationList, 'interval', minutes = 1440) # 每天更新一次

# # 排程更新 - 首頁 - 路況速報
# global count_updateRoadCondition
# count_updateRoadCondition = 0

# async def updateRoadCondition():
#     global count_updateRoadCondition
#     count_updateRoadCondition += 1
    
#     print(f"S: 更新CMS路況速報 - 第{count_updateRoadCondition}次")
    
#     await RoadCondition_Freeway.updateRoadCondition_Freeway_CMS_List()
#     await RoadCondition_Freeway.updateRoadCondition_Freeway_CMS_Content()
#     await RoadCondition_Freeway.updateRoadCondition_Freeway()
#     await RoadCondition_ProvincialHighway.updateRoadCondition_ProvincialHighway_CMS_List()
#     await RoadCondition_ProvincialHighway.updateRoadCondition_ProvincialHighway_CMS_Content()
#     await RoadCondition_ProvincialHighway.updateRoadCondition_ProvincialHighway()
#     await RoadCondition_LocalRoad.updateRoadCondition_LocalRoad_CMS_List()
#     await RoadCondition_LocalRoad.updateRoadCondition_LocalRoad_CMS_Content()
#     await RoadCondition_LocalRoad.updateRoadCondition_LocalRoad()
#     await RoadCondition_Main.updateRoadCondition()
    
#     print(f"E: 更新CMS路況速報 - 第{count_updateRoadCondition}次")

# scheduler.add_job(updateRoadCondition, 'interval', minutes = 5) # 每天更新一次

# 排程更新TDX最新消息
# global count_updateNews
# count_updateNews = 0

# async def updateNews():
#     global count_updateNews
#     count_updateNews += 1
    
#     print(f"S: 更新TDX - 最新消息 - 第{count_updateNews}次")
    
#     await News_AlishanForestRailway.updateNews()
#     await News_Bus.updateNews()
#     await News_Freeway.updateNews()
#     await News_IntercityBus.updateNews()
#     await News_LocalRoad.updateNews()
#     await News_MRT.updateNews()
#     await News_ProvincialHighway.updateNews()
#     await News_PublicBicycle.updateNews()
#     await News_TaiwanHighSpeedRail.updateNews()
#     await News_TaiwanRailway.updateNews()
#     await News_TaiwanTouristShuttle.updateNews()
    
#     print(f"E: 更新TDX - 最新消息 - 第{count_updateNews}次")

# # scheduler.add_job(updateNews, 'interval', minutes = 5)

# 排程更新 - 高速公路服務區停車位狀態
# global count_updateServiceArea_ParkingStatus
# count_updateServiceArea_ParkingStatus = 0

# async def updateServiceArea_ParkingStatus():
#     global count_updateServiceArea_ParkingStatus
#     count_updateServiceArea_ParkingStatus += 1
    
#     print(f"S: 更新1968 - 高速公路服務區停車位狀態 - 第{count_updateServiceArea_ParkingStatus}次")
    
#     await ServiceArea.updateParkingStatus()
    
#     print(f"E: 更新1968 - 高速公路服務區停車位狀態 - 第{count_updateServiceArea_ParkingStatus}次")

# # scheduler.add_job(updateServiceArea_ParkingStatus, 'interval', minutes = 10)

# # 排程更新 - 高速公路服務區停車場資料
# global count_updateServiceAreaData
# count_updateServiceAreaData = 0

# async def updateServiceAreaData():
#     global count_updateServiceAreaData
#     count_updateServiceAreaData += 1
    
#     print(f"S: 更新1968 -高速公路服務區停車場資料 - 第{count_updateServiceAreaData}次")
    
#     async with aiohttp.ClientSession() as session:
#         async with session.put(basic_url + "/Website/CMS/ServiceArea/Data", headers=headers) as response:
#             print(f"回應狀態: {response.status}")
    
#     print(f"E: 更新1968 - 高速公路服務區停車場資料 - 第{count_updateServiceAreaData}次")

# # scheduler.add_job(updateServiceAreaData, 'interval', days = 1)
# scheduler.add_job(updateServiceAreaData, 'interval', minutes = 0.1)


# # 排程更新TDX最新消息
# global count_updateTourismData
# count_updateTourismData = 0

# async def updateTourismData():
#     global count_updateTourismData
#     count_updateTourismData += 1
    
#     print(f"S: 更新TDX - 觀光資訊 - 第{count_updateTourismData}次")
    
#     await Activity.update()
#     await Hotel.update()
#     await Parking.update()
#     await Restaurant.update()
#     await ScenicSpot.update()
    
#     print(f"E: 更新TDX - 觀光資訊 - 第{count_updateTourismData}次")

# scheduler.add_job(updateTourismData, 'interval', minutes = 40)




# # 排程更新 - 即時訊息推播訊息 - 推播有效性判斷 # 測試中
# global count_cms_effectiveness
# count_cms_effectiveness = 0

# async def update_CMS_Effectiveness():
#     global count_cms_effectiveness
#     count_cms_effectiveness += 1
    
#     print(f"S: 更新即時訊息推播訊息 - 推播有效性判斷 - 第{count_cms_effectiveness}次")
    
#     for i in ["cms_main_car","cms_main_scooter","cms_sidebar_car","cms_sidebar_scooter"]:
#         collection = await MongoDB.getCollection("traffic_hero",i)
#         # 將所有的document都判斷一次有效性(若訊息已超過目前時間，則將active設定為false)
#         documents = await collection.find({"active": True})
        
#         # 轉換時區(待模組化)
#         import pytz
#         taipei_timezone = pytz.timezone('Asia/Taipei')
#         current_time = datetime.now(taipei_timezone)

#         for document in documents:
#             collection.update_many({'end': {'$lt': current_time}}, {'$set': {'active': False}})
    
#     print(f"E: 更新即時訊息推播訊息 - 推播有效性判斷 - 第{count_cms_effectiveness}次")

# # scheduler.add_job(update_CMS_Effectiveness, 'interval', minutes = 10)


scheduler.start() # 啟動排程
asyncio.get_event_loop().run_forever()
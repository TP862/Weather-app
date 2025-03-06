import python_weather

import asyncio
import os

import json

async def getweather() -> None:
 async with python_weather.Client(unit=python_weather.METRIC) as client:
    weather = await client.get('Tokyo')

    data = {
      "temp" : weather.temperature,
      "pressure" : weather.pressure,
      "humidity" : weather.humidity,
      "region" : weather.region,
      "time" : weather.datetime
    }

    with open("data.json", "w") as json_file:
      json.dump(data, json_file, indent=4)

if __name__ == '__main__':
   if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.run(getweather())
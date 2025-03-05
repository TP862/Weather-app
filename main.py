import python_weather

import asyncio
import os

async def getweather() -> None:
 async with python_weather.Client(unit=python_weather.METRIC) as client:
    weather = await client.get('Stellenbosch')

    print(weather.location)
    print(weather.local_population)

if __name__ == '__main__':
   if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.run(getweather())
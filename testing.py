
# sync example 

import time
import asyncio

# print ("water is boiling")
# time.sleep(4)
# print("water is boiled")

# print("start cooking the meal")
# time.sleep(4)
# print("meal is cooked!")


async def waterboil ():
    print ("water is boiling")
    await asyncio.sleep(7)
    print("water is boiled")




async def mealCook ():
    print("start cooking the meal")
    await asyncio.sleep(4)
    print("meal is cooked!")


async def main():
    await asyncio.gather(   
    waterboil(),
    mealCook()
    )

asyncio.run(main())
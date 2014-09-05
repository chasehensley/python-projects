

import time

yes = ('yes','yeah','mhm','okay','yup','yep')

no = ('nah','no','nope','not really,''not at all')

while True:
    print("Welcome to SkilBux")
    time.sleep(1)
    start = input("Ready to start?").lower().strip()
    if start.startswith(yes):
        rewards = [
            {
                'name': "Regular Attendance",
                'desc': "One regular class (92-120 mins)",
                'min': 40,
                'max': 40,
            },
            {
                'name': "GitHub Green Dot",
                'desc': "Get a green dot from committing something new",
                'min': 10,
                'max': 40,
            }    
        ]

        items = [
            {
                'name': "Tee Shirt (Basic)",
                'desc': "The basic SkilStak logo on a tee shirt (whatever size).",
                'cost': 600
            },
            {
                'name': "Saturday Minecraft Camp",
                'desc': "Regular 2-hour Minecraft camp held Saturdays (usually 3-5)",
                'cost': 400
            },
            {
                'name': "Water Bottle",
                'desc': "One of our regular water bottles with SkilStak logo",
                'cost': 150
            },

        ]
        print("Rewards:")
        time.sleep(0.5)
        for reward in rewards:
            if reward['min'] == reward['max']:
                time.sleep(1)
                print("{name}: {min}".format(**reward))
                print("------------------------------------")
            else:
                time.sleep(1)
                print("{name}: {min}-{max}".format(**reward))
        print("--------------------------------------")
        time.sleep(1)
        print("Items:")
        time.sleep(0.5)
        for item in items:
            time.sleep(1)
            print('''Item: {name}. Description: {desc}.
Cost: {cost}".format(**item))
            print("----------------------------------------")
        time.sleep(5)

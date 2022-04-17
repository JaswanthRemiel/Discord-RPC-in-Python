from pypresence import Presence
import time
start = int(time.time())
client_id = "#yourCLIENTidHere" #enter your client id here 
RPC = Presence(client_id)
RPC.connect()
while True: #infinite loop
    RPC.update(
        large_image = "rebrand-jr", #name of your image in Developer Portal
        large_text = "RV Logo", #Alt Text For Your Logo 
        details = "Chillin' With Code", #Set Details
        state = "Visual Studio Code", #Set State
        start = start,
        buttons = [{"label": "Remiel's Vlog", "url": "https://www.youtube.com/remielvlogsyt"}, {"label": "Discord Server", "url": "https://discord.gg/rgAZT2aCCH"}] #Add Buttons Here
    )
    time.sleep(60)

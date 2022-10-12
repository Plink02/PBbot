# PB-bot
This bot connects to twitch, discord and src to send pace alerts and retrieve PB data. If you would like the bot active in your twitch chat DM Plink#5726 on Discord. 

## Commands

### **!pb (user) (category)**:

  Retrieves the entered user's PB for the specified category. No category specification will default to single segment
  
  The user is searched for on speedrun.com. This means usernames do not have to be exact, but if somebody else has a very similar username to who you want to look up, results may be retrieved. Categories MUST be spelled exactly as they appear on src. ("Glass Joe" is fine. "Joe" is not as src has no search functionality for categories.
  
  Examples: !pb plink Super Macho Man (retrieves macho man IL time)
  
            !pb plink Another World Circuit (retrieves AWC PB time)
            
            !pb plink (retrieves plink's single segment PB)
 
### **!alert (information)**:

  Sends a pace alert with the submitted information. Pinged roles, username and twitch link are automatically filled in based on what chat it is sent from 
  
  Example: !alert -3.58 into Mr. Sandman - if this alert is send from Plink02's chat the alert will look like **"@Pace Alerts Plink02 is -3.58 into Mr. Sandman twitch.tv/plink02"**


**Extra Information:**

I plan on adding more functionality to this bot in the near future. Adding things such as:

  !rank to find the rank of a given player, or the player at a given rank
  
  !wr to automatically retrieve the world record time and player for any given category
  
  A command to send information after a pace alert (If a player got or didn't get a pb) without the ping and twitch url
  
  If you have any other ideas of things you would like me to add let me know! Plink#5726
  
I am currently adding the bot to user's chats upon request myself. Any automated process (such as being active in anybody's chat who follows the bot) has the risk of making commands available to people who may spam pace alerts in servers or spam src api requests, making the bot slow or unresponsive for people who actually want to use it properly. If I can find a way around this, the process may be automated in the future.


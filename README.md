# PB-bot
This bot connects to twitch to discord and src to send pace alerts and retrieve PB data.

## Commands

### **!pb (user) (category)**:

  Retrieves the entered user's PB for the specified category. No category specification will default to single segment
  The user is searched for on speedrun.com. This means usernames do not have to be exact, but if somebody else has a very similar username to who you want to look up, results may be retrieved.
  
  Examples: !pb plink Super Macho Man (retrieves macho man IL time)
            !pb plink Another World Circuit (retrieves AWC PB time)
            !pb plink (retrieves plink's single segment PB)
 
### **!alert (information)**:

  Sends a pace alert with the submitted information. Pinged roles, username and twitch link are automatically filled in based on what chat it is sent from 
  
  Example: !alert -3.58 into Mr. Sandman - if this alert is send from Plink02's chat the alert will look like **"@Pace Alerts Plink02 is -3.58 into Mr. Sandman twitch.tv/plink02"**

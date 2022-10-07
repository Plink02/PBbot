import srcomapi, srcomapi.datatypes as dt
import datetime

api = srcomapi.SpeedrunCom(); api.debug = 1



def findPB(player, categoryName="Single Segment"):
    #search and obtain game
    games = api.search(dt.Game, {"name": "Mike Tyson"})
    game = games[0]

    category = None
    level = None

    #find user, if user not found return sorry message
    try:
        users = api.search(dt.User, {"name": player})
        userId = users[0].id
    except:
        return("Sorry! I couldn't find a PB for that user.")

    #find category/level, if not found, send sorry message
    try:
        for cat in game.categories:
            if cat.name.lower() == categoryName.lower():
                category = cat
        if category == None:
            category = game.categories[1]
            for lev in game.levels:
                if lev.name.lower() == categoryName.lower():
                    level = lev
    except:
        return("Sorry! I couldn't locate that run category.")

    #if level is null find category leaderboard, otherwise find the specific level board
    if level == None:
        leaderboard = dt.Leaderboard(api, data=api.get("leaderboards/{}/category/{}".format(game.id, category.id)))
    else:
        leaderboard = dt.Leaderboard(api, data=api.get("leaderboards/{}/level/{}/{}".format(game.id, level.id, category.id)))
    #local version of leaderboard created to prevent new API calls for each run
    localBoard = leaderboard.data

    for run in localBoard["runs"]:
        if run["run"]["players"][0]["rel"] == "user" and run["run"]["players"][0]["id"] == userId:
           time = run["run"]["times"]["primary_t"]
           time = datetime.timedelta(seconds=time)
           time = str(time)
           time = time[2:10]
           message = player + "'s " + categoryName + " PB is " + time
           return(message)
    #if nothing found, user does not have submitted run in category, return sorry message
    return("Sorry! That player hasn't submitted a PB for that.")

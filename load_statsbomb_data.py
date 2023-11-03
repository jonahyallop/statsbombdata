from statsbombpy import sb

print(sb.competitions())

events = sb.competition_events(
    country="Germany",
    division="1. Bundesliga",
    season="2019/2020"
)

# grouped_events = sb.competition_events(
#     country="Germany",
#     division= "1. Bundesliga",
#     season="2019/2020",
#     split=True
# )
# grouped_events["dribbles"]

print(events)
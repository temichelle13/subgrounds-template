from subgrounds import Subgrounds, SyntheticField
from subgrounds.contrib.plotly import Figure, Scatter

sg = Subgrounds()

lido_activity = sg.load_subgraph(
    "https://api.thegraph.com/subgraphs/name/messari/lido-ethereum"
)

usage_daily_snapshot_30days = lido_activity.Query.usageMetricsDailySnapshots(
    orderBy=lido_activity.UsageMetricsDailySnapshot.timestamp,
    orderDirection="desc",
    first=30,
)

daily_snapshot = lido_activity.UsageMetricsDailySnapshot

daily_snapshot.datetime = SyntheticField.datetime_of_timestamp(daily_snapshot.timestamp)

# Create the Scatter trace with appropriate field paths
trace = Scatter(
    x=usage_daily_snapshot_30days.datetime,
    y=usage_daily_snapshot_30days.dailyActiveUsers,
)

# Create the Figure instance with the trace and display it
fig = Figure(
    subgrounds=sg,
    traces=trace,
    layout=dict(
        title="Daily Active Users vs Datetime",
        xaxis=dict(title="Datetime"),
        yaxis=dict(title="Daily Active Users"),
    ),
)

# Show the figure:
fig.figure.show()

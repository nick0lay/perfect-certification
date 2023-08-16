import httpx
from prefect import flow, task
from prefect.tasks import task_input_hash
from datetime import timedelta
from prefect.blocks.notifications import SlackWebhook

longtitude_range = [-150, 150]
latitude_range = [-90, 91]

# logger = get_run_logger("weather-flow")


def fetch_weather(lat: float, lon: float):
    base_url = "https://api.open-meteo.com/v1/forecast/"
    weather = httpx.get(
        base_url,
        params=dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
    )
    most_recent_temp = float(weather.json()["hourly"]["temperature_2m"][0])
    print(f"Lat: {lat}, Lon: {lon}, Temp: {most_recent_temp}")
    return most_recent_temp


@task(
    name="Fetch Weather Lon",
    cache_key_fn=task_input_hash,
    cache_expiration=timedelta(days=1),
)
def fetch_weather_list_lon(lat: float):
    temps = []
    for lon in range(longtitude_range[0], longtitude_range[1], 5):
        temp = fetch_weather(lat, lon)
        temps.append(temp)

    return temps


@task(
    name="Fetch Weather Lat",
    cache_key_fn=task_input_hash,
    cache_expiration=timedelta(days=1),
)
def fetch_weather_list_lat(lon: float):
    temps = []
    for lat in range(latitude_range[0], latitude_range[1], 5):
        temp = fetch_weather(lat, lon)
        temps.append(temp)

    return temps


@task(name="Save Weather")
def save_weather(temp: [float]):
    delimiter = ";"
    csv = delimiter.join(str(x) for x in temp)
    with open("weather.csv", "w+") as w:
        w.write(csv)
    return "Successfully wrote temp"


@flow(name="Weather Flow", log_prints=True, retries=3, retry_delay_seconds=5)
def pipeline(lat: float = 38.9, lon: float = -77.0):
    temp = fetch_weather(lat, lon)
    temp_lat = fetch_weather_list_lat(lon)
    temp_lon = fetch_weather_list_lon(lat)
    result = save_weather([temp] + temp_lat + temp_lon)
    return result


if __name__ == "__main__":
    pipeline(38.9, -77.0)
    slack_webhook_block = SlackWebhook.load("slack-send-task-completion")
    slack_webhook_block.notify("Task completed!")

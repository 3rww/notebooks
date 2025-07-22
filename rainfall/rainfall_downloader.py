"""
rainfall_downloader.py

Download 3RWW's rainfall data archive.

requirements (via pip)

click
boto3
requests
python-dateutil

"""

import os
import click
import boto3
import requests
from datetime import datetime
from dateutil.rrule import rrule, MONTHLY
from dateutil.parser import parse as parse_date

# Constants
BUCKET_NAME = "trww-rainfall-prod-3rww-datastore-558340784565"
REGION = "us-east-2"
BASE_URL = f"https://{BUCKET_NAME}.s3.{REGION}.amazonaws.com"

# Anonymous S3 client
s3 = boto3.client("s3", config=boto3.session.Config(signature_version='unsigned'), region_name=REGION)

def get_ids_from_geojson(url, id_field):
    r = requests.get(url)
    r.raise_for_status()
    return [feature["properties"][id_field] for feature in r.json()["features"]]

def generate_s3_keys(date_range, ids, data_type):
    keys = []
    for single_date in date_range:
        year = single_date.year
        month = f"{single_date.month:02d}"
        for id_ in ids:
            s3_key = f"{data_type}/calibrated/15min/{id_}/{year}/{month}/R{month}_{id_}.csv"
            keys.append((s3_key, data_type, id_, year, month))
    return keys

def download_from_s3(keys_with_meta, destination_folder="."):
    downloaded = []
    for key, data_type, id_, year, month in keys_with_meta:
        try:
            obj = s3.get_object(Bucket=BUCKET_NAME, Key=key)

            out_dir = os.path.join(destination_folder, data_type, str(id_), str(year), str(month))
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, os.path.basename(key))

            with open(out_path, "wb") as f:
                f.write(obj["Body"].read())
            downloaded.append(out_path)
            click.echo(f"✅ Downloaded {out_path}")
        except s3.exceptions.NoSuchKey:
            click.echo(f"⚠️ File not found: {key}")
    return downloaded

def fetch_rainfall_data(start_date, end_date, pixel_ids=None, gauge_ids=None, destination_folder="."):
    date_range = list(rrule(MONTHLY, dtstart=parse_date(start_date), until=parse_date(end_date)))

    if pixel_ids is None or len(pixel_ids) == 0:
        pixel_ids = get_ids_from_geojson("https://trwwapi.herokuapp.com/rainfall/pixels/?format=json", "pixel_id")
    if gauge_ids is None or len(gauge_ids) == 0:
        gauge_ids = get_ids_from_geojson("https://trwwapi.herokuapp.com/rainfall/gauges/?format=json", "web_id")

    pixel_keys = generate_s3_keys(date_range, pixel_ids, "pixels")
    gauge_keys = generate_s3_keys(date_range, gauge_ids, "gauges")

    all_keys = pixel_keys + gauge_keys
    return download_from_s3(all_keys, destination_folder)

@click.command()
@click.option('--start', required=True, help='Start date (YYYY-MM-DD)')
@click.option('--end', required=True, help='End date (YYYY-MM-DD)')
@click.option('--pixels', multiple=True, help='Pixel IDs to download (multiple allowed)')
@click.option('--gauges', multiple=True, help='Gauge IDs to download (multiple allowed)')
@click.option('--out', default='.', help='Destination folder')
def cli(start, end, pixels, gauges, out):
    """Download rainfall data by pixel/gauge and date range from a public S3 bucket.
    
    Examples:

    download between January and April 2024 for specific pixels and gauges to a "rain_data" folder:
    
    python rainfall_downloader.py --start 2024-01-01 --end 2024-03-31 --pixels 14224 12345 --gauges 430411 --out rain_data

    download everything between January and April 2024 to a "rain_data" folder:
    
    python rainfall_downloader.py --start 2024-01-01 --end 2024-03-31 --out rain_data

    """
    fetch_rainfall_data(
        start_date=start,
        end_date=end,
        pixel_ids=list(pixels) if pixels else None,
        gauge_ids=list(gauges) if gauges else None,
        destination_folder=out
    )

if __name__ == "__main__":
    cli()

Note: Probably don't bother with this. The free data from worldtides seemed pretty terrible to me.

Better off trying either:
- https://github.com/jpr5/webcaltides (if you're in US or Canada only)
- https://thesurfkit.com

## Running this puppy

Prerequisite: 
Create your own .env file with a free WorldTides API key from https://www.worldtides.info/developer 

1. `cd` into the directory
2. Create a virtual python environment (this approach isolates project dependencies from your system Python installation, which is safer and more manageable): `python3 -m venv low_tide_env`
3. Activate the virtual env: `source low_tide_env/bin/activate`
4. Now, within this virtual environment, install the required packages: `pip install requests ics pytz`
5. Run the script: `python low_tide_calendar.py`
6. Enter latitude and longitude GPS coordinates when prompted by the script
7. An `.ics` file will be generated in the directory with low tide data going forward 3 months
8. Deactivate the virtual environment: `deactivate`

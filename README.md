# TTC API Reader

Python script which calls the TTC Finch Station API and outputs the buses departing the station with their departure times.

## Getting Started

Clone the repository
```
> git clone https://github.com/tromik/ttc <.\path\directory>
```

### Requires Python 2.7 and the requests module, the easiest way to get requests is to start a virtual environment

Create a virtual environment on the repository directory
```
> .\Python27\Scripts\virtualenv.exe <.\path\directory>
```

Activate the virtual environment
```
> .\path\directory\Scripts\activate
```

Install the requests module
```
(venv)> pip install requests
```

## Running

Run the program from the shell
```
(venv)> python ttcapi.py
```

Sample output
```
97 Yonge
-------------------------
97 Yonge To Steeles | 10:59p
97 Yonge To Steeles | 11:29p
97 Yonge To Steeles | 11:59p
97B Yonge To Steeles (morning) | 7:35a
97B Yonge To Steeles (morning) | 8:05a
97B Yonge To Steeles (morning) | 8:35a
97C Yonge To Steeles | 10:30a
97C Yonge To Steeles | 11:00a
97C Yonge To Steeles | 11:30a
97B Yonge To Steeles (afternoon) | 3:58p
97B Yonge To Steeles (afternoon) | 4:28p
97B Yonge To Steeles (afternoon) | 4:58p



125 Drewry
-------------------------
125 Drewry To Bathurst Torresdale | 10:36p
125 Drewry To Bathurst Torresdale | 11:06p
125 Drewry To Bathurst Torresdale | 11:36p



308 Finch East
-------------------------
308 Finch East To Markham Road | 2:00a
308 Finch East To Markham Road | 2:30a
308 Finch East To Markham Road | 3:00a



309 Finch West
-------------------------
309 Finch West To Woodbine Racetrack | 2:00a
309 Finch West To Woodbine Racetrack | 2:30a
309 Finch West To Woodbine Racetrack | 3:00a
```

Deactivate the virtual environment when done work
```
(venv)> deactivate
```

# GreenhouseRest

This project will be used to consolidate and view data from multiple Raspberry Pi Zero sensors which will monitor light and temperature
OriginalDesign (GreenHouseCode) was designed as a flat python app to control Greenhouse Fans with configurable on/off temperatures (thermostatic control)

### Steps

- Setup Github repository
- Generate Default data within SQLite3
- Setup Django structure
- Serve simple web page
- Serve DataDriven page
- Contribute readings from remote sensor (project MicroMonitor)
- Subscribe to Django api to control fan speeds

### Ideas

- Attach to public weather database to compare offical readings with local readings
- Attach to public weather database to alert to freeze threats
- provide alerts for over-temp conditions within greenhouse

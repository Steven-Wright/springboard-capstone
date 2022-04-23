# springboard-capstone
## Motivation
The pace and sheer volume of the New York City residential real estate market can make buying or leasing property tricky. In addition to the overall condition and any amenities that might be available, the setting of a living space is critically important and is difficult to assess. Shrewd renters or buyers might try to visit the area around their potential new home at different times of day or get in contact with people living nearby to screen for nuisances, but the process is fraught with error.

311 is the non-emergency phone number for the city government. From here, callers can access resources and report all kinds of issues including noise pollution, vermin and pests, parking violations and utility outages. In recent years, the city also accepts some 311 reports through a smartphone app. Investigating the reports around a potential home could save buyers and renters significant heartbreak. This project aims to create an API that could be used alongside listings to help solve this problem.
## get_data.py
This python script downloads the 311 data in bulk as a CSV or since a certain data in JSON
### usage
You can download the entire dataset to a csv (by default `311_Service_Requests_from_2010_to_Present.csv`). The output file, API endpoint and the size of the chunks to be downloaded and written at once can optionally be specified as command line arguments.

```
usage: get_data.py bulk [-h] [--file FILE] [--chunk_size CHUNK_SIZE] [--url URL]

optional arguments:
  -h, --help            show this help message and exit
  --file FILE, -f FILE
  --chunk_size CHUNK_SIZE, -bs CHUNK_SIZE
  --url URL
 ```
 
 You can download all records since a specified data to a json file. Warning, this shouldn't be used to download the entire dataset as it loads everything into memory before writing it out as a json string
 
 ```
 usage: get_data.py since [-h] [--file FILE] [--url URL] day

positional arguments:
  day

optional arguments:
  -h, --help            show this help message and exit
  --file FILE, -f FILE
  --url URL
  ```

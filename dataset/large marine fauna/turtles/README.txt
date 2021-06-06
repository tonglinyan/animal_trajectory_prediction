README

This data file is published by the Movebank Data Repository (www.datarepository.movebank.org). As of the time of publication, a version of this published animal tracking dataset can be viewed on Movebank (www.movebank.org) in the study "Satellite Tracking of Oceanic Loggerhead Turtles in the Mediterranean" (Movebank Study ID 1134407259). Individual attributes in the data files are defined below, in the NERC Vocabulary Server at http://vocab.nerc.ac.uk/collection/MVB and in the Movebank Attribute Dictionary at www.movebank.org/cms/movebank-content/movebank-attribute-dictionary. Metadata describing this data package are maintained at https://datacite.org.

This data package includes the following data files:
Satellite Tracking of Oceanic Loggerhead Turtles in the Mediterranean.csv
Satellite Tracking of Oceanic Loggerhead Turtles in the Mediterranean-reference-data.csv
ft20_dive_Hochscheid.csv

Data package citation:
Hochscheid S. 2020. Data from: Study "Satellite Tracking of Oceanic Loggerhead Turtles in the Mediterranean". Movebank Data Repository. https://doi.org/10.5441/001/1.1f1h87r8

These data are described in the following written publication:
Chimienti M, Blasi MF, Hochscheid S. 2020. Movement patterns of large juvenile loggerhead turtles in the Mediterranean Sea: ontogenetic space use in a small ocean basin. Ecol Evol. 10(14):6978-6992. https://doi.org/10.1002/ece3.6370

-----------

Terms of Use
This data file is licensed by the Creative Commons Zero (CC0 1.0) license. The intent of this license is to facilitate the re-use of works. The Creative Commons Zero license is a "no rights reserved" license that allows copyright holders to opt out of copyright protections automatically extended by copyright and other laws, thus placing works in the public domain with as little legal restriction as possible. However, works published with this license must still be appropriately cited following professional and ethical standards for academic citation.

We highly recommend that you contact the data creator if possible if you will be re-using or re-analyzing data in this file. Researchers will likely be interested in learning about new uses of their data, might also have important insights about how to properly analyze and interpret their data, and/or might have additional data they would be willing to contribute to your project. Feel free to contact us at support@movebank.org if you need assistance contacting data owners.

For additional information, see

License description: http://creativecommons.org/publicdomain/zero/1.0

General Movebank Terms of Use: www.movebank.org/cms/movebank-content/general-movebank-terms-of-use

Movebank user agreement: https://www.movebank.org/cms/movebank-content/data-policy#user_agreement

-----------

Data Attributes
These definitions come from the Movebank Attribute Dictionary, available at http://vocab.nerc.ac.uk/collection/MVB and www.movebank.org/node/2381.

algorithm marked outlier: Identifies events marked as outliers using a user-selected filter algorithm in Movebank. Outliers have the value TRUE. units: none
entity described: event

animal ID: An individual identifier for the animal, provided by the data owner. If the data owner does not provide an Animal ID, an internal Movebank animal identifier is sometimes shown. 
example: 91876A, Gary
units: none
entity described: individual
same as: individual local identifier

animal life stage: The age class or life stage of the animal at the beginning of the deployment. Can be years or months of age or terms such as 'adult', 'subadult' and 'juvenile'. Best practice is to define units in the values if needed (e.g. '2 years').
example: juvenile, adult
units: not defined
entity described: deployment

animal sex: The sex of the animal. Allowed values are 
m = male
f = female
u = unknown
format: controlled list
entity described: individual

animal taxon: The scientific name of the species on which the tag was deployed, as defined by the Integrated Taxonomic Information System (ITIS, www.itis.gov). If the species name can not be provided, this should be the lowest level taxonomic rank that can be determined and that is used in the ITIS taxonomy. Additional information can be provided using the term 'taxon detail'. 
example: Buteo swainsoni
format: controlled list
entity described: individual
same as: individual taxon canonical name

Argos altitude: Altitude used for location calculation, Argos diagnostic data (definition from Argos User's Manual 2011).
example: 27
units: m
entity described: event

Argos best level: Best signal strength, Argos diagnostic data (definition from Argos User's Manual 2011).
example: -117
units: dB
entity described: event

Argos calcul freq: Calculated frequency, Argos diagnostic data (definition from Argos User's Manual 2011).
example: 401.6732709
units: Hz
entity described: event

Argos error radius: One standard deviation (sigma) of the estimated location error, assuming isotropic error, Argos diagnostic data (definition from Argos User's Manual 2011).
example: 229
units: m
entity described: event

Argos GDOP: Geometric dilution of precision, a measure of the effect of the geometry of the satellite-beacon configuration on location accuracy, Argos diagnostic data (definition from Argos User's Manual 2011).
example: 254
units: m/Hz
entity described: event

Argos IQ: This quality indicator gives information on the transmitter in terms of two digits, X and Y. X is the first digit and indicates residual error on the frequency calculation
Y is the second digit and indicates transmitter oscillator frequency drift between two satellite passes. Values provided in Argos diagnostic data (definition from Argos User's Manual 2011). Values obtained through some Argos channels do not include leading 0s, so 1-digit values indicate X = 0 and blank values or values of '0' indicate both X and Y = 0. Allowed values are X = 0: No calculation of residual frequency error (fewer than four messages received)
X = 1,2,3: Unsatisfactory convergence of calculation
X = 4: Residual frequency error > 1.5 Hz
X = 5: 0.15 Hz < residual frequency error < 1.5 Hz
X = 6: Residual frequency error < 0.15 Hz
Y = 0: No check on transmit frequency drift, as the two results are more than 12 hours apart
Y = 1: Frequency discrepancy > 400 Hz Probably due to transmit frequency discrepancy, change of oscillator, etc
Y = 2: Previous location is less than 1/2 hour old. Frequency discrepancy > 30 Hz, i.e. F/F (over 10 min) >2.5 E-8
Y = 3: Frequency drift > 4 Hz/minute, i.e. F/F (10 min) > 1.10-7
Y = 4: Frequency drift < 4 Hz/minute, i.e. F/F (10 min) < 1.10-7
Y = 5: Frequency drift < 2 Hz/minute, i.e. F/F (10 min) < 5.10-8
Y = 6: Frequency drift < 1 Hz/minute, i.e. F/F (10 min) < 2.5 . 10-8
Y = 7: Frequency drift < 0.4 Hz/minute, i.e. F/F (10 min) < 1.10-8
Y = 8: Frequency drift < 0.2 Hz/minute, i.e. F/F (10 min) < 5.10-9.
example: 68
format: controlled list
units: none
entity described: event

Argos lat1: Solution 1. platform latitude in degrees and thousandths of degrees, Argos diagnostic data (definition from Argos User's Manual 2011).
example: 19.493
units: decimal degrees, WGS84 reference system
entity described: event

Argos lat2: Solution 2. platform latitude in degrees and thousandths of degrees, Argos diagnostic data (definition from Argos User's Manual 2011).
example: 14.773
units: decimal degrees, WGS84 reference system
entity described: event

Argos LC: The location class retrieved from Argos (0, 1, 2, 3, A, B, Z), Argos diagnostic data (definition from Argos User's Manual 2011)
format: controlled list
units: none
entity described: event

Argos lon1: Solution 1. platform longitude in degrees and thousandths of degrees, Argos diagnostic data (definition from Argos User's Manual 2011).
example: 99.712
units: decimal degrees, WGS84 reference system
entity described: event

Argos lon2: Solution 2. platform longitude in degrees and thousandths of degrees, Argos diagnostic data (definition from Argos User's Manual 2011).
example: 120.286
units: decimal degrees, WGS84 reference system
entity described: event

Argos nb mes: The number of messages received [to calculate location], Argos diagnostic data (definition from Argos User's Manual 2011).
example: 8
units: none
entity described: event

Argos nb mes 120: The number of messages received by the satellite at a signal strength greater than -120 decibels, Argos diagnostic data (definition from Argos User's Manual 2011).
example: 2
units: none
entity described: event

Argos NOPC: Number of plausibility checks successful (from 0-4), Argos diagnostic data (definition from Argos User's Manual 2011).
example: 3
units: none
entity described: event

Argos orientation: The orientation of the semi-major axis of the error elipse, Argos diagnostic data (definition from Argos User's Manual 2011).
example: 83
units: degrees clockwise from north
entity described: event

Argos pass duration: Time elapsed between the first and last message received by the satellite, Argos diagnostic data (definition from Argos User's Manual 2011).
example: 118
units: s
entity described: event

Argos sat ID: The satellite identifier, Argos diagnostic data (definition from Argos User's Manual 2011).
example: P
units: none
entity described: event

Argos semi major: Length of the semi-major axis of the error ellipse, Argos diagnostic data (definition from Argos User's Manual 2011).
example: 300
units: m
entity described: event

Argos semi minor: Length of the semi-minor axis of the error ellipse, Argos diagnostic data (definition from Argos User's Manual 2011).
example: 175
units: m
entity described: event

Argos sensor 1: The value of the first Argos sensor, Argos diagnostic data (definition from Argos User's Manual 2011). Units are specific to the sensor.
example: 229
units: none
entity described: event

Argos sensor 2: The value of the second Argos sensor, Argos diagnostic data (definition from Argos User's Manual 2011). Units are specific to the sensor.
example: 42
units: none
entity described: event

Argos sensor 3: The value of the third Argos sensor, Argos diagnostic data (definition from Argos User's Manual 2011). Units are specific to the sensor.
example: 3
units: none
entity described: event

Argos sensor 4: The value of the fourth Argos sensor, Argos diagnostic data (definition from Argos User's Manual 2011). Units are specific to the sensor.
example: 63
units: none
entity described: event

Argos valid location algorithm: Indicates which of the two location estimates provided by Argos is the valid location, using a user-selected filter algorithm in Movebank. Allowed values are 1 = The Argos filter algorithm has chosen the primary location (solution 1, lat1/lon1) as the valid location
2 = The Argos filter algorithm has chosen the alternate location (solution 2, lat2/lon2) as the valid location
format: controlled list
units: none
entity described: event

attachment type: The way a tag is attached to an animal. Values are chosen from a controlled list: 
collar = The tag is attached by a collar around the animal's neck
glue = The tag is attached to the animal using glue
harness = The tag is attached to the animal using a harness
implant = The tag is placed under the skin of the animal
tape = The tag is attached to the animal using tape
other = user specified 
format: controlled list
entity described: deployment

data processing software: Name of the software program/s, scripts, etc. used to process raw sensor data and derive location estimates.
example: BASTrack
units: none
entity described: deployment

deploy off timestamp: The timestamp when the tag deployment ended. 
example: 2009-10-01 12:00:00.000
format: yyyy-MM-dd HH:mm:ss.SSS
units: UTC or GPS time
entity described: deployment
same as: deploy off date

deploy on latitude: The geographic latitude of the location where the animal was released (intended primarily for instances in which the animal release and tag retrieval locations have higher accuracy than those derived from sensor data).
example: 27.3516
units: decimal degrees, WGS84 reference system
entity described: deployment

deploy on longitude: The geographic longitude of the location where the animal was released (intended primarily for instances in which the animal release and tag retrieval locations have higher accuracy than those derived from sensor data).
example: -97.3321
units: decimal degrees, WGS84 reference system
entity described: deployment

deploy on timestamp: The timestamp when the tag deployment started. 
example: 2008-08-30 18:00:00.000 
format: yyyy-MM-dd HH:mm:ss.SSS 
units: UTC or GPS time
entity described: deployment
same as: deploy on date

deployment comments: Additional information about the tag deployment that is not described by other reference data terms.
example: body length 154 cm; condition good
units: none
entity described: deployment

deployment end comments: A description of the end of a tag deployment, such as cause of mortality or notes on the removal and/or failure of tag.
example: data transmission stopped after 108 days. Cause unknown
units: none
entity described: deployment

deployment end type: A categorical classification of the tag deployment end, from a controlled list:
captured = The tag remained on the animal but the animal was captured or confined
dead = The deployment ended with the death of the animal that was carrying the tag
equipment failure = The tag stopped working
fall off = The attachment of the tag to the animal failed, and it fell of accidentally
other = other
released = The tag remained on the animal but the animal was released from captivity or confinement
removal = The tag was purposefully removed from the animal
unknown = The deployment ended by an unknown cause
format: controlled list
units: none
entity described: deployment

deployment ID: A unique identifier for the deployment of a tag on animal, provided by the data owner. If the data owner does not provide a Deployment ID, an internal Movebank deployment identifier may sometimes be shown. 
example: Jane-Tag42 
units: none 
entity described: deployment

duty cycle: Remarks associated with the duty cycle of a tag during the deployment, describing the times it is on/off and the frequency at which it transmits or records data. Units and time zones should be defined in the remarks.
example: 15-min fixes from 8:00-18:00 local time (0:00-10:00 UTC)
units: not defined
entity described: deployment

event ID: An identifier for the set of values associated with each event, i.e. sensor measurement. A unique event ID is assigned to every time-location or other time-measurement record in Movebank. If multiple measurements are included within a single row of a data file, they will share an event ID. If users import the same sensor measurement to Movebank multiple times, a separate event ID will be assigned to each. 
example: 6340565
units: none
entity described: event

location accuracy comments: Comments about the values provided in 'location error text', 'location error numerical', 'vertical error numerical', 'lat lower', 'lat upper', 'long lower' and/or 'long upper'. The percentile uncertainty can be provided using 'location error percentile'.
example: 1 standard deviation errors, assuming normal distribution, provided by the GPS unit
units: none
entity described: deployment

location lat: The geographic latitude of the location as estimated by the sensor. Positive values are east of the Greenwich Meridian, negative values are west of it. example: -41.0982423 
units: decimal degrees, WGS84 reference system 
entity described: event

location long: The geographic longitude of the location as estimated by the sensor. Positive values are east of the Greenwich Meridian, negative values are west of it. 
example: -121.1761111 
units: decimal degrees, WGS84 reference system 
entity described: event

manipulation comments: Additional comments about the way in which the animal was manipulated during the deployment. Use 'manipulation type' to define the general type of manipulation.
example: Relocated from breeding colony on Smithers Island to release location at 70.02E, 21.21S
units: none
entity described: deployment

manipulation type: The way in which the animal was manipulated during the deployment. Values are chosen from a controlled list: 
confined = The animal's movement was restricted to within a defined area
none = The animal received no treatment other than the tag attachment
relocated = The animal was released from a site other than the one at which it was captured
manipulated other = The animal was manipulated in some other way, such as a physiological manipulation. 
format: controlled list 
entity described: deployment

sensor type: The type of sensor with which data were collected. All sensors are associated with a tag id, and tags can contain multiple sensor types. Each event record in Movebank is assigned one sensor type. If values from multiple sensors are reported in a single event, the primary sensor is used. Values are chosen from a controlled list: 
acceleration = The sensor collects acceleration data
accessory measurements = The sensor collects accessory measurements, such as battery voltage
Argos Doppler shift = The sensor uses Argos Doppler shift to determine position
barometer = The sensor records air or water pressure
bird ring = The animal is identified by a band or ring that has a unique identifier
GPS = The sensor uses GPS to determine location
magnetometer = The sensor records the magnetic field
natural mark = The animal is identified by a unique natural marking
orientation = Quaternion components describing the orientation of the tag are derived from accelerometer and gyroscope measurements
radio transmitter = The sensor is a classical radio transmitter
solar geolocator = The sensor collects light levels, which are used to determine position (for processed locations)
solar geolocator raw = The sensor collects light levels, which are used to determine position (for raw light-level measurements)
solar geolocator twilight = The sensor collects light levels, which are used to determine position (for twilights calculated from light-level measurements). 
format: controlled list
entity described: event

study name: The name of the study in Movebank. 
example: Coyotes, Kays and Bogan, Albany NY
units: none
entity described: study, event

study site: A location such as the deployment site or colony, or a location-related group such as the herd or pack name.
example: Pickerel Island North
units: none
entity described: deployment

tag ID: A unique identifier for the tag, provided by the data owner. If the data owner does not provide a tag ID, an internal Movebank tag identifier may sometimes be shown. example: 2342 
units: none 
entity described: tag
same as: tag local identifier

tag manufacturer name: The company or person that produced the tag. 
example: Holohil
units: none
entity described: tag

tag mass: The mass of the tag. 
example: 24 
units: grams 
entity described: tag

tag model: The model of the tag. 
example: T61 
units: none 
entity described: tag

tag readout method: The way the data are received from the tag. Values are chosen from a controlled list: 
satellite = Data are transferred via satellite 
phone network = Data are transferred via a phone network, such as GSM or AMPS
other wireless = Data are transferred via another form of wireless data transfer, such as a VHF transmitter/receiver
tag retrieval = The tag must be physically retrieved in order to obtain the data.
format: controlled list
entity described: deployment

tag serial no: The serial number of the tag.
example: MN93-33243
units: none
entity described: tag

timestamp: The date and time corresponding to a sensor measurement or an estimate derived from sensor measurements. 
example: 2008-08-14 18:31:00.000 
format: yyyy-MM-dd HH:mm:ss.SSS 
units: UTC or GPS time 
entity described: event

visible: Determines whether an event is visible on the Movebank map. Values are calculated automatically, with TRUE indicating the event has not been flagged as an outlier by 'algorithm marked outlier', 'import marked outlier' or 'manually marked outlier', or that the user has overridden the results of these outlier attributes using 'manually marked valid' = TRUE. Allowed values are TRUE or FALSE. 
units: none 
entity described: event

-----------

File ft20_dive_Hochscheid.csv

These definitions are specific to this original data file from the author, as provided by the Sea Mammal Research Unit at University of St Andrews. This file contains dive data associated with the tracking data. 

REF: A three-part code (e.g. rs3-Fred-07): The first part identifies the batch of tags, the second part is the name or number of the animal, the third part is the year (same as deployment ID above).PTT: Argos PTT number used (same as tag ID above).CNT: The number of times that this record was received.DE_DATE: Dive end: the time at which the depth crossed the threshold on the return to the surface.TIME: The time of day in GMT.SURF_DUR: Surface duration (seconds): the length of time following DE_DATE before the next dive or other event began.DIVE_DUR: Dive duration (seconds): the length of time between the crossing of the dive- start threshold on the descent and DE_DATE.MAX_DEP: The maximum dive depth recorded.D1-D5: Intermediate depth points (metres) in the dive. For most deployments one of these is guaranteed to be the maximum depth (so MAX_DEP is not transmitted).T1-5: The percentage of DIVE_DUR elapsed since the beginning of the dive at each of the intermediate depth points.N_DEPTHS: The number of intermediate dive points present.N_SPEEDS: The number of intermediate speeds present.DEPTH_STR: D1-D5 values as a comma-separated string.PROPN_STR: T1-T5 values as a comma-separated string.GRP_NUMBER: Shows which dives were sent in the same transmission.DS_DATE: The date from DS ARGOS message closest in time to the recording of the dive data.START_LAT: An approximate latitude for the start of the dive, interpolated along the track joining the filtered positions either side of the dive in time.START_LON: An approximate longitude for the start of the dive, interpolated along the track joining the filtered positions either side of the dive in time.LAT: An approximate latitude for the end of the dive, interpolated along the track joining the filtered positions either side of the dive in time.LON: An approximate longitude for the end of the dive, interpolated along the track joining the filtered positions either side of the dive in time.

-----------

More Information
For more information about this repository, see www.movebank.org/cms/movebank-content/data-repository, the FAQ at www.movebank.org/cms/movebank-content/data-repository-faq, or contact us at support@movebank.org.
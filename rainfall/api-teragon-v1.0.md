# Three Rivers Wet Weather Rainfall Dataset API 1.0

*Author: Teragon*

This API speciﬁcation allows access to the physical rain gauge and calibrated "pixel" virtual rain gauge data. There are two RPC calls that allow access to each respective dataset.

## Pixel dataset access

### Access URL

http://web.3riverswetweather.org/trp:API.pixel

### Parameters

* `startyear` - numerical quantity in the range [2000-2030]
* `startmonth` - numerical quantity in the range [1-12]
* `startday` - numerical quantity in the range [1-31]
* `starthour` - numerical quantity in the range [0-23]
* `endyear` - numerical quantity in the range [2000-2030]
* `endmonth` - numerical quantity in the range [1-12]
* `endday` - numerical quantity in the range [1-31]
* `endhour` - numerical quantity in the range [0-23]
* `pixels` - semicolon-separated list of pixel tuples in the format "x,y" - for example: "135,142;135,143;135,144". Please refer to the maps contained on the website to ﬁnd exact pixel coordinates. 
* `interval` - (optional) may be speciﬁed as `Hourly` or `Daily` for summary output. Absence of the parameter or any other speciﬁed parameter value will default to the 15-minute individual output 
* `zeroﬁll` - (optional) a value of `yes` will cause all rows to be included (normally rows that contain zeros for all datapoints are omitted)

### Example (using cURL)

`curl -d zeroﬁll=0 -d interval=Daily -d "pixels=135,142;135,143;135,144" -d startyear=2000 -d startmonth=4 -d startday=1 -d starthour=0 -d endyear=2010 -d endmonth=1 -d endday=1 -d endhour=0 http://web.3riverswetweather.org/trp:API.pixel`

## Rain gauge dataset access

### Access URL

http://web.3riverswetweather.org/trp:API.pixel

### Parameters

* `startyear` - numerical quantity in the range [2000-2030]
* `startmonth` - numerical quantity in the range [1-12]
* `startday` - numerical quantity in the range [1-31]
* `starthour` - numerical quantity in the range [0-23]
* `endyear` - numerical quantity in the range [2000-2030]
* `endmonth` - numerical quantity in the range [1-12]
* `endday` - numerical quantity in the range [1-31]
* `endhour` - numerical quantity in the range [0-23]
* `gauges` - comma-separated list of gauge numbers from `1` to `34`. Please refer to the maps contained on the website to ﬁnd gauge IDs.
* `interval` - (optional) may be speciﬁed as `Hourly` or `Daily` for summary output. Absence of the parameter or any other speciﬁed parameter value will default to the 15-minute individual output 
* `zeroﬁll` - (optional) a value of `yes` will cause all rows to be included (normally rows that contain zeros for all datapoints are omitted)

### Example (using cURL)

`curl -d zeroﬁll=0 -d interval=Daily -d "gauges=1,2" -d startyear=2000 -d startmonth=4 -d startday=1 -d starthour=0 -d endyear=2010 -d endmonth=1 -d endday=1 -d endhour=0 http://web.3riverswetweather.org/trp:API.raingauge`
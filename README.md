# nest_logger
Simple logger for the Nest API

## Create conda environment
conda env create -f environment.yml

## Set environment variables
export NEST_LOG_ROOT=/path/to/repo


## Add script to crontab:

`crontab -e`

Add to bottom of file:

```
NEST_LOG_ROOT="/home/brian/nest_logger"
*/10 * * * * /home/brian/nest_logger/get_nest_data.py > /tmp/nest_logger.log 2>&1
#  ^
# Update period (in minutes)
```

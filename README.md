# nest_logger
Simple logger for the Nest API

## Create conda environment
`conda env create -f environment.yml

`source activate nest_logger

## Set environment variables
`export NEST_LOG_ROOT=/path/to/repo


## Add script to crontab:

`crontab -e`

Add to bottom of file:

```
NEST_LOG_ROOT="/home/brian/nest_logger"
*/10 * * * * /home/brian/nest_logger/get_nest_data.py > /tmp/nest_logger.log 2>&1
#  ^
# Update period (in minutes)
```

## For jupyter notebook server:
`conda install jupyter

`cp ./jupyter_notebook_config.py ~/.jupyter

`cd ~/nest_logger

`jupyter notebook


Access notebook at brianschoolcraft.com:9999

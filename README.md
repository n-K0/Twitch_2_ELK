# Twitch_2_ELK v1.0

## About / Synopsis

* Simple **Python3** script for import specific Twitch streamer in Elastic Search Index.
* For the moment this script will import specific data.
* Project status: working
* Feel free to request.

## Table of contents

Use for instance <https://github.com/ekalinin/github-markdown-toc>:

> * [Twitch_2_ELK v1.0](#title--repository-name)
>   * [About / Synopsis](#about--synopsis)
>   * [Table of contents](#table-of-contents)
>   * [Installation](#installation)
>   * [Configuration](#configuration)
>   * [Usage](#usage)
>   * [License](#license)

## Installation

Go on your server and git clone the project :
    ```git clone https://github.com/n-K0/Twitch_2_ELK```

You need **Python3** Installation: 
The Specific Python modules used in this script are :
* twitchAPI
* pprint 
* elasticsearch 
* datetime 

## Configuration
* Modify the **liste_streamer. txt** Add each Twitch user you are interested in.
* In **zlan_api_twitch.py** Modify the Elastic Search Server ``elastic_host to the current address.``
* Add your **Twitch API KEYs** on the line 8 for replace ```Twitch('api_key', 'secret_api')```



## Usage

When the configuration is done, you can run the script : 

- launch the Script with python like ```python3 zlan_api_twitch.py```
- The script will start to import data in your Elastic Search
- He will logs every line in the logs directory


This script will be executed 1 time. You can include it in a crontab to relaunch the script every minutes, for exemple :

```
* * * * * python3 zlan_api_twitch.py
```


## Contributing / Reporting issues

* [Link to Issues](https://github.com/n-K0/Twitch_2_ELK/issues)
* [Link to project](https://github.com/n-K0/Twitch_2_ELK/projects)

## License

[Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/)

## THANKS / AUTHORS
 [@n-K0] (https://www.github.com/n-K0)

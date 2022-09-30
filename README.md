# Device LPS

> Used to estimate logging rate based on log receiver statistics.

This set of scripts will poll the firewall to see how many logs are written per second. It pulls the LPS value from the `debug log-receiver statistics` for PaloAlto Firewall or `debug log-collector log-collection-stats show incoming-logs` for PaltoAlto Panorama, and is intended to provide an _estimate_ of the number of logs per second that can be forwarded from the device.

> **Note that the number will be accurate provided all policies are configured to forward logs.**

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Credits](#credits)
4. [TODO](#todo)

## Installation

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install expect -y
```

## Usage

```bash
./device_lps.exp <Firewall_IP> <Username> <Device_Type> <Number_of_Samples>
```

- `<Device_Type>` can be either `fw` or `cms`. `fw` will send the appropriate command for a firewall while `cms` will send the appropriate command for Panorama.
- Samples are taken every 10 seconds, so you would enter 360 to get samples over an hour.

## Credits

This is an updated version of the work of art created by `cstancill(at)paloaltonetworks(dot)com` in [**Panorama Sizing and Design Guide**](https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000Clc8CAC)

## TODO

- [ ] Replace `expect` script with a Python (Paramiko) script.

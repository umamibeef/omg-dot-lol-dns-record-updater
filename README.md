# OPNsense omg.lol DNS Record Updater Script
This python script updates a DNS record on omg.lol based on the environment variables set from within the firewall as a form of dynamic DNS. It wrote this to run as a cron action on my OPNsense firewall, but you could adapt this to work on anything else, really. This uses omg.lol's REST API.

# Pre-Reading
I used the following resources to put this together:
* The OPNsense config documention: https://docs.opnsense.org/development/backend/configd.html
* omg.lol's DNS record REST API documenation: https://api.omg.lol/#token-patch-dns-edit-an-existing-dns-record

# Script Installation
The steps below show you how to set up OPNsense to use this script.
* Add `OMG_API_KEY`, `OMG_ADDRESS`, and `OMG_DNS_RECORD_NAME` environment variables in `/usr/local/opnsense/service/conf/configd.conf`:
    ```
    [environment]
    OMG_API_KEY=deadbeef
    OMG_ADDRESS=spookypopiscle
    OMG_DNS_RECORD_NAME=meat
    ```
* Create a new configd service
    - `vim /usr/local/opnsense/service/conf/actions.d/actions_omg.conf`
* Provide an update action that calls the script (the description field is what allows it to be selectable in the OPNsense web GUI).
    ```
    [update]
    command:python3 /path/to/your/update-omg-dns.py
    description:Update a specific DNS record on omg.lol
    parameters:
    type:script_output
    message:Updating omg.lol DNS record
    description:Update omg.lol DNS record
    ```
* Restart the configd service
    - `service configd restart`
* Execute the newly created action
    - `configctl omg update`

# Notes
* The environment variables set in the `configd.conf` file are only active during the execution of the action. So if you want to test the script outside of the action, you'll need to manually set the environment variables prior to calling the script.

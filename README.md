# omg-dot-lol-dns-record-updater
This script updates a DNS record on omg.lol

# Setup
* Review the documentation at https://docs.opnsense.org/development/backend/configd.html and https://api.omg.lol/#token-patch-dns-edit-an-existing-dns-record
* Add `OMG_API_KEY`, `OMG_ADDRESS`, and `OMG_DNS_RECORD_NAME` environment variables in `/usr/local/opnsense/service/conf/configd.conf`:
    ```
    [environment]
    OMG_API_KEY=deadbeef
    OMG_ADDRESS=spookypopiscle
    OMG_DNS_RECORD_NAME=meat
    ```
* Create a new configd service
    - `vim /usr/local/opnsense/service/conf/actions.d/actions_omg.conf`
* Provide an update action that calls the script
    ```
    [update]
    command:python3 /usr/local/opnsense/repos/omg-dot-lol-dns-record-updater/update-omg-dns.py
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

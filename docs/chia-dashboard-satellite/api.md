## API Reference

The [Chia-Dashboard](https://dashboard.chia.foxypool.io) API is organized around REST. It accepts JSON-encoded HTTP requests, returns JSON-encoded responses and uses standard HTTP response codes, authentication, and verbs.

!!! info "Base URL"
    ```
    https://chia-dashboard-api.foxypool.io/api
    ```

## Authentication

The Dashboard API uses API keys to authenticate satellite service stats update requests. The API key for a satellite is shown once after creation.

To use an API key to authenticate a request, append a `Authorization` header to the request with the following content: `Bearer <your API key>`.

!!! example
    ```
    Authorization: Bearer f2d3a4ed-6480-4ae8-b130-06fd1845b440
    ```

## Satellite service stats

### The satellite service stats object

??? example "Full example of a satellite service stats object"
    ```json
    {
        "harvester": {
            "plotCount": 1413,
            "totalCapacityInGib": "143438.92061062715947628029",
            "farmerConnections": [{
                "readMib": "0.5054006576538085888",
                "writtenMib": "0.52267074584960937984",
                "lastMessageTimestamp": "1620897229.0345235",
                "ip": "127.0.0.1"
            }]
        },
        "farmer": {
            "farmingInfos": [{
                "challenge": "0x5474dbce02c2f8fc4e9361c7471c0839e5f816a439073f7865aff4bc343d7d1a",
                "signagePoint": "0x6da1a6ed5ee0efc014d1c855ab7ce77a338991da1a7fbd24ffb1c547155be2df",
                "receivedAt": "2021-05-13T09:13:58.947Z",
                "proofs": 0,
                "passedFilter": 4,
                "totalPlots": 4639,
                "lastUpdated": "2021-05-13T09:13:59.791Z"
            }, {
                "challenge": "0x5474dbce02c2f8fc4e9361c7471c0839e5f816a439073f7865aff4bc343d7d1a",
                "signagePoint": "0x1c6a2168ce4e075da04bd3f45d10d67d08fd9a80cdab5518c1b68ba66150da29",
                "receivedAt": "2021-05-13T09:13:49.035Z",
                "proofs": 0,
                "passedFilter": 5,
                "totalPlots": 4639,
                "lastUpdated": "2021-05-13T09:13:49.796Z"
            }],
            "harvesterResponseTimes": [844, 66, 761, 128]
        },
        "fullNode": {
            "blockchainState": {
                "difficulty": 274,
                "spaceInGib": "4449385793.9692783355712890625",
                "syncStatus": {
                    "synced": true,
                    "syncing": false,
                    "syncedHeight": 273868,
                    "tipHeight": 273868
                },
                "timestamp": null
            },
            "fullNodeConnections": [{
                "readMib": "3.433443069458007808",
                "writtenMib": "29.20577812194824218624",
                "lastMessageTimestamp": "1620897229.2749834",
                "ip": "180.129.22.245"
            }, {
                "readMib": "3.29261589050292968448",
                "writtenMib": "19.08905982971191406592",
                "lastMessageTimestamp": "1620897229.268498",
                "ip": "181.46.139.248"
            }]
        },
        "wallet": {
            "wallets": [{
                "id": 1,
                "name": "Chia Wallet",
                "type": 0,
                "balance": {
                    "confirmed": "12.002",
                    "spendable": "12.002",
                    "unconfirmed": "12.002"
                }
            }],
            "syncStatus": {
                "synced": true,
                "syncing": false,
                "syncedHeight": 273866
            },
            "farmedAmount": {
                "farmedAmount": "602.00567",
                "poolRewardAmount": "526.75",
                "farmerRewardAmount": "75.25",
                "feeAmount": "0.00567",
                "lastHeightFarmed": 268715
            }
        },
        "plotter": {
            "completedPlotsToday": 2, // Optional
            "completedPlotsYesterday": 4, // Optional
            "jobs": [{
                "id": "455a0d9e-f797-4950-91b2-6456353da329",
                "startedAt": "2021-05-13T09:37:09.140Z",
                "state": "RUNNING",
                "kSize": 32,
                "phase": 1, // Optional
                "progress": 0.1984006092916984
            }, {
                "id": "e539bacd-b0e2-41e1-bf1c-959326739201",
                "startedAt": "2021-05-13T09:37:09.145Z",
                "state": "RUNNING",
                "kSize": 32,
                "phase": 1,
                "progress": 0.19954303122619954
            }, {
                "id": "de666862-9c36-44f5-b0e8-7e35d86d7976",
                "state": "SUBMITTED",
                "kSize": 32,
                "progress": 0
            }]
        }
    }
    ```


### Updating the satellite service stats

!!! info inline end "Endpoint"
    `PATCH /satellite`

Clients can update the satellite service stats via sparse `PATCH` requests, containing the updated [services](#the-satellite-service-stats-object) in their JSON body.
Sending `null` as the value of a service clears all stats for this service.

Example:

=== "HTTP"

    ```
    PATCH /api/satellite HTTP/1.1
    Host: chia-dashboard-api.foxypool.io
    Authorization: Bearer f2d3a4ed-6480-4ae8-b130-06fd1845b440
    Content-Type: application/json
    Content-Length: 679
    
    {
        "plotter": {
            "jobs": [{
                "id": "455a0d9e-f797-4950-91b2-6456353da329",
                "startedAt": "2021-05-13T09:37:09.140Z",
                "state": "RUNNING",
                "kSize": 32,
                "progress": 0.1984006092916984
            }, {
                "id": "e539bacd-b0e2-41e1-bf1c-959326739201",
                "startedAt": "2021-05-13T09:37:09.145Z",
                "state": "RUNNING",
                "kSize": 32,
                "progress": 0.19954303122619954
            }, {
                "id": "de666862-9c36-44f5-b0e8-7e35d86d7976",
                "state": "SUBMITTED",
                "kSize": 32,
                "progress": 0
            }]
        }
    }
    ```

=== "cURL"

    ```bash
    curl --location --request PATCH 'https://chia-dashboard-api.foxypool.io/api/satellite' \
    --header 'Authorization: Bearer f2d3a4ed-6480-4ae8-b130-06fd1845b440' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "plotter": {
            "jobs": [{
                "id": "455a0d9e-f797-4950-91b2-6456353da329",
                "startedAt": "2021-05-13T09:37:09.140Z",
                "state": "RUNNING",
                "kSize": 32,
                "progress": 0.1984006092916984
            }, {
                "id": "e539bacd-b0e2-41e1-bf1c-959326739201",
                "startedAt": "2021-05-13T09:37:09.145Z",
                "state": "RUNNING",
                "kSize": 32,
                "progress": 0.19954303122619954
            }, {
                "id": "de666862-9c36-44f5-b0e8-7e35d86d7976",
                "state": "SUBMITTED",
                "kSize": 32,
                "progress": 0
            }]
        }
    }'
    ```

=== "JavaScript"

    ```js
    const axios = require('axios');

    const apiKey = 'f2d3a4ed-6480-4ae8-b130-06fd1845b440';
    const client = axios.create({
      baseURL: 'https://chia-dashboard-api.foxypool.io/api',
      headers: { Authorization: `Bearer ${apiKey}` },
    });
    await client.patch('satellite', {
        plotter: {
            jobs: [{
                id: '455a0d9e-f797-4950-91b2-6456353da329',
                startedAt: '2021-05-13T09:37:09.140Z',
                state: 'RUNNING',
                kSize: 32,
                progress: 0.1984006092916984,
            }, {
                id: 'e539bacd-b0e2-41e1-bf1c-959326739201',
                startedAt: '2021-05-13T09:37:09.145Z',
                state: 'RUNNING',
                kSize: 32,
                progress: 0.19954303122619954,
            }, {
                id: 'de666862-9c36-44f5-b0e8-7e35d86d7976',
                state: 'SUBMITTED',
                kSize: 32,
                progress: 0,
            }],
        },
    });
    ```

# Mock Bidder
## Description
The mock bidder is a RTB bidder that generates random bids for incoming `BidRequest`
## Commands
### Start RTB bidder
```shell script
python -m mock-bidder start_server [--port PORT] [--base_url URL]
```
* `PORT` - the port number on which the bidder listen for incoming bid requests. The default `PORT` is 9000
* `URL` - the url used to construct `adm` field in the bid response
**Both parameters are optional**
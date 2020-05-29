# Mock Bidder
## Description
The mock bidder is a RTB bidder that generates random bids for incoming `BidRequest`
## Commands
### Running RTB bidder
```shell script
python -m mock-bidder start_server [--port PORT] [--base_url URL]
```
* `PORT` - the port number on which the bidder listen for incoming bid requests. The default `PORT` is 9000
* `URL` - the url used to construct `adm` field in the bid response

__Both parameters are optional__
### Using docker container 
#### Building a docker image
```shell script
make build
```
#### Running the docker image
```shell script
make run
```
#### Connection to the docker container
```shell script
make login
```
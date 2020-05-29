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
## Using docker container 
### Building a docker image
```shell script
make build
```
### Running the docker image
```shell script
make run
```
### Connecting to the docker container
```shell script
make login
```
## Testing Docker deployment
```shell script
  endpoint="http://127.0.0.1:8080"
  proto="$(echo ${endpoint} | grep :// | sed -e's,^\(.*://\).*,\1,g')"
  url="$(echo ${endpoint/$proto/})"
  hdr_host_name="$(echo ${url} | cut -d/ -f1)"
  hdr_cont_type="Content-Type: application/json"
  hdr_open_rtb="x-openrtb-version: 2.5"

  dev_ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
  dev_ip="108.185.179.0"
  pub_id="2949"
  pub_cat="[\"sport\", \"coats\", \"spring\"]"
  req_id=$(uuidgen)
  usr_id=$(uuidgen)

  curl $silent --location --request POST ${endpoint} \
  --header "${hdr_cont_type}" \
  --header "${hdr_host_name}" \
  --header "${hdr_open_rtb}" \
  --data-raw "{
      \"id\" : \"${req_id}\",
      \"bcat\" : [],
      \"imp\": [
          {
          \"id\": \"${req_id}\",
          \"instl\": 1
          }
      ],
      \"site\": {
          \"id\": \"${pub_id}\",
          \"cat\" : ${pub_cat}
      },
      \"device\": {
          \"ua\": \"${dev_ua}\",
          \"ip\": \"${dev_ip}\"
      },
      \"user\": {
          \"id\": \"${usr_id}\"
      }
  }"
```
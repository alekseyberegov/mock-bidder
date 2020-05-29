#!/bin/bash

# the default bidder endpoint
endpoint="http://127.0.0.1:8080"

proto="$(echo ${endpoint} | grep :// | sed -e's,^\(.*://\).*,\1,g')"
url="$(echo ${endpoint/$proto/})"

# request's headers
hdr_host_name="$(echo ${url} | cut -d/ -f1)"
hdr_cont_type="Content-Type: application/json"
hdr_open_rtb="x-openrtb-version: 2.5"

# payload data
dev_ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/80.0 Safari/537.36"
dev_ip="108.185.179.0"
pub_id="100"
pub_cat="[\"sport\", \"coats\", \"spring\"]"
req_id=$(uuidgen)
usr_id=$(uuidgen)

# send the request
curl --location  --request POST ${endpoint} \
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

echo ""


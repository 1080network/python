# python
Mica client code for python

## SDKs

* _discount_ --> Contains the API for a discount provider
* _partner_ --> API for transaction acquirers
* _serviceprovider_ --> API for issuers and value providers
* _networksdk_ --> Is a thick SDK with all the APIs, use this for an integration that requires more than one of the above roles


## Building the SDK

### Update the protos

1. Start by cloning with recursive so you get the submodules

```bash
git clone --recurse-submodules git@github.com:1080network/golang.git
```

2. Update the `__version__` line in `about.py` at the root of the repository to reflect the version of the protos being used:

```bash
cat about.py
# common versioning and other indicators

__version__ = "v1.8.0"
__author__ = "Mica"
__author_email__ = "engineering@mica.io"
__license__ = "Apache 2.0"
__copyright__ = "Copyright (c) 2023 Mica"
__url__ = "https://mica.io/"
__python_requires__ = ">=3.10"
```

3. Update the generated files from the protos

```bash
make generate
```

### Building the SDK(s)

It is highly advisable that you build and manage this SDK on a venv!! Activate your venv

Install all requirements into your venv
```bash
make setup_common
```

Build everything
```bash
make build
```

Note if you run into a NameError or KeyError for generate_validate in site-packages/protoc_gen_validate/validator.py you can update this file to change `exec(func)` to `exec(func, globals())`.

To build an individual module/sdk change directory to the module and run
```bash
make build
```

## Manual Testing

To test the SDK, you will need to have the appropriate certificates. They are referenced in the Python example below (in the three lines that include the open function).

In order to test the Discount SDK, start an interactive Python shell by running the following:

```bash
python3 -m venv venv
source venv/bin/activate
version=`grep "__version__" about.py | cut -d '"' -f 2 | tr -d 'v'`
pip install micacommon/dist/micacommon-${version}-py3-none-any.whl
pip install discount/dist/micadiscount-${version}-py3-none-any.whl
python3.10
```

Note that you should be usign the same version of Python that is specified in `about.py`.

Next in the Python shell, run the following commands to exercise the SDK:

```python
import grpc
import discount.mica.member.ping.v1.ping_service_pb2 as ping
import discount.mica.discount.service.v1.discount_to_mica_service_pb2_grpc
import discount

# load the certificates
root_certificates = bytes(open("/path/to/rootca.crt", 'rb').read())
private_key = bytes(open("/path/to/provider-01_discount_mica_io.key", "rb").read())
certificate_chain = bytes(open("/path/to/provider-01_discount_mica_io.crt", "rb").read())

# create the channel credentials
creds = grpc.ssl_channel_credentials(root_certificates=root_certificates, private_key=private_key, certificate_chain=certificate_chain)

# create the channel
chan = grpc.secure_channel(target="api.discount.mica.io", credentials=creds, options=None, compression=None)

# create the stub
s=discount.DiscountToMicaServiceStub(chan)

# call some of the services
s.Ping(ping.PingRequest())
s.SearchDiscountDefinition(discount.mica.discount.discountdefinition.v1.discount_definition_pb2.SearchDiscountDefinitionRequest())
```

This will produce a response like this:

```python
>>> s.Ping(ping.PingRequest())
status: STATUS_SUCCESS
server_time {
  seconds: 1755283392
  nanos: 553821461
}
build_version: "master-c1b3a73"
build_sha: "c1b3a735e1631ece2d5dcaddc7177bada5ec5d08"
build_time: "2025-08-14T15:09:38Z"
service_type: "Discount"
server_start_time {
  seconds: 1755186283
  nanos: 989038756
}

>>> s.SearchDiscountDefinition(discount.mica.discount.discountdefinition.v1.discount_definition_pb2.SearchDiscountDefinitionRequest())
status: STATUS_SUCCESS
discount_definitions {
  discount_definition_key: "EKcdiehgmBkY3RJqHRyVB1J5hiw"
  version: 1
  created {
    seconds: 1697562492
    nanos: 834332000
  }
  updated {
    seconds: 1697562492
    nanos: 834332000
  }
  discount_definition_ref: "536d21e7dfea241bd4c32d72ceb77ecaf6be3414"
  discount_provider_account_ref: "536d21e7dfea241bd4c32d72ceb77ecaf6be3414"
<snip>
  monetary_amount {
    amount: "1.25"
    tax_amount: "0"
  }
  headline: "Save $1.25"
  summary: "on any ONE (1) KRAFT Macaroni & Cheese Dinner Product, Any variety, Any size"
  thumbnail_url: "http://staging.cdn.com/uploads/1668524157_6884821043_thumb.png"
  currency {
    fiat: "USD"
  }
}

>>>
```

## Releasing
Manual for now, will look into how to automate

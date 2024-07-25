# python
Mica client code for python

## SDKs

* _discount_ --> Contains the API for a discount provider
* _partner_ --> API for transaction acquirers
* _serviceprovider_ --> API for issuers and value providers
* _networksdk_ --> Is a thick SDK with all the APIs, use this for an integration that requires more than one of the above roles


## Building the SDK

Start by cloning with recursive so you get the submodules

```bash
git clone --recurse-submodules git@github.com:1080network/golang.git
```

It is highly advisable that you build and manage this SDK on a venv!! Activate your venv

Install all requirements into your venv
```bash
make setup_common
```

Build everything
```bash
make build
```

To build an individual module/sdk change directory to the module and run
```bash
make build
```

## Releasing
Manual for now, will look into how to automate


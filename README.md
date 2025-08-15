# python
Mica client code for python

## SDKs

* _discount_ --> Contains the API for a discount provider
* _partner_ --> API for transaction acquirers
* _serviceprovider_ --> API for issuers and value providers
* _networksdk_ --> Is a thick SDK with all the APIs, use this for an integration that requires more than one of the above roles


## Building the SDK

### Update the protos

Start by cloning with recursive so you get the submodules

```bash
git clone --recurse-submodules git@github.com:1080network/golang.git
```

Update the generated files from the protos

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

## Releasing
Manual for now, will look into how to automate


installs and configure sane on **my** RasPi.

currently works only with the old version from `https://salsa.debian.org/debian/sane-backends`

## config

```
sane_files:
  - libsane
  - libsane-common
  - libsane-extras
  - libsane-extras-common
  - sane
  - sane-utils

sane_repository:
  # upstream
  # https://gitlab.com/sane-project/backends/-/archive/1.0.31/backends-1.0.31.tar.bz2
  # url: https://gitlab.com/sane-project/backends
  # older debian stuff
  url: https://salsa.debian.org/debian/sane-backends
  # branch: 1.0.31

sane_src_directory: /home/saned/src/sane-backends

sane_saned_clients: []

sane_dll_backends:
  - net
  - genesys
```

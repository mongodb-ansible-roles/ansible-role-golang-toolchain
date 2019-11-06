Ansible role for golang-toolchain
=================================

Installs the golang toolchain.

This role will pass the value of golang\_toolchain\_sha to its dependent role: ansible-role-toolchain.
The ansible-role-toolchain will first check if the host has an existing golang toolchain installed at /opt/golang.
If so, ansible-role-toolchain will then check if there is a toolchain\_version file present in /opt/golang/toolchain\_version.
If the version file is present, it will then compare versions to see if we need to download a new toolchain. If the versions match, then no further work is required.
If the versions are different, ansible-role-toolchain will then proceed to download the specified toolchain version from AWS and place the tarball into the /tmp directory.
From here, the ansible-role-golang-toolchain will then delete the old toolchain and then move the newly downloaded toolchain to the correct directory, /opt/golang.
Finally, this role will then create a toolchain\_version file and place it in /opt/golang/toolchain\_version for use in future runs.

[![CircleCI](https://img.shields.io/circleci/build/github/mongodb-ansible-roles/ansible-role-golang-toolchain/master?style=flat-square)](https://circleci.com/gh/mongodb-ansible-roles/ansible-role-golang-toolchain)

Requirements
------------

None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| golang\_toolchain\_sha | SHA of the golang toolchain you want to download | string | "" | yes |
| golang\_toolchain\_dest | Destination to download toolchain | string | /opt | yes |

Dependencies
------------

- [`mongodb-ansible-roles.ansible-role-toolchain`](https://github.com/mongodb-ansible-roles/ansible-role-toolchain)

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-toolchain-golang
      vars:
        golang_toolchain_sha: "001ac697f8f64d5d89625373a0ffa6aae13270a8"
```

License
-------

[Apache License](LICENSE)

Ansible role for toolchain-golang
==================================

Installs the golang toolchain

[![CircleCI](https://img.shields.io/circleci/build/github/mongodb-ansible-roles/ansible-role-toolchain-golang/master?style=flat-square)](https://circleci.com/gh/mongodb-ansible-roles/ansible-role-toolchain-golang)

Requirements
------------

None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| toolchain\_golang\_version | SHA of the golang toolchain you want to download | string | "" | no |

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-toolchain-golang
      vars:
        toolchain_golang_version: "001ac697f8f64d5d89625373a0ffa6aae13270a8"
```

License
-------

[Apache License](LICENSE)

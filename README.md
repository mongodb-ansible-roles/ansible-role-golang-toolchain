Ansible role for golang-toolchain
=================================

Installs the golang toolchain

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

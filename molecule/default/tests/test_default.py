import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_golang_toolchain(host):
    assert host.file("/opt/golang").exists
    assert host.file("/opt/golang/toolchain_version").exists
    assert host.file("/opt/golang/toolchain_version").contains("testing_golang_sha")

    cmd = host.run("GOROOT=/opt/golang/go1.7 /opt/golang/go1.7/bin/go version")
    assert cmd.stdout == """go version go1.7.6 linux/amd64
"""

    cmd = host.run("GOROOT=/opt/golang/go1.8 /opt/golang/go1.8/bin/go version")
    assert cmd.stdout == """go version go1.8.7 linux/amd64
"""

    cmd = host.run("GOROOT=/opt/golang/go1.9 /opt/golang/go1.9/bin/go version")
    assert cmd.stdout == """go version go1.9.7 linux/amd64
"""

    cmd = host.run("GOROOT=/opt/golang/go1.10 /opt/golang/go1.10/bin/go version")
    assert cmd.stdout == """go version go1.10.8 linux/amd64
"""

    cmd = host.run("GOROOT=/opt/golang/go1.11 /opt/golang/go1.11/bin/go version")
    assert cmd.stdout == """go version go1.11.9 linux/amd64
"""

    cmd = host.run("GOROOT=/opt/golang/go1.12 /opt/golang/go1.12/bin/go version")
    assert cmd.stdout == """go version go1.12.8 linux/amd64
"""

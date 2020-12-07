import pytest
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def get_vars(host):
    defaults_files = "file=../../defaults/main.yml name=role_defaults"
    vars_files = "file=../../vars/main.yml name=role_vars"

    ansible_vars = host.ansible(
        "include_vars",
        defaults_files)["ansible_facts"]["role_defaults"]

    ansible_vars.update(host.ansible(
        "include_vars",
        vars_files)["ansible_facts"]["role_vars"])

    return ansible_vars


@pytest.mark.parametrize("dirs", [
    "/usr/local/etc/sane.d",
    "/usr/local/lib/sane"
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/usr/local/etc/sane.d/saned.conf",
    "/usr/local/etc/sane.d/net.conf",
    "/usr/local/etc/sane.d/dll.conf",
    "/lib/udev/rules.d/99-libsane.rules",
    "/usr/local/bin/sane-find-scanner",
    "/usr/local/bin/sane-config",
    "/usr/local/lib/libsane.so.1.0.27"
])
def test_files(host, files):
    f = host.file(files)
    assert f.is_file
    assert f.exists

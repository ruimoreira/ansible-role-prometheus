import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_prometheus_group(host):
    prometheus_group = host.group('prometheus')
    assert prometheus_group.exists
    assert prometheus_group.gid == 9999


def test_prometheus_user(host):
    prometheus_user = host.user('prometheus')
    assert prometheus_user.exists


def test_etc_prometheus(host):
    etcdir = host.file("/etc/prometheus")
    assert etcdir.exists
    assert etcdir.is_directory
    assert etcdir.user == 'prometheus'


def test_varlib_prometheus(host):
    varlib = host.file("/var/lib/prometheus")
    assert varlib.exists
    assert varlib.is_directory
    assert varlib.user == 'prometheus'


def test_file_download(host):
    tmpfile = host.file("/tmp/prometheus-2.6.0.linux-amd64.tar.gz")
    assert tmpfile.exists
    assert tmpfile.is_file


def test_binaries_exist(host):
    promfile = host.file("/usr/local/bin/prometheus")
    promtool = host.file("/usr/local/bin/promtool")
    assert promfile.exists
    assert promfile.is_file
    assert promtool.exists
    assert promtool.is_file


def test_prometheus_config_file(host):
    prmcfg = host.file("/etc/prometheus/prometheus.yml")
    assert prmcfg.exists
    assert prmcfg.is_file
    assert prmcfg.user == 'prometheus'


def test_systemd_unit(host):
    systemdfile = host.file("/etc/systemd/system/prometheus.service")
    assert systemdfile.exists
    assert systemdfile.is_file
    assert systemdfile.user == 'root'

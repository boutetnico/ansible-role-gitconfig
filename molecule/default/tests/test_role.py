import pytest


@pytest.mark.parametrize(
    "file,section,line",
    [
        ("/root/.gitconfig", "alias", "ci = commit"),
        ("/etc/gitconfig", "alias", "remotev = remote -v"),
        ("/role_test/.git/config", "user", "email = root@root"),
    ],
)
def test_git_config_files_exist(host, file, section, line):
    git_config = host.file(file)
    assert git_config.exists
    assert git_config.is_file
    assert git_config.contains(section)
    assert git_config.contains(line)


def test_git_command_works(host):
    cmd = host.run("git --version")
    assert cmd.rc == 0


def test_system_gitconfig_has_alias_section(host):
    config = host.file("/etc/gitconfig")
    assert config.contains("[alias]")


def test_user_gitconfig_has_alias_section(host):
    config = host.file("/root/.gitconfig")
    assert config.contains("[alias]")

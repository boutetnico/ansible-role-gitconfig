import pytest


@pytest.mark.parametrize(
    "file,section,line",
    [
        ("/root/.gitconfig", "alias", "ci = commit"),
        ("/etc/gitconfig", "alias", "remotev = remote -v"),
        ("/role_test/.git/config", "user", "email = root@root"),
    ],
)
def test_git_config_file(host, file, section, line):
    git_config = host.file(file)
    assert git_config.exists
    assert git_config.is_file
    assert git_config.contains(section)
    assert git_config.contains(line)

from _typeshed import FileDescriptorLike, Unused
from collections.abc import Iterable

from .spawnbase import SpawnBase, _Logfile

class fdspawn(SpawnBase):
    args: None
    command: None
    child_fd: int
    own_fd: bool
    closed: bool
    name: str
    use_poll: bool
    def __init__(
        self,
        fd: FileDescriptorLike,
        args: Unused = None,
        timeout: int = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: _Logfile | None = None,
        encoding: str | None = None,
        codec_errors: str = "strict",
        use_poll: bool = False,
    ) -> None: ...
    def close(self) -> None: ...
    def isalive(self) -> bool: ...
    def terminate(self, force: bool = False) -> None: ...
    def send(self, s: str | bytes) -> bytes: ...
    def sendline(self, s: str | bytes) -> bytes: ...
    def write(self, s: str | bytes) -> None: ...
    def writelines(self, sequence: Iterable[str | bytes]) -> None: ...
    def read_nonblocking(self, size: int = 1, timeout: int | None = -1) -> bytes: ...

from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict, List, Literal, Dict, get_args
from collections.abc import Callable

from oai_portal.abs_val import ID_FLAG_LEN, MINIMUM_REQ_TIMEOUT, MAX_REQ_TIMEOUT
from oai_portal.errors import \
    RuntimeIDError, UrlsTypeError, NoneOfUrlError, \
    TimeoutDidnotMatchUrls, TimeoutValError, \
    TimeoutTypeError

NetworkMethod = Literal["get", "post", "delete", "put", "patch", "head"]

head_key = Literal[
  "Host",
  "Content-Type",
  "Accept",
  "Authorization",
  "Cookie",
  "User-Agent",
  "Referer",
  "Origin",
  "Cache-Control",
  "Connection",
  "X-Request-ID",
  "Accept-Language"
]

@dataclass(frozen=True)
class ID:
    parent: ID|None
    flag: str
    def __post_init__(self):
        if len(self.flag) != ID_FLAG_LEN:
            raise RuntimeIDError(f"Invalid Id value: length error, except {ID_FLAG_LEN} chars, got {len(self.flag)}")


@dataclass(slots=True)
class RequestInfo:
    name: str|None
    id: ID
    urls: List[str]  # 在当前代码文件校验存在，在使用时校验可用性
    timeout: int | float | List[int|float]  # 支持为每一个url配置，校验长度，正负和极小绝对值值
    method: NetworkMethod
    header: Dict[head_key, str] | List[Dict[head_key, str]]  # 不校验
    data: dict | List[dict]

    def __post_init__(self):  # 为了最好的报错体验，我们（或者说我本人）采用手写了。
        def _t_vali(t: int|float):
            if t <= MINIMUM_REQ_TIMEOUT:
                raise TimeoutValError(f"Arg-timeout: Set value too small, at least {MINIMUM_REQ_TIMEOUT}s")
            if t >= MAX_REQ_TIMEOUT:
                raise TimeoutValError(f"Arg-timeout: Set value too large, at most {MAX_REQ_TIMEOUT}s")
        
        if type(self.name) not in [str, type(None)]:
            raise TypeError(f"Arg-name: expected None or str: list, got {type(self.name)}")

        if not isinstance(self.id, ID):
            raise TypeError(f"Arg-id: expected types/network/cores/types.ID, got {type(self.id)}")

        if self.urls:
            if isinstance(self.urls, list):
                pass
            else:
                raise UrlsTypeError(f"Arg-urls: Need a list, got {type(self.urls)}")  # to ask required "list" type
        else:
            raise NoneOfUrlError("Arg-urls: Need at least one url but got zero.")

        if type(self.timeout) in [int, float, list]:
            if isinstance(self.timeout, list):
                if len(self.urls) == len(self.timeout):
                    for t in self.timeout:
                        _t_vali(t)
                else:
                    raise TimeoutDidnotMatchUrls(
    f"Arg-timeout: When timeout is a list, the length of it is required that same as urls. "+
    f"It need be {len(self.urls)} objects, but got {len(self.timeout)}.")
            else:
                _t_vali(self.timeout)
        else:
            raise TimeoutTypeError(f"Arg-timeout: timeout must be number or a list of number.")
        
        if self.method not in get_args(NetworkMethod):
            raise ValueError(f"Arg-method: Unexpected method-{self.method}")

        # WARNING: 这里没有校验Arg-args, 需要应用代码





        
        
        
x = RequestInfo(None, id = ID(None, "123456789012"), urls = [""], timeout = 2, method="get", header={}, data={})


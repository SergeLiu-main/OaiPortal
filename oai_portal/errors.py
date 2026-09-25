class DevException(Exception): pass
class UserException(Exception): pass

# 请注意，来自父类提供的便利捕获使我们能够更清楚的描述class而不是过度概括
# 您可以使用 "except DevException: ..." 或 "except UserException" 直接捕获一系列的错误且分类良好

# network
class RuntimeIDError(DevException): pass
class UrlsTypeError(DevException): pass
class NoneOfUrlError(DevException): pass
class TimeoutDidnotMatchUrls(DevException): pass
class TimeoutValError(DevException): pass
class TimeoutTypeError(DevException): pass
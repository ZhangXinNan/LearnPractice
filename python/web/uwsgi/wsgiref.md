
**Web服务器网关接口（WSGI）**是Web服务器软件和用Python编写的Web应用程序之间的标准接口。拥有标准接口可以轻松使用支持WSGI和多个不同Web服务器的应用程序。

只有Web服务器和编程框架的作者需要知道WSGI设计的每个细节和角落案例。您不需要了解WSGI的每个细节，只需安装WSGI应用程序或使用现有框架编写Web应用程序即可。

`wsgiref` 是WSGI规范的参考实现，可用于将WSGI支持添加到Web服务器或框架。它提供了用于操纵WSGI环境变量和响应头的实用程序，用于实现WSGI服务器的基类，为WSGI应用程序提供服务的演示HTTP服务器以及用于检查WSGI服务器和应用程序是否符合WSGI规范（PEP 333）的验证工具。






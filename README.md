# NLP_api
将自然语言处理作为服务

# 设计
*  [http-api-design](https://github.com/interagent/http-api-design)
*  [hug](https://github.com/timothycrosley/hug):依赖很少，只依赖[falcon](https://github.com/falconry/falcon),falcon也精简。目前只支持python3

# 问题
*  是否需要做成RESTful服务
  *  并没有资源问题（除非用户个性化）
  *  写成rest服务，前台可以用react
*  当前核心是action，而不是resource
*  写命令行工具（智能化），参考[使用Python Prompt Toolkit构建强大的REPL](http://blog.just4fun.site/python-prompt-toolkit.html)

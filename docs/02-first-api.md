# 第一课：请求如何进入接口

`app = FastAPI()` 创建应用；`@app.get("/")` 把 GET 请求交给下面的函数。返回的字典会成为 JSON 响应。

## 动手实验

1. 启动后访问 `/`，预期得到 `{"message":"Hello FastAPI"}`。
2. 访问 `/items/7?q=book`：`7` 是路径参数，`q` 是查询参数。
3. 访问 `/items/abc`，预期状态码 422，因为 `item_id` 声明为整数。
4. 在 `/docs` 调用 `POST /items/`，输入 `{"name":"book","price":12.5}`，预期 201。
5. 将价格改成 `-1`，预期 422：`Field(gt=0)` 要求大于零。

POST 示例只校验并返回请求体，没有保存操作。不要把响应成功理解为数据已落盘。

## 自己完成

- 新增 `/hello/{name}`，返回包含姓名的问候。
- 为商品增加可选描述字段。
- 给新增接口写一个正常输入测试。
- 用自己的话解释路径参数、查询参数和请求体的区别。

## 常见问题

- `No module named fastapi`：确认当前解释器已安装 requirements 中的依赖。
- 无法导入 `main`：在包含 `main.py` 的仓库根目录启动。
- 8000 端口被占用：停止旧服务，或使用 `--port 8001` 并修改访问地址。
- 404：检查 HTTP 方法和路径是否与代码一致。

参考：[官方入门说明](https://fastapi.tiangolo.com/tutorial/first-steps/)。

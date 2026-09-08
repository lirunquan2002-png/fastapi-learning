# FastAPI 学习记录

使用 PyCharm 练习 FastAPI，将代码、示例数据和中文笔记放在同一个 Git 仓库。

## 从这里开始

1. 在 PyCharm 中打开本仓库文件夹 `fastapi-learning`。
2. 为项目创建 `.venv` 虚拟环境，选择 Python 3.10 或更新版本作为基础解释器。
3. 在项目终端运行：

```powershell
python -m pip install -r requirements-dev.txt
python -m uvicorn main:app --reload
```

打开 http://127.0.0.1:8000/docs ，展开接口，点击 **Try it out** 后执行请求。停止服务按 Ctrl+C。

也可以右键运行 `main.py`；这种方式没有自动重载，适合初次运行和打断点调试。若模块找不到，检查 PyCharm 项目解释器与终端是否都使用 `.venv`。

## 文件导航

| 位置 | 用途 |
| --- | --- |
| `main.py` | 可运行的入门示例：GET、路径参数、查询参数、POST、数据校验 |
| `tests/test_main.py` | 接口成功与参数错误的测试 |
| [学习路线](docs/01-roadmap.md) | 学习阶段和完成标准 |
| [第一课](docs/02-first-api.md) | 运行、实验、预期结果 |
| [笔记模板](docs/note-template.md) | 每次学习后复制填写 |
| [Git 与 GitHub](docs/03-git-workflow.md) | 保存版本和上传步骤 |
| `exercises/` | 自己动手写的章节练习 |
| `data/samples/` | 可提交的虚构 JSON 示例数据 |

## 验证

在仓库根目录执行：

```powershell
python -m pytest -q
```

## 学习方式

每学一个主题，在 `exercises/` 中建对应目录，在 `docs/` 中复制笔记模板，记录目标、代码路径、运行方式、结果和错误原因。完成后提交一次 Git 版本。当前示例只返回数据，不会将 POST 数据保存到数据库。

依赖文件限定兼容范围，并非精确锁定版本；需要复现环境时，可在专用虚拟环境安装成功后运行 `python -m pip freeze > requirements-lock.txt` 并提交锁定文件。

参考：[FastAPI 官方教程](https://fastapi.tiangolo.com/tutorial/)、[第一个接口](https://fastapi.tiangolo.com/tutorial/first-steps/)。本仓库笔记是学习整理，不是官方文档的全文复制。

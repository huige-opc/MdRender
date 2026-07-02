# MdRender — 公众号 Markdown 编辑器

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

微信公众号 Markdown 排版工具，支持本地图片上传、代码高亮、实时预览。

> ⚠️ **重要说明：本项目的图片上传功能默认将图片存储在本地 `uploads/` 文件夹中。如果部署到服务器，建议根据实际情况修改 `server.py` 中的图片存储逻辑，或者自行部署对象存储（如 OSS、S3）。**

---

## 功能特性

- Markdown 实时编辑与预览
- 本地图片上传（Ctrl+V / 拖拽）
- 代码语法高亮（支持 JavaScript、Python、CSS 等）
- 一键复制到公众号后台
- 本地部署，图片不经过第三方

## 使用方法

### 1. 安装依赖

```bash
pip install flask flask-cors
```

### 2. 启动服务

```bash
python server.py
```

### 3. 打开浏览器

访问 `http://127.0.0.1:10094`

### 4. 编辑内容

- 在左侧编辑区编写 Markdown
- 直接粘贴（Ctrl+V）或拖拽图片到编辑器
- 右侧实时预览渲染效果
- 点击"复制到公众号"将排版好的内容粘贴到公众号后台

## 配置

编辑 `config.py`：

```python
SERVER_HOST = '0.0.0.0'   # 监听地址
SERVER_PORT = 10094        # 监听端口
```

## 目录结构

```
MdRender/
├── server.py          # Flask 服务端
├── config.py          # 配置文件
├── index.html         # 前端页面
├── marked.min.js      # Markdown 解析库
├── prism*.js          # 代码高亮库
├── images/            # README 示例图片
├── uploads/           # 上传图片存储目录（自动创建）
└── requirements.txt   # Python 依赖
```

## 技术栈

- **后端:** Python Flask
- **前端:** 原生 HTML + Marked.js + Prism.js
- **图片存储:** 本地文件系统

## 联系

有问题或建议欢迎联系：
- 微信：HgAiAgent（扫码添加，拉你进交流群）
- 邮箱：[szlihui801@gmail.com](mailto:szlihui801@gmail.com)

![微信：HgAiAgent](docs/wechat.png)

---

# MdRender — Markdown Editor for WeChat Official Accounts

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

A Markdown formatting tool designed for WeChat Official Accounts, featuring local image upload, code highlighting, and real-time preview.

> ⚠️ **Note: This project stores uploaded images locally in the `uploads/` folder by default. If deploying to a server, consider modifying the image storage logic in `server.py` or integrating an object storage service (e.g., OSS, S3).**

## Features

- Real-time Markdown editing and preview
- Local image upload (Ctrl+V / drag & drop)
- Code syntax highlighting (JavaScript, Python, CSS, etc.)
- One-click copy to WeChat Official Account editor
- Local deployment — images stay on your server

## Quick Start

### 1. Install Dependencies

```bash
pip install flask flask-cors
```

### 2. Start Server

```bash
python server.py
```

### 3. Open Browser

Visit `http://127.0.0.1:10094`

### 4. Start Editing

- Write Markdown on the left panel
- Paste (Ctrl+V) or drag & drop images directly
- Right panel renders the preview in real-time
- Click "复制到公众号" to copy formatted content to WeChat

## Tech Stack

- **Backend:** Python Flask
- **Frontend:** Vanilla HTML + Marked.js + Prism.js
- **Image Storage:** Local filesystem

## Contact

Feel free to reach out:
- WeChat：HgAiAgent (scan the QR code)
- Email：[szlihui801@gmail.com](mailto:szlihui801@gmail.com)

![WeChat：HgAiAgent](docs/wechat.png)

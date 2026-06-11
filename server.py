# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from datetime import datetime
import uuid
import sys
import io

# 设置标准输出为UTF-8编码
if sys.stdout.buffer:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 导入配置
try:
    import config
except ImportError:
    print("错误: 找不到config.py配置文件")
    sys.exit(1)

# 自动清理 __pycache__
def clean_pycache():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pycache_dir = os.path.join(script_dir, '__pycache__')
    if os.path.exists(pycache_dir):
        try:
            import shutil
            shutil.rmtree(pycache_dir)
            print("[OK] 已清理 __pycache__ 文件夹")
        except Exception as e:
            print(f"[警告] 清理 __pycache__ 失败: {e}")

clean_pycache()

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        if 'image' not in request.files:
            return jsonify({'success': False, 'error': '没有上传文件'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'success': False, 'error': '没有选择文件'}), 400
        
        # 生成唯一文件名
        ext = file.filename.split('.')[-1] if '.' in file.filename else 'png'
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{timestamp}_{uuid.uuid4().hex[:8]}.{ext}"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        
        # 保存文件到本地
        file.save(filepath)
        
        image_url = f"/uploads/{filename}"
        
        return jsonify({
            'success': True,
            'url': image_url,
            'filename': filename
        })
        
    except Exception as e:
        print(f"[错误] 上传失败: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/libs/<filename>')
def libs_file(filename):
    return send_from_directory('.', filename)

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    print("=" * 70)
    print("公众号Markdown编辑器 - 图片上传服务")
    print("=" * 70)
    print("[OK] 本地存储模式: 图片保存在本地uploads文件夹")
    print("=" * 70)
    print("服务已启动！")
    print(f"访问地址: http://127.0.0.1:{config.SERVER_PORT}")
    print("=" * 70)
    print("使用说明:")
    print("1. 在浏览器中打开上面的地址")
    print("2. 直接粘贴图片（Ctrl+V）或拖拽图片到编辑器")
    print("3. 图片会自动上传并插入到编辑器中")
    print("4. 编辑完成后点击'复制到公众号'")
    print("=" * 70)
    
    app.run(host=config.SERVER_HOST, port=config.SERVER_PORT, debug=False, use_reloader=False)

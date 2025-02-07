from flask import Flask

def create_app():
    app = Flask(__name__)
    

    # 注册 API 蓝图
    from app.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app 
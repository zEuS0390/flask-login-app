from app import create_app
from views_bp import views_bp

app = create_app()

app.register_blueprint(views_bp)

if __name__=="__main__":
  app.run(debug=True)
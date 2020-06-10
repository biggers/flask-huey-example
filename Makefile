
run_app:
	env APP_SETTINGS=app.config.DevelopmentConfig \
	    FLASK_ENV=development \
	    DEBUG=True \
	  python run_app.py

run_consumer:
	env HUEY_APP_SETTINGS=app.config.DevelopmentConfig \
	    PYTHONPATH=. \
	  huey_consumer.py \
	    --no-periodic --delay=0.5 --scheduler-interval=5 \
	    --workers=1 --worker-type=thread  run_huey.huey

#  --logfile=hconsumer.log

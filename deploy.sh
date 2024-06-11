#!/usr/bin/env bash
(cd /home/pregcfye/repositories/preguteca; git pull)
#BUILD THE FRONTEND
(cd /home/pregcfye/repositories/preguteca/preguteca_frontend; npm run build)

#COLLECT THE FRONTEND
(source /home/pregcfye/virtualenv/repositories/preguteca/preguteca_backend/3.9/bin/activate; cd /home/pregcfye/repositories/preguteca/preguteca_backend; python manage.py collectstatic)

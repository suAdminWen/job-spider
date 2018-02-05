from flask import render_template, request
from . import web
from .models import Job
from app import db
from spider.zhilian import main as zl_main
from spider.boss import main as bs_main


@web.route("/index")
def index():
    page = int(request.args.get("page", 1))
    paginate = Job.query.order_by("-date").paginate(page,
                                                    per_page=10)
    jobs = paginate.items
    return render_template("index.html",
                           jobs=jobs,
                           paginate=paginate)


@web.route("/drop")
def drop():
    db.drop_all()
    db.create_all()
    return "db is drop"


@web.route("/zl_init")
def zl_init():
    zl_main()
    return "success"


@web.route("/bs_init")
def bs_init():
    bs_main()
    return "success"


@web.route("/made")
def made():
    return render_template("made.html")
